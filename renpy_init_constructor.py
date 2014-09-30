#!/usr/bin/env python
#-*-coding:Utf-8-*-
# version : 0.5
# First, of course this script is purely GPL : you're welcome if you want ton enhance it (Fufuuuuu and it's needed !)
#
# Modify the Parameters section according to your project
# This script is intended to be executed just a rep below assets (BG directory, Sprites directory, ...). It will parse the subdirectories
# However, try to organize your directories to generate a usable-for-common-user script !
# 
# Working fine with my GNU/Linux distro
# Should work with MacOS and Windows since no unix-unique methods are used
#
# for any comments : baldarhion@gmail.com


# Parameters section

indent = "     "                   # Number of " " you like to use in your script for indentation purpose
path_to_character = "/Character/"  # Of course use of absolute path is allowed
path_to_BG = "/Background/"        #
dest= "_script.rpy"                # The script generated . To prevent accidental "script.rpy"  brutal death...

intro_text = ("""\
# Ren'Py, by Py'Tom (Kudos to you !)
#
﻿# You can place the script of your game in this file.
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
#
# Declare characters used by this game.


""")

# Dear Python, i think you'll need this:                                    
import os
import os.path


# Let's go !

dest = open ("./_script.rpy","w")   # Create _script.rpy WARNING: it will replace any existing "_script.rpy"
dest.write (intro_text)             # Write Header to our new very friend "_script.rpy" 


# Generate Characters &  Sprites Declarations (Hum... experimental for Characters declaration (if the subdirectories are named with char name, it's ok)

dest.write ("# Characters declaration ##############################################################################\n\n")

list_seq = []

for root, dirs, files in os.walk("."+path_to_character):  # Well, let'move in the character directory... Assume there  is one dir per character
  for name in dirs :                                      # Let's parse the directories...
    for sprite in os.listdir("."+path_to_character+name): # and let's parse the files in these directories
      acces_file = (path_to_character+sprite)             # Assuming that the name of the file reflect the sprite posture,
      sprite = sprite.replace("_"," ")                    # Very optional... Just to replace "_" of the file name with " " (not recommanded)
      if sprite.endswith ((".png",".PNG",".jpg",".JPG")): # Strip off file's type
        sprite = sprite [:-4]                             
      files.append (path_to_character)                    # Concatenate path+file name
      seq = ("image "+sprite+":\""+acces_file+"\"\n"+indent+"yanchor 1 ypos 1 xanchor 0.5\n"+indent+"zoom 0.6\n"+indent+"subpixel True\n") #Of course, you can remove anchor, zoom setting heh ;)
      list_seq.append(seq)                                # append codes lines to a list (we'll see why further...)
    tag_char = name.lower()[0:3]                          # Assuming the directory's name is also the character name, we get the 3 first letters(lowercase) 
    name_char = name.replace ("/","")                     # we remove the "/" and the "."
    name_char.replace (".","")                            # and with that we have our three-letters tags !
    seq_char = ("define "+tag_char+" character (\""+name_char+"\", who_xalign=0.5)\n")
    dest.write (seq_char)                                 # Write the declaration to our _script.rpy
dest.write ("\n\n# Sprites declaration ###################################################################################\n\n")

for seq in list_seq :                                     # and now, we write line by line the sprites declarations
  dest.write (seq)                                        # Else the result vwould be an awful mix of Sprites/character declaration.
                                                          # and it would be messy, very messy... And I don't like mess (*ahem...*)

# Generate BG
dest.write ("\n\n# BG begins here ####################################################################################\n\n\n")


for fich in os.listdir("."+path_to_BG):                   # Parsing the given directory
  fich2 = fich
  fich = fich.lower()                                     # lowering the string
  if fich.endswith ((".PNG",".png",".JPG",".jpg")):       # Strip off file's type to generate the right name to call the BG
    fich = fich [:-4]
  seq = ("image bg "+fich+":"+path_to_BG+fich2+"\n"+indent+"x.align 0.5\n"+indent+"y.align 0.5\n\n")
  dest.write (seq)
    
print ("Job's done ! You can edit \"_script.rpy\" now...")

dest.close()

# Yep... code is drown in comments... And i like that... 
# This code is not optimised for... huh... education purpose (:o]) (at least... mine :p)
# Hope it will be useful for those who want to port Dostoievsky books to VN. 


