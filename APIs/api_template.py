from flask import Flask, request

# Flask is a class

app = Flask(__name__) # building a flask app object using __init__()

SampleList = [
    {
        "id": 123,
        "name": "name1",
        "job": "job1"
    },
    {
        "id": 456,
        "name": "name2",
        "job": "job2"
    },
    {
        "id": 789,
        "name": "name3",
        "job": "job3"
    }
]

@app.get('/name/<int:id>') # if any user sends this get request
def get_name_by_id(id):
    for member in SampleList:
        if member["id"] == id:
            return member["name"] # return this dict

@app.get('/job/<int:id>')
def get_job_by_id(id):
    for member in SampleList:
        if member["id"] == id:
            return member["job"] # return this val

@app.post('/add-member') #need to add a Body in raw mode
def add_member():
    member = request.json #takes the body and converts it to json
    # validation
    SampleList.append(member)
    return SampleList

@app.put('/change-member/<int:id>')
def change_member(id):
    new_member = request.json # take the new member
    for i in range(len(SampleList)):
        if SampleList[i]["id"] == id: # find the member
            SampleList.pop(i) # pop the member
            SampleList.insert(i, new_member) # add new member
            return SampleList
    return {"id not found": id}

@app.delete('/delete/<int:id>')
def delete_by_id(id):
    for member in SampleList:
        if member.get('id') == id:
            SampleList.remove(member)
            return SampleList
    return {"id not found": id}

@app.delete('/del-members')
def delete_all():
    SampleList.clear()
    return {"message":"Done"}

app.run(host='0.0.0.0', port=5000, debug=True) #run the app (port=5000,host='0.0.0.0.0')
