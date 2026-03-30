a={"key":"value","list":[1,2,3,4],"car":"BMW M4","bike":"s1000r"}
value_to_find = "BMW M4"
for key, value in a.items():
    if value == value_to_find:
        print(key)




students = [
    {"name":"Amit","marks":80},
    {"name":"Ravi","marks":45},
    {"name":"Neha","marks":90}
]
for s in students:
    if s["marks"]>=60:
        print(s["name"])



students = {"Amit":80,"Ravi":45,"Neha":90}
for key,value in students.items():
    x=int(value)
    if value >=60:
        print(key)



a={"brand":"cetaphil","product":"moisturizer","price":"₹500"}

value_to_find = "cetaphil"

for key, value in a.items():
    if value == value_to_find:
        print(key)
   


a={"brand":"cetaphil","product":"moisturizer","price":"₹500"}
print(list(a.keys())[2])


