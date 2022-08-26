from datetime import datetime

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PopulationResponse(CamelCaseModel):
    description: str = Field("", title="Data description")
    source_name: str = Field("", title="Data source name")
    population: int = Field(..., title="The population value")
    updated_at: datetime = Field("", title="Data updated at datetime")


class PopulationRequest(CamelCaseModel):
    city: str = Field(
        "",
        title="City or region",
        description="City or a region name, leaving the field empty selects country's total",
    )
    year: int = Field(2021, title="Year")


DEFINITION = DataProductDefinition(
    description="Data Product for population figure",
    request=PopulationRequest,
    response=PopulationResponse,
    summary="Figure for population",
)
