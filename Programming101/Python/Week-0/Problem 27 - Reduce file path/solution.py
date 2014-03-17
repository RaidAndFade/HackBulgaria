# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems2.md#problem-27---reduce-file-path


# FUNCTIONS
def reduce_file_path(path):
    path = path.split("/")
    output_path = []

    for element in path:
        if element == "..":
            if output_path:
                output_path.pop()
        elif element != "." and element != "/":
            output_path.append(element)

    output_path = list(filter(None, output_path))
    return "/" + "/".join(output_path)


# main
def main():
    reduce_file_path("/")
    reduce_file_path("/srv/../")
    reduce_file_path("/srv/www/htdocs/wtf/")
    reduce_file_path("/srv/www/htdocs/wtf")
    reduce_file_path("/srv/./././././")
    reduce_file_path("/etc//wtf/")
    reduce_file_path("/etc/../etc/../etc/../")
    reduce_file_path("/etc//wtf/")
    reduce_file_path("/etc/../etc/../etc/../")
    reduce_file_path("//////////////")
    reduce_file_path("/../")


# PROGRAM RUN
if __name__ == '__main__':
    main()
