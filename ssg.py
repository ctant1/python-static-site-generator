import typer
from ssg.site import site

def main(source="content", dest=dist):
    config = {
        "source": source,
        "dest": dest
        }
    mysite = Site(**config)
    mysite.build(mysite)

typer.run(main)