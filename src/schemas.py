from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List

## Schemas for data validation in credit scoring application

class ChatRequest(BaseModel):
    """
    Schema for chat request data validation.
    """
    memory: List[str] = Field(..., description="Lista de mensajes de conversación")

class InputsUser(BaseModel):
    """
    Schema for input data validation.
    """
    id_user: Optional[int] = Field(None, description="Identificador del cliente")
    edad: Optional[int] = Field(None, description="Edad del cliente")
    ingresos_mensuales: Optional[int] = Field(None, description="Ingresos mensuales del cliente")
    region: Optional[str] = Field(None, description="Región del cliente")
    justificacion: Optional[str] = Field(None, description="Justificación del crédito")
    message: Optional[str] = Field(None, description="Mensaje adicional del cliente")
    
    
class InputsEvaluator(BaseModel):
    """
    Schema for input data validation.
    """
    edad: Optional[int] = Field(None, description="Edad del cliente")
    ingresos_mensuales: Optional[int] = Field(None, description="Ingresos mensuales del cliente")
    region: Optional[str] = Field(None, description="Región del cliente")
    justificacion: Optional[str] = Field(None, description="Justificación del crédito")
    es_cliente: Optional[int] = Field(None, description="Indicador de si es cliente")
    scoring: Optional[int] = Field(None, description="Puntuación de crédito")

   
class InputsQuery(BaseModel):
    """
    Schema for input query validation.
    """
    id_user: Optional[int] = Field(None, description="Identificador del cliente")
    
class OutputQuery(BaseModel):
    """
    Schema for data query validation.
    """
    es_cliente: Optional[int] = Field(None, description="Indicador de si es cliente")
    scoring: Optional[int] = Field(None, description="Puntuación de crédito")
    
class DecisionFinal(str, Enum):
    """
    Enum for final decision on credit application.
    """
    APROBADO = "APROBADO"
    RECHAZADO = "RECHAZADO"
    
class OutputsUser(BaseModel):
    """
    Schema for output data validation.
    """
    decision_final: DecisionFinal = Field(..., description="Decisión final sobre la solicitud de crédito")
    justificacion: Optional[str] = Field(None, description="Justificación de la decisión")