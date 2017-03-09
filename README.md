# Codecool Management System

## Development

**Check _Contributing_ section below before you start submit new features**

#### Prerequsites

Check that you have installed following:

* Python >= 3.5
* [PIP](https://pypi.python.org/pypi)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)

_Make sure PIP and Virtualenv are installed for proper version of Python
(if you have installed more than one version of Python)._

If you never worked with Virtualenv before, go to
https://virtualenv.pypa.io/en/stable/ and read concept about it.

#### Getting started

After you clone repo to your local computer, navigate to newly created
directory and do the following steps:

1. Create Virtualenv

   ```
   $ virtualenv env
   ```

   This will create `env` directory inside project. Don't worry,
   it's ignored by GIT by default.

2. Activate Virtualenv for the project

   ```
   $ source ./env/bin/activate
   ```

   This will activate local development environment in current terminal
   session only. You have to run this command for every new terminal session.

   You should notice `(env)` text at the beginning of your command line prompt.

3. Install requirements
   ```
   (env) $ pip install -r requirements.txt
   ```

4. Run server

   ```
   (env) $ python run.py
   ```

4. Open web-browser and navigate to [http://localhost:8080](http://localhost:8080)

## Contributing

1. Fork the project & clone locally.
2. Create an _upstream_ remote and sync your local copy before you branch.
3. Branch for each separate piece of work.
4. Do the work, and write [good commit messages](https://blogs.gnome.org/danni/2011/10/25/a-guide-to-writing-git-commit-messages/).
5. Push to your _origin_ repository.
6. Create a new PR (Pull Request) in GitHub.
7. Respond to any [code review feedback](https://lornajane.net/posts/2015/code-reviews-before-you-even-run-the-code).

## Documentation

All documentation can be found in [docs](docs/README.md) directory.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) file.