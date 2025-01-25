import matplotlib.pyplot as plt

# データセット
scenarios_1 = {
    "OppositeVehicleTakingPriority": 30,
    "StaticCutIn": 30,
    "ControlLoss": 30,
    "ConstructionObstacle": 30,
    "NonSignalizedJunctionLeftTurn": 63,
    "VehicleTurningRoute": 30,
    "InterurbanAdvancedActorFlow": 30,
    "MergerIntoSlowTrafficV2": 30,
    "VehicleOpensDoorTwoWays": 30,
    "ParkedObstacleTwoWays": 30,
    "OppositeVehicleRunningRedLight": 30,
    "NonSignalizedJunctionRightTurn": 30,
    "HardBreakRoute": 30,
    "ParkedObstacle": 30,
    "noScenarios": 30,
    "HighwayExit": 30,
    "InvadingTurn": 30,
    "ParkingExit": 30,
    "CrossingBicycleFlow": 29,
    "Accident": 30,
    "SignalizedJunctionLeftTurn": 30,
    "BlockedIntersection": 30,
    "MergerIntoSlowTraffic": 30,
    "PriorityAtJunction": 30,
    "HazardAtSideLane": 30,
    "DynamicObjectCrossing": 30,
    "AccidentTwoWays": 30,
    "PedestrianCrossing": 30,
    "SignalizedJunctionRightTurn": 30,
    "HighwayCutIn": 30,
    "HazardAtSideLaneTwoWays": 30,
    "EnterActorFlow": 67,
    "EnterActorFlowV2": 50,
    "YieldToEmergencyVehicle": 30,
    "VehicleTurningRoutePedestrian": 66,
    "ParkingCutIn": 30,
    "ParkingCrossingPedestrian": 30,
    "ConstructionObstacleTwoWays": 30,
    "InterurbanActorFlow": 30
}

scenarios_2 = {
    "OppositeVehicleTakingPriority": 80,
    "StaticCutIn": 80,
    "ControlLoss": 80,
    "ConstructionObstacle": 80,
    "NonSignalizedJunctionLeftTurn": 93,
    "VehicleTurningRoute": 80,
    "InterurbanAdvancedActorFlow": 80,
    "MergerIntoSlowTrafficV2": 80,
    "VehicleOpensDoorTwoWays": 80,
    "ParkedObstacleTwoWays": 80,
    "OppositeVehicleRunningRedLight": 80,
    "NonSignalizedJunctionRightTurn": 80,
    "HardBreakRoute": 80,
    "ParkedObstacle": 80,
    "noScenarios": 80,
    "HighwayExit": 80,
    "InvadingTurn": 80,
    "ParkingExit": 80,
    "CrossingBicycleFlow": 49,
    "Accident": 80,
    "SignalizedJunctionLeftTurn": 80,
    "BlockedIntersection": 80,
    "MergerIntoSlowTraffic": 80,
    "PriorityAtJunction": 80,
    "HazardAtSideLane": 80,
    "DynamicObjectCrossing": 80,
    "AccidentTwoWays": 80,
    "PedestrianCrossing": 80,
    "SignalizedJunctionRightTurn": 80,
    "HighwayCutIn": 80,
    "HazardAtSideLaneTwoWays": 80,
    "EnterActorFlow": 97,
    "EnterActorFlowV2": 50,
    "YieldToEmergencyVehicle": 80,
    "VehicleTurningRoutePedestrian": 96,
    "ParkingCutIn": 80,
    "ParkingCrossingPedestrian": 80,
    "ConstructionObstacleTwoWays": 80,
    "InterurbanActorFlow": 80
}

scenarios_3 = {
    "OppositeVehicleTakingPriority": 96,
    "StaticCutIn": 91,
    "ControlLoss": 264,
    "ConstructionObstacle": 94,
    "NonSignalizedJunctionLeftTurn": 93,
    "VehicleTurningRoute": 616,
    "InterurbanAdvancedActorFlow": 99,
    "MergerIntoSlowTrafficV2": 102,
    "VehicleOpensDoorTwoWays": 97,
    "ParkedObstacleTwoWays": 95,
    "OppositeVehicleRunningRedLight": 278,
    "NonSignalizedJunctionRightTurn": 91,
    "HardBreakRoute": 92,
    "ParkedObstacle": 95,
    "noScenarios": 364,
    "HighwayExit": 102,
    "InvadingTurn": 89,
    "ParkingExit": 97,
    "CrossingBicycleFlow": 49,
    "Accident": 94,
    "SignalizedJunctionLeftTurn": 347,
    "BlockedIntersection": 96,
    "MergerIntoSlowTraffic": 97,
    "PriorityAtJunction": 99,
    "HazardAtSideLane": 96,
    "DynamicObjectCrossing": 263,
    "AccidentTwoWays": 90,
    "PedestrianCrossing": 95,
    "SignalizedJunctionRightTurn": 283,
    "HighwayCutIn": 98,
    "HazardAtSideLaneTwoWays": 94,
    "EnterActorFlow": 97,
    "EnterActorFlowV2": 50,
    "YieldToEmergencyVehicle": 93,
    "VehicleTurningRoutePedestrian": 96,
    "ParkingCutIn": 94,
    "ParkingCrossingPedestrian": 89,
    "ConstructionObstacleTwoWays": 93,
    "InterurbanActorFlow": 100
}

# グラフ描画
fig, ax = plt.subplots(figsize=(12, 8))

# カスタムカラー
colors = ['#FFA500', '#00BFFF', '#FF69B4']  # オレンジ、水色、ピンク

# データセット1
ax.bar([i - 0.25 for i in range(len(scenarios_1))], scenarios_1.values(), width=0.25, label='Dataset 1', color=colors[0])

# データセット2
ax.bar([i for i in range(len(scenarios_2))], scenarios_2.values(), width=0.25, label='Dataset 2', color=colors[1])

# データセット3
ax.bar([i + 0.25 for i in range(len(scenarios_3))], scenarios_3.values(), width=0.25, label='Dataset 3', color=colors[2])

# 軸設定
ax.set_xticks(range(len(scenarios_1)))
ax.set_xticklabels(scenarios_1.keys(), rotation=90, fontsize=10)
ax.set_yticks(range(0, 700, 50))  # y軸の目盛りを調整
ax.set_title('Comparison of Three Scenario Distributions', fontsize=14)
ax.set_xlabel('Scenarios', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.legend()

# レイアウトを整えて表示
plt.tight_layout()
plt.show()
