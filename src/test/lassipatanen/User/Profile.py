from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, constr


class Gender(str, Enum):
    male = "MALE"
    female = "FEMALE"


class Address(CamelCaseModel):
    street_address: str = Field(
        ...,
        title="Street address",
        description="Street address",
        example="Mannerheimintie 42",
    )
    zip_code: constr(min_length=5, max_length=5) = Field(
        ..., title="ZIP code", description="ZIP code of the address", example="00100"
    )
    city: str = Field(
        ...,
        title="City",
        description="City of the address location",
        example="Helsinki",
    )
    country: str = Field(
        ..., title="Country", description="Country of the address", example="Suomi"
    )


class ProfileResponse(CamelCaseModel):
    id: UUID = Field(
        title="Id",
        description="uuid formatted string used to identify users",
        example="cf57432e-809e-4353-adbd-9d5c0d733868",
    )
    created: datetime = Field(
        title="Created",
        description="Created at timestamp",
        example="2042-04-23T10:20:30.400",
    )
    modified: datetime = Field(
        title="Modified",
        description="Modified at timestamp",
        example="2042-04-23T10:20:30.400",
    )
    first_name: Optional[str] = Field(
        ..., title="First name", description="First name of the user", example="John"
    )
    last_name: str = Field(
        ..., title="Last name", description="Last name of the user", example="Doe"
    )
    address: Address = Field(..., title="Address", description="Address of the user")
    immigration_data_consent: bool = Field(
        title="Immigration data consent",
        description="Has user given permission to use their data on Registration of Foreigners application",
    )
    jobs_data_consent: bool = Field(
        title="Jobs data consent",
        description="Has user given permission to use their data on form application",
    )
    date_of_birth: date = Field(
        ...,
        title="Date of birth",
        description="Date of Birth (date only)",
        example="2000-01-01",
    )
    gender: Gender = Field(..., title="Gender", description="Gender of the user")
    country_of_birth_code: constr(min_length=2, max_length=2, to_upper=True) = Field(
        ...,
        title="Country of birth code",
        description="ISO 3166-1 alpha-2 code for country",
        example="FI",
    )
    native_language_code: constr(min_length=2, max_length=2, to_upper=True) = Field(
        ...,
        title="Native language code",
        description="ISO 639-1 code for language",
        example="fi",
    )
    occupation_code: str = Field(
        ...,
        title="Occupation code",
        description="Code scheme for occupation. Full set of codes can be found at https://koodistot.suomi.fi/codelist-api/api/v1/coderegistries/jhs/codeschemes/ammatti_1_20100101/codes/",
        example="11122",
    )
    citizenship_code: constr(min_length=2, max_length=2, to_upper=True) = Field(
        ...,
        title="Nationality code",
        description="ISO 3166-1 alpha-2 code for nationality",
        example="FI",
    )
    job_titles: Optional[List[str]] = Field(
        ...,
        title="Job titles",
        description="List of job titles",
        example=["Chef", "Programmer"],
    )
    regions: Optional[List[str]] = Field(
        ...,
        title="Regions",
        description="List of regions where user would want to search for a job",
        example=["Etelä-Suomi"],
    )


class ProfileRequest(CamelCaseModel):
    ...


DEFINITION = DataProductDefinition(
    description="Data product for basic user profile information",
    request=ProfileRequest,
    response=ProfileResponse,
    route_description="User profile information",
    summary="Basic user profile information",
)
