<img src="./images/banner.png">

# Monty Hall Simulation

The simulation of the famous Monty Hall problem allows you to interact with an interactive dashboard that simulates two scenarios: switching or not switching the chosen door.

## Project Structure

```
monty_hall_problem/
|
|- images - banner.js ...
|- src
|  |- app.py
|  |- monty_hall.py
|- README.md
|- requirements.txt
```

## Requirements

- Python 3.7 or higher
- streamlit

To install the necessary run the below command:

```
pip install -r requirements.txt
```

## Usage


If you are using `Linux`,  `WSL`, and `Mac` use this command to add src path to the PYTHONPATH :

```
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

To start Streamlit dashboard:

```
streamlit run src/app.py
```

## Results

On running the Streamlit application, you will see an input field where you can specify the number of games to simulate. The app will then perform a simulation for each game, both where the contestant switches doors and where they don't. Lastly, the dashboard will display the win percentages dynamically as two separate line charts - showing how the likelihood of winning changes based on your decision to switch or not to switch doors.