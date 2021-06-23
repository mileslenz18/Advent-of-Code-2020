def getFileContet(url):
    with open(url) as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    return content
