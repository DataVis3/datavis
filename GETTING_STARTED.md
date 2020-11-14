## Getting Started
### Setting up your Development Enviroment
To work on this project you will need four things:
* Python 2.7 or higher
* A way to run python such as Sublime, PyCharm, the command line, or eclipse
* Access to a copy of *Python Crash Course: A Hands-On Project Based Introduction to Programming (2nd ed.)* by Eric Matthes
* The matplotlib python library

Feel free to request access to our Microsoft Teams so you can communicate with the team.

#### Installing Python
Head over to the [Python website][python] and download python for whichever OS you have. 
To check what version is installed you can use
~~~
python -v
~~~
If you start having issues, especially with your path, refer to Appendix A of your book (pg. 467-470).  

#### Setting up your IDE
We suggest setting up an IDE instead of using a command line, as most people find it easier,
but if you are more comfortable with using command line feel absolutely free to!
Explore the different options and find which suits you best, just make sure you 
add any additional files populated by it to your .gitignore file.


### Accessing your book
You can purchase a copy of this book on [amazon][amazon] for just over 20 dollars, there are many other places to find it though.

### Installing Matplotlib
Depending on your OS this may be slightly different.<br>
All computers will need to run this in their terminal (You may need to make sure your running as an admin or with sudo):
~~~
python -m pip install --user matplotlib
~~~
If this throws back an error you may not have pip installed. You can check by running:
~~~
pip help
~~~
If it does you can install pip manually by downloading it from a website, navigating to the folder and running
~~~
python get-pip.py
~~~
OR by using an installer, such as choco (Windows) or brew (MacOS) to install it for you.<br>
If pip help, responds but you're still having issues try running.
~~~
pip upgrade
~~~
Make sure to run the first line after making sure pip is installed correctly.


Refer to page 306 in Chapter 15 of your book for additional help.

### Setting up a .gitignore file
We strongly suggest doing this to make sure your commits are clean and don't contain any extra files.
To set up run this in your command line:
~~~
touch .gitignore
~~~
and then open the file either in command line or with a text editor of your choice. 
If you don't see it pop up in your visual file directory, you probably have it set to hide hidden files.
To show them on Windows:
1. Click on the View tab at the top
2. There will be a checkbox next to Hidden Items
3. Toggle it to it's other setting and then reload the folder<br>

It may take a couple of seconds to take effect so you may need to refresh a few times.<br>
Once you have opened the file in the text editior of your choice, 
add any files or directories you don't want git to see like this:
~~~
# Ignored Files:
filename
directoryname/
~~~
For PyCharm some things to ignore are:
~~~
# Ignored Files:
.gitignore
.idea/
__pycache__/
~~~

Before you contribute make sure to check our our [Contributor's Guide][contributor-guide]!

[python]: https://www.python.org/
[amazon]: https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280/ref=pd_lpo_14_t_0/144-8328931-0355433?_encoding=UTF8&pd_rd_i=1593279280&pd_rd_r=5c2d68f9-f4d2-428f-bd9f-3f7f64a77d7a&pd_rd_w=zpqY6&pd_rd_wg=6rRaU&pf_rd_p=7b36d496-f366-4631-94d3-61b87b52511b&pf_rd_r=9H2Z7241V9KNR0TK8E5P&psc=1&refRID=9H2Z7241V9KNR0TK8E5P
[contributor-guide]: https://github.com/DataVis3/datavis/blob/master/CONTRIBUTER.md

