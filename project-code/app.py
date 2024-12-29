# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get database configuration from environment variables
db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('POSTGRES_HOST')

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://adham:1234@postgres-service/devopsDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Rest of the application code remains the same...

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
