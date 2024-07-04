import random
import time

class TruckPlatoonSimulation:
    def __init__(self):
        self.MIN_PLATOON_SIZE = 3
        self.MAX_TRUCKS = 5
        self.SAFE_DISTANCE = 10  # in meters
        self.nTrucks = 0
        self.currentCondition = 0  # 0: NORMAL, 1: HEAVY_TRAFFIC, 2: RAIN, 3: STORM
        self.road_conditions = ['NORMAL', 'HEAVY_TRAFFIC', 'RAIN', 'STORM']
        self.globalClock = 0
        self.leader_state = "Idle"
        self.follower_states = ["Idle"] * self.MAX_TRUCKS
        self.platoon_formation = False

    def adjust_cruise(self):
        self.currentCondition = random.choice(range(4))
        distance_adjustment = [0, 5, 10, 15][self.currentCondition]
        speed_adjustment = [50, 40, 30, 20][self.currentCondition]
        print(f"Adjusting cruise becuase of {self.road_conditions[self.currentCondition]}: New distance {self.SAFE_DISTANCE + distance_adjustment}, New speed {speed_adjustment}")

    def platoon_ready(self):
        if self.nTrucks >= self.MIN_PLATOON_SIZE and self.platoon_formation == False:
            self.leader_state = "Lead"
            print("Platoon is now ready!")
            self.platoon_formation = True
            for i in range(self.MAX_TRUCKS):
                if self.follower_states[i] == "Waiting":
                    self.follower_states[i] = "Follow"
                    print(f"Follower {i+1} is now following")

    def join_platoon(self):
        if self.nTrucks < self.MAX_TRUCKS:
            self.nTrucks += 1
            print(f"Truck joined. Total trucks: {self.nTrucks}")
        else:
            print("No more trucks can join. Platoon is at maximum capacity.")

    def run_simulation(self):
        while True:
            time.sleep(1)
            self.globalClock += 1
            if self.globalClock % 10 == 0:
                self.adjust_cruise()
            if self.globalClock % 15 == 0 and self.nTrucks < self.MAX_TRUCKS:
                self.join_platoon()
            if self.globalClock % 50 == 0:
                self.platoon_ready()

# Create a simulation object and start it
simulation = TruckPlatoonSimulation()
simulation.run_simulation()
