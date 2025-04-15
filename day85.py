#  creating command line utility
import argparse
import requests

def DownloadFile(url, local_filename):
 if local_filename == "None":
    local_filename = url.split('/')[-1]
    r = requests.get("https://imagej.net/images/")
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 
parser = argparser.ArgumentParser()

# add command line arguments
parser.add_argument("url", help="url of the file to download")
parser.add_argument("output", help="by which name do you want to save your file")

# parse the arguments
args = parser.parse_args()

# use the arguments in your code
print(args.url)
print(args.output) 
download_file("args.url","args.output")