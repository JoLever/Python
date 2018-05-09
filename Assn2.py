import sys
import re

f = open(sys.argv[1],"r")
with f as fp:
    for cont, contents in enumerate(fp):
            regex = re.compile("^\$\^*(0|[1-9](\d{1,2})?(,\d{3})*)(\.\d{2})?$")
            if(regex.match(contents)):
                line = contents.strip()
                print("Matched: {}{}".format("",line))
            else:
                line = contents.strip()
                print("Not Matched: {}{}".format("",line))



