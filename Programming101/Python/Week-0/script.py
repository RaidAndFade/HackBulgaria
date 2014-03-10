# A Py script that traverses a folder and runs unit tests named test.py.

# IMPORTS
import glob
from subprocess import call

# main
def main():
    unit_test = str(input("Unit test's name:>"))
    files = (glob.glob('*/%s' % unit_test))
    for filename in files:
        call("python3 \"%s\"" % (filename), shell=True)


# PROGRAM RUN
if __name__ == "__main__":
    main()
