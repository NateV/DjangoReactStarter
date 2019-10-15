# Start up development servers.
# this requires running `npm run watch` in one process
# and flask run in another.

from multiprocessing import Process
import subprocess

def npm():
    subprocess.run("npm run watch", shell=True)

def django():
    #subprocess.run("pipenv run flask run", shell=True)
    subprocess.run("pipenv run python manage.py runserver", shell=True)

if __name__ == '__main__':
    npm_p = Process(target=npm)
    django_p = Process(target=django)
    npm_p.start()
    django_p.start()
