# auto-metadata
you're a lazy pirate aren't you

## about
if you happen to download youtube music videos using tools like youtube-dl, you can use this script to automatically apply the metadata to the audio file. it will edit the title and artist tags of the file. it doesn't apply album tag or anything. this is just a list comprehension script that gets the data straight from the file name.

before using, please `pip3 install music-tag`. this is the module the script will use to write the metadata to the file. in the script, indicate the `source_directory` and `dest_directory` to where your files are and where you want to move the files afterward. you can make them the same if you want.

please note that depending on the video or file name, it may not work properly. i have had trouble using the script with some old Monstercat videos as the dash in the title is somehow different. if the file's metadata wasn't correctly edited, put the file back in the source directory and manually reformat the file name. 
