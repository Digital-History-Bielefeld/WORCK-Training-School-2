# Panel 1

## Codespaces

GitHub Codespaces eliminates the complexity of setup and configuration by providing a predefined development environment in a cloud. With just one click, you can start coding and focus on the essentials. So you can choose a repository, open a codespace and work alone or with others in a pre-organized development environment. Codespaces are a whole system, so you can use the terminal, the file explorer, the editor and much more. You can also install extensions and customize the environment to your needs. The surface of the codespace is a Visual Studio Code environment, so you can use all the features of Visual Studio Code.

#### Summarized:

- No local setup steps: Start coding immediately without wasting time on setup.
- Real-time collaboration: Work seamlessly with others no matter where they are.
- Predefined environment: Avoid conflicts and disruptions with a consistent development environment

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. It is highly customizable, allowing users to change the theme, keyboard shortcuts, preferences, and install extensions that add additional functionality. Visual Studio Code is a free and open-source software.

### What you see in Visual Studio Code

- **Activity Bar**: The Activity Bar is located on the left side of the window and gives you quick access to different views (Explorer, Search, Source Control, Run and Debug, Extensions, and Remote).
- **Side Bar**: The Side Bar contains different views like the Explorer to assist you while working on your project. The Explorer view lets you navigate and manage files and folders.
- **Editor**: The Editor is where you write your code. You can open as many editors as you like side by side vertically and horizontally.
- **Panel**: The Panel is located at the bottom of the window and gives you access to different views like Output and Terminal.
- In the codespace you can also find a Burger Menu in your Activity Bar. This menu contains all the settings and configurations you need to customize your codespace. There you can also open a new terminal, if your can't see your terminal anymore.
<br>
<br>

![Visual Studio Code Window](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)
> -- <cite>https://code.visualstudio.com/docs/getstarted/userinterface</cite>

**Note:** If you are not familiar with Visual Studio Code, you can find a detailed guide on how to use it [here](https://code.visualstudio.com/docs/getstarted/userinterface). There are some differences between the Visual Studio Code and the Visual Studio Code in the codespace, but the most important features are the same. 

## The Terminal

This unit aims to teach you the basic principles of executing a terminal application. This includes understanding the syntax (grammar and language) of the terminal, finding help and executing a terminal program.

At the end of this unit you should know what a terminal is, how to use it, how to find help and be able to execute a program with the terminal.

### Text-based terminal operation of computers

The text-based terminal operation of computers, has its roots in the early days of computing when interactive communication with a computer was primarily achieved through punched cards and printouts. A significant advancement in human-computer interaction where teletype machines.

Teletypes were electromechanical devices that combined a typewriter with a communication system, allowing users to interact with computers in a more dynamic way. The interaction took place through a text-based interface, with the teletype serving as both input and output device. Users could type commands on the keyboard, and the teletype would print the results of those commands on paper.

This text-based terminal operation became a standard mode of communication with early computers. Users interacted with the computer through a command-line interface, typing instructions and receiving text-based feedback. This method of interaction laid the foundation for the development of more sophisticated user interfaces in the future, including the graphical user interfaces (GUIs) that are prevalent in modern computing.

The transition from teletypes to video terminals and, eventually, personal computers, further refined and expanded the ways users could interact with computers. However, the text-based terminal operation remains a fundamental concept in computing history, influencing the design and usability of computer interfaces for decades.

### GUI and text based operation today

Both terminal and GUI applications serve specific purposes and cater to different user preferences and needs. They complement each other, providing various ways to interact with a computer system based on the user's comfort level and the complexity of the task at hand.

<table>
    <tr>
        <th style="width: 50%; text-align: center;">Terminal</th>
        <th style="width: 50%; text-align: center;">Graphical User Interface</th>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Input Method</b></td>
    </tr>
    <tr>
        <td>Commands and text-based input are used to perform tasks. Users type specific commands and parameters to execute actions.</td>
        <td>Users interact with visual elements such as buttons, menus, and icons using a mouse or touch interface.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Interface Complexity</b></td>
    </tr>
    <tr>
        <td>Generally, it requires memorization of commands, flags, and their syntax. Users need to know specific commands to perform tasks efficiently.</td>
        <td>Provides a more intuitive interface with visual cues, menus, and buttons. Users can often explore functionality without needing to memorize specific commands.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Resource Consumption</b></td>
    </tr>
    <tr>
        <td>Typically consumes fewer system resources as it operates in a text-based environment.</td>
        <td>Often requires more system resources due to graphical rendering and additional interface components.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Flexibility and Automation</b></td>
    </tr>
    <tr>
        <td>Offers greater flexibility and automation through scripting. Users can create complex workflows and automate tasks by combining multiple commands.</td>
        <td>May have limitations in terms of automation and scripting capabilities compared to terminal applications.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Learning Curve</b></td>
    <tr>
        <td>Can have a steeper learning curve for beginners due to reliance on memorizing commands and understanding their syntax.</td>
        <td>Generally considered more user-friendly and intuitive, reducing the initial learning curve for performing basic tasks.</td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><b>Accessibility</b></td>
    </tr>
    <tr>
        <td>Might be challenging for some users, especially those less familiar with command-line interfaces or individuals who rely heavily on visual elements.</td>
        <td>Offers a more accessible interface for a broader range of users, particularly those who prefer visual interactions.</td>
    </tr>
</table>

### Introduction to Using a Linux Terminal

The Linux terminal is a text-based interface for interacting with the operating system. Initially the terminal shows a configureable prompt, which provides information about the terminal session and waits for user input. In most cases the command prompt includes information about the currently logged in user, the name of the machine and the path/directory in which you are operating right now.

Let's take a look at the command prompt, that this GitHub Codespace is providing for us.

```bash
@John ➜ "/workspaces/WORCK-DH-Winter-School-2024" (main) $ 
```

- Next to the `@` sign you will see the currently logged in user. In this case `John`, you should see your own GitHub username here.
- On the right sight of the `➜` sign you see the current path/directory
- If the current directory is a git repository, you will see an indicator like `(main)`. It shows the active branch of the repository.
- The `$` sign is a seperator, seperating your input from the prompt.

The user input follows a simple schema:

- **Command Structure**: `<command> <options> <arguments>`
    - **Command**: The name of the program (we call it command in this context) to be executed.
    - **Options** (optional): Modify the behavior of the command. Most of the times options begin with one or two `-`.
    - **Arguments** (optional): The objects on which the command is applied.

To get first idea of it (this won't work because the firefox application is not installed in the Codespace):

```bash
# Example executing the <command> firefox
@John ➜ "/workspaces/WORCK-DH-Winter-School-2024" (main) $ firefox
```

```bash
# Example executing the <command> firefox with <option> --private-window
@John ➜ "/workspaces/WORCK-DH-Winter-School-2024" (main) $ firefox --private-window
```

```bash
# Example executing the <command> firefox with <option> --private-window and <argument> https://github.com
@John ➜ "/workspaces/WORCK-DH-Winter-School-2024" (main) $ firefox --private-window https://github.com
```

It is best to lern this by example and trying things out. Don't worry, you can't really break something in this Codespace. If something unexpected happens, you can restart your Codespace.<br>
*Pro tip: Use the Tab key to automatically complete commands, file names, etc.*

#### Navigating the File System

**pwd**: Display the current working directory.

```bash
# schema > command: pwd
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ pwd
/workspaces/WORCK-DH-Winter-School-2024
```

**ls**: List contents of the current working directory.

```bash
# schema > command: ls
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls
README.md  panel-1  panel-2  panel-3  panel-4  panel-5  panel-6  panel-7  panel-8

# schema > command: ls | option: -l
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls -l
-rw-rw-rw-  1 codespace root 3489 Feb  9 10:09 README.md
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-2
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-3
drwxrwxrwx+ 6 codespace root 4096 Feb  9 10:09 panel-4
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-5
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-6
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-7
drwxrwxrwx+ 2 codespace root 4096 Feb  9 10:09 panel-8

# schema > command: ls | option: --help
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls --help
...

# schema > command: ls | argument: panel-2
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls panel-2
EAP.txt  python_basics.ipynb README.md

# schema > command: ls | option: -l | argument: panel-2
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls -l panel-2
-rw-rw-rw- 1 codespace root  5565 Feb  9 10:09 EAP.txt
-rw-rw-rw- 1 codespace root  8443 Feb  9 10:09 README.md
-rw-rw-rw- 1 codespace root 37327 Feb  9 10:09 python_basics.ipynb
```

**cd**: Change the current working directory.

```bash
# schema > command: cd | argument: panel-2
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cd panel-2
```

As you can see, not every command will print an output for you. In this case their is one rule "no news are good news".


#### File Manipulation

**mkdir**: Create a new directory.

```bash
# schema > command: mkdir | arguments: new_dir
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ mkdir new_dir
```

**cp**: Copy files.

```bash
# schema > command: cp | arguments: README.md, README_COPY.md
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cp README.md README_COPY.md
```

**mv**: Move or rename files.

```bash
# schema > command: mv | arguments: README_COPY.md, new_dir
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ mv README_COPY.md new_dir
```

**rm**: Delete files.

```bash
# schema > command: cp | arguments: new_dir/README_COPY.md
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ rm new_dir/README_COPY.md
```


#### Help and Documentation

**man**: Manual pages for commands.

```bash
# schema > command: man | arguments: ls
man ls
```

**--help**: Option for many commands to display help.

```bash
# schema > command: man | options: --help
ls --help
```


#### Lern more

> **LinuxFoundationX: Introduction to Linux**: Never learned Linux? Want a refresh? Develop a good working knowledge of Linux using both the graphical interface and > command line across the major Linux distribution families.
> 
> -- <cite>edX: https://www.edx.org/learn/linux/the-linux-foundation-introduction-to-linux</cite>


## Enter the world of Python

The last lecture taught you how to use the terminal. Your last task was to execute a Python program.

```bash
python3 script.py
```

You may have already wondered why you need to use the `python3` program to execute a Python program. Why can't you just write `script.py` in order to execute it? Unlike other programming languages, Python is an interpretet language, this means you need to use an interpreter program which then translates your code to a machine understandable format on execution time (just like a real world live translator does for natural language). Other programming languages like C or C++ for example are compiled languages, they are translated in a format that can be executed by your computer without the help of any other programs before execution. Both of these methods have their advantages, you don't need to know more about this topic, it's just so you know that a Python program needs a Python interpreter to be executed (command for Python Interpreter: `python3`). 

### Python programming

Before we can learn to write our own programs, we should define what a program is.

> A computer program is a sequence or set of instructions in a programming language for a computer to execute.
>
> -- <cite>Wikipedia: https://en.wikipedia.org/wiki/Computer_program</cite>

This does not sound to complicated right? Let's take a look into a simple Python program.

```python
print("Hello, i am a Python program that adds to numbers.")

number_1 = 10
print("The first number is:")
print(number_1)

number_2 = 20
print("The second number is:")
print(number_2)

sum = number_1 + number_2
print("The sum is:")
print(sum)
```

The good thing about the Python programming language is that it is easy to read. Even someone without any clue about Programming can at least guess what is happening in this short example. This makes it a perfect choice for beginners, the Python community is also very welcoming and has built a lot of tools that will make it easier to lern their favourite language.

### Jupyter

One of these tools is the [Jupyter Notebook](https://jupyter.org/). Jupyter Notebooks are interactive documents that allow you to create and share live code, equations, visualizations, and narrative text. They are widely used in data science, machine learning, scientific research, and education due to their versatility and ease of use. A Jupyter Notebook consists of cells, which can contain code, markdown, or rich media. The combination of executable code and explanatory text makes it an ideal tool for creating reproducible and interactive lerning resources. You can see a notebook implementing the same example program from above in `example.ipynb`.

## Motivational notes

Lerning Python is a beginner friendly and fun adventure into the world of programming. It is a rewarding experience with a lot of practical use cases. Putting your ideas into practice and sharing the results with the world, solving not just yours but potentially also a lot of problems others have is a huge motivation. It is one more tool to bring your creative ideas to live.

### The most important part: Expectation management

Sounds great right... Well, there is a "but" and here it comes: *But* you have to be prepared for a lot of head scratching. Programming follows strict rules, sometimes these are well comprehenseable but most of the time you will need time to understand them... There will also be occasions where you will stare at your screen for hours without even touching the root of the problem with your code, just to notice that in the end you just forgot to set a `.` or `,` at the right place. You have to practice a lot and be prepared to not understand everything on the first attempt.

You will lern the basic principles of programming in Python, maybe you will even be able to write small scripts. You will lern how to read existing code and how to use it. This sounds good to you? I think so, too! What you will lern in this Winter School is just the beginning. You can revisit this repository at any time and explore the topics that we won't be able to discuss this week. As a motivational challenge we prepared four step by step projects that you will be able to challenge with the knowledge gained. You will also find a lot more informations and exercises to lern Python in more depth.
