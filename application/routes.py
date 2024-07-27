from flask import current_app as app
from flask_security import current_user, auth_required, roles_required

@app.get('/admin')
@auth_required('token')
@roles_required('admin')
def admin_dashboard():
    
    return f"Welcome, Your are in Admin Dashboard"