# Smart Thermostat (Python CLI)

A simple Python CLI project that simulates a smart thermostat.  
Built to practice clean architecture, OOP, configuration-driven logic, error handling, and testing.

---

## What this project does

- Simulates reading temperature from a sensor
- Decides thermostat mode:
  - Heat
  - Cool
  - Off (neutral)
- Runs continuously in a loop
- Logs temperature and mode to a file
- Uses a JSON config for temperature thresholds
- Includes basic unit tests

---

## Project structure

- `src/`
  - `controller.py` – core decision logic
  - `sensor.py` – temperature sensor (simulated)
  - `modes.py` – Heat / Cool / Off mode classes
  - `logger.py` – file logging
  - `exceptions.py` – custom exceptions
  - `temp_thresholds.json` – configuration file
- `tests/`
  - `test_controller.py` – tests for mode selection logic
- `cli.py` – entry point for running the app

---

## How the thermostat decides modes

Based on `temp_thresholds.json`:

- Temperature < heating minimum → **Heat**
- Temperature ≥ cooling minimum → **Cool**
- Temperature in between → **Off**

The neutral range is implicit (anything not heating or cooling).

---

## How to run

Activate virtual environment:

```bash
source .venv/bin/activate
```

## Run the app:

```bash
python cli.py
```

## Stop the app:

```bash
Ctrl + C
```

---

## Logging

Logs are written to a file named `thermostat.log` in the current directory.

### Example log entry:

```bash
2025-12-14 20:43:53 | 31 | Cooling Mode
```

---

## Testing

```bash
pytest
```
---

## Purpose of this project

To practice clean architecture, OOP, configuration-driven logic, error handling, and testing.

---

## Author

[github.com/kishensjain](https://github.com/kishensjain)

[linkedin.com/in/kishen-s](https://www.linkedin.com/in/kishen-s/)
