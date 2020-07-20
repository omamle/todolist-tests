import client


def test_list_tasks():
    return True


def test_get_task():
    pass


def test_create_tasks():
    return True


def test_modify_task():
    return True


def test_task_complete():
    pass


def test_task_incomplete():
    pass


def test_delete_tasks():
    pass


def run_tests():
    tests = [test_list_tasks,
             test_get_task,
             test_create_tasks,
             test_modify_task,
             test_task_complete,
             test_task_incomplete,
             test_delete_tasks]

    success_count = 0

    for test in tests:
        if test():
            print "TEST {} PASSED".format(test.func_name)
            success_count += 1
        else:
            print "TEST {} FAILED".format(test.func_name)

    print "PASSED {}/{} TESTS".format(success_count, len(tests))


if __name__ == "__main__":
    run_tests()
