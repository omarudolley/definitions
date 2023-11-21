import datetime
from datetime import date
from enum import Enum

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class IncomeTaxRequest(CamelCaseModel):
    pass


class TaxPayerType(str, Enum):
    RESIDENT = "resident"
    NON_RESIDENT = "non-resident"


class IncomeTaxResponse(CamelCaseModel):
    tax_payer_type: TaxPayerType = Field(
        ...,
        title="Tax Payer Type",
        description="The type of the tax liability of a person",
        examples=[TaxPayerType.RESIDENT, TaxPayerType.NON_RESIDENT],
    )
    withholding_percentage: float = Field(
        ...,
        title="Tax Percentage",
        description="The primary withholding percentage of the income",
        examples=[0.18],
    )
    income_limit: float = Field(
        ...,
        title="Income Limit",
        description="The income limit for the use of withholding percentage in euros",
        examples=[40000],
    )
    additional_percentage: float = Field(
        ...,
        title="Additional Percentage",
        description="The secondary withholding percentage of the income",
        examples=[0.45],
    )
    validity_period: date = Field(
        ...,
        title="Validity Period",
        description="The date from which the tax withholding details are valid",
        examples=[datetime.datetime(2023, 6, 30)],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Employment Income Tax",
    description="Tax withholding details of a person's income",
    request=IncomeTaxRequest,
    response=IncomeTaxResponse,
    requires_authorization=True,
    requires_consent=True,
)
