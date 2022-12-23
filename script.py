from weasyprint import HTML,CSS
from jinja2 import Environment, FileSystemLoader
import json


env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("final_template.html")


with open('data.json', 'r', encoding='utf-8') as f:
    my_data = json.loads(f.read())
    print(my_data)
    print(type(my_data))
    for i in my_data['services']:
        print(f"{i}: {my_data['services'][i]}")
        
template_vars = {
    "name" : my_data['name'],
    "invno": my_data['invno'],
    "vac":my_data['vac'],
    "services":my_data['services'],
    "total":my_data['total']
 }

html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("icr.pdf",stylesheets=[CSS('template_css.css')])
