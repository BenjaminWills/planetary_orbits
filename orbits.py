from orbits.planets import Planet
from orbits.trajectory import Trajectory
from orbits.plotting import Plotter

planets = Planet.load_multiple_from_json("./planet_information/planets.json")

traj = Trajectory(
    planets=planets,
    start_time=0,
    end_time=2 * 60 * 60 * 24 * 365,
    number_of_steps=1e6,
)

trajectory = traj.calculate_trajectories()

plotter = Plotter(trajectory)

plotter.plot_orbits()
