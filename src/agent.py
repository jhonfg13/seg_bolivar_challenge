import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from .schemas import InputsUser, OutputsUser

def create_prompt(inputs: InputsUser) -> str:
    """
    Function to create a prompt for the GenAI model based on the provided schema.
    """
    
    with open("docs/politicas.txt", "r") as file:
        policies = file.read()
        
    # Create the prompt using the inputs and policies
    prompt = f"""
    Actuar como un experto en evaluación de crédito./n
    Analizar la solicitud de crédito del cliente y generar una decisión final sobre la solicitud./n
    
    Ten en cuenta las siguientes politicas de crédito:/n
    {policies}/n
    **Datos del cliente**:
    Edad: {inputs.edad}
    Ingresos mensuales: {inputs.ingresos_mensuales}
    Región: {inputs.region}
    Justificación del crédito: {inputs.justificacion}

    Genere una decisión final sobre la solicitud de crédito.
    """
    return prompt

def call_model(requets: str) -> OutputsUser:
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
            contents=requets,
            config={
            "response_mime_type": "application/json",
            "response_schema": OutputsUser,
            },
        )
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return OutputsUser(decision_final="RECHAZADO", justificacion="Error in model call")
    
    # Use the response as a JSON string.
    print(response.text)

    # Use instantiated objects.
    my_recipes: OutputsUser = response.parsed
    print(my_recipes)
    
    return my_recipes
