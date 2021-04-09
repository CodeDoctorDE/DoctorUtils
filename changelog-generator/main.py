import requests
import json
import argparse
import sys
import os


def main(argv):
    parser = argparse.ArgumentParser(
        description="Generate a changelog based on commits, release tags...")
    parser.add_argument("owner", type=str, help="The owner of the repository")
    parser.add_argument("repo", type=str, help="The repository name")
    parser.add_argument("--issue", "-i", action='store_true',
                        default=False, help="Create changelog from issues")
    parser.add_argument("--pullrequest", "-pr", action='store_true',
                        default=False, help="Create changelog from pull requests")
    parser.add_argument("--theme", "-t", metavar="folder", type=str,
                        default="classic", help="The theme which will be used")
    parser.add_argument("--output", "-o", metavar="file", default="CHANGELOG.md",
                        help="Change the output file. Default is 'CHANGELOG.md'")
    parser.add_argument("--user", "-u", metavar="client-id", default=None, type=str,
                        help="Add the client-id to the request to increase the rate limit'")
    parser.add_argument("--password", "-p", metavar="client-secret", default=None, type=str,
                        help="The secret to the client-id'")

    args = parser.parse_args()
    gh_session = requests.Session()
    if args.user is not None and args.password is not None:
        gh_session.auth = (args.user, args.password)
    f = open(args.output, "a")

    f.write(create_milestones(args, gh_session))

    f.close()

def create_milestones(args, gh_session):
    milestones = gh_session.get(
        f"https://api.github.com/repos/{args.owner}/{args.repo}/milestones").json()
    milestones.reverse()
    msOutput = ""
    for milestone in milestones:
        msOutput += create_milestone(milestone, args, gh_session)
    file = open(f"{args.theme}/milestones.md", "r")
    output = file.read().format(milestones=msOutput)
    file.close()
    return output

def create_milestone(milestone, args, gh_session):
    issues = create_issues(milestone, args, gh_session)
    pulls = create_pulls(milestone, args, gh_session)
    file = open(f"{args.theme}/milestone.md", "r")
    output = file.read().format(title=milestone['title'] or "", description=milestone['description'] or "", issues=issues, pulls=pulls)
    file.close()
    return output

def create_issues(milestone, args, gh_session):
    issues = gh_session.get(
        f"https://api.github.com/repos/{args.owner}/{args.repo}/issues?milestone={milestone['number']}&state=all").json()
    iOutput = ""
    for issue in issues:
        iOutput += create_issue(issue, args)
    file = open(f"{args.theme}/issues.md")
    output = file.read().format(issues=iOutput)
    file.close()
    return output

def create_issue(issue, args):
    file = open(f"{args.theme}/issue.md")
    output = file.read().format(title=issue["title"], link=issue["html_url"])
    file.close()
    return output

def create_pulls(milestone, args, gh_session):
    pulls = gh_session.get(
        f"https://api.github.com/repos/{args.owner}/{args.repo}/pulls?milestone={milestone['number']}&state=all").json()
    prOutput = ""
    for pull in pulls:
        prOutput += create_pull(pull, args)
    file = open(f"{args.theme}/pull-requests.md")
    output = file.read().format(pulls=prOutput)
    file.close()
    return output

def create_pull(pull, args):
    file = open(f"{args.theme}/pull-request.md")
    output = file.read().format(title=pull["title"]or "", link=pull["html_url"])
    file.close()
    return output

if __name__ == "__main__":
    main(sys.argv)
