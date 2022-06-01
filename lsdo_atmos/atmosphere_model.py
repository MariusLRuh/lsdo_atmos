import numpy as np
from csdl import Model
import csdl

from inputs_model import InputsModel

class AtmosphereModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
        self.parameters.declare('h', types=np.ndarray)
    def define(self):
        shape = self.parameters['shape']
        h = self.parameters['h']
        self.add(InputsModel(
            shape=shape,
            h=h,
        ))

        h = self.declare_variable('altitude', shape=shape) * 1e-3 # convert from m to km
        
        L           = 6.5
        R           = 287
        T0          = 288.16
        P0          = 101325
        g0          = 9.81
        mu0         = 1.735e-5
        S1          = 110.4
        gamma = 1.4

         # Temperature 
        T           = T0 - L * h

        # Pressure 
        P           = P0 * (T/T0)**(g0/(L * 1e-3)/R)
        
        # Density
        rho         = P/R/T
        
        # Dynamic viscosity (using Sutherland's law)  
        mu          = mu0 * (T/T0)**(3/2) * (T0 + S1)/(T + S1)

        # speed of sound 
        a = (gamma * R * T)**0.5

        self.register_output('temperature',T)
        self.register_output('pressure',P)
        self.register_output('density',rho)
        self.register_output('dynamic_viscosity',mu)
        self.register_output('speed_of_sound', a)
        
