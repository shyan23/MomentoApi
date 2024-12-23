from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from models import Eventlist,GuestList
from typing import Union
from config import supabase_url,supabase_key
from GetAllitems import get_all_items

app = FastAPI()

Supabase_url = supabase_url
Supabase_key = supabase_key


supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)



async def PostEventitem(obj:Eventlist):
    try:
        result = supabase.table("EventList").insert(
                {"Date" : obj.Date,
                "Time" : obj.Time,
                "Location" : obj.Location,
                "Budget" : obj.Budget,
                "Organized_By":obj.Organized_By,
                "EventName":obj.EventName}).execute()
            
        if result:
            return {"status": "success", "data": result.data}
        else:
            raise HTTPException(status_code=400, detail="Error inserting/updating data")
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")   