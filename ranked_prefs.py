
from random import shuffle
from collections import defaultdict

def find_collisions(mapping):
    new_dict = defaultdict(list)    # Reverse the mapping
    for (k, v) in mapping.items():
        new_dict[v].append(k)

    for k in list(new_dict.keys()): # Delete non-colliding entries (< 2 values)
        if len(new_dict[k]) < 2:
            del new_dict[k]
            
    return new_dict

def assigned(pref, assigned_list):
    for (k, v) in assigned_list.items():
        if v == pref:
            return True
    return False

def assign_roles(preference_mapping):
    if len(preference_mapping) > 5:
        players = input("Who is playing? ").split(',')     # Find out who is playing (relevant for big systems where you have players selected from a pool)
    else:
        players = preference_mapping.keys()
    
    roles = dict((p.strip(), '') for p in players)
    for player in players:
        roles[player] = preference_mapping[player][0]

    collisions = find_collisions(roles)
    return resolve_collisions(collisions, roles, preference_mapping, 1)

def shuffled(the_list):
    new_list = []
    i_list = [i for i in range(len(the_list))]
    shuffle(i_list)
    for i in i_list:
        new_list.append(the_list[i])

    return new_list

def resolve_collisions(collisions, roles, mapping, t):
    if len(collisions) == 0:
        return roles
    
    for (r, p) in collisions.items():
        shuffled_player_list = shuffled(p[1:])  # first obviously gets his pick
        next_set = dict((c, mapping[c][t]) for c in p)
        for rand_p in shuffled_player_list:
            if not assigned(next_set[rand_p], roles):
                roles[rand_p] = next_set[rand_p]

    new_collisions = find_collisions(roles)
    return resolve_collisions(new_collisions, roles, mapping, t + 1)

# Sample run/testing methods
def test():
    test_different_preferences()
    print()
    test_similar_preferences()

def test_different_preferences():
    print ('Different preferences')
    preferences = {
        'p1': [0, 1, 2, 3, 4],
        'p2': [2, 3, 0, 4, 1],
        'p3': [1, 4, 2, 0, 3],
        'p4': [1, 3, 0, 2, 4],
        'p5': [4, 0, 2, 1, 3]
    }

    ADC, SPT, MID, TOP, JGL = range(5)
    string_reps = {
        ADC : 'Carry',
        SPT : 'Support',
        MID : 'Mid',
        TOP : 'Top',
        JGL : 'Jungle'
    }

    mapping = assign_roles(preferences)
    for (k, v) in mapping.items():
        print(k, string_reps[v], sep = ': ')
    
def test_similar_preferences():
    print ('Similar preferences')
    preferences = {
        'p1': [0, 1, 2, 3, 4],
        'p2': [2, 3, 0, 4, 1],
        'p3': [1, 4, 2, 0, 3],
        #'p4': [1, 3, 0, 2, 4],
        'p4': [1, 4, 2, 0, 3],
        #'p5': [4, 0, 2, 1, 3]
        'p5': [1, 4, 2, 0, 3]
    }

    ADC, SPT, MID, TOP, JGL = range(5)
    string_reps = {
        ADC : 'Carry',
        SPT : 'Support',
        MID : 'Mid',
        TOP : 'Top',
        JGL : 'Jungle'
    }

    mapping = assign_roles(preferences)
    for (k, v) in mapping.items():
        print(k, string_reps[v], sep = ': ')
