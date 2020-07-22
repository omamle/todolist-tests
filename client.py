import requests

SERVER_URL = "http://localhost:5000/{PATH}"


def request(request_info):
    """
    Wrapper to send a request to the server, according to request_info.
    :param request_info: a tuple in the following format -
                        (request_method, url, params)
                        each detailed as inner_param below.
    :inner_param request_method: a http request type from requests.
                        for example: requests.get
    :inner_param url: the URL to send request to
    :inner_param params: additional parameters to the request.
                        (if none - {} or None)
    :returns: the json response from the server
    :raises AssertionError: if request_info  length isn't 3
    :raises ConnectionError: when can't connect to server TODO:
    :raises AssertionError: if response status code isn't 200
    """
    assert len(request_info) == 3, "Missing parameters"
    request_method, url, params = request_info
    try:
        r = request_method(url, json=params)
    except requests.exceptions.ConnectionError:
        raise requests.exceptions.ConnectionError, \
              "Failed to connect to server"

    assert r.status_code == 200, "Error {}".format(r.status_code)

    return r.json()


def list_tasks():
    return (requests.get, SERVER_URL.format(PATH="tasks"), None)


def get_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    return (requests.get, SERVER_URL.format(PATH=path), None)


def create_task(task_name, completed):
    params = {"task": task_name, "completed": completed}
    return (requests.post, SERVER_URL.format(PATH="tasks"), params)


def modify_task(task_id, task_name, completed):
    params = {"task": task_name, "completed": completed}
    path = "tasks/{ID}".format(ID=task_id)
    return (requests.put, SERVER_URL.format(PATH=path), params)


def task_completed(task_id):
    path = "tasks/{ID}/completed".format(ID=task_id)
    return (requests.post, SERVER_URL.format(PATH=path), None)


def task_incomplete(task_id):
    path = "tasks/{ID}/incomplete".format(ID=task_id)
    return (requests.post, SERVER_URL.format(PATH=path), None)


def delete_task(task_id):
    path = "tasks/{ID}".format(ID=task_id)
    return (requests.delete, SERVER_URL.format(PATH=path), None)
