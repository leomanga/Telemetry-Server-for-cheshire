from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, get_type_hints, Union
from uuid import UUID

class TelemetryData(BaseModel):
    telemetry_id: UUID
    country: Optional[str] = None
    version: str
    llm_model: Optional[str] = None
    embedder_model: Optional[str] = None
    system: str

    model_config = ConfigDict(extra="ignore")

def parse_telemetry(data: dict) -> TelemetryData:
    try:
        telemetry_data = TelemetryData(**data)
        return telemetry_data
    except Exception as e:
        raise e
    