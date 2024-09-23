import streamlit as st

from src.monty_hall import simulate_games
import time

st.title(":zap: Money Hall Simulation")
st.image("./images/image1.png")
num_games = st.number_input(
    "Enter the number of games to stimulate", min_value=1, max_value=10000
)


col1, col2 = st.columns(2)

col1.subheader("Win percentage without switching")
col2.subheader("win percentage with switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

# Create two lists to hold win percentages for both cases
wins_no_switch = 0
wins_switch = 0


for i in range(num_games):
    # Stimulate one game at time
    num_wins_with_switching, num_wins_without_switching = simulate_games(num_games=1)

    # Calculate win percentages for both cases and add to lists
    wins_switch += num_wins_with_switching
    wins_no_switch += num_wins_without_switching

    # Display the current percentages after each game
    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])

    time.sleep(0.01)
