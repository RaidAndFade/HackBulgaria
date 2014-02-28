# Problem 27 - Reduce file path
#
# A file path in a Unix OS looks like this - /home/radorado/code/hackbulgaria/week0
#
# We start from the root - / and we navigate to the destination fodler.
#
# But there is a problem - if we have .. and . in our file path, it's not clear where we are going to end up.
#
# .. means to go back one directory
# . means to stay in the same directory
# we can have more then one / between the directories - /home//code
# So for example : /home//radorado/code/./hackbulgaria/week0/../ reduces to /home/radorado/code/hackbulgaria
#
# Implement a function, called reduce_file_path(path) which takes a string and returns the reduced version of the path.
#
# Every .. means that we have to go one directory back
# Every . means that we are staying in the same directory
# Every extra / is unnecessary
# Always remove the last /
# Signature
#
# def reduce_file_path(path):
#     # Implementation
# Test examples
#
# >>> reduce_file_path("/")
# "/"
# >>> reduce_file_path("/srv/../")
# "/"
# >>> reduce_file_path("/srv/www/htdocs/wtf/")
# "/srv/www/htdocs/wtf"
# >>> reduce_file_path("/srv/www/htdocs/wtf")
# "/srv/www/htdocs/wtf"
# >>> reduce_file_path("/srv/./././././")
# "/srv"
# >>> reduce_file_path("/etc//wtf/")
# "/etc/wtf"
# >>> reduce_file_path("/etc/../etc/../etc/../")
# "/"
# >>> reduce_file_path("//////////////")
# "/"
# >>> reduce_file_path("/../")
# "/"

# IMPORTS

# FUNCTIONS
def reduce_file_path(path):
    path = path.split("/")
    print("In list:", path)
    pathOut = ""

    i = 0
    while i < len(path) - 1:
        if path[i+1] == ".." and path[i+1]:
            path[i] = ""
            path[i+1] = ""

        elif path[i] == ".":
            path[i] = ""

        elif path[i] != "":
            pathOut += "/" + path[i]
        i += 1


    if pathOut == "":
        pathOut = "/"

    return pathOut

# main
def main():
    print("Output:", reduce_file_path("/"))
    print("Expected: /\n")

    print("Output:", reduce_file_path("/srv/../"))
    print("Expected: /\n")

    print("Output:", reduce_file_path("/srv/www/htdocs/wtf/"))
    print("Expected: /srv/www/htdocs/wtf\n")

    print("Output:", reduce_file_path("/srv/www/htdocs/wtf"))
    print("Expected: /srv/www/htdocs/wtf\n")

    print("Output:", reduce_file_path("/srv/./././././"))
    print("Expected: /srv\n")

    print("Output:", reduce_file_path("/etc//wtf/"))
    print("Expected: /etc/wtf\n")

    print("Output:", reduce_file_path("/etc/../etc/../etc/../"))
    print("Expected: /\n")

    print("Output:", reduce_file_path("//////////////"))
    print("Expected: /\n")

    print("Output:", reduce_file_path("/../"))
    print("Expected: /\n")

# PROGRAM RUN
main()