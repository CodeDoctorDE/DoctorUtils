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

## GitHub Action

An example for a workflow
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - name: Clone repository
      run: git clone https://github.com/CodeDoctorDE/DoctorUtils.git
    - run: cd DoctorUtils/changelog-generator
    - name: Run a one-line script
      run: |
        cd DoctorUtils/changelog-generator
        python main.py -o ../../CHANGELOG.md LinowodCloud dev_doctor
    - name: switching from HTTPS to SSH
      run: git remote set-url origin ${{ secrets.ssh }}
    - name: check for changes
      run: git status
    - name: stage changed files
      run: git add CHANGELOG.md
    - name: commit changed files
      run: git commit -m "Auto updating CHANGELOG.md"
    - name: fetch from main
      run: git fetch origin main
    - name: push code to main
      run: git push origin HEAD:main
```
