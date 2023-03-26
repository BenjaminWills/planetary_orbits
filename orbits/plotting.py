import matplotlib.pyplot as plt
import numpy as np

from typing import Tuple


class Plotter:
    def __init__(self, position_dictionary: dict) -> None:
        self.positions = position_dictionary
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(111)
        self.ax.set_aspect("equal")

    def __convert_to_scatter_format(self, planet_name: str) -> Tuple[list]:
        x_s, y_s = [], []
        for element in self.positions.get(planet_name):
            x_s.append(element[0])
            y_s.append(element[1])
        return (x_s, y_s)

    def __display_plot(self):
        self.ax.legend()
        plt.show()

    def plot_orbits(self):

        for key in self.positions.keys():
            x_s, y_s = self.__convert_to_scatter_format(key)
            self.ax.scatter(x_s, y_s, s=0.3, label=key)
        self.__display_plot()
