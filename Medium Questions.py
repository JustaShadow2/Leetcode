'''class Solution(object): # Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        baseA = abs(ax1) + abs(ax2)
        heightA = abs(ay1) + abs(ay2)

        baseB = abs(bx1) + abs(bx2)
        heightB = abs(by1) + abs(by2)

        cx1 = bx1 # using given coordinates, find the coordinates of the square created by the overlap (draw it if you need an aid)
        cy1 = ay1
        cx2 = ax2
        cy2 = by2
        
        baseC = abs(cx1) + abs(cx2)
        heightC = abs(cy1) + abs(cy2)

        areaA = baseA*heightA
        areaB = baseB*heightB
        areaC = baseC*heightC

        totalArea = areaA+areaB-areaC

        return totalArea''' # this code does not work for certain inputs, below fixes this and is more efficient

class Solution(object): # Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        # find the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        # find the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)
        # find the area of the overlap
        overlap = max(min(ax2, bx2) - max(ax1, bx1), 0) * max(min(ay2, by2) - max(ay1, by1), 0)
        # return the sum of the areas minus the overlap
        return area1 + area2 - overlap