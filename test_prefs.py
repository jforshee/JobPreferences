from random import shuffle
from ranked_prefs import assign_roles, shuffled

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
    'Banda' : shuffled([ADC, SPT, TOP, MID]) + [JGL]    # The man only cares about not playing jungle -.-
}

mapping = assign_roles(preferences)
for k, v in mapping.items():
    print(k, string_reps[v], sep = ': ')
