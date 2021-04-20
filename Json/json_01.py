
PYTHON JASON TO PYTHON OBJECT
import json

json_sample = '{ "name" : "David" , "class": "I" , "age" : 6 }'
json_python_object = json.loads(json_sample)

print("JSON data")
print(json_python_object)

print("Name: ", json_python_object['name'] )
print("Class: ", json_python_object['class'] )
print("Age: ", json_python_object['age'] )


PYTHON OBJECT TO JSON

import json

python_object = { "name" : "David" , "class" : "i" , "age" : 16 }

#checking type
# dictionary
print(type(python_object))

json_object = json.dumps(python_object)

print(type(json_object))

print(json_object)


######################

json file '{ " " : " " }'
python object { " " : " " } dictionary

json.dumps or json.loads 
dictionary { " " : " " }
list [ " " , " "]
string " "
int 123
float 123.44
boolean  True , False
None None


json.dumps( variable , sory_keys = (True,False) , indent = integer )


#

import json

#creating dictionary
python_object = { "name" : "John" , "age" : 19 , "address" : "nort west south east" }   
print (python_object)

print(json.dumps(python_object, sort_keys = True , indent = 4))


import json
json_int = "1234"

python_int_object = json.loads(json_int)

print(type(python_int_object))


import json

with open('states.json') as j:
    state_data = json.load(j)

#    and load to object using with
#    with is will auto close connection  

open json file 

for state in state_data['state']:
    del ['area_codstatee']

with open('new_state_no_AC.json', 'w') as n:
    json.dump(state_data, n , indent=2 )


import json

def encode_complex(object):
    if isinstance(object,complex):
        return [object.real, object.imag]
    raise TypeError(repr(object) + " is not JSON serialized")

complex_obj = json.dumps( 2+ 3j , default=encode_complex)
print(complex_obj)

dint get that one

json unique key will replay same key  and will not show the repaced value

Original Python object:
{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}

Unique Key in a JSON object:
{'a': 4, 'b': 2}
 

