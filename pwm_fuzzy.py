import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#RANGE:[-10 , 10]
#phải scale pwm về dương

a=input('Left or Right? \n')

position = ctrl.Antecedent(np.arange(-10, 11, 1), 'position')
distance = ctrl.Antecedent(np.arange(-10, 11, 1), 'distance')
pwm = ctrl.Consequent(np.arange(-10, 11, 1), 'pwm')

#position
position['NB']=fuzz.trapmf(position.universe,[-20, -10, -7,-4])
position['NS']=fuzz.trimf(position.universe,[-7,-4,0])
position['ZE']=fuzz.trimf(position.universe,[-4,0,4])
position['PS']=fuzz.trimf(position.universe,[0,4,7])
position['PB']=fuzz.trapmf(position.universe,[4, 7, 10, 20])

#distance
distance['NE']=fuzz.trapmf(distance.universe,[-20, -10, -5,-0])
distance['ZE']=fuzz.trimf(distance.universe,[-5,0,5])
distance['PO']=fuzz.trapmf(distance.universe,[0, 5, 10, 20])

#PWM
#pwm.automf(3)
pwm['NB']=fuzz.trapmf(pwm.universe,[-20, -10, -8,-6])
pwm['NM']=fuzz.trimf(pwm.universe,[-8,-6,-4])
pwm['NS']=fuzz.trimf(pwm.universe,[-6,-3,0])
pwm['ZE']=fuzz.trimf(pwm.universe,[-3,0,3])
pwm['PS']=fuzz.trimf(pwm.universe,[0,3,6])
pwm['PM']=fuzz.trimf(pwm.universe,[4,6,8])
pwm['PB']=fuzz.trapmf(pwm.universe,[6, 8, 10, 20])

#view
position.view()
distance.view()
pwm.view()

#RULES
if (a=='L' or a=='l'):
    rule1 = ctrl.Rule(position['NB'] & distance['NE'],pwm['PB'])
    rule2 = ctrl.Rule(position['NB'] & distance['ZE'],pwm['PM'])
    rule3 = ctrl.Rule(position['NB'] & distance['PO'],pwm['PS'])

    rule4 = ctrl.Rule(position['NS'] & distance['NE'],pwm['PM'])
    rule5 = ctrl.Rule(position['NS'] & distance['ZE'],pwm['PS'])
    rule6 = ctrl.Rule(position['NS'] & distance['PO'],pwm['ZE'])

    rule7 = ctrl.Rule(position['ZE'] & distance['NE'],pwm['PS'])
    rule8 = ctrl.Rule(position['ZE'] & distance['ZE'],pwm['ZE'])
    rule9 = ctrl.Rule(position['ZE'] & distance['PO'],pwm['NS'])

    rule10 = ctrl.Rule(position['PS'] & distance['NE'],pwm['ZE'])
    rule11 = ctrl.Rule(position['PS'] & distance['ZE'],pwm['NS'])
    rule12 = ctrl.Rule(position['PS'] & distance['PO'],pwm['NM'])

    rule13 = ctrl.Rule(position['PB'] & distance['NE'],pwm['NS'])
    rule14 = ctrl.Rule(position['PB'] & distance['ZE'],pwm['NM'])
    rule15 = ctrl.Rule(position['PB'] & distance['PO'],pwm['NB'])

else:
    rule1 = ctrl.Rule(position['NB'] & distance['NE'],pwm['NS'])
    rule2 = ctrl.Rule(position['NB'] & distance['ZE'],pwm['NM'])
    rule3 = ctrl.Rule(position['NB'] & distance['PO'],pwm['NB'])

    rule4 = ctrl.Rule(position['NS'] & distance['NE'],pwm['ZE'])
    rule5 = ctrl.Rule(position['NS'] & distance['ZE'],pwm['NS'])
    rule6 = ctrl.Rule(position['NS'] & distance['PO'],pwm['NM'])

    rule7 = ctrl.Rule(position['ZE'] & distance['NE'],pwm['PS'])
    rule8 = ctrl.Rule(position['ZE'] & distance['ZE'],pwm['ZE'])
    rule9 = ctrl.Rule(position['ZE'] & distance['PO'],pwm['NS'])

    rule10 = ctrl.Rule(position['PS'] & distance['NE'],pwm['PM'])
    rule11 = ctrl.Rule(position['PS'] & distance['ZE'],pwm['PS'])
    rule12 = ctrl.Rule(position['PS'] & distance['PO'],pwm['ZE'])

    rule13 = ctrl.Rule(position['PB'] & distance['NE'],pwm['PB'])
    rule14 = ctrl.Rule(position['PB'] & distance['ZE'],pwm['PM'])
    rule15 = ctrl.Rule(position['PB'] & distance['PO'],pwm['PS'])

#CONTROL
pwm_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                rule10, rule11, rule12, rule13, rule14, rule15])
pwm_ = ctrl.ControlSystemSimulation(pwm_ctrl)
pwm_.input['position'] = 6
pwm_.input['distance'] = 9

# Crunch the numbers
pwm_.compute()

print(pwm_.output['pwm'])
pwm.view(sim=pwm_)
