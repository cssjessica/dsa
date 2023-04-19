class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # slope = (coordinates[-1][1]-coordinates[0][1])/(coordinates[-1][0]-coordinates[0][0])
        # intercept = coordinates[0][1] - coordinates[0][0]*slope
        # # y = a*x + b
        # for i in range(1,len(coordinates)):
        #     if coordinates[i][0]*slope + intercept != coordinates[i][1]:
        #         return False
        # return True

        if len(coordinates) == 2:
            return True
        
        # make vectors with two points of the coordinates
        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[-1][0], coordinates[-1][1]

        for x,y in coordinates:
            # check if cross product is zero
            if (x1-x)*(y2-y) - (x2-x)*(y1-y) != 0:
                return False
        return True
