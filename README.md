# boomin-beats
Ryan's Boomin' Beats


## Virtual Environment
 1. Create Virtual Environment
    python -m venv ~/.venv/ryans-boomin-beats-venv
 2. Activate the Virtual Environment~
    ##### Git Bash
        source ~/.venv/ryans-boomin-beats-venv/Scripts/activate
    ##### Powershell
        ~\.venv\ryans-boomin-beats-venv\Scripts\activate.ps1
    ##### CMD
        ~\.venv\ryans-boomin-beats-venv\Scripts\activate.bat

## Django
### Download Django in Virtual Environment
    python -m pip install Django

### Start Django Project
    cd src/web/
    django-admin startproject backend

### Run Server
##### Development Server
    python manage.py runserver
##### Specify Port
    python manage.py runserver 8000
##### Fix 'Watching for file changes with StatReloader
    python manage.py runserver --noreload

### Add Django App to Project
    python manage.py startapp <app_name>


## Svelte Kit
### Install npm
    npm create svelte@latest <app_name>
    cd <app_name>
    npm i

### Run Server
    npm run dev

## NPM Packages

### Spotipy
    pip install spotipy --upgrade
## d3-shape
    npm install d3-shape
## d3-scale
    npm install d3-scale
## Layercake
    npm install --save layercake

## Links
### Django
    - https://docs.djangoproject.com/en/4.2/intro/tutorial01/
### Spotipy
    - https://spotipy.readthedocs.io/en/2.22.1/
    - https://www.javatpoint.com/spotify-api-python
    - https://www.youtube.com/watch?v=cU8YH2rhN6A
### Styling
    - https://svelte.dev/repl/cb6bb95b7d1549f7be8d8fc7258ea1da?version=3.46.2
    

### Youtube
    - https://www.youtube.com/watch?v=G_WFk4wg9fk
    
    

## Styles
### Color Palette
    - Light Blue: #5ec9ff
    - Purple: #a235ff
    - Dark Gray: #242424
    - Gray: #444444
