# swarm-playground

Install dependencies

```
pdm install
```

Remember to set `OPEN_API_KEY` to `.env` file.

Run the get temperature
```
export PYTHONPATH=src

pdm run python src/swarm_playground/get_temperature/main.py
```

Run the employee support
```
export PYTHONPATH=src

pdm run python src/swarm_playground/employee_support/main.py
```

Run test employee support
```
pdm run python -m pytest src/swarm_playground/employee_support/eval.py
```
