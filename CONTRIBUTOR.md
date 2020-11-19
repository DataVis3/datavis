## Contributor's Guide

#### Setting up your local repository
To set up a local repository push the button labeled Fork that's in the top right of the repository you want to work on.
This will create 

#### Guide to a Good Commit
To make a commit you can use the command
```
git commit -m "Your message goes here"
```
You can also just use plain git commit,
but that will open a in-line text editor.
Often just easier to make your commits in one line.

To make a good commit, make commits often and keep the titles simple.
Rule of thumb is to make it after any step is done, such as one function.
Keep them concise.
You want to be able to tell at a glance what the commit did.
In general, it's recommended that commit messages start with a verb to show what is happening.
If extra information is necessary make sure it's on it's own line below the initial commit message.
In this case, the easiest way to do this is to **use the headers** provided in the book.

#### Guide to a Good Pull Request
After you have pushed all your commits up to the branch you have been working on you can submit a pull request.
The easiest way to do this is if you have pushed up commits recently 
git will add a notification above the repository prompting you to create a pull request.
All you need to do then is click the green button and fix the title and description.
Before you do this though, it's good to check if there will be any merge conflicts,
which occur when someone has changed one of the files you were working on in the branch you are trying to merge into
(typically master).
If you create a pull request without checking though or
if an update is made to master in the time between when you submit your pull request and it gets accepted
git will inform you if a conflict will occur.
To check for conflicts run
```
git pull upstream master
```
while on the branch you want to merge in.
The upstream and master may be different depending on where you are trying to merge to.
If a conflict occurs it will show you where the issue happened and you will need to open up the file and fix any conflicts.
When you open it up you will see some strange lines around the code,
one will show the changes that are local to your computer,
the other will show the changes that exist in the upstream.
To fix it, remove the excess lines from the merge and either add in the additional lines that each side added
or choose one to keep.
After you have done this, commit the changes and the problem will be solved.
Once everything is up to date, run one final *git status* to check for uncommited changes and resolve any of those.
Now you're ready to create your pull request.

A good pull request has a clear and concise title and a description that details what the pull request does.
Some people will also link the issue being solved in the title.
An example of a good title is
``` 
Creates Scatter Plots using MatPlotLib
```
For the description, give a brief (apx. 1-5 sentences) description of what your pull request does.
An example of a good description is
```
Fixes issue #4, which uses matplotlib to create several scatter plots.
```
It's generally good practice to get someone else to check if your work is working as intended before merging in the request.
To add a reviewer, click on the box on the right labeled Reviewers.
It should be right next to the description box.
Then select someone to review it and they will be notified to look it over before merging it in.

One last thing,
**please do not directly push up to master, we want to keep it clean and working.**
Remember to request a pull request to make changes to master.

#### Keeping a Clean Commit History
We won't be worrying too much about this on this project,
but many professional projects prefer a clean and neat git log for easy searching.
A clean commit history makes it easier to find when things were working and
makes it easier to rollback any issues.
The first step to having a clean commit history is to have good commits and pull requests.
Sometimes though you make a mistake in a commit, like a typo.
The best way to deal with this is the *rebase* command.
It can get complicated though so for now I'll just link [this website][rebase] for if you are curious.

[rebase]: https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase#:~:text=Rebase%20is%20one%20of%20two,has%20powerful%20history%20rewriting%20features.