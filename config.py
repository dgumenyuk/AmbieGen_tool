ga = {"pop_size": 150, "n_gen": 100, "mut_rate": 0.4, "cross_rate": 1}

vehicle_env = {
    "map_size": 200,
    "min_len": 5,  # minimal possible distance in meters
    "max_len": 30,  # maximal possible disance to go straight in meters
    "min_angle": 10,  # minimal angle of rotation in degrees
    "max_angle": 80,  # maximal angle of rotation in degrees
}

robot_env = {
    "map_size": 40,  # 50,
    "min_len": 8,  # 3,  # minimal possible distance in meters
    "max_len": 15,  # 12,#15,  # maximal possible disance to go straight in meters
    "min_pos": 1,  # minimal possible
    "max_pos": 38,  # 49 29,  # maximal possible position in meters
}


files = {
    "ga_archive": ".\\GA_archive\\",
    "tc_img": ".\\TC_img\\",
    "tc_file": ".\\TC_file\\",
    "ga_conv": ".\\GA_conv\\",
}
