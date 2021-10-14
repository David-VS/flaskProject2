from flask import Flask, request
from person import Person

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.get("/username/<pathvariable>")
def get_user(pathvariable):
    return "t'is " + pathvariable

@app.post("/sum")
def sum():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    sum = a+b
    return str(sum)

@app.get("/person")
def get_person():
    person = Person("Daan Banaan", 30)
    person_json = {
        "name":person.name,
        "age":person.age
    }
    return person_json

if __name__ == '__main__':
    app.run()
