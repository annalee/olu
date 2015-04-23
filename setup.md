
# The Terminal

We're going to be doing a lot of work in the terminal--using what's called "the command line." All the command line is is a way of talking to your computer without using a graphical user interface. We input typed commands instead of clicking on menus.

The terminal can be a little intimidating when you're first getting started, but as you work with it, it gets easier.

### Opening the Terminal

To open the terminal, go to spotlight and search for `terminal`. It should come right up.

> TIP: You'll notice that a lot of the devs keep the terminal on their dock. We'll be using it a lot.

When the terminal opens, you should see something like this:

    computername:~ yourusername$

That's called the "command prompt." It's the computer telling you it's ready to receive a new command.

### Terminal Commands

Let's try out some commands. I'm going to start all these with `$` but you don't need to type that part--that's just to indicate we're at the command prompt. When you google for advice on how to do something on the terminal, you'll usually see responses that start each command with `$`.

    $ pwd

"pwd" means "print working directory." It prints the directory you're in to the screen.

You should be in your home directory. It should print something like `/Users/yourusername`.

That starting `/` indicates that the path is *absolute*. When parsing an absolute path, your computer starts from "root," which is the very top of your file tree, and navigates down the file tree to the file you specify--in this case, it goes to `Users`, which is in root, then goes to `yourusername`, which is in `Users`. We'll learn more about file paths later.

Let's see what's in our directory:

    $ ls
    
"ls" stands for "list." It lists all the files in the current directory.

Want to change directories? We can do that, too! 

    $ cd Documents
    
"cd" means "change directories." We've given it a *relative* path to the `Documents` directory, telling the computer where it is relative to your current directory. The *absolute* path is `/Users/yourusername/Documents`. You can cd using either relative or absolute paths.

Let's go back to our home directory:

    $ cd ../
    
`../` just means "go up one level." You can go up two levels by going `../../`, and so on. `../` is a relative path.

# Install ALL THE THINGS:

We're going to need some software to start coding in python, so step one is installing stuff.

###Homebrew

Homebrew is a package manager--basically an app store for the terminal. It helps you download and update software you'll need to work with python and django. We're installing it first, then we'll use it to install some other stuff.

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

###Python 3

`brew install python3`

###Virtuanenv and Virtualenv Wrapper

Virtualenv is a way of managing 'dependencies,' or programs we need to make our program run. Dependencies are usually packages we download through the package manager. Packages usually come in multiple versions, and they may have their own dependencies, which also come in multiple versions. Sometimes, you'll be working on different projects that need different versions of the same package. In order to make sure that each project has access to the dependencies it needs without affecting any other project, we isolate them from each other.

You can think of virtual environments like fish tanks. They allow you to keep saltwater and freshwater fish in different tanks, so they don't have to share the same water. (Your code projects are fish).

    $ pip install virtualenv
    
Virtualenv is really handy, but it's not even a little bit user-friendly. It's so unfriendly, actually, that there's a whole separate tool to give us a set of convenient commands to run virtual environments. It's called virtualenvwrapper. Let's install that:

    $ pip install virtualenvwrapper
    
Now we need to do a little bit of setup for virtualenvwrapper to give us access to its commands.

To do this, we need to access  file called `.bash_profile`. The challenge is that bash_profile is a *hidden file* (which is why it starts with `.`), so before we can edit it, we need to be able to view it. To do that, we need to tell our system to show us hidden files. Here's the command for that:

    $ defaults write com.apple.finder AppleShowAllFiles YES
    
Now we need to restart Finder:

    $ killall Finder
    
Now if you open finder and go to your home directory, you'll see a lot of grey files with names that start with `.`. Find `.bash_profile` and open it in a text editor.

> TIP: text editors are not the same as word processors. Word processors, like MS Word or LibreOffice, use a markup language to make documents pretty for printing and viewing. Computers can't read code that includes this kind of formatting. We need to use a program that's specifically for writing code.
