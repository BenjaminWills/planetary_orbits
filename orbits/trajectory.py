from typing import List

from orbits.forces import Forces
from orbits.planets import Planet


class Trajectory:
    def __init__(
        self,
        planets: List[Planet],
        start_time: float,
        end_time: float,
        number_of_steps: int,
    ) -> None:
        self.planets = planets
        self.planet_names = [planet.name for planet in self.planets]
        self.start_time = start_time
        self.end_time = end_time
        self.number_of_steps = int(number_of_steps)
        self.delta_t = (start_time - end_time) / number_of_steps

    def calculate_trajectory_at_timestep(self):

        system_state = Forces(self.planets)

        forces = system_state.calculate_total_force()

        updated_planets = []

        for index, planet in enumerate(self.planets):
            accelaration = (1 / planet.mass) * forces[index]
            velocity = planet.velocity + accelaration * self.delta_t
            position = (
                planet.position
                + planet.velocity * self.delta_t
                + accelaration * (self.delta_t**2)
            )

            planet.velocity = velocity
            planet.position = position

            updated_planets.append(planet)

        self.planets = updated_planets

    def calculate_trajectories(self) -> dict:
        position_dict = dict(
            zip(self.planet_names, [[planet.position] for planet in self.planets])
        )
        for step in range(self.number_of_steps):
            if step % 100_000 == 0:
                print(f"step: {step:,}")
            self.calculate_trajectory_at_timestep()
            for planet in self.planets:
                position_dict[planet.name].append(planet.position)
        return position_dict
