import copy
import random
class Hat():
    def __init__(self, **ball):
        self.contents = []
        for color, quantity in ball.items():
            self.contents += quantity * [color]
    def draw(self, quantity):
        if quantity > len(self.contents):
            return self.contents
        drawn_balls = []
        for times in range(quantity):
            chance = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(chance))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succeded_experiment = 0

    for test in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        success = True
        result = hat_copy.draw(num_balls_drawn)

        i = 0
        for color in expected_balls:
            result_ball = result.count(color)
            if expected_balls[color] > result_ball:
                success = False
                break
        if success:
            succeded_experiment += 1
    print(succeded_experiment)
    probability = succeded_experiment / num_experiments
    return probability