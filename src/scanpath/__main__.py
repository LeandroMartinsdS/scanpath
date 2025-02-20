"""Interface for ``python -m scanpath``."""

from argparse import ArgumentParser
from collections.abc import Sequence

from . import __version__

__all__ = ["main"]


def main(args: Sequence[str] | None = None) -> None:
    """Argument parser for the CLI."""
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
    )
    parser.parse_args(args)

    trajectory = Trajectory(3)
    trajectory.init_trajectory()
    trajectory.set_input_params(None,None,None)
    trajectory_points = trajectory.walk_through_trajectory()

# file_manager = File(filename_prefix='output/trajectory_points')
file_manager = File(filename_prefix='output/trajectory_points2')
file_manager.write_to_file(trajectory_points, max_file_size=12*1024, decimal_places=5)

inp=Input()
inp.current.position = [1.0, 0.1, 2.2]
print(inp.current.get_position())


if __name__ == "__main__":
    main()
