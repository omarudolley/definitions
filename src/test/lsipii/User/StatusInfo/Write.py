from datetime import datetime
from enum import Enum

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class StatusInfoValue(str, Enum):
    SENT = "SENT"
    PROCESSING = "PROCESSING"
    WAITING_FOR_COMPLETION = "WAITING_FOR_COMPLETION"
    READY = "READY"


class StatusInfoResponse(CamelCaseModel):
    status_label: str = Field(
        ...,
        title="Label of the status",
        description="Label of the status in English",
        example="Sent",
    )
    status_name: str = Field(
        ...,
        title="Name of the status",
        description="Programmatic identity field of the status",
        example="tax_form",
    )
    status_value: StatusInfoValue = Field(
        ...,
        title="Status",
        description="Value of the status",
        example=StatusInfoValue.SENT,
    )
    updated_at: datetime = Field(
        ...,
        title="Datetime the data was last updated at",
        description="A datetime in RFC3339 date-time syntax",
        example="2022-06-17T11:52:00Z",
    )
    created_at: datetime = Field(
        ...,
        title="Datetime the data was created at",
        description="A datetime in RFC3339 date-time syntax",
        example="2022-06-17T11:52:00Z",
    )


class StatusInfoRequest(CamelCaseModel):
    status_name: str = Field(
        ...,
        title="Name of the status",
        description="The name of the status to retrieve",
    )
    status_value: StatusInfoValue = Field(
        ...,
        title="Status",
        description="Value of the status",
        example=StatusInfoValue.SENT,
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    title="Save user's status information",
    description="Data product for user's status information",
    request=StatusInfoRequest,
    response=StatusInfoResponse,
    requires_authorization=True,
)
