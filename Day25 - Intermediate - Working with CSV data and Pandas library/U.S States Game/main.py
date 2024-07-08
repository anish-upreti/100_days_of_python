
import turtle
import pandas

screen = turtle.Screen()
state_map = "blank_states_img.gif"
screen.addshape(state_map)

turtle.shape(state_map)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data.state.to_list()

game_on = True
guess_number = 0
correct_guess = []
guess_remaining = 50

while game_on:
    answer = screen.textinput(title=f"Score: {len(correct_guess)}/50. Guesses left: {guess_remaining}",
                              prompt="Enter a state name to fill in the map or 'exit': ").title()

    if answer in state_list:
        correct_guess.append(answer)
        our_turtle = turtle.Turtle()
        our_turtle.hideturtle()
        our_turtle.penup()
        state_row = state_data[state_data.state == answer]
        our_turtle.goto(int(state_row.x.iloc[0]), int(state_row.y.iloc[0]))
        # our_turtle.write(state_row.state.item())   #use this or the one below to write out the state name in map
        our_turtle.write(answer)

    guess_remaining -= 1
    guess_number += 1
    if guess_number > 49 or answer == "Exit":
        missing_states = [state for state in state_list if state not in correct_guess]  # Use this or the code below
        # missing_states = []
        # for state in state_list:
        #     if state not in correct_guess:
        #         missing_states.append(state)
        test_data = pandas.DataFrame(missing_states)
        test_data.to_csv("remaining_states_to_guess.csv")
        game_on = False


screen.exitonclick()

