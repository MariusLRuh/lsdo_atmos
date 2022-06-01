import numpy as np
from csdl import Model
import csdl


class InputsModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
        self.parameters.declare('h', types=np.ndarray)


    def define(self):
        shape = self.parameters['shape']
        h = self.parameters['h'] * 1e-3 # in m but needed in km

        self.create_input('altitude', shape=shape, val=h)

      

