# test_rbac.py
from auth import create_token, get_current_user, require_role

# create tokens for different roles
admin_token = create_token('admin@test.com', 'admin')
user_token = create_token('user@test.com', 'user')

print(admin_token)
print(user_token)