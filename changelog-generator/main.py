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
    parser.add_argument("--releases", "-r", action='store_true',
                        default=False, help="Create changelog from releases")
    parser.add_argument("--headings", "-headings", metavar="false", type=bool,
                        default=False, help="Create headings for the input types")
    parser.add_argument("--output", "-o", metavar="file", default="CHANGELOG.md",
                        help="Change the output file. Default is 'CHANGELOG.md'")

    args = parser.parse_args()

    milestones = requests.get(
        f"https://api.github.com/repos/{args.owner}/{args.repo}/milestones").json()
    print(milestones)
    f = open(args.output, "a")
    f.write("# Changelog\n")
    milestones.reverse()
    for milestone in milestones:
        create_milestone(f, milestone)
        if(args.issue):
            create_issues(f, milestone, args.owner, args.repo)

    f.close()
    #answer = args.x**args.y

    # if args.owner:
    #    print(answer)
    # elif args.repo:
    #    print("{} to the power {} equals {}".format(args.x, args.y, answer))
    # else:
    #    print("{}^{} == {}".format(args.x, args.y, answer))


def create_milestone(file, milestone):
    file.write(f"\n## [{milestone['title']}]({milestone['html_url']})\n")
    file.write(f"{milestone['description']}\n")


def create_issues(file, milestone, owner, repo):
    issues = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues?milestone={milestone['number']}&state=all").json()
    for issue in issues:
        file.write(f"[{issue['title']}]({issue['html_url']})\n")


if __name__ == "__main__":
    main(sys.argv)
