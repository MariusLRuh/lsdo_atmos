import numpy as np
from csdl import Model
import csdl
from csdl_om import Simulator

class AtmosphereModel(Model):
    def initialize(self):
        self.parameters.declare('shape', types=tuple)
    def define(self):
        shape = self.parameters['shape']
        h = self.declare_variable('z',shape=shape, val=0) * 1e-3 # value in meters; then convert to km
        L = 6.5 # K/km
        R = 287
        T0 = 288.16
        P0 = 101325
        g0 = 9.81
        mu0 = 1.735e-5
        S1 = 110.4
        gamma = 1.4

        # Temperature 
        T           =  - h * L + T0

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

# sim = Simulator(AtmosphereModel(
#     shape=(1,),
# ))
# sim.run()

# sim.prob.check_totals(of='temperature',wrt='altitude')
# sim.prob.check_totals(of='pressure',wrt='altitude')
# sim.prob.check_totals(of='density',wrt='altitude')
# sim.prob.check_totals(of='dynamic_viscosity',wrt='altitude')
# sim.prob.check_totals(of='speed_of_sound',wrt='altitude')

# print('temperature [K]: ', sim['temperature'])
# print('pressure [Pa]: ',sim['pressure'])
# print('density [kg/m^3]: ',sim['density'])
# print('dynamic_viscosity [N s/m^2]: ',sim['dynamic_viscosity'])
# print('speed_of_sound [m/s]: ', sim['speed_of_sound'])


        
