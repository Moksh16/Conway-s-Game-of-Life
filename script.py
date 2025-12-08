import random
import pprint
import time

#initializing the random state
def random_state(width, height):
    a=[]
    b=[]
    for i in range(height):
        b=[]
        for j in range(width):
            num = random.randint(0, 1)
            b.append(num)
        a.append(b)
    return a

# to get the dead state
def dead_state(width, height):
    a=[]
    b=[]
    for i in range(height):
        b=[]
        for j in range(width):
            b.append(0)
        a.append(b)
    return a

first_arr = random_state(5,5) # array with random state
my_arr= [
    [0,1,0],
    [0,0,1],
    [1,1,1]
]
dead_arr=dead_state(5,5)

def check_case(alive,dead,case):
    if case:
        return 1 if alive in (2, 3) else 0
    else:
        return 1 if alive == 3 else 0

def count_case(alive,dead,lst):
    for i in lst:
        if i==1:
            alive+=1
        else:
            dead+=1
    return (alive,dead)

def next_state(initial_state): # to get next state
    height = len(initial_state)      # FIX 1
    width = len(initial_state[0])
    dead_arr = dead_state(width, height)  # FIX 4

    for i in range(height):
        for j in range(width):
            alive = 0
            case=True
            for ci in [-1,0,1]:
                for cj in [-1,0,1]:
                    inner_i,inner_j = i+ci, j+cj
                    if 0 <= inner_i < height and 0 <= inner_j < width:
                        if not (ci == 0 and cj == 0):
                            alive += initial_state[inner_i][inner_j]

            if initial_state[i][j] == 0:
                case=False
            else:
                case=True

            dead_arr[i][j] = check_case(alive, 8 - alive, case)  # FIX 3 applied inside check

    return dead_arr

while True:
    print_arr = next_state(my_arr)
    time.sleep(0.5)
    for i in print_arr:
        print(f"{i}")
    print("\r")
    first_arr=print_arr
