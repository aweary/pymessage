#!/usr/bin/python

from applescript import asrun, asquote
import sys

number = sys.argv[1]
message = sys.argv[2]

ascript = '''
		tell application "Messages"
			set targetService to 1st service whose service type = iMessage
			set targetBuddy to buddy {0} of targetService
			send {1} to targetBuddy
		end tell
'''.format(asquote(number), asquote(message))
asrun(ascript)
