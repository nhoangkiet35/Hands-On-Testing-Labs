# Creating Virtual Environments

The module used to create and manage virtual environments is called venv. venv will install the Python version from which the command was run (as reported by the --version option). For instance, executing the command with python3.12 will install version 3.12.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

```bash
python -m venv tutorial-env
```

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is .venv. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```bash
tutorial-env\Scripts\activate
```
