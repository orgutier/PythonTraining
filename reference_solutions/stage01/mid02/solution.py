race_distance_km_text = "42.195"
elapsed_minutes_text = "255"
target_minutes_text = "240"

race_distance_km = float(race_distance_km_text)
elapsed_minutes = int(elapsed_minutes_text)
target_minutes = int(target_minutes_text)

pace_min_per_km = elapsed_minutes / race_distance_km

pace_report = (
    f"{(minutes_over := elapsed_minutes - target_minutes)} minutes over target, "
    f"averaging {pace_min_per_km:.2f} min/km"
)

minutes_over_per_km = minutes_over / race_distance_km

on_pace = 0 < pace_min_per_km <= 6.5

total_penalty_seconds = 0
total_penalty_seconds += 30
total_penalty_seconds += minutes_over * 2

fatigue_index = 2 + 3 * pace_min_per_km ** 2

print(pace_report)
