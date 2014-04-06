# Documentation
# https://github.com/HackBulgaria/Programming101/blob/master/week5/problems.md#the-github-problem


# IMPORTS
from local_config import github_username
from local_config import github_password
from os.path import splitext
import requests
import zipfile
import io


# FUNCTIONS
def auth_request(path):
    return requests.get(path, auth=(github_username(), github_password()))


def _fetch_user_name_info(username):
    return auth_request("https://api.github.com/users/{}".format(username)).json()


def _fetch_user_repos_names(username):
    all_repos_data = auth_request("https://api.github.com/users/{}/repos".format(username)).json()
    repo_names = []
    for dictionary in all_repos_data:
        for data in dictionary:
            if data == "html_url":
                repo_names.append(dictionary[data])
    return repo_names


def show_user_info(username_info):
    output = ["~~~~~Username info~~~~~"]
    try:
        output.append("Name: {}".format(username_info["name"]))
    except KeyError:
        return "Error: No such username in Github."
    output.append("Username: {}".format(username_info["login"]))
    output.append("Email: {}".format(username_info["email"]))
    output.append("Location: {}".format(username_info["location"]))
    output.append("Public gists: {}".format(username_info["public_gists"]))
    output.append("Public repos: {}".format(username_info["public_repos"]))
    return "\n".join(output)


def show_user_repos(username_repos):
    output = ["\n~~~~~Username repos~~~~~"]
    output += username_repos
    return "\n".join(output)


def _fetch_repos_contents(username_repos):
    output = []
    for repo_name in username_repos:
        zip_url = "{}/archive/master.zip".format(repo_name)
        request = auth_request(zip_url)
        try:
            zip_file = zipfile.ZipFile(io.BytesIO(request.content), "r")
            for filename in zip_file.namelist():
                filename = filename.replace("-master", "/blob/master")
                output.append(filename)
        except zipfile.BadZipfile:
            continue
    return output


def get_file_extensions_set(username_repos_contents):
    filenames = set()
    for filename in username_repos_contents:
        filenames.add(splitext(filename)[1])
    return filenames


def get_file_extensions_list(username_repos_contents):
    filenames = []
    for filename in username_repos_contents:
        filenames.append(splitext(filename)[1])
    return filenames


def file_extensions_occurrence(username_repos_contents):
    file_extensions_set = get_file_extensions_set(username_repos_contents)
    file_extensions_list = get_file_extensions_list(username_repos_contents)
    occurrence_dictionary = {}
    for file_ext in file_extensions_set:
        if file_ext not in occurrence_dictionary.keys():
            occurrence_dictionary[file_ext] = file_extensions_list.count(file_ext)
    return occurrence_dictionary


def show_occurrences(username_repos_contents):
    dictionary = file_extensions_occurrence(username_repos_contents)
    output = []
    for key in dictionary:
        output.append("{} - {}".format(key, dictionary[key]))
    return "\n".join(sorted(output))


def show_total_number_of_files(file_extensions):
    return "Number of files: {}".format(len(file_extensions))


def show_total_lines_of_code(username, username_repos_contents):
    total_count = 0
    for filename in username_repos_contents:
        path = "http://github.com/{}/{}".format(username, filename)
        if path[-1] != "/":
            request = auth_request(path)
            contents = request.text
            print(contents.count("\n"))
            total_count += contents.count("\n")
    return "Total lines of code: {}".format(total_count)


# main
def main():
    username = input("github username>")
    username_info = _fetch_user_name_info(username)
    username_repos = _fetch_user_repos_names(username)
    username_repos_contents = _fetch_repos_contents(username_repos)
    file_extensions = get_file_extensions_list(username_repos_contents)

    print(show_user_info(username_info))
    print(show_user_repos(username_repos))
    print(show_total_number_of_files(file_extensions))
    print(show_occurrences(username_repos_contents))
    # print(show_total_lines_of_code(username, username_repos_contents))



if __name__ == '__main__':
    main()
