from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from typing import Union
from config import supabase_url, supabase_key

app = FastAPI()

Supabase_url = supabase_url
Supabase_key = supabase_key

supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)


async def delete_guest(guestName: str, EventName: str):
    try:
        
        result = supabase.table("EventList").select().eq('EventName', EventName).execute()
        data = result.data

        if data:
            
            guest_result = supabase.table("GuestList").select().eq('GuestName', guestName).execute()
            guestdata = guest_result.data

            if guestdata:
                
                deletion = supabase.table("GuestList").delete().eq('GuestName', guestName).execute()
                if deletion.data:  
                    return {
                        "status": "success",
                        "message": f"Guest '{guestName}' has been deleted from event '{EventName}'"
                    }
                else:
                    return {
                        "status": "failed",
                        "message": "Deletion failed due to an unknown error"
                    }
            else:
                return {
                    "status": "failed",
                    "message": "Guest Not Found"
                }
        else:
            return {
                "status": "failed",
                "message": "Event Not Found"
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


