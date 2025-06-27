import docker
from jinja2 import Environment, FileSystemLoader

client = docker.from_env()

app_name = "vpn.app.name"
port_nr = "vpn.app.port"

containers = client.containers.list()

applications=[]
vpn="optiplex.tail71d46f.ts.net"

for container in containers:
    labels = container.labels
    app_info = {"name": labels.get(app_name), "port": labels.get(port_nr)}
    if app_info["name"] != None and app_info["port"] != None:
        applications.append(app_info)


environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("homepage_bookmarks.jinja")

content = template.render(applications=applications, vpn=vpn)
print(content)
