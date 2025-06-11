from google.cloud import storage
import json

PROJECT_ID = 'ogcs-av8t-ailaboratory'
BUCKET_NAME = 'hackathon-team2-bucket'
FILE_NAME = 'all_customer_support_analysis.json'

def load_data():
    """Load data from Google Cloud Storage."""
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_NAME)

    data = blob.download_as_text()
    # JSON data to Python dictionary
    data_dict = json.loads(data)
    return data_dict

def edit_data(data_dict, key, value):
    """Edit a specific key in the data dictionary."""
    if key in data_dict:
        data_dict[key] = value
    else:
        raise KeyError(f"Key '{key}' not found in data.")
    return data_dict

def delete_data(data_dict, key):
    """Delete a specific key from the data dictionary."""
    if key in data_dict:
        del data_dict[key]
    else:
        raise KeyError(f"Key '{key}' not found in data.")
    return data_dict

def add_data(data_dict, key, value):
    """Add a new key-value pair to the data dictionary."""
    if key in data_dict:
        raise KeyError(f"Key '{key}' already exists in data.")
    data_dict[key] = value
    return data_dict

def upload_data(data):
    """Upload data to Google Cloud Storage."""
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(FILE_NAME)

    # Convert Python dictionary to JSON string
    json_data = json.dumps(data)
    blob.upload_from_string(json_data, content_type='application/json')
