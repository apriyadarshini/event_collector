How to run Event Collector locally:

1) Install the packages present in requirements.txt
2) import create_app from EventCollector
3) Initialize the app var to create_app()
4) create all tables within this app context by importing all the tables present in EventCollector.models
5) export FLASK_APP=run.py
6) flask run --host=0.0.0.0
7) Open http://localhost:5000/ in a web browser


To deploy on AWS we can use NGINX for parsing static contents like css and gunicorn to handle python code

We can update the NGINX config file appropriately as above

gunicorn lets us specify multiple worker threads which can handle multiple requests

Complete detail about the project is present in EventCollector.docx
