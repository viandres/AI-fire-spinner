import json

def load_json(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, file_path):
    """
    Save data to a JSON file.

    Args:
        data (dict): Data to save.
        file_path (str): Path to the JSON file.

    Returns:
        str: Path to the saved JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    return file_path

def normalize_pose_data(pose_data):
    """
    Normalize pose data for consistent processing.

    Args:
        pose_data (list): List of dictionaries with pose information.

    Returns:
        list: Normalized pose data.
    """
    normalized_data = []
    for data in pose_data:
        normalized_data.append({
            'frame': data['frame'],
            'position': {
                'x': data['position']['x'],
                'y': data['position']['y'],
                'z': data['position']['z']
            },
            'rotation': {
                'x': data['rotation'].get('x', 0),
                'y': data['rotation'].get('y', 0),
                'z': data['rotation'].get('z', 0)
            }
        })
    return normalized_data
