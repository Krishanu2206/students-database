from fastapi import FastAPI, Path 
from typing import Optional 
from pydantic import BaseModel

app=FastAPI()

# GET - GET AN INFO
# POST - CREATE SOME NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING

students={
    1:{
        "name" : "John",
        "age" : 17,
        "year" : "year12"
    }
} #dictionary of dictionaries 

class Student(BaseModel):
    name:str
    age:int
    year:str

class updatestudent(BaseModel):
    name:Optional[str] = None
    age:Optional[int] = None
    year:Optional[str] = None


@app.get("/")
def index():
    return {"name" : "First Data"}
 
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description = "HELLO", gt=0, lt=4)):
    return students.get(student_id)


@app.get("/get-by-name/{student_id}") 
def get_student(*, student_id : int, name : Optional[str] = None, test: int):
    for student_id in students:
        if students.get(student_id).get("name") == name:
            return students.get(student_id)
    return {"data" : "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"error" : "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student-id}")
def update_student(student_id : int, student : updatestudent ):
    if student_id not in students:
        return {"error" : "student not exists"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]
    
@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "Does not exist"}
    
    del students[student_id]
    return {"Data" : "Student deleted succesfully"}


