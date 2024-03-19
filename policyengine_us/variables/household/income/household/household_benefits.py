from policyengine_us.model_api import *


class household_benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = USD
    definition_period = YEAR
    adds = [
        "social_security",
        "ssi",
        "state_supplement",
        "co_state_supplement",
        # State child care subsidies.
        "ca_child_care_subsidies",
        "co_child_care_subsidies",
        "ca_cvrp",  # California Clean Vehicle Rebate Project.
        "ca_care",
        "ca_fera",
        "co_oap",
        "snap",
        "wic",
        "free_school_meals",
        "reduced_price_school_meals",
        "spm_unit_broadband_subsidy",
        "tanf",
        "high_efficiency_electric_home_rebate",
        "residential_efficiency_electrification_rebate",
        "unemployment_compensation",
        # Contributed.
        "basic_income",
        "spm_unit_capped_housing_subsidy",
    ]
