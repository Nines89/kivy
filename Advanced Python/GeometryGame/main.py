from math import sqrt
import turtle

def draw_rect(rect, canvas):
    if rect.point1.x < rect.point2.x:
        first = rect.point1
        third = rect.point2
    else:
        first = rect.point2
        third = rect.point1

    second = Point(third.x, first.y)
    fourth = Point(first.x, third.y)

    canvas.penup()
    canvas.goto(rect.point1.x, rect.point1.y)
    canvas.pendown()
    canvas.forward(first.distance_from_point(second))
    canvas.left(90)
    canvas.forward(second.distance_from_point(third))
    canvas.left(90)
    canvas.forward(third.distance_from_point(fourth))
    canvas.left(90)
    canvas.forward(fourth.distance_from_point(first))



class Rectangle:
    def __init__(self, point1, point2):
        """
        Tuple in input
        :param lowleft: angolo in basso a sx
        :param upright: angolo in basso a dx
        """
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

"""guirectangle è child rectangle è parent"""
class GuiRectangle(Rectangle):

    def draw(self, canvas):
        draw_rect(Rectangle(self.point1, self.point2), canvas)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        """Con le tuple non possiamo considerare di prendere l' n-esimo elemento, dobbiamo
        considerare la x e la y (rect.lowleft.x, rect.upright.x)"""
        if rect.point1.x <= self.x <= rect.point2.x and rect.point1.y <= self.y <= rect.point2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return int(((self.x - point.x)**2 + (self.y - point.y)**2)**0.5)

class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class House:
    def __init__(self, wall_area):
        self.well_area = wall_area

    def paint_needed(self):
        return self.well_area *2.5


class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        tp = self.total_price()
        return tp - (tp * discount_percentage/100)

if __name__ == '__main__':
    p_start = Point(90, 90)
    p = GuiPoint(180, 280)
    p_stop = Point(300, 300)
    rect = Rectangle(p_start, p_stop)
    gui_rect = GuiRectangle(p_start, p_stop)
    my_turtle = turtle.Turtle()
    gui_rect.draw(canvas=my_turtle)
    p.draw(canvas=my_turtle, size=20)

    turtle.done()

