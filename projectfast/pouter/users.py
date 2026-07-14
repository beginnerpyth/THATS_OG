from auth import hashpass, hasverify, jwt_te, err_ch
from keema import users_signup, users_login,users_verify  # Fixed imports
from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer

# 1. Router Setup
bb = APIRouter(prefix='/train', tags=['/hibiya/'])
nothing = OAuth2PasswordBearer(tokenUrl='/train/login')  # Removed trailing slash to match route
user_db = {}

# 2. SIGNUP ENDPOINT
@bb.post('/')
def signup(users: users_signup):
    # FIXED: Pydantic automatically blocks None, but if you check, you must RAISE with status_code
    if users.email in user_db:  # FIXED: Changed .mail to .email
        raise HTTPException(status_code=400, detail='Email already registered')
    
    # Saves your clean nested database dictionary structure
    user_db[users.email] = {
        'email': users.email,
        'password': hashpass(users.password)
    }
    return {'message': 'User created successfully'}

# 3. LOGIN ENDPOINT
@bb.post('/login',response_model=users_verify)  # FIXED: Added the mandatory '/login' path string here
def login(seco: users_login):
    # FIXED: Safely fetch the user dictionary out of the keys first
    db_user = user_db.get(seco.email)
    if not db_user:
        raise HTTPException(status_code=401, detail='Invalid email or password')
    
    # FIXED: Reached inside db_user to grab the hashed password string safely
    if not hasverify(seco.password, db_user['password']):
        raise HTTPException(status_code=401, detail='Invalid email or password')
    
    # Generate token passport string
    token = jwt_te({'sub': seco.email})
    
    # FIXED: Changed the key name to 'access_token' to match global web standards
    return {'access_token': token, 'token_type': 'bearer'}

# 4. SECURITY GUARD DEPENDENCY
def get_current_login(token: str = Depends(nothing)):
    checker = err_ch(token)
    if checker is None:
        raise HTTPException(status_code=401, detail='Invalid or expired token')  # FIXED: Added status_code
    return checker

# 5. PROTECTED ROUTE
@bb.get('/me')  # FIXED: Added the mandatory '/me' path string here
def okay(current_user: str = Depends(get_current_login)):
    return {'email': current_user, 'detail': 'logged in'}
