import os
import csv

from copy import copy

from ruckig import InputParameter, OutputParameter, Result, Ruckig
from points import Input


class Trajectory:
    def __init__(self, dof, fs=5e3):
        self.dof = dof
        self.fs = fs
        self.Ts = 1 / fs
        self.init_trajectory()

    def init_trajectory(self):
        self.otg = Ruckig(self.dof, self.Ts)
        self.inp = InputParameter(self.dof)
        self.out = OutputParameter(self.dof)

    def set_input_params(self, current, target, boundaries):
        # TEST
        ############################################
        self.inp.current_position = [0.0, 0.0, 0.5]
        self.inp.current_velocity = [0.0, -2.2, -0.5]
        self.inp.current_acceleration = [0.0, 2.5, -0.5]
        self.inp.target_position = [5.0, -2.0, -3.5]
        self.inp.target_velocity = [0.0, -0.5, -2.0]
        self.inp.target_acceleration = [0.0, 0.0, 0.5]
        self.inp.max_velocity = [3.0, 1.0, 3.0]
        self.inp.max_acceleration = [3.0, 2.0, 1.0]
        self.inp.max_jerk = [4.0, 3.0, 2.0]
        ####################################

    def walk_through_trajectory(self):
        out_list = []
        self.out = OutputParameter(self.inp.degrees_of_freedom)

        res = Result.Working
        while res == Result.Working:
            res = self.otg.update(self.inp, self.out)

            self.out.pass_to_input(self.inp)
            out_list.append(copy(self.out))

        return out_list

class File:
    def __init__(self, filename_prefix='output/trajectory_points'):
        self.filename_prefix = filename_prefix
        # Ensure the output directory exists
        output_dir = os.path.dirname(os.path.abspath(self.filename_prefix))
        os.makedirs(output_dir, exist_ok=True)

    def open_new_file(self, index=0):
        file_path=f'{self.filename_prefix}_{index}.csv'
        file = open(file_path, 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['User', 'Motor 1', 'Motor 2'])
        return file, writer

    def write_to_file(self, points, max_file_size=None, decimal_places=3):
        file_index = 0
        file, writer = self.open_new_file(file_index)
        current_file_size = 0

        for point in points:
            formatted_point = [f"{value:.{decimal_places}f}"
                               for value in point.new_position]
            #formatted_point = [int(value) for value in point.new_position]
            writer.writerow(formatted_point)

            if max_file_size is not None:
                # Buffer to account for CSV overhead
                overhead_buffer = 1024  # 1 KB buffer for overhead

                file.flush()  # Ensure all data is written to disk
                current_file_size = os.path.getsize(file.name)

                if current_file_size + overhead_buffer  >= max_file_size:
                    file.close()
                    file_index += 1
                    current_file_size = 0
                    file, writer = self.open_new_file(file_index)

        file.close()

#class Stream:



def main():
    trajectory = Trajectory(3)
    trajectory.init_trajectory()
    trajectory.set_input_params(None,None,None)
    trajectory_points = trajectory.walk_through_trajectory()

    # file_manager = File(filename_prefix='output/trajectory_points')
    file_manager = File(filename_prefix='output/trajectory_points2')
    file_manager.write_to_file(trajectory_points,
                               max_file_size=12*1024, decimal_places=5)

    inp=Input()
    inp.current.set_point([1.0, 0.1, 2.2],[1, 2, 3], [5,10,20])
    print(inp.current.get_point())


if __name__ == "__main__":
    main()
