from auth import jwt_te
from auth import jwt_te,err_ch

# create a token
token = jwt_te({'sub': 'user@example.com'})
print(token)

# verify the real token
email =err_ch(token)
print(email)   # user@example.com

# verify a fake token
fake =err_ch('thisisafaketoken')
print(fake)    # None
joji=jwt_te({'sub':'bbc@expmle.com'})
print(joji)