import turtle
import pandas as pd

# creating the screen
window = turtle.Screen()
window.title("Sri Lanka Districts")
image = 'Sri Lanka Map.gif'
turtle.addshape(image)
turtle.shape(image)

# to recognize the locations
# def get_mouse_click_coor(x,y):
#    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# reading csv file and getting districts names
df = pd.read_csv('Districts in SL.csv')
district = df["districts"]


# A function to write districts names by using turtle objects
def write_name(name):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(name, font=("Arial", 10, "normal"))


count = 0
while True:

    # asking user to input a district name
    user_answer = window.textinput(title=f"{count}/25 Districts of Sri Lanka",
                                   prompt="Enter a District( If You don't know type 'Exit'): ").title()

    # if user don't know any other districts exit the loop and show all the name
    if user_answer == "Exit":

        window.title("Learn Mod")
        for name in district:       # filling all 25 districts in the map
            condition = df['districts'] == name
            x = int(df[condition]['x'].iloc[0])
            y = int(df[condition]['y'].iloc[0])
            write_name(name)
        break

    else:
        for name in district:
            # if user's guess is  correct then fill the name in map
            if name == user_answer:
                condition = df['districts'] == name
                x = int(df[condition]['x'].iloc[0])
                y = int(df[condition]['y'].iloc[0])

                print(x, y)
                write_name(name)
                count += 1  # counting how many guesses are correct

window.mainloop()
