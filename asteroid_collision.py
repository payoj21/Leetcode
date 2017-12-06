def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """

    after_collision= []
    for i in range(len(asteroids)):
        if len(after_collision) == 0 or asteroids[i] > 0:

            after_collision.append(asteroids[i])

        else:
            while after_collision[-1] > 0 and len(after_collision) > 0:
                if after_collision[-1] == -(asteroids[i]):
                    after_collision.pop()
                    break
                else:
                    if after_collision[-1] < -(asteroids[i]):
                        after_collision.pop()
                        continue
                    else:
                        break
            else:

                after_collision.append(asteroids[i])


    return after_collision


print(asteroidCollision([10,2,-5]))