from pydantic import BaseModel , EmailStr, Field
from typing import Optional, Annotated

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,lt=10,default=5,description="A cumulative grade point average that should be float") 
    #gt : greater than
    #lt : less than

new_student = {'name':'Suyash'}
#Case of implicit type casting (coercion)

s = {'name' :'Nitish','age':'32','email':'abc@gmail.com'} 
# student = Student(**new_student)
student2 = Student(**s)
print(student2)
# print(type(student))

# def show(name,age):
#     print(name,age)

# show(**new_student)
student_json = student2.model_dump_json()
print(student_json)

student_dict = student2.model_dump()
print(student_dict)