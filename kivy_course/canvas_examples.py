from kivy.graphics import Line, Color, Rectangle, Ellipse
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget

Builder.load_file('canvas_examples.kv')


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 1)
            self.rect = Rectangle(pos=(300, 100), size=(50, 50))
            Color(1, 1, 0)
            Line(points=(200, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(500, 300, 80))

    def move_rect(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            Color(0, 0, 0)
            self.bg = Rectangle(pos=self.pos, size=self.size)
            Color(1, 1, 1)
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            self.vx = dp(3)
            self.vy = dp(3)
        Clock.schedule_interval(self.update, 1 / 60)

    def on_size(self, *args):
        # print('On size: ' + str(self.width) + ', ' + str(self.height))
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        x, y = self.ball.pos
        limit_x = x + self.ball_size
        limit_y = y + self.ball_size
        limit_x_0 = x
        limit_y_0 = y

        if limit_x >= self.width or limit_x_0 <= 0:
            self.vx = -self.vx

        if limit_y >= self.height or limit_y_0 <= 0:
            self.vy = -self.vy

        x += self.vx
        y += self.vy
        self.ball.pos = (x, y)

    class CanvasExample6(Widget):
        pass

    class CanvasExample7(Widget):
        pass
