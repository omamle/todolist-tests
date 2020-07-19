import requests

SERVER_URL = "http://localhost:5000/{PATH}"


def list_tasks():
    r = requests.get(SERVER_URL.format(PATH="tasks"))
    return r.json()


def get_task(task_id):
    r = requests.get(SERVER_URL.format(PATH=f"tasks/{task_id}"))
    return r.json()


# create task doesn't use task_id in server.py implementation?
def create_task(task_id, task_name, completed):
    params = {"task": task_name, "completed": completed}
    r = requests.post(SERVER_URL.format(PATH="tasks"), json=params)
    return r.json()


def modify_task(task_id, task_name, completed):
    params = {"task": task_name, "completed": completed}
    r = requests.put(SERVER_URL.format(PATH=f"tasks/{task_id}"), json=params)
    return r.json()


def task_completed(task_id):
    r = requests.post(SERVER_URL.format(PATH=f"tasks/{task_id}/completed"))
    return r.json()


def task_incomplete(task_id):
    r = requests.post(SERVER_URL.format(PATH=f"tasks/{task_id}/incomplete"))
    return r.json()


def delete_task():
    r = requests.delete(SERVER_URL.format(PATH=f"tasks/{task_id}"))
    return r.json()


def main():
    try:
        print(list_tasks())
        print(get_task("zJX8KXIe"))
        print(create_task(123, "task_123", False))
        print(list_tasks())
    except requests.exceptions.ConnectionError:
        print("Failed to connect to server.")


if __name__ == "__main__":
    main()
