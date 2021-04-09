# Changelog Generator

> Create changelogs automatically from milestones

## Features

* Custom themes
* Github Action support
* Lightweight

## Help

```
usage: main.py [-h] [--issue] [--pullrequest] [--theme folder] [--output file] [--user client-id] [--password client-secret] owner repo

Generate a changelog based on commits, release tags...

positional arguments:
  owner                 The owner of the repository
  repo                  The repository name

optional arguments:
  -h, --help            show this help message and exit
  --issue, -i           Create changelog from issues
  --pullrequest, -pr    Create changelog from pull requests
  --theme folder, -t folder
                        The theme which will be used
  --output file, -o file
                        Change the output file. Default is 'CHANGELOG.md'
  --user client-id, -u client-id
                        Add the client-id to the request to increase the rate limit'
  --password client-secret, -p client-secret
                        The secret to the client-id'
```
