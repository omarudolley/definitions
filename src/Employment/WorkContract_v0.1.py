import datetime
from datetime import date
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class WorkContractRequest(CamelCaseModel):
    pass


class EmployerInfo(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=250,
        description="The official name of the employer",
        examples=["Staffpoint Oy"],
    )
    businessID: str = Field(
        ...,
        title="Business ID",
        max_length=250,
        description="The business ID of the employer",
        examples=["2492090-1"],
    )
    street_name: str = Field(
        ...,
        title="Street Name",
        max_length=40,
        description="The street name of the employer contact address",
        examples=["Ruoholahdenkatu 17 A 6"],
    )
    postal_code: str = Field(
        ...,
        title="Postal Code",
        max_length=10,
        description="The postal code of the employer address",
        examples=["00180"],
    )
    city: str = Field(
        ...,
        title="City",
        max_length=40,
        description="The city of the employer address",
        examples=["Helsinki"],
    )
    signature_date: date = Field(
        ...,
        title="Signature Date",
        description="The date of the employer signature for the work contract",
        examples=[datetime.datetime(2023, 8, 25)],
    )


class EmployeeInfo(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=250,
        description="The name of the employee",
        examples=["Tom Williams"],
    )
    street_address: str = Field(
        ...,
        title="Street Address",
        max_length=40,
        description="The street name of the employee contact address",
        examples=["49 Featherstone Street"],
    )
    postal_code: str = Field(
        ...,
        title="Postal Code",
        max_length=10,
        description="The postal code of the employee address",
        examples=["EC1Y 8SY"],
    )
    city: str = Field(
        ...,
        title="City",
        max_length=40,
        description="The city of the employee address",
        examples=["London"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        max_length=3,
        min_length=3,
        description="The country code of the employee address in Alpha-3 format",
        examples=["GBR"],
    )
    signature_date: date = Field(
        ...,
        title="Signature Date",
        description="The date of the employee signature for the work contract",
        examples=[datetime.datetime(2023, 8, 27)],
    )


class TermsOfWork(CamelCaseModel):
    employment_start: date = Field(
        ...,
        title="Employment Start",
        description="The start date of the employment",
        examples=[datetime.datetime(2023, 11, 7)],
    )
    employment_end: date = Field(
        ...,
        title="Employment End",
        description="The end date of the employment",
        examples=[datetime.datetime(2024, 2, 19)],
    )
    grounds_for_fixed_term: Optional[str] = Field(
        None,
        title="Grounds for Fixed Term",
        max_length=250,
        description="The reasoning if the contract is fixed term",
        examples=["The winter time tourism in Lapland"],
    )
    work_duties: str = Field(
        ...,
        title="Work Duties",
        max_length=400,
        description="The work duties of the employee",
        examples=["Hotel guest reception"],
    )
    work_conditions: Optional[str] = Field(
        None,
        title="Work Conditions",
        max_length=400,
        description="The special conditions regarding the work duties, e.g. work for another party than the employer",
        examples=["The work duties done for Lapland Hotels"],
    )
    industry: Optional[str] = Field(
        None,
        title="Industry",
        max_length=10,
        description="The work industry based on the Statistical classification of economic activities in the European "
        "Community, abbreviated as NACE.",
        examples=["79.1"],
    )
    locations: List[str] = Field(
        None,
        title="Locations",
        description="The region in Finland where the work is done",
        examples=["Rovaniemi, Lapland"],
        max_length=250,
    )
    working_hours: float = Field(
        ...,
        title="Working Hours",
        description="The number of work hours per week",
        examples=[30],
    )
    collective_agreement: Optional[str] = Field(
        None,
        title="Collective Agreement",
        max_length=250,
        description="The name of the applicable collective agreement",
        examples=["The collective agreement for Employment industry (HELA)"],
    )
    overtime_rules: str = Field(
        ...,
        title="Overtime Rules",
        max_length=400,
        description="The terms for the overtime work and compensation",
        examples=["For overtime work you receive 25 € per overtime hour"],
    )
    probation: str = Field(
        ...,
        title="Probation",
        max_length=250,
        description="The terms for the period of conditional employment",
        examples=[
            "The probationary period lasts 2 months from the employment start date"
        ],
    )


class PaymentGrounds(str, Enum):
    MONTHLY = "monthly"
    HOURLY = "hourly"


class Compensation(CamelCaseModel):
    payment_grounds: PaymentGrounds = Field(
        ...,
        title="Payment Grounds",
        description="The grounds for paying the salary",
        examples=[PaymentGrounds.MONTHLY, PaymentGrounds.HOURLY],
    )
    salary: float = Field(
        ...,
        title="Salary",
        description="The amount of salary in euros",
        examples=[2500],
    )
    bonuses: Optional[str] = Field(
        None,
        title="Bonuses",
        description="The details of the salary bonuses",
        examples=["No additional bonuses"],
        max_length=250,
    )
    payment_time: str = Field(
        ...,
        title="Payment Time",
        description="The conditions for paying the salary",
        examples=["The 15th of every month"],
        max_length=250,
    )


class BenefitType(str, Enum):
    PART_OF_SALARY = "part of salary"
    ADDITION_TO_SALARY = "addition to salary"


class Benefit(CamelCaseModel):
    benefit: Optional[str] = Field(
        None,
        title="Benefit",
        max_length=250,
        description="The name of the benefit received as a compensation",
        examples=["Lunch benefit"],
    )
    benefit_type: Optional[BenefitType] = Field(
        None,
        title="Benefit Type",
        description="The type of the taxable benefit",
        examples=[BenefitType.PART_OF_SALARY, BenefitType.ADDITION_TO_SALARY],
    )
    taxable_value: Optional[float] = Field(
        None,
        title="Taxable Value",
        description="The taxable value for the compensation per month",
        examples=[200],
    )


class DeterminationOfHoliday(str, Enum):
    ANNUAL_HOLIDAY_ACT = "annual holiday act"
    COLLECTIVE_AGREEMENT = "collective agreement"


class Holidays(CamelCaseModel):
    paid_holiday: bool = Field(
        ...,
        title="Paid Holiday",
        description="Indicates if the contract includes paid holiday",
        examples=[True],
    )
    number_of_holidays: Optional[int] = Field(
        None,
        title="Number Of Holidays",
        description="The terms used for the paid holidays",
        examples=[5],
    )
    determination_of_holiday: Optional[DeterminationOfHoliday] = Field(
        None,
        title="Determination Of Holiday",
        description="The determination of the holiday",
        examples=["The holiday is determined by the employer"],
    )


class Term(CamelCaseModel):
    term_description: Optional[str] = Field(
        None,
        title="Term Description",
        max_length=250,
        description="The description of the term",
        examples=[
            "The employee is mandated to use workwear appointed by the Lapland Hotels and return them at the "
            "end of the contract"
        ],
    )


class WorkContractResponse(CamelCaseModel):
    employer_info: EmployerInfo = Field(
        ...,
        title="Employer Info",
        description="The details of the employer",
    )
    employee_info: EmployeeInfo = Field(
        ...,
        title="Employee Info",
        description="The details of the employee",
    )
    terms_of_work: TermsOfWork = Field(
        ...,
        title="Terms of Work",
        description="The terms and conditions for the work",
    )
    compensation: Compensation = Field(
        ...,
        title="Compensation",
        description="The details of the compensation for the work",
    )
    holidays: Holidays = Field(
        ...,
        title="Holidays",
        description="The details of the paid holidays",
    )
    benefits: List[Benefit] = Field(
        ...,
        title="Benefits",
        description="The list of taxable benefits for the employee in addition to salary compensation",
    )
    termination: str = Field(
        ...,
        title="Termination",
        max_length=500,
        description="The terms and conditions for the contract termination",
        examples=[
            "To terminate the work contract, the terminating party must provide 30 days of written notice to "
            "the other party"
        ],
    )
    other_terms: List[Term] = Field(
        ...,
        title="Other Terms",
        description="The description other terms included in the work contract",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Employment Work Contract",
    description="Contents of a work contract",
    request=WorkContractRequest,
    response=WorkContractResponse,
    requires_authorization=True,
    requires_consent=True,
)
