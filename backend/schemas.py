from pydantic import BaseModel,HttpUrl
from typing import Dict,List, Union , Optional
from datetime import datetime





class EventRequest(BaseModel):
    Content: str
    Organiser: str
    Date: str
    Flyer: str
    
    
class EventResponse(BaseModel):
    Content: str
    Organiser: str
    Date: str
    Flyer: str
    Accepted : str | None = None
    





