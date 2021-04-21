#!/usr/bin/env python3
"""
This python script implements 
the basic functionality of wget:
Write the content of a web response
to a file with the appropriate extension.

The script follows this basic principle: 
1. Make a web request to the specified server (endpoint)
2. Read the response from the server
3. Write the output to a file (with the correct extension)
"""

# Module imports
import requests
import re
import getopt
import sys


def getFileFromURL(url):
    uri = re.search(r"(?:.(?!\/))+$", url)[0]
    file = uri.replace("/", "")
    return file


def makeFileRequest(url):
    req = requests.get(url)
    return req.content


def writeResponse(content: bytes, filename):
    file = open(filename, "wb")
    file.write(content)
    file.close
    return filename


def main(argv, url=""):
    out_file = ""

    try:
        opts, args = getopt.getopt(argv, "ho:", ["output="])
    except getopt.GetoptError:
        print("usage: ", "pyget.py [-o <outputfile>] <url>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("usage: ", "pyget.py [-o <outputfile>] <url>")
            sys.exit()
        elif opt in ("-o", "--output"):
            out_file = arg
    if "://" not in url:
        print("Please specify a url!")
        print("usage: ", "pyget.py [-o <outputfile>] <url>")
        sys.exit(2)
    file_content = makeFileRequest(url)
    if out_file == "":
        out_file = getFileFromURL(url)
    print()
    print("\nDownloading", out_file, "from", url, "...")
    writeResponse(file_content, out_file)
    print("\nDownloaded ", out_file, "!\n")


if __name__ == "__main__":
    main(sys.argv[1:], sys.argv[-1])
