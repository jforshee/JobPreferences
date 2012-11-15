from random import shuffle
from ranked_prefs import assign_roles, shuffled

## This is a sample program on how to use the ranked_prefs library.
## It is an implementation of assigning roles for the team game League
## of Legends. The names used are online tagnames of my teammates, as
## well as their preferences on roles, in descending order. For example,
## Garver has the preference ordering ADC > SPT > TOP > MID > JGL, which
## is encoded as [ADC, SPT, TOP, MID, JGL].

ADC, SPT, MID, TOP, JGL = range(5)
string_reps = {
    ADC : 'Carry',
    SPT : 'Support',
    MID : 'Mid',
    TOP : 'Top',
    JGL : 'Jungle'
}

preferences = {
    'Garver' : [ADC, SPT, TOP, MID, JGL],
    'Benny' : [MID, TOP, JGL, ADC, SPT],
    'Banda' : shuffled([ADC, SPT, TOP, MID]) + [JGL],   # The man only cares about not playing jungle -.-
    'Vekter' : [TOP, ADC, MID, JGL, SPT],
    'Frostee' : [ADC, JGL, MID] + shuffled([TOP, SPT]), # Only cares about ADC, Jungle, and Mid
    'Temby' : [SPT, MID, ADC, TOP, JGL]
}

mapping = assign_roles(preferences)
for k, v in mapping.items():
    print(k, string_reps[v], sep = ': ')
