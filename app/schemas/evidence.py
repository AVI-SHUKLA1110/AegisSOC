
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class EvidenceType(str, Enum):
    LOG = "log"
    NETWORK = "network"
    ENDPOINT = "endpoint"
    THREAT_INTEL = "threat_intel"
    IDENTITY = "identity"


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID = Field(default_factory=uuid4)

    alert_id: UUID

    evidence_type: EvidenceType

    source: str

    description: str

    data: dict = Field(default_factory=dict)

    collected_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    reference: str | None = None
