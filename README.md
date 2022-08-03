# ChangeMyDesktop and I'll LearnToLive!

This repository contains a script that changes my wallpapers with images
with different themes. For example, an image of a key position from some 
past chess game where some tactic was missed, or some strategic error was
made, can be made as the home desktop. The program can be run two or three
times a day by a crontab or the Windows tasks scheduler. Hopefully by repeatedly 
seeing the key positions in which some mistake or tactic was missed we will
be better able to learn from them. Great insights made by past or present
philosophers can also be made as the desktop image. In this case, the --theme
option should be used with "Philosophy" rather than "Chess".


The change_my_wallpaper script can be run in two ways:
(1) By specifying a theme, with the --theme option flags.
(2) Without specifying a theme. In this case the script
picks a theme at random, from a list. The current themes are: Chess, Philosophy, Maths, and Music.

As an example, to run the script while specifying the theme to be Chess, the following
command might be run in the shell (assuming Bash):

"py change_my_wallpaper --theme Chess"

Note: In the shell, the double quotation marks would not be needed.
