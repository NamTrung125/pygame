import pygame
import pgzrun
import random
grid_x_count=30
grid_y_count=20
size_cell=20
timer=0
direction_queue='right'
snake_alive=True
WIDTH=grid_x_count*size_cell
HEIGHT=grid_y_count*size_cell

def reset(): #set up ve ran
    global  snake_segment
    snake_segment=[
        {'x':3,'y':0},
        {'x':2,'y':0},
        {'x':1,'y':0},
        {'x':0,'y':0},
    ]
    snake_alive
reset()
def move_food(): #set up ve thuc an 
    global food_position
    possible_food_position=[]
    for food_x in range (grid_x_count):
        for food_y in range (grid_y_count):
            possible=True
            for segment in snake_segment:
                if food_x==segment['x'] and food_y ==segment['y']:
                    possible=False
            if possible:
                possible_food_position.append({'x':food_x,'y':food_y})
    food_position=random.choice(possible_food_position)
move_food()
def on_key_down(key):   #set up ve cach di chuyen
    global direction_queue
    if  key == keys.RIGHT and direction_queue != 'left':
        direction_queue='right'
    elif key == keys.LEFT and direction_queue != 'right':
        direction_queue='left'
    elif key == keys.UP and direction_queue != 'down':
        direction_queue='up'
    elif key == keys.DOWN and direction_queue != 'up':
        direction_queue='down'
def update(dt):
    global timer ,direction_queue,snake_alive
    timer+=dt
    if snake_alive:
        if timer>=0.15:
            timer=0
            next_x_possition=snake_segment[0]['x']
            next_y_possition=snake_segment[0]['y']
            if direction_queue=='right':
                next_x_possition+=1
                if next_x_possition > grid_x_count:
                    next_x_possition=0
            elif direction_queue=='left':
                next_x_possition-=1
                if next_x_possition<0:
                    next_x_possition=grid_x_count-1
            elif direction_queue=='up':
                next_y_possition-=1
                if next_y_possition < 0:
                    next_y_possition=grid_y_count-1
            elif direction_queue=='down':
                next_y_possition+=1
                if next_y_possition>grid_y_count:
                    next_y_possition=0
            can_move=True
            for segment in snake_segment:
                if next_x_possition==segment['x'] and next_y_possition==segment['y']:
                    can_move=False
            if can_move:
                snake_segment.insert(0,{'x':next_x_possition,'y':next_y_possition})
                
                if snake_segment[0]['x']==food_position['x'] and snake_segment[0]['y']==food_position['y']:
                    move_food()
                else:
                    snake_segment.pop()
            else:
                snake_alive=False

    elif timer>=2:
            reset()
            snake_alive=True
def draw():
    screen.fill((0,70,70))
    def draw_cell(x,y,color):
        screen.draw.filled_rect(Rect(x*size_cell,y*size_cell,size_cell-1,size_cell-1),color=color)
    for segment in snake_segment:
        if snake_alive:
            color='red'
        else:
            color='white'
        draw_cell(segment['x'],segment['y'],color)
    draw_cell(food_position['x'],food_position['y'],'green')    

pgzrun.go()