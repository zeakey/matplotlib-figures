rm -rf .git
git init
git add -A
git commit -m 'release'
git remote add origin git@github.com:zeakey/matplotlib-figures
git push -u origin master -f
