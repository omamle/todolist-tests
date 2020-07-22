import requests

SERVER_URL = "http://localhost:5000/{PATH}"


def list_tasks():
    r = requests.get(SERVER_URL.format(PATH="tasks"))

    assert r.status_code == 200, \
           "Error {} in list_tasks".format(r.status_code)
    return r.json()


def get_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.get(SERVER_URL.format(PATH=path))

    assert r.status_code == 200, \
           "Error {} in get_task".format(r.status_code)
    return r.json()


def create_task(task_name, completed):
    params = {"task": task_name, "completed": completed}
    r = requests.post(SERVER_URL.format(PATH="tasks"), json=params)

    assert r.status_code == 200, \
           "Error {} in create_task".format(r.status_code)
    return r.json()


def modify_task(task_id, task_name, completed):
    params = {"task": task_name, "completed": completed}
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.put(SERVER_URL.format(PATH=path), json=params)

    assert r.status_code == 200, \
           "Error {} in modify_task".format(r.status_code)
    return r.json()


def task_completed(task_id):
    path = "tasks/{ID}/completed".format(ID=task_id)
    r = requests.post(SERVER_URL.format(PATH=path))

    assert r.status_code == 200, \
           "Error {} in task_completed".format(r.status_code)
    return r.json()


def task_incomplete(task_id):
    path = "tasks/{ID}/incomplete".format(ID=task_id)
    r = requests.post(SERVER_URL.format(PATH=path))

    assert r.status_code == 200, \
           "Error {} in task_incomplete".format(r.status_code)
    return r.json()


def delete_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.delete(SERVER_URL.format(PATH=path))

    assert r.status_code == 200, \
           "Error {} in delete_task".format(r.status_code)
    return r.json()
