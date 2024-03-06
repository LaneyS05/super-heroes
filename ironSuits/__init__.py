from flask import Flask, render_template
from .ironman import bp as ironman_bp  # Absolute import

def create_app():
    app = Flask(__name__)      
    app.register_blueprint(ironman_bp)

    @app.route('/')
    def hello():
        return render_template('index.html')

    return app       
