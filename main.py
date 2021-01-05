import connexion
from flask import Flask, render_template

# crate an app instance (based on Flask)
app = connexion.App(__name__, specification_dir='./')
# configure API endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
    """Opens home.html on localhost:5000/"""
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
