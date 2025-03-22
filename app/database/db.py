from supabase import create_client, Client
from app.utils.encryption import encrypt_password, decrypt_password

# Initialize Supabase client
url = "https://kflbfzocxdgpmpmcpmvd.supabase.co"  # Replace with your Supabase URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtmbGJmem9jeGRncG1wbWNwbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI2NTI3NzQsImV4cCI6MjA1ODIyODc3NH0.n4QlPzMrRSFxlOVSXu9A44LEcVE9qBAN1fW4PQbzH9k"  # Replace with your Supabase API key
supabase: Client = create_client(url, key)

def sign_up(email, password):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
        })
        return response
    except Exception as e:
        print(f"Error signing up: {e}")
        return None

def sign_in(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
        return response
    except Exception as e:
        print(f"Error signing in: {e}")
        return None

def get_current_user():
    try:
        user = supabase.auth.get_user()
        return user
    except Exception as e:
        print(f"Error fetching current user: {e}")
        return None

def add_password(website, username, password):
    try:
        user = get_current_user()
        if not user:
            raise Exception("User not authenticated")

        encrypted_password = encrypt_password(password)
        supabase.table("passwords").insert({
            "website": website,
            "username": username,
            "password": encrypted_password,
            "user_id": user.user.id  # Associate password with the current user
        }).execute()
    except Exception as e:
        print(f"Error adding password: {e}")

def get_passwords():
    try:
        user = get_current_user()
        if not user:
            raise Exception("User not authenticated")

        response = supabase.table("passwords").select("*").eq("user_id", user.user.id).execute()
        for row in response.data:
            row["password"] = decrypt_password(row["password"])
        return response.data
    except Exception as e:
        print(f"Error fetching passwords: {e}")
        return []

def reset_password(email):
    try:
        # Send password reset email
        response = supabase.auth.reset_password_for_email(email)
        return True
    except Exception as e:
        print(f"Error resetting password: {e}")
        return False

def update_password(new_password):
    try:
        response = supabase.auth.update_user({
            "password": new_password,
        })
        return response
    except Exception as e:
        print(f"Error updating password: {e}")
        return None