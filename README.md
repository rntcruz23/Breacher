# Breacher
A faster script to find admin login pages.

#### Features
- [x] Multi-threading on demand
- [x] Big path list (482 paths)
- [x] Supports php, asp and html extensions
- [x] Checks for robots.txt
- [x] Support for custom paths

### Usages
- Check paths without threads
```
./breacher.py -u example.com
```
- Adding a custom path. For example if you want all paths to start with /data (example.com/data/...) you can do this:
```
./breacher.py -u example.com --path /data
```
- Fast check paths with concurrency, 10 threads
```
./breacher.py -u example.com --path /data -c 10
```