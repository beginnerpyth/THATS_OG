from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

SECRET_KEY = 'mysecretkey'
ALGORITHM = 'HS256'

def create_token(email: str, role: str):
    data = {
        'sub': email,
        'role': role,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
#When a user hits your route, FastAPI looks inside the function arguments of get_current_user.
# It sees Depends(oauth2_scheme).FastAPI instantly pauses your function from running.It reaches into the incoming internet traffic, 
# grabs the Authorization header, and strips away the word "Bearer "
# .It takes the remaining scrambled token string and drops it directly into your token variable.
#It will only grab the hidden HTTP header.......
# if you explicitly add Depends(oauth2_scheme) (or another dependency that calls it)  to that endpoint.
#once it uvicorn july20:app --reload runs it runs untl server shut downs and when user logins it pass the data

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get('sub')
        role = payload.get('role')
        if email is None:
            raise HTTPException(status_code=401, detail='Invalid token')
        return {'email': email, 'role': role}
    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid token')

def require_role(role: str):
    def checker(current_user: dict = Depends(get_current_user)):
        if current_user['role'] != role:
            raise HTTPException(
                status_code=403,
                detail=f'only {role}s can access this'
            )
        return current_user
    return checker