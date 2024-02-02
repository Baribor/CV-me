from flask import Flask
from route import api_base

app = Flask(__name__)
app.register_blueprint(api_base, url_prefix="/api/v1")
app.url_map.strict_slashes = False
print(app.url_map)

if __name__ == "__main__":
    print(app.url_map, "Yeah")
    app.run()
