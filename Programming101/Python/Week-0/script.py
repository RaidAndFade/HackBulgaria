# A Py script that traverses a folder and runs unit tests named test.py.

# IMPORTS
from os import walk, path
from subprocess import call


# main
def main():
    for root, dirs, files in walk("."):
        for filename in files:
            if filename == "test.py":
                filename = path.join(root, filename)
                try:
                    call("python3 \"%s\"" % (filename), shell=True)

                except Exception as error:
                    print("MAYDAY! Error encountered!")
                    print(error)


# PROGRAM RUN
if __name__ == "__main__":
    main()
