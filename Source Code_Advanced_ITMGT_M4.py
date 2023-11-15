def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["follows"] and from_member in social_graph[to_member]["follows"]:
        return "friends"
    elif to_member in social_graph[from_member]["follows"]:
        return "follower"
    elif from_member in social_graph[to_member]["follows"]:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    size = len(board)
    
    # Check rows and columns
    for i in range(size):
        if all(board[i][j] == board[i][0] for j in range(size)):
            return board[i][0]
        if all(board[j][i] == board[0][i] for j in range(size)):
            return board[0][i]

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]
    if all(board[i][size - i - 1] == board[0][size - 1] for i in range(size)):
        return board[0][size - 1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop
    
    while current_stop != second_stop:
        total_time += route_map[current_stop][second_stop]
        current_stop = route_map[current_stop]["next_stop"]
    
    return total_time
