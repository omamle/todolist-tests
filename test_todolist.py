import requests
import client
import pytest


@pytest.mark.dependency()
def test_list_tasks():
    tasks = client.list_tasks()
    assert type(tasks) == list


@pytest.mark.dependency(depends=["test_list_tasks"])
def test_create_task():
    old_tasks = client.list_tasks()
    created_task = client.create_task("created", False)
    new_tasks = client.list_tasks()
    new_id = created_task["task_id"]

    # make sure task was created and wasn't there before
    assert any([new_id == task["id"] for task in new_tasks]), "Task not created"
    assert not any([new_id == task["id"] for task in old_tasks])


@pytest.mark.dependency(depends=["test_list_tasks"])
def test_get_task():
    tasks = client.list_tasks()
    assert len(tasks) > 0, "No tasks to get"

    existing_id = tasks[0]["id"]
    task = client.get_task(existing_id)

    assert tasks[0]["task"] == task["task"]
    assert tasks[0]["completed"] == task["completed"]

    # TODO:
    # try to get non-existing ID
    # task = client.get_task("Non_Existent")
    # print task


@pytest.mark.dependency(depends=["test_list_tasks", "test_get_task"])
def test_modify_task():
    tasks = client.list_tasks()
    assert len(tasks) > 0, "No tasks to modify"

    # modify first task in list
    old_task = tasks[0]
    client.modify_task(old_task["id"], "modified_task", True)
    modified_task = client.get_task(old_task["id"])

    assert modified_task["task"] == "modified_task"
    assert modified_task["completed"]


@pytest.mark.dependency(depends=["test_create_task", "test_get_task"])
def test_task_complete():
    task_id = client.create_task("incomplete_task", False)["task_id"]
    client.task_completed(task_id)
    complete = client.get_task(task_id)

    # make sure marking complete again doesn't affect it
    client.task_completed(task_id)
    still_complete = client.get_task(task_id)

    assert complete["completed"]
    assert still_complete["completed"]


@pytest.mark.dependency(depends=["test_create_task", "test_get_task"])
def test_task_incomplete():
    task_id = client.create_task("complete_task", True)["task_id"]
    client.task_incomplete(task_id)
    incomplete = client.get_task(task_id)

    # make sure marking incomplete again doesn't affect it
    client.task_incomplete(task_id)
    still_incomplete = client.get_task(task_id)

    assert not incomplete["completed"] 
    assert not still_incomplete["completed"]


@pytest.mark.dependency(depends=["test_list_tasks", "test_create_task"])
def test_delete_tasks():
    task_id = client.create_task("to_delete", False)["task_id"]
    list_before = client.list_tasks()
    client.delete_task(task_id)
    list_after = client.list_tasks()

    # make sure task was in list before and isn't in list after
    assert any([task_id == task["id"] for task in list_before])
    assert not any([task_id == task["id"] for task in list_after])

    # also make sure only one task got deleted
    assert len(list_after) == len(list_before) - 1
