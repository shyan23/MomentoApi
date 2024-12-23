from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class Eventlist(BaseModel):
    EventID: Optional[int] = None  
    Date: date
    Time: str
    Location: str
    Budget: float
    Organized_By: str
    EventName: str

    @field_validator('Date')
    def convert_date_to_string(cls, v):
        if isinstance(v, date):
            return v.isoformat()  
        return v

    
class GuestList(BaseModel):
    GuestID : Optional[int] = None
    GuestName:str
    GuestDesignation:str
    EventName : str
    
