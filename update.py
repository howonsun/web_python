#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
print("content-type: text/html; charset=utf-8\n")
import cgi, os, view

form=cgi.FieldStorage()
if 'id' in form:
  pageID=form["id"].value
  description=open('data/'+pageID).read()
else:
  pageID='Welcome'
  description = 'Hello Web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ul>
    {listStr}
  </ul>
  <a href="create.py">Create</a>
  <form action="process_update.py" method="post">
  	<p><input type="hidden" name="pageID" value="{form_default_title}"></p>
    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
    <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
    <p><input type="submit" value="Update"></p>
  </form>
</body>
</html>
'''.format(
      title=pageID, 
      desc=description, 
      listStr=view.getList(), 
      form_default_title=pageID, 
      form_default_description=description
      )
)