from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field, constr


class CitizenshipArea(str, Enum):
    EEA = "EEA"
    NON_EEA = "non-EEA"


class BasicInformationRequestResponse(CamelCaseModel):
    given_name: Optional[str] = Field(
        None,
        title="Given name",
        description="The first name that the person is being called by",
        example="John",
        max_length=250,
    )
    last_name: Optional[str] = Field(
        None,
        title="Last name",
        description="The person's current family name",
        example="Doe",
        max_length=250,
    )
    email: EmailStr = Field(
        ...,
        title="Email",
        description="The person's contact email address",
        example="john.doe@test.fi",
    )
    phone_number: Optional[str] = Field(
        None,
        title="Phone number",
        description="The person's phone number in the international format",
        example="+358501234567",
        max_length=250,
    )
    citizenship_area: Optional[CitizenshipArea] = Field(
        None,
        title="Citizenship Area",
        description="The citizenship area based on his or her native country."
        " Switzerland is considered as part of the EEA category.",
        example=CitizenshipArea.EEA,
    )


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="Write Person Basic Information",
    description="Create or update a minimal set of basic information of a person",
    request=BasicInformationRequestResponse,
    response=BasicInformationRequestResponse,
    requires_authorization=True,
    requires_consent=True,
)
