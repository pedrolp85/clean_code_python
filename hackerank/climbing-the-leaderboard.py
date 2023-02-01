from typing import List


def climbingLeaderboard(ranked, player):
    # Write your code here
    pass


def remove_duplicates(array: List[int]) -> List[int]:
    return_list = []

    index = 0
    value = 10000000
    while index < len(array):

        if array[index] < value:
            return_list.append(array[index])
            value = array[index]
        index += 1

    return return_list


def remove_duplicates_david(array: List[int]) -> List[int]:
    array_size = len(array)
    if array_size == 0:
        return []
    return_list = [array[0]]
    index = 1
    while index < array_size:
        if array[index] != return_list[-1]:
            return_list.append(array[index])
        index += 1
    return return_list


def solve_ranked_first_version(ranked, player):

    player_rank = []
    unique_sorted_rank = list(set(ranked))
    unique_sorted_rank.sort()

    i = 0
    current_position = len(unique_sorted_rank) + 1
    for score in player:

        if current_position > 1:
            while i < len(unique_sorted_rank) and score >= unique_sorted_rank[i]:
                current_position -= 1
                i += 1

        player_rank.append(current_position)

    return player_rank


def solve_ranked_no_set(ranked, player):

    player_rank = []
    unique_rank = remove_duplicates_david(ranked)

    rank_index = len(unique_rank) - 1
    current_position = len(unique_rank) + 1

    for score in player:
        if current_position > 1:

            while rank_index >= 0 and score >= unique_rank[rank_index]:
                current_position -= 1
                rank_index -= 1

        player_rank.append(current_position)

    return player_rank


def solve_ranked_no_unique(ranked, player):
    player_rank = []

    ranked_size = len(ranked) - 1

    position = 1

    for score in player:
        rank_index = 1
        last_value = ranked[0]

        while rank_index <= ranked_size and score < ranked[rank_index]:

            if ranked[rank_index] != last_value:
                position += 1
            rank_index += 1

        player_rank.append(position)

    return player_rank


def solve_ranked_no_unique_david(ranking, player):
    player_rank = []
    player_index = len(player) - 1
    ranking_size = len(ranking)
    ranking_index = 0
    position = 1

    while ranking_index < ranking_size and player_index >= 0:
        current_player = player[player_index]
        ranking_points = ranking[ranking_index]
        if current_player >= ranking_points:
            player_rank.append(position)
            player_index -= 1
        else:
            ranking_index += 1
            if ranking_index < ranking_size and ranking[ranking_index] < ranking[ranking_index - 1]:
                position += 1
    position += 1
    while player_index >= 0:
        player_rank.append(position)
        player_index -= 1

    return player_rank[::-1]


if __name__ == "__main__":

    ranked = [100, 100, 50, 40, 40, 20, 10]
    player = [1, 5, 25, 50, 120]

    print(solve_ranked_first_version(ranked, player))
    print(solve_ranked_no_set(ranked, player))
    print(solve_ranked_no_unique(ranked, player))
    print(solve_ranked_no_unique_david(ranked, player))
