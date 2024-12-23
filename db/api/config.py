
from supabase import create_client, Client
import os
import dotenv

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

def create_Connection() -> Client:
    # Create and return the Supabase client
    return create_client(supabase_url, supabase_key)
