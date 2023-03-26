import numpy as np
import json

from typing import List

from orbits.utilities.make_logger import make_logger

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

    @staticmethod
    def load_from_json(json_path: str):
        with open(json_path, "r") as planet_information:
            planet_info = json.load(planet_information)
        return Planet(
            name=planet_info.get("name"),
            mass=planet_info.get("mass"),
            radius=planet_info.get("radius"),
            inital_position=np.array(planet_info.get("initial_position")),
            initial_velocity=np.array(planet_info.get("initial_velocity")),
        )

    @staticmethod
    def load_multiple_from_json(json_path: str) -> list:
        with open(json_path, "r") as planet_information:
            planet_info = json.load(planet_information)

        planet_list = []

        for planet in planet_info.get("planets"):
            p = Planet(
                name=planet.get("name"),
                mass=planet.get("mass"),
                radius=planet.get("radius"),
                inital_position=np.array(planet.get("inital_position")),
                initial_velocity=np.array(planet.get("initial_velocity")),
            )
            planet_list.append(p)
        return planet_list
