from turtle import Turtle, Screen
import pandas
from state_name import StateName
from finished_message import FinishedMessage

screen = Screen()
image_path = "blank_states_img.gif"
screen.bgpic(image_path)
is_game_on = True
states_data = pandas.read_csv("50_states.csv")
states_handler = StateName()
all_states_list = states_data["state"].tolist()
states_guessed_list = []
exit_code = "Exit"
finished_message = FinishedMessage()


while is_game_on:
    states_guessed = len(states_guessed_list)
    input_title = "Guess the State" if len(states_guessed_list) <= 0 else f"{states_guessed} / 50 States Correct"
    answer_state = screen.textinput(title=input_title, prompt="What's another State's name?").title()

    if len(states_data[states_data["state"] == answer_state]) > 0 and answer_state not in states_guessed_list:
        states_guessed_list.append(answer_state)
        row_index = states_data[states_data["state"] == answer_state].index[0]
        x = states_data.loc[row_index]["x"]
        y = states_data.loc[row_index]["y"]
        states_handler.fill_in_name(answer_state, x, y)

    if answer_state == exit_code:
        print("exit")
        break

    if states_handler.is_finished():
        finished_message.show_message()
        is_game_on = False

results_list = [state for state in all_states_list if state not in states_guessed_list]
results_dict = {
    "state": results_list
}

df = pandas.DataFrame(results_dict)
df.to_csv("states_to_learn.csv")

