# Terminal tasks

In the *Explorer view*: Right click on the `README.md` file > Open in Integrated Terminal.

Use the Terminal to complete the following tasks.

## Task 1

Use the `pwd` command to check what is the current working directory
- Try to understand the path that is printed by the command
- Would you have been able to know the current working directory without using the `pwd` command?

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ pwd
/workspaces/WORCK-DH-Winter-School-2024
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $
```

The path printed by the `pwd` command shows you an absolute path to the directory from where your terminal session is operating from. You can read it the following way:
- `/` -> The root of the file system
- `/workspaces` -> A directory called "workspaces" within the root of the file system
- `/workspaces/WORCK-DH-Winter-School-2024` -> A directory within the "workspaces" directory explained above.

As the command prompt already prints out the current working directory next to the `➜` sign, one could have been knowing it without using the `pwd` command.

## Task 2

Use the `ls` command to get an overview what files and directories are in the current working directory

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls
README.md  panel-1  panel-2  panel-3  panel-4  panel-5  panel-6  panel-7  panel-8
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $
```

## Task 3

Use the `ls` command to explore the contents of a directory within the current working directory

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls panel-1
README.md  '[tasks]_terminal.md'   example.ipynb   example.py   hero.png   script.py
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $
```

## Task 4

Use the `cd` command to navigate into one of the directories within the current working directory

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cd panel-1
@John ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-1 (main) $ 
```

## Task 5

Use your search engine of choice and lern what is the difference between a **relative** and **absolute path** in the linux terminal

### Solution

- A **relative path** is a path that is starting from, or relative to, your current working directory.
- An **absolute path** is a path that is starting from the root of the file systemy.

If you type a path **beginning with a `/`** the Terminal will interprete it as an **absolute path**. In **all other cases** it will assume you are defining a **relative path**.

## Task 6

Use the `cd` command with an **absolute path** to navigate to the `panel-4` directory of the workspace.

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-1 (main) $ cd /workspaces/WORCK-DH-Winter-School-2024/panel-4
@John ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-4 (main) $ 
```

## Task 7

Use the command `cd ..` and try to figure out what the special meaning of `..` is in the context of a path.<br>
*Hint: Compare the current working directory before using the command with the one after using it*

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-4 (main) $ cd ..
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

The command prompt shows you the current working directory. Comparing both prompts, before and after executing `cd ..`, you will see that the current working directory changed to the directory containing the current working directory from before. It is the "go up a level" function you may already know from your graphical file explorer.

## Task 8

Use the `--help` option for the `ls` command and find out how to include files and directories beginning with a `.` sign in the output.
- What does the `.` prefix for file and directory names mean?

### Solution

```bash
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
# Output cut for clarity
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls -a
.  ..  .devcontainer  .git  .gitignore  .vscode  README.md  panel-1  panel-2  panel-3  panel-4  panel-5  panel-6  panel-7  panel-8
@John ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

The `.` prefix for file and directory names indicate that this file should be hidden. It is important to note, that this is note for security reasons it is just for convinience. As you can see in the output, their are a lot of directories starting with a `.` in our workspace. These contain configuration files, e.g. for the GitHub Codespace environment. These configuration files are not important to be seen at all time, they would potentially obstruct the view to important files which we want to pay attention to.

## Task 9

Use the `ls` command to list the contents of the hidden `.vscode` directory

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ ls .vscode
settings.json
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

## Task 10

Use the the `mkdir` command to create a new directory.

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ mkdir new_directory
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

## Task 11

Copy the `README.md` file into your new directory using `cp`

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cp README.md new_directory/README.md
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

## Task 12

Use the `--help` option or your search engine of choice to find out what the `cat` command is doing. Use it on the README.md you just copied.

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cat new_directory/README.md
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

The `cat` command will concatenate the contents of the files provided as argument and print it to the standard output. In our case it will just print the contents of the `new_directory/README.md` file to the Terminal.

## Task 13

Use the `rm` command to delete the directory you created before.
- This may fail, check the help and try to find an option to achieve the task.

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ rm -r new_directory
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ 
```

The `rm` command can, by default, just delete files. If you want to delete directories and the files within you can the `-r` option: remove directories and their contents recursively.

## Task 14

Navigate into the `panel-1` directory.

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024 (main) $ cd panel-1
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-1 (main) $ 
```

## Task 15

Use the `python3` command with `script.py` as an argument.

### Solution

```bash
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-1 (main) $ python3 script.py
Hello from python_script.py. I am here to tell you that you completed all terminal tasks. Congratulations!
@Pevtrick ➜ /workspaces/WORCK-DH-Winter-School-2024/panel-1 (main) $ 
```
