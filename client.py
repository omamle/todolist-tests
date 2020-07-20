import requests

SERVER_URL = "http://localhost:5000/{PATH}"


def list_tasks():
    r = requests.get(SERVER_URL.format(PATH="tasks"))
    return r.json()


def get_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.get(SERVER_URL.format(PATH=path))
    return r.json()


def create_task(task_name, completed):
    params = {"task": task_name, "completed": completed}
    r = requests.post(SERVER_URL.format(PATH="tasks"), json=params)
    return r.json()


def modify_task(task_id, task_name, completed):
    params = {"task": task_name, "completed": completed}
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.put(SERVER_URL.format(PATH=path), json=params)
    return r.json()


def task_completed(task_id):
    path = "tasks/{ID}/completed".format(ID=task_id)
    r = requests.post(SERVER_URL.format(PATH=path))
    return r.json()


def task_incomplete(task_id):
    path = "tasks/{ID}/incomplete".format(ID=task_id)
    r = requests.post(SERVER_URL.format(PATH=path))
    return r.json()


def delete_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    r = requests.delete(SERVER_URL.format(PATH=path))
    return r.json()


def main():
    try:
        print list_tasks()
        print get_task("zJX8KXIe")
        print create_task("task_555", False)
        print list_tasks()
        print delete_task("zJX8KXIe")
        print list_tasks()
        print task_completed("LmtlN1Bl")
        print list_tasks()
        print task_incomplete("LmtlN1Bl")
        print list_tasks()
    except requests.exceptions.ConnectionError:
        print "Failed to connect to server."


if __name__ == "__main__":
    main()
