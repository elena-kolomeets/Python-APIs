"""
opens Swagger UI (API interface) on homepage

This API was built with the help of the Real Python tutorial:
https://realpython.com/flask-connexion-rest-api/
"""
from flask import redirect
from config import connex_app

# get the app instance created in config.py
app = connex_app
# configure API endpoints from yml file
app.add_api('swagger.yml')


@app.route('/')
def home():
    """Opens Swagger UI"""
    return redirect("/api/ui/#/People")


if __name__ == "__main__":
    app.run(debug=True)
