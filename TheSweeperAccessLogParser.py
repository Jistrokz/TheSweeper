creator = "Kartavya Trivedi"
projectLocation = "https://github.com/Jistrokz/TheSweeper"

import re

rx = re.compile(r'"(?:GET|POST)\s+([^\s?]*)', re.M)


def ParseAccessedFileNameList(RequestString) :
    return rx.findall(RequestString)


def GetAccessedFilesList(AccessLogs):
    AccessedFileSet = set()
    for line in AccessLogs:
            matches = ParseAccessedFileNameList(line) # passing a single line, the list will contain only 1 element
            if matches is None or len(matches) <= 0:
                continue
            AccessedFileSet.add(matches[0])

    return AccessedFileSet

