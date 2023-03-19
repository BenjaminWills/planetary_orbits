import numpy as np

from typing import List

from utilities.make_logger import make_logger

planet_logger = make_logger(logging_path="./logs/orbital.log", logger_name="PLANETS")


class Planet:
    def __init__(
        self,
        name: str,
        mass: float,
        radius: float,
        inital_position: np.array,
        initial_velocity: np.array,
    ) -> None:
        self.name = name
        self.mass = mass
        self.radius = radius
        self.colour = self.__generate_planet_colour()
        self.forces = None
        self.position = inital_position
        self.velocity = initial_velocity

        planet_logger.info(
            f"""
        planet: {name} created, with attributes:
            mass: {mass:,} kg
            radius: {radius:,} m
            RGB colour: {self.colour}
            initial_position: {inital_position}
        """
        )

    def __generate_planet_colour(self) -> List[int]:
        """Generates a random RGB colour for the planet to show as on the plot.

        Returns
        -------
        List[int]
            A list of RGB colour codes.
        """
        rgb_colour = list(np.random.choice(range(256), size=3))
        return rgb_colour
