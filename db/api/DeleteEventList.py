from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from PostGuest import post_GuestList
from models import Eventlist,GuestList
from typing import Union
from config import supabase_url,supabase_key
from GetAllitems import get_all_items
from PostEvent import PostEventitem


app = FastAPI()

Supabase_url = supabase_url
Supabase_key = supabase_key


supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)

async def delete_event(EventName: str):
    try:
        
        res = supabase.table("EventList").select('EventName').execute()
        data = res.data

        if data:
            
            for r in data:
                if r['EventName'] == EventName:
                    
                    deletion = (
                        supabase.table("EventList")
                        .delete()
                        .eq('EventName', EventName)
                        .execute()
                    )
                    if deletion:
                        return {
                            "status": "success",
                            "message": f"Event '{EventName}' has been deleted"
                        }
                    else:
                        return {
                            "status": "failed",
                            "message": "Deletion failed due to an unknown error"
                        }

            
            return {
                "status": "failed",
                "message": f"No event found with the name '{EventName}'"
            }
        else:
            return {
                "status": "failed",
                "message": "Event list is empty or could not be retrieved"
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")