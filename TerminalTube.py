import os
print("Welcome to TerminalTube!")
search = input("type what you want to search: ")
search = search.replace(" ", "+")
os.system('curl -s \"https://vid.puffyan.us/search?q='+search+'\" | grep -Eo \"watch\?v=.{11}\"')
os.system('curl -s \"https://vid.puffyan.us/search?q=\"'+search+' | grep -o -P \'(?<=<p dir=\\\"auto\\\">).*(?=</p>)\'')
videoplay = input("\n\ntype video link (format: watch?v=abcd12345)\n\n")
os.system('clear')
# If you want to use mpv, chamge 'vlc' to 'mpv'
os.system('vlc \"https://www.youtube.com/\"'+videoplay) # video directly from youtube
