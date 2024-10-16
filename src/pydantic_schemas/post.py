from pydantic import BaseModel, field_validator #, Field

class Post(BaseModel):
    id: int
    title: str

    @field_validator("id")
    def check_id_less_than_two(cls, v):
        if v > 2:
            raise ValueError("Id is not less than two")
        else:
            return v