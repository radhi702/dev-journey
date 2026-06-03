import sys
import json

# Read data from command line argument
raw_data = sys.argv[1]
data = json.loads(raw_data)

# Process the data
results = []
for item in data:
    results.append({
        'name': item.get('name', '').upper(),
        'email': item.get('email', '').lower(),
        'status': 'valid' if '@' in item.get('email', '') else 'invalid'
    })

# Print results as JSON (n8n will read this output)
print(json.dumps(results))
