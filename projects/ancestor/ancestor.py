
def earliest_ancestor(ancestors, starting_node):
    table = {}
    for i in ancestors:
        if i[1] not in table:
            table[i[1]] = [i[0]]
        elif i[0] not in table[i[1]]:
            table[i[1]].append(i[0])
    
    if starting_node not in table:
        return -1
    visited = []
    position = starting_node
    while position in table:
        if position != starting_node:
            visited.append(position)
        if len(table[position]) == 1:
            position = table[position][0]
        else:
            if table[position][0] in table:
                position = table[position][0]
            elif table[position][1] in table:
                position = table[position][1]
            else:
                if table[position][0] > table[position][1]:
                    position = table[position][1]
                else: 
                    position = table[position][0]
    print(position)   
    return position