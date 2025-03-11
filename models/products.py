from typing import Optional
from pydantic import BaseModel,Field


class SearchFormData(BaseModel):

    search_text:str
    isFilterApplied:bool = Field(default = False)
    FINAL_PRICE:Optional[list[float]]
    CURRENCY:Optional[str]
    RATING:Optional[float]
    STOCK:Optional[int]