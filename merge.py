def merge_data(google_data, microsoft_data):
    merged_data = {}
    merged_data['files'] = google_data.get('items', []) + microsoft_data.get('value', [])
    return merged_data