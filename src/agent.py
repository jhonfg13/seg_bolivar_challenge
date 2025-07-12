import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from .schemas import InputsUser, OutputsUser, InputsEvaluator

def prompt_advisor(memory) -> str:
    """
    Function to create a prompt for the GenAI model based on the provided schema.
    """
    
    with open("docs/advisor.txt", "r", encoding="utf-8") as file:
        advisor = file.read()
    
    # Create the prompt using attention of user request
    prompt = f"""
    {advisor}\n
    
    **Estado del proceso**:
    {memory}
    """
    return prompt

def agent_advisor(prompt: str) -> InputsUser:
    """
    Function to call the GenAI model and generate content based on the provided schema.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    try:
        # Initialize the GenAI client with the API key
        client = genai.Client(api_key=os.getenv("API_KEY"))
    
        response = client.models.generate_content(
            model=os.getenv("MODEL_NAME"),
            contents=prompt,
            config={
            "response_mime_type": "application/json",
            "response_schema": InputsUser,
            },
        )
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return InputsUser(
            edad=None,
            ingresos_mensuales=None,
            region=None,
            justificacion=None,
            message=None
            )

    # Use instantiated objects.
    parsed_response: InputsUser = response.parsed
    
    return parsed_response

def prompt_evaluator(inputs: InputsEvaluator) -> str:
    """
    Function to create a prompt for the GenAI model based on the provided schema.
    """
    
    with open("docs/politicas.txt", "r", encoding="utf-8") as file:
        policies = file.read()
        
    # Create the prompt using the inputs and policies
    prompt = f"""
    Actuar como un experto en evaluación de crédito.\n
    Analizar la solicitud de crédito del cliente y generar una decisión final sobre la solicitud.\n
    
    Ten en cuenta las siguientes politicas de crédito:\n
    {policies}\n
    **Datos del cliente**:
    Edad: {inputs.edad}
    Ingresos mensuales: {inputs.ingresos_mensuales}
    Región: {inputs.region}
    Justificación del crédito: {inputs.justificacion}
    Tipo de cliente: {inputs.es_cliente}, (1 es cliente recurrente, 0 es cliente nuevo)
    Score crediticio: {inputs.scoring}

    Genere una decisión final sobre la solicitud de crédito.
    """
    return prompt

def agent_evaluator(requests: str) -> OutputsUser:
    """
    Function to call the GenAI model and generate content based on the provided schema.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    try:
        # Initialize the GenAI client with the API key
        client = genai.Client(api_key=os.getenv("API_KEY"))
    
        response = client.models.generate_content(
            model=os.getenv("MODEL_NAME"),
            contents=requests,
            config={
            "response_mime_type": "application/json",
            "response_schema": OutputsUser,
            },
        )
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return OutputsUser(decision_final="RECHAZADO", justificacion="Error in model call")
    
    # Use instantiated objects.
    parsed_response: OutputsUser = response.parsed
    
    return parsed_response