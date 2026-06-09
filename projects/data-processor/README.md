# Data Processor

Reads a JSON array from a command-line argument, normalises name and email fields,
and prints the result as JSON. Designed to be called from n8n.

## Run

```bash
python src/data_processor.py '[{"name":"Radhika","email":"x@y.com"}]'
```
