# 贪婪算法：集合覆盖问题
# 需要被覆盖的州
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# 每个广播台覆盖的州
stations = dict()
stations["k1"] = {"id", "nv", "ut"}
stations["k2"] = {"wa", "id", "mt"}
stations["k3"] = {"or", "nv", "ca"}
stations["k4"] = {"nv", "ut"}
stations["k5"] = {"ca", "az"}

# 最终选择的广播台list
final_stations = []
# 每轮最好的广播台名
best_station = None

while len(states_needed) > 0:
    states_coverd = set()  # 每轮最好广播台覆盖的州
    for station, states_for_station in stations.items():
        include_now = states_needed & states_for_station
        if len(include_now) > len(states_coverd):
            best_station = station
            states_coverd = include_now
    final_stations.append(best_station)
    states_needed -= states_coverd  # 差集，需要覆盖的广播台减少
print(final_stations)

