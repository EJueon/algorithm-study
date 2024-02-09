import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

positions = [list(input().split()) for _ in range(N)]
orders = [list(input().split()) for _ in range(M)]

DIRS = {'N': (0, 0, 1), 'W': (3, -1, 0), 'S': (2, 0, -1), 'E': (1, 1, 0)}
DIR_str = 'NESW'

def change_robot_integer(pos):
    new_positions = [[]]
    for y, x, d in pos:
        new_positions.append([int(y), int(x), d])
    return new_positions

def change_order_integer(orders):
    new_orders = []
    for num, order, n_iter in orders:
        new_orders.append((int(num), order, int(n_iter)))
    return new_orders

positions = change_robot_integer(positions)
orders = change_order_integer(orders)

def test_robot():
    for robot, category, iter_cnt in orders:
        if category == 'F':
            _, dx, dy = DIRS[positions[robot][2]]
            nx = int(positions[robot][0]) 
            ny = int(positions[robot][1]) 
            
            for _ in range(iter_cnt):
                nx += dx
                ny += dy
                
                # crash 1
                if ny > B or ny <= 0 or nx > A or nx <= 0:
                    print(f'Robot {robot} crashes into the wall')
                    return

                # crash 2
                for trobot, (tx, ty, _) in enumerate(positions[1:], 1):
                    if trobot == robot: continue
                    if ny == ty and nx == tx: 
                        print(f'Robot {robot} crashes into robot {trobot}')
                        return 
            
                positions[robot][0] = nx
                positions[robot][1] = ny
        
        elif category == 'L':
           positions[robot][2] = DIR_str[(DIRS[positions[robot][2]][0] - iter_cnt) % 4]
        elif category == 'R':
           positions[robot][2] = DIR_str[(DIRS[positions[robot][2]][0] + iter_cnt) % 4]
    print("OK")
    
test_robot()