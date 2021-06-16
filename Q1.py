import math

# Point class to keep a track
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return f'X = %1.0f and Y = %1.0f'%(self.x,self.y)


#Distance Formulae
def distance(P1,P2):
    return math.sqrt(pow(P1.x-P2.x,2)+pow(P1.y-P2.y,2))


#Checking if intersection point lies within the line segemnet or not
def withinLineSegment(P1,P2,P3):

    if(distance(P1,P2)==distance(P1,P3)+distance(P2,P3)):
        return P3

    if(P3==None):
        return False
    else:
        return False

## Logic in readme.md

# Returns the point of intersection  of 2 lines
# formed from each-pair of points
def solve(p1,p2,p3,p4):
    x1,y1 = p1.x,p1.y
    x2,y2 = p2.x,p2.y

    u1,v1 =p3.x,p3.y
    u2,v2 =p4.x,p4.y


    x = -1 * ((x1 - x2) * (u1 * v2 - u2 * v1) - (u2 - u1) * (x2 * y1 - x1 * y2)) / ((v1 - v2) * (x1 - x2) - (u2 - u1) * (y2 - y1))
    y = -1 * (u1 * v2 * y1 - u1 * v2 * y2 - u2 * v1 * y1 + u2 * v1 * y2 - v1 * x1 * y2 + v1 * x2 * y1 + v2 * x1 * y2 - v2 * x2 * y1) / (-1 * u1 * y1 + u1 * y2 + u2 * y1 - u2 * y2 + v1 * x1 - v1 * x2 - v2 * x1 + v2 * x2)

    return Point(x,y)



if __name__=="__main__":

    #Driver Code

    """Initializing  4  Points """

    # p1 to p2  -> Line segment 1
    p1 = Point(1,4)
    p2 = Point(3,6)

    # p3 to p4  -> Line segment 2
    p3 = Point(0,5)
    p4 = Point(6,5)


    ## getting point of intersection real or expected both
    p5 = solve(p1,p2,p3,p4)

    #If Line segments are not parallel
    if(p5!=None):

        ## if intersection point lies within linesegment or not
        ans1 = withinLineSegment(p1,p2,p5)
        ans2 = withinLineSegment(p3,p4,p5)

        if ans1!=False and ans2!=False:
            print("Yes, it is possible!, Both line segment intersects at : ", end="")
            print(ans1 if ans1 else ans2)
        else:
            print("No, both line segment are'nt intersecting! ")

    else:
        print("Both line segment are'nt intersecting, instead they are parallel.")

