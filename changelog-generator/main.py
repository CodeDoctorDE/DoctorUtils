import requests
import json
import argparse
import sys

#repo = os.environ['CHANGELOG_REPO']
#owner = os.environ['CHANGELOG_OWNER']

def main(argv):
    parser = argparse.ArgumentParser(description="Generate a changelog based on commits, release tags...")
    parser.add_argument("owner", type=str, help="The owner of the repository")
    parser.add_argument("repo", type=str, help="The repository name")
    parser.add_argument("--issue", "-i", action='store_true', default=False, help="Create changelog from issues")
    parser.add_argument("--pullrequest", "-pr", action='store_true', default=False, help="Create changelog from pull requests")
    parser.add_argument("--releases", "-r", action='store_true', default=False, help="Create changelog from releases")
    parser.add_argument("--headings", "-headings", metavar="false", type=bool, default=False, help="Create headings for the input types")
    parser.add_argument("--output", "-o", metavar="file", default=False, help="Change the output file. Default is 'CHANGELOG.md'")
    args = parser.parse_args()
    #answer = args.x**args.y

    #if args.owner:
    #    print(answer)
    #elif args.repo:
    #    print("{} to the power {} equals {}".format(args.x, args.y, answer))
    #else:
    #    print("{}^{} == {}".format(args.x, args.y, answer))

if __name__ == "__main__":
   main(sys.argv)
