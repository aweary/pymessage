#! /usr/local/bin/python3

from applescript import asrun, asquote
from user import register
import sys

flag = sys.argv[1]
name = sys.argv[2]
number = sys.argv[3]

if flag == '-r':
	register(name, 'SMS', number)

# ascript = '''
# 		tell application "Messages"
# 			set targetService to 1st service whose service type = iMessage
# 			set targetBuddy to buddy {0} of targetService
# 			send {1} to targetBuddy
# 		end tell
# '''.format(asquote(number), asquote(message))
# asrun(ascript)
#
print(flag, name, number)
