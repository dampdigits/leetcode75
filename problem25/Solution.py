def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        # asteroid going right
        if asteroid > 0:
            stack.append(asteroid)
            continue
        # asteroid going left
        asteroidDestroyed = False
        while stack:
            prev = stack[-1]
            # both going left
            if prev < 0:
                stack.append(asteroid)
                break
            # collision
            absVal = abs(asteroid)
            # small asteroid --> <-- big asteroid
            if prev < absVal: stack.pop()
            else:
                # colliding asteroids are of same size
                if prev == absVal: stack.pop()
                asteroidDestroyed = True
                break
        # no asteroids in stack
        if not asteroidDestroyed and not stack:
            stack.append(asteroid)
    return stack

def main():
    asteroidsList = [[5,10,-5],[8,-8],[10,2,-5]]
    for asteroids in asteroidsList:
        print("stack = ", asteroidCollision(asteroids))

if __name__ == "__main__":
    main()
