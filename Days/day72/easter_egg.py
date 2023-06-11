# Fun with lines
# - Check if Cartesian Coordinates form a Straight Line
# - Optimized for Space Complexity

# - Contraints
'''2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.'''

def checkStraightLine(coordinates):
        
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        idx1, idx2 = 0, 1
        slope = 'temp'
        point1, point2 = coordinates[idx1], coordinates[idx2]
        is_vertical = False
        is_horizontal = False

        while True:
            
            x2, x1 = point2[0], point1[0]
            y2, y1 = point2[1], point1[1]
            run = x2 - x1
            rise = y2 - y1

            if run == 0 and not is_vertical:
                new_slope = rise
                is_vertical = True
                if type(slope) == int:
                    return False
                # We have lines that form right angles
                elif is_horizontal:
                    return False
                
            elif rise == 0 and not is_horizontal:
                new_slope = run
                is_horizontal = True
                if type(slope) == int:
                    return False
                # We have lines that form right angles
                elif is_vertical:
                    return False

            elif is_vertical:
                if run:
                    return False

            elif is_horizontal:
                    if rise:
                        return False

            else:
                new_slope = rise/run
            
                if type(slope) == str:
                    slope = new_slope
                
                elif new_slope != slope:
                    return False
                    
            # - Indcrease the indices and reassign coordinates
            idx1 += 1
            idx2 += 1

            try:
                point1, point2 = coordinates[idx1], coordinates[idx2]

            # - We have reached the end of our coordinates list, exit loop
            except IndexError:
                break

        return True



print(checkStraightLine([[0,0],[0,5],[5,5],[5,0]]))
