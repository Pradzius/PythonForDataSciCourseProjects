def celsius_converter(f_temp: float) -> float:
    """Converts float values of fahrenheit temprature to celsius"""
    return round((f_temp - 32) / 1.8, 2)

def parse_and_clean(line: str) -> list[str | float]:
    """
    Checks if input lines are structured as formatted in 
    the exercise task, has the correct amount of 
    datapoints, the sensor has the correct status and
    that the recorded temprature is not an error value
    Inputs:
    a string formatted as:
    Timestamp | StationID | Temp(F) | Humidity(%) | Sensor_Status
    Outputs:
    a list of these datapoints or None if errors are found 
    """
    data = list(map(lambda x: x.strip(), line.split("|")))
    if len(data) != 5:
        return None
    if data[-1] != "ACTIVE":
        return None
    try:
        data[2] = float(data[2])
    except:
        return None
    return data

skipped_lines = 0

with open("environmental_cleaned.csv", "w") as o:
    with open("environmental_raw.txt", "r") as f:
        for line in f:
            cleaned_line = parse_and_clean(line)
            print
            if cleaned_line == None:
                skipped_lines += 1
            else:
                cleaned_line[2] = str(celsius_converter(cleaned_line[2]))
                o.write(",".join(cleaned_line) + "\n")

print(f"Skipped lines: {skipped_lines}")