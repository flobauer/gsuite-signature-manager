from httplib2 import Http
from pystache import Renderer
import csv

def write_file(email, name, title, tel, telnice):
  with open('signatures/'+email+'.html', 'w+') as f:
    f.write(Renderer().render_path('template.mustache', {
            'name': name,
            'title': title,
            'tel': tel,
            'telnice': telnice,
            'email': email
        }))

with open('users.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        write_file(row[0], row[1], row[2], row[3], row[4])