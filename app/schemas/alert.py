
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"


class AlertStatus(str, Enum):
    NEW = "new"
    INVESTIGATING = "investigating"
    ESCALATED = "escalated"
    CLOSED = "closed"


class Alert(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID = Field(default_factory=uuid4)

    external_id: str | None = None

    title: str = Field(min_length=3, max_length=300)
    description: str

    source: str
    severity: Severity

    status: AlertStatus = AlertStatus.NEW

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    raw_event: dict = Field(default_factory=dict)

    @field_validator("created_at")
    @classmethod
    def validate_timezone(cls, value):
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")
        return value
