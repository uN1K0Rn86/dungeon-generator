# User Instructions

## Installation

1. Navigate to a suitable directory and clone this repository:
```
git clone https://github.com/uN1K0Rn86/dungeon-generator.git
```

2. Navigate to the directory containing the app:
```
cd dungeon-generator
```

3. Install dependencies:
```
poetry install
```

4. Run the application:
```
python3 src/index.py
```

## Using the Application

Follow the instructions given by the application.

## Tests

Run the tests by navigating to the application's root folder and running the command
```
poetry run pytest
```

To see a coverage report, run
```
coverage run --branch -m pytest
```

And then
```
coverage report -m
```