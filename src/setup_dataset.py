import mirdata

beatles = mirdata.initialize('beatles', data_home='data/beatles')

print("Downloading annotations and metadata...")
beatles.download()
print("Annotations downloaded successfully!")