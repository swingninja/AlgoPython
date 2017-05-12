# Given 2 rectangles, check if they intersect.
# Assume that both the rectangles are aligned parallel to the axis
# If both x-axis and y-axis overlap then both the rectangles overlap


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect(object):
    def __init__(self, p1, p2):
        # Store the top, bottom, left and right values for points p1 and p2 are the (corners) in either order
        self.left = min(p1.x, p2.x)
        self.right = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top = max(p1.y, p2.y)


def overlap(r1, r2):
    # Overlapping rectangles overlap both horizontally & vertically
    return range_overlap(r1.left, r1.right, r2.left, r2.right) and range_overlap(r1.bottom, r1.top, r2.bottom, r2.top)


def range_overlap(a_min, a_max, b_min, b_max):
    # Neither range is completely greater than the other
    return not ((a_min > b_max) or (b_min > a_max))

p1 = Point(1,1)
p2 = Point(3,3)
r1 = Rect(p1,p2)
p3 = Point(2,2)
p4 = Point(4,4)
r2 = Rect(p3,p4)

print overlap(r1,r2)
print overlap(r2,r1)