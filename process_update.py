#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe


import cgi, os
form=cgi.FieldStorage()
pageID=form["pageID"].value
title=form["title"].value
description=form["description"].value

opened_file=open('data/'+pageID,'w')
opened_file.write(description)
opened_file.close()

if pageID != title:
	os.rename('data/'+pageID, 'data/'+title)

#redirection
print("Location: index.py?id="+title)
print()