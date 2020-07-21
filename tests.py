import requests
import client


def test_list_tasks():
    tasks = client.list_tasks()

    return True


def test_get_task():
    success = False
    tasks = client.list_tasks()

    # try get  an existing task
    if len(tasks) > 0:
        existing_id = tasks[0]["id"]
        task = client.get_task(existing_id)
        success = tasks[0]["task"] == task["task"] and \
            tasks[0]["completed"] == task["completed"]
    # try to get non-existing ID
    # task = client.get_task("Non_Existent")
    # print task

    return success


def test_create_tasks():
    old_tasks = client.list_tasks()
    new_task = client.create_task("new_task", False)
    new_tasks = client.list_tasks()

    new_id = new_task["task_id"]

    return any([new_id == task["id"] for task in new_tasks]) and \
        not any([new_id == task["id"] for task in old_tasks])


def test_modify_task():
    success = True
    tasks = client.list_tasks()

    if len(tasks) > 0:
        old_task = tasks[0]
        client.modify_task(old_task["id"], "modified_task", True)
        new_task = client.get_task(old_task["id"])
        success = new_task["task"] == "modified_task" and \
            new_task["completed"] is True

    return success


def test_task_complete():
    task_id = client.create_task("incomplete_task", False)["task_id"]
    client.task_completed(task_id)
    complete = client.get_task(task_id)

    # make sure marking complete again doesn't affect it
    client.task_completed(task_id)
    still_complete = client.get_task(task_id)

    return complete["completed"] and still_complete["completed"]


def test_task_incomplete():
    task_id = client.create_task("complete_task", True)["task_id"]
    client.task_incomplete(task_id)
    incomplete = client.get_task(task_id)

    # make sure marking incomplete again doesn't affect it
    client.task_incomplete(task_id)
    still_incomplete = client.get_task(task_id)

    return not incomplete["completed"] and not still_incomplete["completed"]


def test_delete_tasks():
    task_id = client.create_task("to_delete", False)["task_id"]
    list_before = client.list_tasks()
    client.delete_task(task_id)
    list_after = client.list_tasks()

    # make sure task was in list before and isn't in list after
    deleted = any([task_id == task["id"] for task in list_before]) and \
        not any([task_id == task["id"] for task in list_after])

    # also make sure only one task got deleted
    return len(list_after) == len(list_before) - 1 and deleted


def run_tests():
    tests = [test_list_tasks,
             test_get_task,
             test_create_tasks,
             test_modify_task,
             test_task_complete,
             test_task_incomplete,
             test_delete_tasks]

    success_count = 0

    try:
        for test in tests:
            try:
                if test():
                    print "TEST {} PASSED".format(test.func_name)
                    success_count += 1
                else:
                    print "TEST {} FAILED".format(test.func_name)
            except AssertionError as error:
                print error.message, " in {}".format(test.func_name)
    except requests.exceptions.ConnectionError:
        print "Failed to connect to server."
        print "Make sure it's running on {}".format(client.SERVER_URL)
        print "or modify SERVER_URL in client.py accordingly"

    print "PASSED {}/{} TESTS".format(success_count, len(tests))


if __name__ == "__main__":
    run_tests()
