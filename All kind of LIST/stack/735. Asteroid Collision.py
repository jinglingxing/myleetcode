"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
 Two asteroids moving in the same direction will never meet.



Example 1:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # asteroids = [10,2,-5]
        # flag=1, q: [10,2], star=-5,
        # neighbor=2, q: [10], continue
        # neighbor=10, q: [10], flag=0, break

        q = []
        for star in asteroids:
            flag = 1
            # when q is not empty and the current star is moving left
            # while the neighbor star is moving right
            while q and star < 0 and q[-1] > 0:

                neighbor = q.pop(-1)
                # two asteroids meet, the neighbor star explored
                # check if the q is empty or not
                if abs(neighbor) < abs(star):
                    continue
                # both are the same size, we change flag to 0, so we don't add   the current star in the q since it's explored already
                elif abs(neighbor) == abs(star):
                    pass
                # add the poped star back to q
                else:
                    q.append(neighbor)
                flag = 0
                break

            if flag:
                q.append(star)

        return q





