class solution:
    def findCelebrity(n, knows):
        # Create a stack and push all ids in it.
        ids = []
        for i in range(0, n):
            ids.append(i)
        #  Finding celebrity.
        while (len(ids) > 1):
            id1 = ids.pop()
            id2 = ids.pop()
            if knows(id1, id2) == True:
                # Because person with id1 can not be celebrity.
                ids.append(id2)
            else:
                # Because person with id2 can not be celebrity.
                ids.append(id1)

        celebrity = ids[len(ids)-1]

        knowAny = False
        knownToAll = True
        # Verify whether the celebrity knows any other person.
        for i in range(0, n):
            if knows(celebrity, i) == True:
                knowAny = True
                break

        # Verify whether the celebrity is known to all the other person.
        for i in range(0, n):
            if i != celebrity and knows(i, celebrity) == False:
                knownToAll = False
                break

        if knowAny != False or knownToAll == False:
            # If verificatin failed, then it means there is no celebrity at the party.
            celebrity = -1

        return celebrity

    def knows(self, a, b, M):
        if M[a][b] == 1:
            return True
        else:
            return False

    def findCelebrity(n, knows):
        # Two pointers pointing at start and end of search space.
        p = 0
        q = n-1
        while (p < q):
            # This means p cannot be celebrity.
            if knows(p, q) == True:
                p += 1
            # This means q cannot be celebrity.
            else:
                q -= 1

        celebrity = p
        knowAny = False
        knownToAll = True
        # Verify whether the celebrity knows any other person.
        for i in range(0, n):
            if knows(celebrity, i) == True:
                knowAny = True
                break
        # Verify whether the celebrity is known to all the other person.
        for i in range(0, n):
            if i != celebrity and knows(i, celebrity) == False:
                knownToAll = False
                break

        if knowAny != False or knownToAll == False:
            # If verificatin failed, then it means there is no celebrity at the party.
            celebrity = -1

        return celebrity


"""
    Time complexity: O(N * N)
    Space complexity: O(N)
	
    Where ‘N’ is the number of people at the party.
"""


def findCelebrity(n, knows):
    #  Calculating indegree and outdegree of each nodes.
    indegree = [0] * n
    outdegree = [0] * n

    for i in range(0, n):
        for j in range(0, n):
            if knows(i, j) == 1:
                indegree[j] += 1
                outdegree[i] += 1

    # Finding Celebrity
    celebrity = -1
    for i in range(0, n):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            celebrity = i
            break

    return celebrity
