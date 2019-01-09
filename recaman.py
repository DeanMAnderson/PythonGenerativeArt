#source - https://simpleprogrammer.com/python-generative-art-math/
import turtle
window = turtle.Screen();
turtlePen = turtle.Turtle();
scale = 3;
speed = 10




def init():
    turtlePen.shape("turtle");
    turtlePen.speed(speed);
    screenOffset = turtle.window_width() / 2 * -1;
    moveTurtle(screenOffset,0)

def moveTurtle(x,y):
    turtlePen.penup();
    turtlePen.setpos(x,y);
    turtlePen.pendown();

def startRecaman():
    currentIndex = 0;
    visited = set();

    for index in range(1,200):
        backIndex = currentIndex - index

        if backIndex > 0 and backIndex not in visited:
            turtlePen.setheading(90);
            turtlePen.circle(index/2 * scale, 180);
            currentIndex = index;
            visited.add(index);
        else:
            turtlePen.setheading(270);
            turtlePen.circle(index/2 * scale, 180);
            currentIndex += index;
            visited.add(currentIndex);

        print(currentIndex);

    turtle.done();


init();
startRecaman();
