__author__ = 'Boot'

# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        current_comb = (current, letter)
        try:
            next_edge = edges[current_comb]
        except:
            return False

        if next_edge in accepting:
            return True

        return fsmsim(string[1:], next_edge, edges, accepting)



print fsmsim("aaaa1111111",1,edges,accepting)
# >>> True