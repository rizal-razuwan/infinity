#!/bin/zsh -xv 

#     #!/bin/zsh -xv or #!/bin/bash 


function mke(){
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
}

mke

#notes 
# python manage.py shell_plus --ipython

