########################
python-packaging-example
########################

Purpose
-------
This repository is a bare-bones example of how to package a Python script as a
wheel, with the intent of being able to pip install and run it, as if the
script was executable and had the ``#!/usr/bin/env python3`` prefix. This is
mostly for my own education so I don't forget, but it is my hope it can also be
of use to you.

Why Not Just Do That?
---------------------
While doing that is far simpler in the short term, it requires the end user to
download the file from Github/source control location to somewhere their system
PATH references. Furthermore, they would have to follow this process every time
they want the latest changes. Leveraging Python's packaging system handles all
of those details in a consistent, cross-platform way.

What's Needed?
--------------
Surprisingly, not much. From the sample repo here, you can see that only a
``setup.py`` file to define key metadata (including what name you want to give
the final executable via ``console_scripts``), a package directory (as
identified by the inclusion of an ``__init__.py`` file), and the script itself.

How Does This Work?
-------------------
The easiest way is to create and activate a virtualenv/pyvenv, ensure the
latest versions of **pip**, **twine**, and **wheel** are installed.

Building
--------
Use ``python setup.py bdist_wheel`` to create a "pure python wheel" that is
not compatible across Python 2 and 3. If your script is version-agnostic, you
can create a "universal wheel" by running this instead:
``python setup.py bdist_wheel universal``. It's important to note that in both
of these cases, they will only work if they don't contain compiled extensions.

Yes, you want to use **wheels** as they include dependencies as well. Trust that
your end users will thank you when, after installing your script, they will not
receive a weird stack trace because they don't have one of your dependencies
already installed.

Installing
----------
For local development, you can simply run ``pip install -e .`` while in the
top level of the project where setup.py is (and an active virtualenv/pyvenv).
This allows you to see how the end user will view the package installation
after pip installing it. Which brings us to...

Distributing
------------
Did you know that `PyPI has a test site <https://test.pypi.org>`_? After the
wheel has built, use twine to upload the project using the following:
``twine upload --repository-url https://test.pypi.org/legacy/ dist/*``. Clean
out the ``dist/`` folder before uploading to ensure that old versions don't
pollute your uploads or otherwise cause weird problems.

Installing: Part Deux
---------------------
Uploaded wheels can be installed in the usual manner, but with the test site:
``pip install <package> -i https://test.pypi.org/simple/``.

Executing
---------
Whatever name you specified in the following code block in ``setup.py`` (as
illustrated by the name 'jarvis'):

::

    entry_points = {
        "console_scripts": ['jarvis = printer.printer:main']
        },

will be the name of the command the user must run to use your script. Using
the same example, this is effectively the same as if your script was called
``jarvis``, was ``chmod +x jarvis``, and began with ``#!/usr/bin/env python3``.