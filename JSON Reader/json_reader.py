import json

def get_nested_keys(data, parent_key='', separator='.'):
    """
    Recursively get all nested keys from a JSON-like data structure.

    Args:
        data (dict): JSON-like data.
        parent_key (str): Parent key for the current level.
        separator (str): Separator used to join keys.

    Returns:
        list: List of all nested keys.
    """
    nested_keys = []
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            nested_keys.extend(get_nested_keys(value, new_key, separator=separator))
        else:
            nested_keys.append(new_key)
    return nested_keys

try:
    # Read JSON input from the user
    user_input = input("Enter JSON data: ")

    # Replace single quotes with double quotes
    user_input = user_input.replace("'", "\"")

    # Parse the JSON input
    user_json = json.loads(user_input)

    # Get all nested keys from the user's JSON data
    nested_keys = get_nested_keys(user_json)

    # Print the result
    for key in nested_keys:
        print(key)
except json.JSONDecodeError as e:
    print("Error parsing JSON input:", e)
except Exception as e:
    print("An error occurred:", e)
