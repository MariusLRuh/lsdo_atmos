import numpy as np 
import csdl 
from csdl import Model 
from csdl_om import Simulator

from atmosphere_model import AtmosphereModel

num_evaluations = 1

shape = (num_evaluations,)

atmosphere_model = AtmosphereModel(
    shape=shape,
    h=np.array([1000]),
)

sim =  Simulator(atmosphere_model)
sim.run()

print('temperature', sim['temperature'])
print('pressure',sim['pressure'])
print('density',sim['density'])
print('dynamic_viscosity',sim['dynamic_viscosity'])
print('speed_of_sound', sim['speed_of_sound'])