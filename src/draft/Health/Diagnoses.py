from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class HealthDiagnosesRequest(CamelCaseModel):
    pass


class HealthDiagnosesResponse(CamelCaseModel):
    diagnoses: List[str] = Field(
        ..., description="List of users diagnoses in ICD10 code", examples=["icd10:J45"]
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    deprecated=True,
    title="Persons health diagnoses",
    description="Diagnoses of a user with ICD10 codes",
    request=HealthDiagnosesRequest,
    response=HealthDiagnosesResponse,
)
