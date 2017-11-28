import math
import turtle
import random

def drawarc(t,r,angle) :
    c = 2 * math.pi * r *angle/360
    n = int(c/3) + 1
    plength = c/n
    pangle = angle/n
    for i in range(n) :
        t.fd(plength)
        t.lt(pangle)

def main():
    plants=['s0','s1','s2','s3','s4','s5','s6']

    red = [255,255,255,0,0,0,139]
    green = [0,165,255,255,127,0,0]
    blue = [0,0,0,0,255,255,255]

    for t in plants:
        n=int(t[-1])
        r=30*n**1.3
        t=turtle.Turtle()
        t.speed(0)
        t.shape('circle')
        t.up()
        t.lt(random.choice(range(360)))
        t.fd(r)
        t.down()
        t.lt(90)
        t.pensize(3)
        turtle.colormode(255)
        t.color((red[n],green[n],blue[n]))
        drawarc(t,r,360)

if __name__ == '__main__':
    main()
