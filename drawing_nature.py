'''
YuHan Chi
CS 5001, Spring 2021
HW 6: Spirals, implement Turtle library in python to create unique design.
My Design: Nature
           A blue sky with a sun and few birds,
           On the ground, there are trees, snails and flowers.
'''
import turtle


def paint_ground(color):
    '''
    Function: paint_ground, paint ground color
    Parameter: string, the Hex Color Codes
    Return: None
    Do: using given color draw the ground
    '''
    ground = turtle.Turtle()
    ground.speed(10)
    ground.penup()
    ground.goto(-1000, -1200)
    ground.pendown()
    ground.left(270)
    ground.speed(10)
    ground.color(color)
    ground.begin_fill()
    ground.circle(1000)
    ground.end_fill()


def draw_birds(pos_x, pos_y, size):
    '''
    Function: draw_birds, draw a serious of birds
    Parameter: 3 integers, drawing position (pos_x and pos_y) and bird's size
    Return: None
    Do: draw a serious of birds start from the given position
    '''
    if size < 2 or pos_x > 400 or pos_y > 350:
        return
    else:
        bird = turtle.Turtle()
        bird.speed(10)
        bird.pensize(7)
        bird.penup()
        bird.goto(pos_x, pos_y)
        bird.pendown()
        bird.color('white')
        bird.left(10)
        for i in range(30):
            bird.right(2)
            bird.forward(size // 3)
        bird.left(120)
        for i in range(30):
            bird.right(2)
            bird.forward(size // 3)
        draw_birds(pos_x - 50, pos_y + 100, size - 2)
        draw_birds(pos_x + 150, pos_y + 80, size - 3)


def draw_sun(pos_x, pos_y, outline_color, fill_in_color):
    '''
    Function: draw_sun, draw a sun
    Parameter: 2 integers, for drawing position (pos_x and pos_y)
               2 strings, for outline color and fill in color
    Return: None
    Do: using given color to draw a sun at given position
    '''
    sun = turtle.Turtle()
    sun.speed(10)
    sun.pensize(3)
    sun.penup()
    sun.goto(pos_x, pos_y)
    sun.pendown()
    sun.color(outline_color, fill_in_color)
    sun.begin_fill()
    for i in range(36):
        sun.forward(200)
        sun.right(170)
    sun.end_fill()
    sun.hideturtle()


def draw_tree(tree_x, tree_y, size):
    '''
    Function: draw_tree, a tree has both branch and leaf
              (there are two functions inside: draw_leaf and draw_branch)
    Parameter: 3 integers, first two for drawing position (tree_x and tree_y)
                           last one for the tree size
    Return: None
    Do: draw a tree on the screen at the given position
    '''
    def draw_leaf(pos_x, pos_y, leaf_size):
        '''
        Function: draw_leaf, draw leaves for a tree
        Parameter: 3 integers, two for position and one for size
        Return: None
        Do: draw leaves on the screen at the given position
        '''
        leaf.penup()
        leaf.goto(pos_x, pos_y)
        leaf.pendown()
        if leaf_size > 20:
            leaf.color('#3A5F0B')
            leaf.circle(leaf_size)
        elif leaf_size > 10:
            leaf.color('#03b652')
            leaf.circle(leaf_size)
        else:
            return
        draw_leaf(pos_x, pos_y, leaf_size * 0.6)
        leaf.hideturtle()

    def draw_branch(branch_lengh):
        '''
        Function: draw_branch, draw branch for a tree
        Parameter: integer, the length for branch
        Return: None
        Do: draw branch on the screen
        '''
        if branch_lengh > 10:
            branch.color('#964B00')
            branch.forward(branch_lengh)
            branch.left(30)
            draw_branch(branch_lengh * 0.7)
            pos_x, pos_y = branch.pos()
            branch.right(60)
            draw_branch(branch_lengh * 0.7)
            if branch_lengh < 30:
                draw_leaf(pos_x, pos_y, branch_lengh)
            branch.left(30)
            branch.backward(branch_lengh)
            branch.hideturtle()
    branch = turtle.Turtle()
    branch.penup()
    branch.goto(tree_x, tree_y)
    branch.pendown()
    branch.pensize(7)
    branch.left(90)
    branch.speed(10)
    leaf = turtle.Turtle()
    leaf.speed(10)
    leaf.pensize(3)
    draw_branch(size)


def draw_snail(pos_x, pos_y, size, color):
    '''
    Function: draw_snail, draw a snail
              (there are two functions inside: body and head)
    Parameter: 3 integers, for drawing position (pos_x and pos_y), and size
               1 strings, for snail's color
    Return: None
    Do: draw the given size of snail using given color at the given position
    '''
    def body():
        '''
        Function: body
        Parameter: None
        Return: None
        Do: draw the body for a snail, according to given color and size
        '''
        colors_index = [["#6e99e2", "#588bde", "#437cd9", "#2e6dd5", "#2762c2",
                         "#2357ad"],
                        ["#a266f8", "#934ef7", "#8435f6", "#751df5", "#670bee",
                         "#5d09d6"],
                        ["#f79b64", "#f68b4b", "#f47c33", "#f36c1b", "#e85f0c",
                         "#d0550b"]]
        colors_string = ['blue', 'purple', 'orange']
        if color in colors_string:
            snail.penup()
            snail.goto(pos_x, pos_y)
            snail.pendown()
            colors = colors_index[colors_string.index(color)]
            snail.begin_fill()
            snail.forward(size)
            for i in range(size, 1, -1):
                snail.color(colors[i % 6])
                snail.forward(i)
                snail.left(50 - i/3)
            snail.end_fill()

    def head():
        '''
        Function: head
        Parameter: None
        Return: None
        Do: draw the head for a snail, according to given position
        '''
        snail.color('black')
        snail.penup()
        snail.goto(pos_x, pos_y)
        snail.pendown()
        snail.left(100)
        snail.forward(size)
        snail.penup()
        snail.right(15)
        snail.goto(pos_x, pos_y)
        snail.pendown()
        snail.right(45)
        snail.forward(size)
    snail = turtle.Turtle()
    snail.speed(10)
    snail.pensize(3)
    body()
    head()
    snail.hideturtle()


def draw_flower(pos_x, pos_y, color1, color2, size):
    '''
    Function: draw_flower, draw a flower
    Parameter: 2 integers, two drawing position (pos_x and pos_y)
               2 strings, two drawing colors
               1 integer, the size of this flower
    Return: None
    Do: draw a two-color flower at given position
    '''
    flower = turtle.Turtle()
    flower.speed(10)
    flower.pensize(1)
    flower.penup()
    flower.goto(pos_x, pos_y)
    flower.pendown()
    for i in range(20):
        if i % 2 == 0:
            flower.color(color1)
        else:
            flower.color(color2)
        flower.begin_fill()
        flower.left(5)
        flower.forward(size)
        flower.right(90)
        flower.forward(size//3)
        flower.right(120)
        flower.forward(size)
        flower.end_fill()
        flower.right(45)


def main():
    '''
    Function: main
    Parameter: None
    Return: None
    Do: call all functions needed to paint a blue sky with a sun and few birds,
        five trees on the ground, three snails and five flowers in the front.
    '''
    turtle.setup(1200, 800)
    turtle.bgcolor('#dffaff')
    paint_ground('#964B00')
    draw_sun(-500, 250, 'red', 'orange')
    draw_birds(100, 250, 10)
    draw_tree(0, -200, 125)
    draw_tree(270, -250, 100)
    draw_tree(-270, -250, 100)
    draw_tree(450, -320, 75)
    draw_tree(-450, -320, 75)
    draw_snail(100, -300, 25, 'blue')
    draw_snail(-180, -280, 35, 'orange')
    draw_snail(300, -380, 25, 'purple')
    draw_flower(300, -280, '#ff0006', '#ff4d51', 30)
    draw_flower(-390, -300, '#0b4221', '#20c661', 30)
    draw_flower(0, -350, '#a7ab0c', '#eff35d', 30)
    draw_flower(-230, -320, '#ff0006', '#ff4d51', 20)
    draw_flower(450, -330, '#a7ab0c', '#eff35d', 20)


if __name__ == '__main__':
    main()
