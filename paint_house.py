def paint_house(costs):

    cost_min = 0
    index = -1

    for i in range(costs):
        min_index = -1
        min_cost = 0
        other_index = []

        min_cost = min(costs[i])
        min_index = costs[i].index(min_cost)
        for j in range(3):
            if costs[i][j] < min_cost:
                min_index = j
            else:
                other_index.append(j)
        if min_index == index:
            cost_min += min(costs[i][other_index[0]],costs[i][other_index[1]])
            index = costs[i].index(min(costs[i][other_index[0]],costs[i][other_index[1]]))
        else:
            cost_min += min_cost
            index = min_index

    return cost_min