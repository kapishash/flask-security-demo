from flask import current_app as app
from flask_security import current_user, auth_required, roles_required, roles_accepted

@app.get('/admin')
@auth_required('token')
@roles_required('admin')
def admin_dashboard():
    
    return f"Welcome, Your are in Admin Dashboard"

@app.get('/student')
@auth_required('token') # session, basic, token
# @roles_required('student', 'instructor') # roles required has and condition
@roles_accepted('student', 'instructor') # roles accepted has or condition
def student_dashboard():
    roles = [role.name for role in current_user.roles]
    return {
        "user": current_user.email,
        "roles": roles
    }