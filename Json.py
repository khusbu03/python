# JOSN in python

import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}

# Convert Python object to JSON string
jsonString=json.dumps(data)
print("Data",jsonString)


# Convert JSON string to Python object
data = json.loads(jsonString)
print("converting the data from Json back to python",data)