from policyengine_us.model_api import *


class de_deduction_joint(Variable):
    value_type = float
    entity = Person
    label = "Delaware deduction when married filing jointly"
    unit = USD
    definition_period = YEAR
    reference = "https://delcode.delaware.gov/title30/c011/sc02/index.html title 30, chapter 11, subchapter II, section 1108"
    defined_for = StateCode.DE

    def formula(person, period, parameters):
        itemized = person("de_itemized_deductions_joint", period)
        standard = person("de_standard_deduction_joint", period)
        return max_(itemized, standard)
