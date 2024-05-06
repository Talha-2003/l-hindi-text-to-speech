import csv
import json

# Load the combined CSV data
with open('combined.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Split data into training and validation sets (80% train, 20% val)
split_index = int(len(data) * 0.8)
train_data = data[:split_index]
val_data = data[split_index:]

# Save the training data to a JSON file in the '1.project' directory
with open('1.project/train_data.json', 'w') as train_json:
    json.dump(train_data, train_json, ensure_ascii=False, indent=2)

# Save the validation data to a JSON file in the 'text_project' directory
with open('text_project/val_data.json', 'w') as val_json:
    json.dump(val_data, val_json, ensure_ascii=False, indent=2)

