ga = {"pop_size": 40, "n_gen": 5, "mut_rate": 0.4, "cross_rate": 1}

vehicle_env = {
    "map_size": 200,
    "elem_types": 3,
    "min_len": 5,  # minimal possible distance in meters
    "max_len": 30,  # maximal possible disance to go straight in meters
    "min_angle": 10,  # minimal angle of rotation in degrees
    "max_angle": 80,  # maximal angle of rotation in degrees
}

robot_env = {
    "map_size": 40,
    "elem_types": 2,
    "min_len": 8,  # 3,  # minimal possible distance in meters
    "max_len": 15,  # 12,#15,  # maximal possible disance to go straight in meters
    "min_pos": 1,  # minimal possible
    "max_pos": 38,  # 49 29,  # maximal possible position in meters
}


files = {
    "stats_path": ".\\stats",
    "tcs_path": ".\\tcs",
    "images_path": ".\\images"
}
