import re
import sys

def validate_title(title):
    print("The title is:", title)
    prefix_pattern = r'^(build|chore|ci|docs|feat|fix|perf|refactor|style|test|sample)[:\s].+'
    max_length = 50
    
    match = re.match(prefix_pattern, title, re.IGNORECASE)
    print("Match:", match)
    
    if not match:
        print("PR title must start with one of the following prefixes: build, chore, ci, docs, feat, fix, perf, refactor, style, test, sample", file=sys.stderr)
        sys.exit(1)
    
    title_content = title.split(':', 1)[-1].strip()
    print("Title Content:", title_content)
    
    if len(title_content) > max_length:
        print(f"PR title content must not exceed {max_length} characters", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    title = sys.argv[1]
    validate_title(title)
