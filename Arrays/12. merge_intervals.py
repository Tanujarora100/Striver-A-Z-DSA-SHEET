from typing import List


class solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # Sort the array by the first small list in list of list
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            # if the list is empty add it to the list or if it is not then
            # compare the last element of list by[-1][1]-->[[1,3][5,10]]-->10
            # if smaller then append it else just update the bigger value in the last list last element
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res

    '''
    merged=[]
    i=0-->[[1,3]]
    i=1-->[1,3]-->[1,6]
    i=2-->[1,6],8>6-->[1,6][8,10]
    i=3->-->[1,6][8,10][15,18]

    '''

if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    ob = solution()
    print(ob.merge(intervals))
