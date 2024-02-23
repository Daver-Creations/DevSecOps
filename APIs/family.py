from flask import Flask, request

# Flask is a class

app = Flask(__name__) # building a flask app object using __init__()

family = [
    {
        "first-name": "Dave",
        "last-name": "Raisman",
        "id": 0
    },
    {
        "first-name": "Sarah",
        "last-name": "Kaplan",
        "id": 1
    },
    {
        "first-name": "Chasey",
        "last-name": "Raisman-Kaplan",
        "id": 2
    }
]

@app.get('/first-name/<int:id>') # if any user sends this get request
def get_name(id):
    for member in family:
        if member["id"] == id:
            return member["first-name"] # return this value

@app.get('/last-name/<int:id>')
def get_surname(id):
    for member in family:
        if member["id"] == id:
            return member["last-name"]

@app.get('/full-name/<int:id>')
def get_fullname(id):
    for member in family:
        if member["id"] == id:
            first = member["first-name"]
            last = member["last-name"]
            return f"{first} {last}"
        
@app.post('/member')
def add_member():
    member = request.json #takes the body and converts it to json
    member['id'] = family[-1]['id']
    # validation
    family.append(member)
    return family

@app.put('/member/<int:id>')
def change_member(id):
    new_member = request.json # take the new member
    for i in range(len(family)):
        if family[i][id] == id: # find the member
            family.pop(i) # pop the member
            family.insert(i, new_member) # add new member

@app.delete('/users')
def delete_all():
    family.clear()
    return {"message":"Done"}

@app.delete('/users/<int:user_id>')
def delete_by_id(user_id):
    for member in family:
        if member.get('id') == user_id:
            family.remove(member) 
            # replace the users with new list of userts that dont have the same id as the user_id param
            # TODO: [user for user in users if user['id']!= user_id ] 
    return {"message": "Done"}

app.run() #run the app (port=5000,host='0.0.0.0.0')