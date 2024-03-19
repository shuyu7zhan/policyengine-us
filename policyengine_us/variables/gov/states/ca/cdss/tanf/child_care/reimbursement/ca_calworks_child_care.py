from policyengine_us.model_api import *


class ca_calworks_child_care(Variable):
    value_type = float
    entity = SPMUnit
    label = "California CalWORKs Child Care final payment"
    unit = USD
    definition_period = MONTH
    defined_for = "ca_calworks_child_care_eligible"

    adds = ["ca_calworks_child_care_payment"]
