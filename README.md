# boomin-beats
Ryan's Boomin' Beats


## Virtual Environment
 1. Create Virtual Environment
    python -m venv ~/.venv/ryans-boomin-beats-venv
 2. Activate the Virtual Environment~
    - Git Bash
        source ~/.venv/ryans-boomin-beats-venv/Scripts/activate
    - Powershell
        ~\.venv\ryans-boomin-beats-venv\Scripts\activate.ps1
    - CMD
        ~\.venv\ryans-boomin-beats-venv\Scripts\activate.bat

## Django
### Download Django in Virtual Environment
    python -m pip install Django

### Start Django Project
    cd src/web/
    django-admin startproject backend

### Run Server
- Development Server
    python manage.py runserver
- Specify Port
    python manage.py runserver 8000






## Links
- Django
    https://docs.djangoproject.com/en/4.2/intro/tutorial01/