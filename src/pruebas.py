import mirdata

beatles = mirdata.initialize('beatles', data_home='data/beatles')

for track_id in beatles.track_ids[:5]:
    track = beatles.track(track_id)
    print(f"ID: {track_id} | Título: {track.title} | Audio path: {track.audio_path}")