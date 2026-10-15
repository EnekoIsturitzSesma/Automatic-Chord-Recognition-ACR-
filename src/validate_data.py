import mirdata

beatles = mirdata.initialize('beatles', data_home='data/beatles')
print("Validating the dataset integrity...")

validation_report = beatles.validate()

all_valid = all(validation_report.values())

if all_valid:
    print("All good! The audio and annotations match the official version.")
else:
    print("Careful! There are discrepancies in some files (check names or versions).")
    for track_id, status in validation_report.items():
        if not status:
            print(f"Track with problems: {track_id}")