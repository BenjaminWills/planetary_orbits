import numpy as np

from numpy.linalg import norm
from typing import List, Dict

from planets import Planet
from utilities.make_logger import make_logger

G = 6.6743e-11

force_logger = make_logger("./logs/orbital.log", logger_name="FORCES")


class Forces:
    def __init__(self, planets: List[Planet]) -> None:
        self.planets = planets

        force_logger.info(
            f"""
            Calculating forces for the planets: {[planet.name for planet in planets]}
            """
        )

    def calculate_force(self, planet_1: Planet, planet_2: Planet) -> float:
        direction = planet_1.position - planet_2.position
        distance = norm(direction)

        unit_direction = direction / distance

        force = (G * planet_1.mass * planet_2.mass) / (distance**2)
        return -force * unit_direction

    def calculate_total_force(self) -> Dict[str, np.array]:
        """To calculate the force we need to calculate the force on each body that is exerted by the other bodies.

        Returns
        -------
        List[float]
            A list of forces that act along the unit vector between each planet.
        """

        planet_names = [planet.name for planet in self.planets]
        forces = []

        for planet_1 in self.planets:
            force_1_2 = np.array([0, 0])
            for planet_2 in self.planets:
                if planet_1 != planet_2:
                    force_1_2 = force_1_2 + self.calculate_force(planet_1, planet_2)
                else:
                    continue
            forces.append(force_1_2)

        # return dict(zip(planet_names, forces))
        return forces
