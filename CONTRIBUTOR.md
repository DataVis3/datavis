## Contributor's Guide

#### Setting up your local repository
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