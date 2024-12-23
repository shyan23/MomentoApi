
from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from models import Eventlist,GuestList
from typing import Union
from config import supabase_url,supabase_key
from GetAllitems import get_all_items
from PostEvent import PostEventitem


app = FastAPI()

Supabase_url = supabase_url
Supabase_key = supabase_key


supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)

async def post_GuestList(obj1: GuestList):
    try:
        eventlist = obj1.EventName
        result = supabase.table("EventList").select('EventName').execute()

        if result.data:  
            for e in result.data:
                if e['EventName'].lower() == eventlist.lower():  
                    insert_result = supabase.table("GuestList").insert(
                        {
                            "GuestName": obj1.GuestName,
                            "EventName": obj1.EventName,
                            "GuestDesignation": obj1.GuestDesignation
                        }
                    ).execute()

                    if insert_result:
                        return {"status": "success", "data": insert_result.data}
                    else:
                        raise HTTPException(status_code=400, detail="Error inserting/updating data")

            
            return {"Status": "Failed", "Message": "No such name in the events exists"}
        else:
            return {"Status": "Failed", "Message": "No events found"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
