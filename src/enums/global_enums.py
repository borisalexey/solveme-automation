from enum import Enum

class GlobalErrorMassages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Element count is not equal to expected"
