# todolist-client
"To Do List" client for Aqua's "To Do List" mock server

## Dependencies:
To install the dependencies of this project, use:
```bash
pip install -r requirements.txt
```
*(installs following packages: pytest, pytest-dependency, requests)*


## Running the tests:
To run the tests simply use -
```bash
pytest test_todolist.py
```
*(inside the directory that test_todolist.py is in)*

to produce more verbose outputs you could use:
```bash
pytest -v -ra test_todolist.py
```
*The tests could take some time to finish (around 1 minute or so)*
