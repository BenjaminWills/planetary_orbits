from orbits.planets import Planet
from orbits.trajectory import Trajectory
from orbits.plotting import Plotter

import numpy as np

earth = Planet(
    name="earth",
    mass=5.972e24,
    radius=6371e3,
    inital_position=np.array([149.6e9, 0]),
    initial_velocity=np.array([0, 29951.68]),
)

sun = Planet(
    name="sun",
    mass=1.989e30,
    radius=696340e3,
    inital_position=np.array([0, 0]),
    initial_velocity=np.array([0, 0]),
)

venus = Planet(
    name="venus",
    mass=4.867e24,
    radius=6051.8e3,
    inital_position=np.array([107.71e9, 0]),
    initial_velocity=np.array([0, 35021.561]),
)


traj = Trajectory(
    planets=[sun, venus, earth],
    start_time=0,
    end_time=2 * 60 * 60 * 24 * 365,
    number_of_steps=1e3,
)

trajectory = traj.calculate_trajectories()

plotter = Plotter(trajectory)

plotter.plot_orbits()
