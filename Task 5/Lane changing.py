import time
import random

class TruckPlatooning:
    def __init__(self):
        self.leftLaneAvailable = True
        self.rightLaneAvailable = True
        self.currentLane = 'Start'

    def change_to_left_lane(self):
        if self.leftLaneAvailable:
            self.currentLane = 'Left_Lane'
            print("Changed to left lane.")
            self.rightLaneAvailable = True

    def change_to_right_lane(self):
        if self.rightLaneAvailable:
            self.currentLane = 'Right_Lane'
            print("Changed to right lane.")
            self.leftLaneAvailable = True

    def return_to_lane(self):
        self.currentLane = 'In_Lane'
        print("Returned to main lane.")

    def simulate(self):
        print(f"Current Lane: {self.currentLane}")
        if random.choice([True, False]):
            self.change_to_right_lane()
        else:
            self.change_to_left_lane()
        time.sleep(1)  # Wait for 1 second before the next action
        self.return_to_lane()
        time.sleep(1)  # Wait for 1 second before the next cycle

# Place for other scenario classes
class obstacle:
    def simulate(self):
        print("obstacle ")

class driveassist:
    def simulate(self):
        print("driveassist")

def main_simulation_loop():
    scenarios = [TruckPlatooning(), OtherScenario1(), OtherScenario2()]
    while True:
        scenario = random.choice(scenarios)  # Randomly select a scenario to simulate
        scenario.simulate()

main_simulation_loop()
