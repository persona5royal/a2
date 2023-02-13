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
	
	E []