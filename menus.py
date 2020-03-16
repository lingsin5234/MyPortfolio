# navbar menu
from menu import Menu, MenuItem
from django.urls import reverse
from . import views as resume_vw
from djangoapps import settings as st


# add items to the main menu
Menu.add_item("main", MenuItem("Home", reverse(resume_vw.homepage), weight=10))
Menu.add_item("main", MenuItem("Resume", reverse(resume_vw.show_resume), weight=10))

# set if statement for the links to other apps - which won't work in dev
debug = st.DEBUG
if debug:
    # make fake links
    Menu.add_item("main", MenuItem("Projects", url="#", weight=10))
else:
    # the real links that will be accepted in prod
    from baseball import views as baseball_vw
    Menu.add_item("main", MenuItem("Baseball", reverse(baseball_vw.homepage), weight=10))
    from budget import views as budget_vw
    Menu.add_item("main", MenuItem("Budget App", reverse(budget_vw.homepage), weight=10))
