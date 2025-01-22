employee = {}

i = 1
while True:
    name = (input("Name : "))

    if not name:
        break

    mobile = input("Enter Mo No")
    email = input("Enter Email")
    city = input("Enter City")


    employee[f'employee_{i}'] = {

        'name' : name,
        'mobile' : mobile,
        'email': email,
        'city' : city
    }
    
    i = i+1
for name,value in employee.items():
    print(f"{name} : {value}")