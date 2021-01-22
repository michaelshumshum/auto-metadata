import os, sys, stat
import music_tag
import shutil

source_directory = ''
dest_directory = ''
file_types = ['.m4a','.mp3','.wav','.aiff']

files = os.listdir(source_directory)
for file in files:
    if not any(type in file for type in file_types):
        files.remove(file)
for i in range(len(files)):
    song = files[i]
    files[i] = source_directory+files[i]
    os.chmod(files[i],stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    load_song = music_tag.load_file(files[i])
    x1 = song.find(' - ')
    for type in file_types:
        x2 = song.find(type)
        if x2 != -1:
            break
    load_song['title'] = song[x1+3:x2]
    load_song['artist'] = song[:x1]
    load_song.save()
    shutil.move(files[i],dest_directory)

print('Edited metadata of:')
for file in files:
    print(file)
