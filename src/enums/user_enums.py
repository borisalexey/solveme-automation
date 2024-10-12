from enum import Enum

class Gender(Enum):
    female = "female"
    male = "male"

class Status(Enum):
    inactive = "inactive"
    active = "active"

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"