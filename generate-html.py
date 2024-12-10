file = open("pages", "r")
template = open("template.html", "r").read()

for project in file.readlines():
    (name, url) = map(str.strip,project.split(" "))

    open(f"{name}.html", "w").write(
        template.replace("%name%", name).replace("%url%", url)
    )
