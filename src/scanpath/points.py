class Point:
    def __init__(self):
        self.position = []
        self.velocity = []
        self.acceleration = []

    def set_point(self, position, velocity=[], acceleration=[]):
        self.set_position(position)
        #TODO Handle both lines bellow if []
        self.set_velocity(velocity)
        self.set_acceleration(acceleration)

    def set_position(self, values):
        self.position = values

    def set_velocity(self, values):
        self.velocity = values

    def set_acceleration(self, values):
        self.acceleration = values

    def get_point(self):
        return self.position, self.velocity, self.acceleration

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_acceleration(self):
        return self.acceleration

    def append_to_point(self):
        pass

class Current_Point(Point):
    def __init__(self):
        #super().__init__()
        current = Point()
        # Ruckig exlusive
        self.current_position = current.position
        self.current_velocity = current.velocity
        self.current_acceleration = current.acceleration


class Target_Point(Point):
    def __init__(self):
        target = Point()
        # Ruckig format
        self.target_position = target.position
        self.target_velocity = target.velocity
        self.target_acceleration = target.acceleration

class Boundaries:   # Ruckig exlusive
    def __init__(self):

        self.min = Point()
        self.max = Point()
        self.max_jerk = []

class Input:        # Ruckig exlusive
    def __init__(self):
        self.current = Current_Point()
        self.target = Current_Point()
        self.bound = Boundaries()

class Parse:
    def __init__(self):
        pass

    def parse_from_scanspec(self):
        pass

    def parse_to_ruckig(self):
        pass
