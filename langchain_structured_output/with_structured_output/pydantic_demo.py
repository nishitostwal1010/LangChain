from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# class Student(BaseModel):
#     name: str

# Incorrect Method: Not safe as it is just assigns plain dictionary
# student: Student = {'name': 'nishit'}
# print(student)
# print(type(student)) # This will return dict

# Correct Method 2: Safe - Runtime validation, Autocomplete support, 
# new_student = {'name': 'nishit'}
# student = Student(**new_student)
# print(student)
# print(type(student)) # This will return Student which inherits BaseModel so it is a pydantic object

# Validating if wrong data type is there - 

# new_student = {'name': 10} # This will throw error because of data type validation
# student = Student(**new_student)
# print(student)
# print(type(student))

#####

# To set default values use - 

# class Student(BaseModel):
#     name: str = 'nishit'

# new_student = {}
# student = Student(**new_student)
# print(student) # It prints nishit as by default name = nishit
# print(student.name) # As Student is class so you can use it's argument by using object_name.argument_name

#####

# To use Optional -

# class Student(BaseModel):
#     name: str = 'nishit'
#     age: Optional[int] = None # You need to specify if key's value is not present then what will be printed

# # new_student = {'name': 'gyro', 'age': 21} => name='gyro' age=21
# # new_studnet = {'age': 21}
# new_student = {}
# student = Student(**new_student)
# print(student)

#####

# EmailStr validation -

# class Student(BaseModel):
#     name: str = 'nishit'
#     age: Optional[int] = None
#     email: EmailStr

# # new_student = {'email': 'abc'}
# new_student = {'email': 'abc@gmail.com'}
# student = Student(**new_student)
# print(student)

#####

# Using field function - (To give constaints, default values, add custom description, etc)

class Student(BaseModel):
    name: str = 'nishit'
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0, lt=10, default=9.38, description='A decimal value representing the cgpa of the student')

# new_student = {'cgpa': 12}
new_student = {}
student = Student(**new_student)
print(student)


# To convert Pydantic object to dictionary object -
student_dict = dict(student)
print(student_dict['cgpa'])


# To convert Pydantic object to json object -
student_json = student.model_dump_json()
print(student_json)

