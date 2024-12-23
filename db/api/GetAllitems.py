from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from models import Eventlist,GuestList
from typing import Union
from config import supabase_url,supabase_key



Supabase_url = supabase_url
Supabase_key = supabase_key


supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)


async def get_all_items(table_name:str):
    try:
        result = supabase.table(table_name).select("*").execute()
        return {"data": result.data}
    
    except Exception as e:
        
        raise HTTPException(
            status_code=500, detail=f"An error occurred: {str(e)}"
        )