# MeX-URL-shortener
Basic URL shortener web app for Google App Engine - python.
* Project file structure :
  - lib folder conatin project apps (user app, short_url app)
  - each app folder composed of :
    - data_models.py (contain ndb models).
    - request_handlers.py (contain webapp2 req handler classes).
    - urls.py (contains url mapping of the app).
  - extlib folder contains 3rd party libraries.
  - style folder contains style static files:
    - css (css files).
    - js (javascript files).
    - fonts (font files).
    - templates (html template files [jinja2 templates]).
  - locale folders contains translation files :
    - you can produce translation files by babel.

* TODO : 
  - Copmlete endpoints Api. ('/lib/short_url/api_req_handlers.py')
  - build front-end for user area.

* How to deply on local machine :
  - download the project zip.
  - download Google App Engine Python Launcher and install it.
  - extract the project zip file.
  - cd to project folder.
  - use comand : "devappserver.py app.yaml".

* How to deploy online :
  - create google cloud application.
  - edit app.yaml file with your created project id.
  - deply online with this command : "appcfg.py update app.yaml"

