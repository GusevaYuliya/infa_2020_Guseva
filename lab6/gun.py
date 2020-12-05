from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        global screen1
        canv.itemconfig(screen1, text='')

        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        global balls

        if self.y <= 550:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy / 2
                self.vx = self.vx / 2
                self.y = 549
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = - self.vx / 2
            self.x = 779

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)) <= self.r + obj.r:
            return True
        else:
            return False

class gun():
    def __init__(self):
       self.f2_power = 10
       self.f2_on = 0
       self.an = 1
       self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
       self.points = 0
       self.live = 1
       self.id = canv.create_oval(0,0,0,0)
       self.vx = rnd(-10, 10)
       self.vy = rnd(-10, 10)
       self.x = rnd(600, 780)
       self.y = rnd(300, 550)
       self.r = rnd(2, 50)
       self.color = 'red'
       self.new_target()


    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x
        y = self.y
        r = self.r
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.r + 4 <= self.y <= 600 - self.r:
            self.y -= self.vy
            self.x += self.vx
            self.set_coords()
        elif self.y > 600 - self.r:
            self.vy = -self.vy
            self.y = 600 - self.r
        else:
            self.vy = -self.vy
            self.y = self.r + 4

        if self.x >= 800 - self.r:
            self.vx = -self.vx
            self.x -= 1
        if self.x <= self.r:
            self.vx = -self.vx
            self.x = self.r + 1

    def hit(self):
        """Попадание шарика в цель."""
        global points, screen_points
        self.live -= 1
        if self.live <= 0:
            self.live = 0
            canv.delete(self.id)
            points += 1
        canv.coords(self.id, -10, -10, -10, -10)
        canv.itemconfig(screen_points, text=str(points))


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
screen_points = canv.create_text(30,30,text = '0',font = '28')
g1 = gun()
balls = []
bullet = 0
points = 0


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, points
    t1.new_target()
    t2.new_target()
    bullet = 0
    prev_bullet = 0
    points = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet - prev_bullet) + ' выстрелов')
                prev_bullet = bullet
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet - prev_bullet) + ' выстрелов')
                prev_bullet = bullet
            if t2.live == 0 and t1.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
        t1.move()
        t2.move()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()


