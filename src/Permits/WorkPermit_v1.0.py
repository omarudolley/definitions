import datetime
from datetime import date
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PermitType(str, Enum):
    A = "A"
    B = "B"


class Permit(CamelCaseModel):
    permit_name: str = Field(
        ...,
        title="Permit Name",
        description="The name of the permit issued to a person for residence",
        examples=["Seasonal work certificate"],
    )
    permit_accepted: bool = Field(
        ...,
        title="Permit Accepted",
        description="The decision if the permit was accepted.",
        examples=[True],
    )
    permit_type: Optional[PermitType] = Field(
        ...,
        title="Permit Type",
        description="The type of the permit validity issued for a person",
        examples=[PermitType.A, PermitType.B],
    )
    validity_start: Optional[date] = Field(
        None,
        title="Validity Start",
        description="The start date of the residence permit validity",
        examples=[datetime.datetime(2023, 11, 7)],
    )
    validity_end: Optional[date] = Field(
        None,
        title="Validity End",
        description="The end date of the residence permit validity",
        examples=[datetime.datetime(2024, 2, 19)],
    )
    industries: Optional[List[float]] = Field(
        ...,
        title="Industries",
        description="The list of industries that the permit holder is allowed to work based on the Statistical "
        "classification of economic activities in the European Community, abbreviated as NACE.",
        examples=[79.1, 79.9],
    )
    employer_name: Optional[str] = Field(
        None,
        title="Employer Name",
        description="The name of the employer that the person is allowed to work for",
        examples=["Staffpoint Oy"],
    )


class WorkPermitRequest(CamelCaseModel):
    end_user_authentication_token: str = Field(
        ..., description="The end user authentication token"
    )


class WorkPermitResponse(CamelCaseModel):
    permits: List[Permit] = Field(
        ...,
        title="Permits",
    )


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="Permits Work Permit",
    description="Work permit details of a person",
    request=WorkPermitRequest,
    response=WorkPermitResponse,
    requires_authorization=True,
    requires_consent=True,
)
