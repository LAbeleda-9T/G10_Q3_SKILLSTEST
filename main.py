# account creation
from pyscript import display, document

def verify_account(e):
    document.getElementById('output').innerHTML = ''  # Clear previous output

    password = document.getElementById('password').value  # Get password as a string

    if len(password) < 8:
        display('Password must be at least 8 characters long.', target='output')
    else:
        display('Account created successfully!', target='output')