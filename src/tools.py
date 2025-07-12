import pandas as pd
from src.schemas import InputsUser, OutputQuery
import os
from dotenv import load_dotenv
import json

def query_data(id_user: int) -> OutputQuery:
    """
    Load data from a CSV file based on the user ID.
    """
    
    # Consult the CSV file and filter by user ID
    data_user = pd.read_csv(r'..\data\solicitudes_credito_simuladas.csv')[['id', 'es_cliente', 'score_crediticio']].query(f"id == {id_user}")
    data_user = data_user[['es_cliente', 'score_crediticio']].to_dict(orient='records')[0] if not data_user.empty else {}
    # Convert to OutputQuery schema
    response = OutputQuery(    
        es_cliente=data_user.get('es_cliente', None),
        scoring=data_user.get('score_crediticio', None)
        )
    return response


