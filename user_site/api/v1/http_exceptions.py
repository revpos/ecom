from fastapi import HTTPException, status

def raise_user_not_found(user_id: int):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with ID {user_id} not found"
    )

def raise_invalid_email(email: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Invalid email format: {email}"
    )

def raise_email_already_registered(email: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Email already registered: {email}"
    )

def raise_invalid_password():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid password. Must be 8-16 characters."
    )  

def raise_user_already_inactive(user_id: int):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"User with ID {user_id} is already inactive"
    )
