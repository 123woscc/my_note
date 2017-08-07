import os

posts=list()
title='#Note List'
posts.append(title)
git_url='https://github.com/123woscc/my_note/blob/master/'

for index,file in enumerate(os.listdir('.')):
    if file.endswith('.md'):
        post='{0}.  [{1}]({2}{1})'.format(index,file[:-3],git_url)
        posts.append(post)

body='\n'.join(posts)

with open('README.md','w') as f:
    f.write(body)

