"""
This module contains the RRT algorithm
for path finding autonomous vehicles / robots.

This module will be imported in main_MR.py
"""

# importing main modules screen object
from main_MR import p2p_dist, screen


# setting parameter
INT_MAX = 100000000000000


def rrt(x, y, parent):   # function to contain RRT algo
    if (x,y) not in parent and screen.get_at((x,y)) != (0,0,0,255):
        x_m, y_m = -1, -1
        cur_min = INT_MAX
        
        # setting a loop in parent
        for v in parent:
            if p2p_dist(v, (x,y)) < cur_min:
                x_m, y_m = v
                cur_min =  p2p_dist(v,(x,y))

        good = True
        ans = []

        if abs(x_m - x)<abs(y_m-y):
            if y_m<y:
                for u in range(y_m+1, y+1):
                    x_cur = int (((x_m - x)/(y_m - y))*( u - y) + x)
                    y_cur = u
                    if screen.get_at((x_cur,y_cur)) == (0,0,0,255):
                        good=False
                        break
                if good:
                    ans=[int (((x_m - x)/(y_m - y))*( y_m+Step - y) + x),y_m+Step]
            else:
                for u in range(y, y_m):
                    x_cur = int(((x_m - x)/(y_m - y))*( u - y) + x)
                    y_cur = u
                    if screen.get_at((x_cur,y_cur)) == (0,0,0,255):
                        good=False
                        break
                if good:
                    ans=[int (((x_m - x)/(y_m - y))*( y_m-Step - y) + x),y_m-Step]

        else:
            if x_m<x:
                for u in range(x_m + 1, x+1):
                    x_cur = u
                    y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
                    if screen.get_at((x_cur,y_cur)) == (0,0,0,255):
                        good=False
                        break
                if good:
                    ans=[x_m+Step,int( ((y_m-y)/(x_m-x))*(x_m+Step-x) + y ) ]
            else:
                for u in range(x , x_m):
                    x_cur = u
                    y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
                    if screen.get_at((x_cur,y_cur)) == (0,0,0,255):
                        good=False
                        break
                if good:
                    ans=[x_m-Step,int( ((y_m-y)/(x_m-x))*(x_m-Step-x) + y ) ]
        return(good,x_m,y_m,ans)
    return(False,-1,-1,[])

        


    