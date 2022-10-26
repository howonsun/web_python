#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
print("content-type: text/html; charset=utf-8\n")
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form=cgi.FieldStorage()
if 'id' in form:
  pageID=form["id"].value
  description=open('data/'+pageID).read()
  #description=description.replace('<','&lt;')
  #description=description.replace('>','&gt;')
  description=sanitizer.sanitize(description)
  update_link='<strong><a href="update.py?id={}">Update</a></strong>'.format(pageID)
  delete_action='''
      <form action="process_delete.py" method="post">
        <input type="hidden" name="pageID" value="{}">
        <input type="submit" value="Delete">
      </form>
  '''.format(pageID)
else:
  pageID='Welcome'
  description = 'Hello Web'
  update_link=''
  delete_action=''
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
  <strong><a href="create.py">Create</a></strong>
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(
      title=pageID, 
      desc=description, 
      listStr=view.getList(), 
      update_link=update_link, 
      delete_action=delete_action
      )
    )