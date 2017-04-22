pysvg-py3
=========

pysvg-py3 is a Python 3 portage of popular library [pysvg](http://codeboje.de/pysvg/). **I am not the original author
of the library**.

The original code has been duplicated, then lib2to3 has been used with default parameters to update the code
for Python 3. No additional steps have been applied. See commits history for more info.

The resulting library is available on Pypi
> Note: the root module has name 'pysvg' to silently replace the original version on Python 3 environments. For that
reason, you should remove the original package before installing this one.

    pip uninstall pysvg
    pip install pysvg-py3
