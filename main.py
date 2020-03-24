import pyhop

pyhop.declare_methods('move', move_iterative)

def move_iterative(state,goal):
    for who in goal.loc.keys():
        x = state.loc[who]
        y = goal.loc[who]
        if x != y:
            return [('travel_method',who,x,y), ('travel',goal)]
    return []



def mover_paqueteM1(state, paquete, ubicacion_paquete, destino):
    return[('conseguir_camion', ubicacion_paquete), ('conseguir_conductor', destino), ('cargar_paquete', paquete), ('conducir_al_destino', ubicacion_paquete, destino), ('descargar_paquete', paquete)]


pyhop.declare_methods('mover_paquete', mover_paqueteM1)

def ya_disponible(state, destino):
    for truck in state.trucks.keys():
        if state.trucks[truck] == destino:
            return []
        else: return False


def mover_camion(state, destino):
    for truck in state.trucks.keys():
        ubicacion = state.trucks[truck]
    return[('conseguir_conductor', ubicacion), ('conducir_al_destino', ubicacion, destino)]

pyhop.declare_methods('conseguir_camion', ya_disponible, mover_camion)

def ya_presente(state, destino):
    for driver in state.drivers.keys():
        if state.drivers[driver] == destino:
            return []
        else: return False

def desplazarse_carretera(state, destino):
    for driver in state.drivers.keys():
        ubicacionDriver = state.drivers[driver]
        for truck in state.trucks.keys():
            ubicacionTruck = state.trucks[truck]
            if ubicacionDriver == ubicacionTruck:
                return [('conducir_al_destino', ubicacionDriver, destino)]
    return False

def desplazarse_sendas(state, destino):
    return [('moverse_por_sendas', destino)]

pyhop.declare_methods('conseguir_conductor', ya_presente, desplazarse_carretera, desplazarse_sendas)

def 

#INITIAL STATE

state1 = pyhop.State('state1')

state1.connectionRoad = {'C0':{'C1', 'C2'}, 'C1':{'C0', 'C2'}, 'C2':{'C0', 'C2'}} 

state1.connectionPath = {'P_01':{'C1','C2'}, 'P_12':{'C1', 'C2'}}

state1.packets = {'P1': 'C0', 'P2': 'C0'}

state1.drivers = {'D1': 'P_01', 'D2': 'P_12'}

state1.trucks = {'T1': 'C1', 'T2': 'C0'}

state1.busesPrices = {'C0': {'P_01': 5}, 'P_01': {'C0': 5, 'C1': 4}, 'C1': {'P_01': 4, 'P_12': 7}, 'P_12': {'C1': 7, 'C2': 2}, 'C2':{'P_12': 2}}

state1.drivers = {'D1': 'P_01', 'D2': 'C1'}

# Objective definition

goal1 = pyhop.Goal('goal1')
goal1.loc = {'D1':'C1', 'T1':'C1', 'P1':'C1', 'P2':'C2'}