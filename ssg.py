import typer
from ssg.site import site

main(source="content", dest=dist):
    config = {
        "source": source,
        "dest": dest
        }
    mysite = site(**config)
    mysite.build(mysite)

typer.run(main)