
# Environment Setup and Customization

In this class you need python 3.6 or 3.6, preferably from anaconda
version >= 4.5. Anaconda is a package manager that comes python
libraries useful for data science. You will also need git.

There are two options for development in this class: local and
remote. Developing locally, on your personal computer, is preferred,
as it allows you to start customizing your work environment; learning
such customization allows you to be much more productive in your
work. We also have servers you can use through a web-browser, you can
use as well. There are advantages and disadvantages to using the
servers; we encourage you to use both at some point in the quarter.

## Working Remotely (DataHub)

There are servers available to use at
[datahub.ucsd.edu](datahub.ucsd.edu). These are a lot like the
jupyterhub servers that you used in DSC 10, however they are
customized for this course. After logging in with your ucsd account,
you will be taken the familiar juptyer landing page. The server you
are logged into has ~4GB of RAM available, and is running anaconda
with all the necessary packages (as well as R and Julia installs).

### JuptyerLab

The remote servers have a development environment installed on them,
however, it's non-intuitive how to access it. Once on the landing
page, the url should read something like:
```
https://datahub.ucsd.edu/user/<user>/tree
```
You can access the IDE (integrate development environment) by changing
`tree` to `lab`. This brings up jupyterlab. The url should look
something like this:
```
https://datahub.ucsd.edu/user/afraenkel/lab
```

For more information on this IDE, you can see read about it
[here](https://jupyterlab.readthedocs.io/en/stable/). From within
jupyterlab, you can:
* use a python console
* run jupyter notebooks
* use a terminal (e.g. to pull git repos)
* develop python code in `.py` files.


## Local Development

Getting a development environment on your own computer is a valuable
experience that will pay dividends; work in data science first
requires getting the neccesary tools working! 

1. Download [Anaconda](https://www.anaconda.com/download/) and follow
   the instructions for installing it. You should install the standard
   anaconda (not miniconda) with python 3.6 or 3.7.
2. Follow the tutorials (link on the class website) for installing and
   using git. If you are running Windows, you should download 'gitbash'.
   
More to come...

### Choosing a text editor or IDE (Integrated Development Environment)

* The [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) text editor: see above. A nice combination with notebooks.
* [nano](https://www.nano-editor.org): available on most unix commandlines (e.g. DataHub Terminal).
* [vi](https://en.wikipedia.org/wiki/Vi): lightweight, productive text-editor available on most
  command-lines, if you can ever learn how to use it. Beware opening
  vi, as you may never figure out how to quit (literally).
* [emacs](https://www.gnu.org/s/emacs/): A text editor for those who prefer a life of endless
  toil. Endlessly customizable, it promises everything, but you're
  never good enough to deliver. The preferred text editor of the prof.
* [sublime](https://www.sublimetext.com/): Basic, servicable python
  IDE; can only work locally.
* [atom](https://atom.io/): GitHub's editor. Pretty nice fully
  featured IDE. Can only work locally.
* [PyCharm (IntelliJ)](https://www.jetbrains.com/pycharm/): Those who
  feel at home coding Java. Can only work locally.

## Customizing your Environment

To come...


