from fastapi import FastAPI, HTTPException
from supabase import Client, create_client
from PostGuest import post_GuestList
from DeleteEventList import delete_event
from DeleteGuest import delete_guest
from models import Eventlist,GuestList
from typing import Union
from config import supabase_url,supabase_key
from GetAllitems import get_all_items
from PostEvent import PostEventitem

app = FastAPI()

Supabase_url = supabase_url
Supabase_key = supabase_key
supabase: Client = create_client(supabase_url=Supabase_url, supabase_key=Supabase_key)

@app.get('/table')
async def Allitems(table_name:str):
    return await get_all_items(table_name=table_name)

@app.post('/table/EventList')
async def post_EventList(obj:Eventlist):
    return await PostEventitem(obj=obj)
    
@app.post('/table/GuestList')
async def postGuestList(obj1: GuestList):
    return await post_GuestList(obj1=obj1)
    
@app.delete('/Guest/delete_guest')
async def deleteGuest(guestName: str,EventName :str):
    return await delete_guest(guestName=guestName,EventName=EventName)
   
@app.delete('/EventList')
async def deleteEvent(EventName: str):
    return await delete_event(EventName=EventName)
      
        
        
