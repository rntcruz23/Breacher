#!/usr/bin/python3

import requests #module for making request to a webpage
import threading #module for multi-threading
import argparse #module for parsing command line arguments

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
parser = argparse.ArgumentParser() #defines the parser

#Arguements that can be supplied
parser.add_argument("-u", help="target url", dest='target')
parser.add_argument("-c", help="Concurrent threads to use", dest='threads', type=int, default=0)
parser.add_argument("--paths", help="uses multithreading", dest='paths', default="paths.txt")
parser.add_argument("-b", "--cookies", type=str, dest="cookies", help="Cookies to send with requets")
args = parser.parse_args() #arguments to be parsed

target = args.target #Gets tarfet from argument

def scan(links):
    for link in links: #fetches one link from the links list
        link = target + link.strip() # Does this--> example.com/admin/
        r = requests.get(link, verify=False, headers={"Cookies":args.cookies}) #Requests to the combined url
        http = r.status_code #Fetches the http response code
        if http == 200: #if its 200 the url points to valid resource i.e. admin panel
                print(link)
        
paths = []
with open(args.paths, "r") as f:
    paths = f.readlines()

if args.threads: #if the user has supplied --threads argument

    threads = []
    size = int(len(paths) / args.threads)
    current = 0

    # Start threads
    for thread in range(args.threads):
        links = paths[current:current + size]
        new = threading.Thread(target=scan, args=(links,))
        threads.append(new)
        new.start()
        current += size

    # Wait to finish
    for thread in threads:
        thread.join() #Joins both
    
else: #if --threads isn't supplied we go without threads
    scan(paths)
