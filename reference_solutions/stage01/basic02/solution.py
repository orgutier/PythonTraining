total_seconds_text = "9384"
is_daylight_saving_text = "False"

total_seconds = int(total_seconds_text)

hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

is_daylight_saving = is_daylight_saving_text == "True"

print(
    str(total_seconds) + "s = " + str(hours) + "h " + str(minutes) + "m " +
    str(seconds) + "s"
)
