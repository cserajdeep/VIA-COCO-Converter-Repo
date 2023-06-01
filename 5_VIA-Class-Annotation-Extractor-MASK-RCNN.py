# Import required modules
import argparse
import json

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input VIA JSON filename")
args = parser.parse_args()
​

# Read input JSON file into memory as dictionary data structure:
via_data = {}
with open(args.input, 'r') as f:
  via_data = json.load(f)
​

# Filter annotations by desired class label ("car" in this example):
car_annotations = [a for a in via_data['regions'] if a['region_attributes']['class'] == 'car']
​

# Update regions list of original data dict with only car annotations:
via_data['regions'] = car_annotations
​
# Write updated output JSON file:
with open('output.json', 'w') as f:
  json.dump(via_data, f)
