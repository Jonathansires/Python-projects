import pandas
import turtle
import pandas as pd
file = "50_states.csv"
game = 1
screen = turtle.Screen()

screen.title('US States Game')
background = "blank_states_img.gif"
screen.bgpic(background)

def search_csv(csv_file, search_column, search_query, return_columns):
    # read the CSV file using the read_csv method of the Pandas library
    df = pd.read_csv(csv_file)
  
    # search the specified column of the DataFrame for the search query using the str.contains method
    result = df[search_column].str.contains(search_query)

    # return the specified columns where the search query was found
    return df[result][return_columns]


score = 0


def get_mouse_click_coor(x, y):
    print(x, y)

while game == 1:
    answer = screen.textinput(title=f"Your score is {score}", prompt= "How many states names do you know?")
    results = search_csv(file, "state", answer, ["x", "y"])
    x_values = results["x"].tolist()
    y_values = results["y"].tolist()
    for x, y in zip(x_values, y_values):
        turtle.penup()
        turtle.hideturtle()
        turtle.setpos(x, y)
        turtle.write(answer)
        score += 1


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()