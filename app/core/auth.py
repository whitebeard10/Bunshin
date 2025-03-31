from app.core.supabase_client import get_supabase

def login(email: str, password: str) -> bool:
    supabase = get_supabase()
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return True
    except Exception as e:
        print(f"Login error: {e}")
        return False

def signup(email: str, password: str) -> bool:
    supabase = get_supabase()
    try:
        res = supabase.auth.sign_up({"email": email, "password": password})
        return True
    except Exception as e:
        print(f"Signup error: {e}")
        return False

def forgot_password(email: str) -> bool:
    supabase = get_supabase()
    try:
        res = supabase.auth.reset_password_for_email(email)
        return True
    except Exception as e:
        print(f"Password reset error: {e}")
        return False