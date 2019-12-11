def load(path):
    with open(path, "r") as file:
        contents = file.readlines()
        urls = []
        for link in contents:
            urls.append(link.strip('\n'))

    return urls
