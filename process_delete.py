#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe


import cgi, os
form=cgi.FieldStorage()
pageID=form["pageID"].value

os.remove('data/'+pageID)

#redirection
print("Location: index.py")
print()