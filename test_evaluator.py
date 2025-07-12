import pandas as pd
from src.schemas import InputsEvaluator
from src.agent import prompt_evaluator, agent_evaluator
import time

def test_evaluator_with_csv():
    """
    Función para probar el agente evaluador con datos del CSV y guardar resultados.
    """
    # Leer el CSV de datos
    df = pd.read_csv(r'data\solicitudes_credito_simuladas.csv').sort_values(by='id') # Ajusta el nombre del archivo si es diferente
    
    # Lista para almacenar resultados
    results = []
    
    print(f"Procesando {len(df)} registros...")
    
    # Procesar cada fila
    for index, row in df.iterrows():
        try:
            # Crear objeto InputsEvaluator con los datos de la fila
            inputs = InputsEvaluator(
                edad=row['edad'],
                ingresos_mensuales=row['ingresos_mensuales'],
                region=row['region'],
                justificacion=row['justificacion'],
                es_cliente=row['es_cliente'],
                scoring=row['score_crediticio']
            )
            
            # Generar prompt y evaluar
            prompt = prompt_evaluator(inputs)
            time.sleep(4)  # Espera para simular procesamiento límite de 30 RPM
            response = agent_evaluator(prompt)
            
            # Guardar resultado
            results.append({
                'cliente_id': row.get('id', index),  # Usa 'id' si existe, sino el índice
                'decision_final': response.decision_final,
                'justificacion_agente': response.justificacion
            })
            
            print(f"Procesado cliente {index + 1}/{len(df)}: {response.decision_final}")
            
        except Exception as e:
            # En caso de error, guardar como RECHAZADO
            results.append({
                'cliente_id': row.get('id', index),
                'decision_final': 'RECHAZADO',
                'justificacion_agente': f'Error: {str(e)}'
            })
            print(f"Error en cliente {index + 1}: {str(e)}")
    
    # Crear DataFrame con resultados
    results_df = pd.DataFrame(results)
    
    # Guardar en CSV
    output_file = 'data/resultados_evaluador.csv'
    results_df.to_csv(output_file, index=False)
    
    print(f"\nResultados guardados en: {output_file}")
    print(f"Total procesados: {len(results)}")
    
    # Mostrar resumen
    print("\nResumen de decisiones:")
    print(results_df['decision_final'].value_counts())
    
    return results_df

if __name__ == "__main__":
    # Ejecutar la prueba
    resultados = test_evaluator_with_csv()