import os
import sys

sys.stdout = open('SUMMARY.md', 'w')

# leetcode pages
leetcode_pages = [path for path in os.listdir('source/leetcode')]
leetcode_pages.sort(key=lambda x: int(x.split('.')[0]))
print('Leetcode Java')
print("* Leetcode练习题")
for page in leetcode_pages:
    print("  * [%s](source/leetcode/%s)" % (page[:-3], page))

# java pages
java_pages = [path for path in os.listdir('tips')]
java_pages.sort()
print('* Java类库')
for i, page in enumerate(java_pages):
    print("  * [%d. %s](tips/%s)" % (i + 1,page[:-3], page))

sys.stdout.close()

    