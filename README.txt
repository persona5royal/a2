
# Edward Lee
# edwarhl4@uci.edu
# 61666868

A1P1 COMMANDS
	Q --- quit


	L [FILEPATH] [-COMMAND] [OPTIONAL: FIELD] --- list files and folders (in that order, mind you.)
		 -r - recursively
		 -f - files only
		 -s - search [NAME]
		 -e - search [EXTENSION]
		 
		 COMBINATIONS 
		 -r -f = recursively, but files only
		 -r -s [NAME] = recursively searches for file named [NAME] 
		 -r -e [EXTENSION] = recursively searches for files ending in [EXTENSION]

A1P2 COMMANDS
	C [FILEPATH] -n [NAME] --- creates a file with the [NAME] at that [FILEPATH], default extension is .dsu
						   --- SECONDARY CONSIDERATION - after C, should ask for username, password, and biography

	D [FILEPATH] --- deletes a file at [FILEPATH], then prints (f'{path} DELETED')
				 if path is not a .dsu file, print error
	
	R [FILEPATH] --- reads a file at [FILEPATH], then prints it's contents
				 if file is empty, print ("EMPTY")
	
	
A2 COMMANDS	 
	O [FILEPATH] --- open the .dsu file at this filepath location and allow the user to edit and make changes to it.
	             --- print a confirmation message with user details as well
	
	E            --- edits the .dsu file loaded by a C or O command
	                 subcommands
	                    -usr [USERNAME]
	                    -pwd [PASSWORD]
	                    -bio [BIO]
                        -addpost [NEW POST]
                        -delpost [ID]


P
-usr Prints the username stored in the profile object

-pwd Prints the password stored in the profile object

-bio Prints the bio stored in the profile object

-posts Prints all posts stored in the profile object with their ID (using list index is fine)

-post [ID] Prints post identified by ID

-all Prints all content stored in the profile object