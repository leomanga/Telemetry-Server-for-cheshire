from pydantic import BaseModel, ConfigDict, field_validator
from typing import Optional
from uuid import UUID

class TelemetryData(BaseModel):
    # required telemetries
    telemetry_id: UUID
    version: str
    system: str

    # optional telemetries
    country: Optional[str] = None
    llm_model: Optional[str] = None
    embedder_model: Optional[str] = None
    
    # config
    model_config = ConfigDict(extra="ignore")

    @field_validator("version", "system")
    def not_empty(cls, value, field):
        if value == "":
            raise ValueError(f"\n{field} cannot be an empty string")
        return value

def parse_telemetry(data: dict) -> TelemetryData:
    try:
        telemetry_data = TelemetryData(**data)
        return telemetry_data
    
    except Exception as e:
        raise e
    