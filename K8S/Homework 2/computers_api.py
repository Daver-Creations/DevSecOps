from flask import Flask, request
import json
import json_util
from urllib import request


app = Flask(__name__)

FileName = "computers_list.json"
ListFile = json_util.JsonUtil.open_file_in_same_directory(FileName)
ComputersList = json.load(ListFile)

@app.get('/test')
def test_api():
    return '200'

@app.get('/ready')
def ready_api():
    return '200'

@app.get('/healthy')
def is_healthy():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return '200'
    except: 
        return '400'

@app.get('/computers')
def get_computers_list():
    return ComputersList

@app.post('/add-computer') #need to add a Body in raw mode
def add_computer():
    new_computer = request.json
    # TODO: validation
    ComputersList.append(new_computer)
    json_util.JsonUtil.save_file_in_same_directory(FileName ,ComputersList)
    return [{"added": new_computer}]

@app.put('/change-computer/<int:id>')
def change_computer(id):
    new_computer = request.json
    for i in range(len(ComputersList)):
        if ComputersList[i]["id"] == id:
            ComputersList.pop(i)
            ComputersList.insert(i, new_computer)
            return [{"changed": new_computer}]
    return {"id not found": id}

@app.delete('/delete/<int:id>')
def delete_by_id(id):
    for computer in ComputersList:
        if computer.get('id') == id:
            ComputersList.remove(computer)
            return {"removed": id}
    return {"id not found": id}

if __name__ == "__main__":
    app.run(debug=True)
#app.run(host='0.0.0.0', port=5000, debug=True) #run the app (port=5000,host='0.0.0.0.0')