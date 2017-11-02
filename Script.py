import os.path

# Download latest version of the page and check if it changed


if not os.path.isfile("testfiles/result.csv"):
    if os.path.isfile("testfiles/long.html"):
        import Parser
else:
    if os.path.isfile("testfiles/long.html"):
        if os.path.getmtime("testfiles/long.html") > os.path.getmtime("testfiles/result.csv"):
            import Parser

