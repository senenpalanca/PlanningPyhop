pyhop.declare_methods('move', move_iterative)






#INITIAL STATE

state1 = pyhop.State('state1')

state1.connectionRoad = {'C0':{'C1', 'C2'}, 'C1':{'C0', 'C2'}, 'C2':{'C0', 'C2'}} 

state1.connectionPath = {'P_01':{'C1','C2'}, P_12:{'C1', 'C2'}}

state1.packets = {'P1': 'C0', 'P2': 'C0'}

state1.drivers = {'D1': 'P_01', 'D2': 'P_12'}

state1.trucks = {'T1': 'C1', 'T2': 'C0'}

state1.busesPrices = {'C0': {'P_01': 5}, 'P_01': {'C0': 5, 'C1': 4}, 'C1': {'P_01': 4, 'P_12': 7}, 'P_12': {'C1': 7, 'C2': 2}, 'C2':{'P_12': 2}}

state1.drivers = {'D1': 'P_01', 'D2': 'C1'}

# Objective definition

goal1 = pyhop.Goal('goal1')
goal1.loc = {'D1':'C1', 'T1':'C1', 'P1':'C1', 'P2':'C2'}