import json

def validate_json_file(json_string):
    try:
        data = json.loads(json_string)
        print(f"valid JSON: {data}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")

#Test
validate_json_file('{"name": "siddiq", "age": 25}')       # Valid
validate_json_file("{name: siddiq, age: 25}")             # Invalid