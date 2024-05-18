import json

# Load the original JSON data
with open('exercises.json', 'r') as f:
    data = json.load(f)

# Create a new list of dictionaries, each with only the 'name' and 'equipment' fields
new_data = [{'name': exercise['name'], 'equipment': exercise['equipment']} for exercise in data]

# Write the new data to a new JSON file
with open('out.json', 'w') as f:
    json.dump(new_data, f, indent=1)

