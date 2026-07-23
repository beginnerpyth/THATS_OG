from fastapi import APIRouter, Depends, HTTPException
from auth import create_token, get_current_user, require_role
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# ONLY ONE LOGIN ENDPOINT — removed the old one
@router.post('/auth/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == 'admin@test.com' and form_data.password == 'admin123':
        token = create_token('admin@test.com', 'admin')
        return {'access_token': token, 'token_type': 'bearer'}
    
    elif form_data.username == 'user@test.com' and form_data.password == 'user123':
        token = create_token('user@test.com', 'user')
        return {'access_token': token, 'token_type': 'bearer'}
    
    raise HTTPException(status_code=401, detail='Invalid credentials')

# only admins
@router.get('/admin-only')
def admin_route(current_user: dict = Depends(require_role('admin'))):
    return {'message': f'hello admin {current_user["email"]}'}

# only users
@router.get('/user-only')
def user_route(current_user: dict = Depends(require_role('user'))):
    return {'message': f'hello user {current_user["email"]}'}

# anyone logged in
@router.get('/profile')
def profile(current_user: dict = Depends(get_current_user)):
    return current_user