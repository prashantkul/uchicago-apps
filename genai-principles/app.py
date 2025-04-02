import os
from flask import Flask
from pymilvus import MilvusClient
import json

app = Flask(__name__)

# Zilliz Cloud connection details
ZILLIZ_CLOUD_URI = "https://in03-e8fcec4b8124486.serverless.gcp-us-west1.cloud.zilliz.com"
ZILLIZ_CLOUD_TOKEN = os.environ.get("ZILLIZ_CLOUD_TOKEN") # "e148f86e45fe83290b4360076a3a67fce56ab791f91cf91aa6830d3a3c110afea5bac9de0ee847bff4d40b4fc7c82ac5fc42d6b6"
COLLECTION_NAME = "medium_articles"
DIMENSION = 768

# Initialize ZillizVectorDB
zilliz_db = MilvusClient(uri=ZILLIZ_CLOUD_URI, token=ZILLIZ_CLOUD_TOKEN)


def get_zilliz_collection():
    """Gets or creates the Zilliz collection."""
    try:
        collection = zilliz_db.has_collection(COLLECTION_NAME)
        if collection:
            print(f"Successfully connected to existing collection: {COLLECTION_NAME}")
            collection_description = zilliz_db.describe_collection(collection_name=COLLECTION_NAME)
            result_message = json.dumps(collection_description, indent=2)
            return collection, result_message
    except Exception as e:
        error_msg = f"Collection '{COLLECTION_NAME}' not found. Error: {e}"
        print(error_msg)
        return None, error_msg


@app.route("/")
def hello_world():
    """Hello World route with formatted Zilliz interaction."""
    name = os.environ.get("NAME", "World")
    collection, collection_property = get_zilliz_collection()

    html_output = f"""
    <html>
    <head>
        <title>Zilliz Collection Info</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 2rem; }}
            pre {{ background-color: #f4f4f4; padding: 1rem; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Hello, {name}!</h1>
        <h2>Zilliz Interaction</h2>
        <p><strong>Collection Name:</strong> {COLLECTION_NAME}</p>
        <h3>Collection Details:</h3>
        <pre>{collection_property}</pre>
    </body>
    </html>
    """
    return html_output


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
