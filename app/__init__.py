from flask import Flask
from app.routes import main_routes  # Import Blueprint dari main.py

app = Flask(__name__)
app.register_blueprint(main_routes)  # Mendaftarkan Blueprint ke aplikasi
