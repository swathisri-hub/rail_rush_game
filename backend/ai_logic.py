def choose_lane(player_lane, obstacle_lane):
    if player_lane == obstacle_lane:
        return max(0, player_lane - 1)
    return player_lane
