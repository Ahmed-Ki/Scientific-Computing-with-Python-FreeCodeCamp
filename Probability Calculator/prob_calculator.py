import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    balls = []
    if number > len(self.contents):
      return self.contents
    for i in range(number):
      choice = random.randrange(len(self.contents))
      balls.append(self.contents.pop(choice))
    return balls      



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successful_draws = 0
  expected_no_of_balls = []
  for key in expected_balls:
      expected_no_of_balls.append(expected_balls[key])

  for _ in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    balls = new_hat.draw(num_balls_drawn)

    no_of_balls = []
    for key in expected_balls:
      no_of_balls.append(balls.count(key))

    if no_of_balls >= expected_no_of_balls:
      successful_draws += 1

  return successful_draws/num_experiments



