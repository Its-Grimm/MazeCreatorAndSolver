import os

def mazeDisplay(maze):
    mazeDisplay = ''
    for row in maze:
        print(row)
        for col in row:
            mazeDisplay += str(col) + ' '
        mazeDisplay += '\n'
        
    print('\nDisplay:')
    print(mazeDisplay)
            
def randomMazeGen(height, width):
    maze = [[0] * width for _ in range(height)]
    
    for h in range(height):
        for w in range(width):
            if h == 0 or h == height-1:
                maze[h][w] = '-'
                
            if w == 0 or w == width-1: 
                maze[h][w] = '|'
            
            if (w == 0 and h == 0) or (w == 0 and h == height-1) or (w == width-1 and h == height-1) or (w == width-1 and h == 0):
                maze[h][w] = '+'
    mazeDisplay(maze)

if __name__ == '__main__':
    mazeSizeLength = int(input('Maze height: '))
    mazeSizeWidth = int(input('Maze width:  '))
    randomMazeGen(mazeSizeLength+2, mazeSizeWidth+2)
    