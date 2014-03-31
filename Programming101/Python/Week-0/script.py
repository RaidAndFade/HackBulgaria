# A Py script that traverses a folder and runs unit tests named test.py.


# IMPORTS
from glob import glob
from subprocess import call


# main
def main():
    files = glob('*/test*')
    for filename in files:
        call("python3 \"%s\"" % (filename), shell=True)


# PROGRAM RUN
if __name__ == "__main__":
    main()
