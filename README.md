pysvg-py3
=========

pysvg-py3 is a Python 3 portage of popular library [pysvg](http://codeboje.de/pysvg/). **I am not the original author
of the library**.

The original code has been duplicated, then lib2to3 has been used with default parameters to update the code
for Python 3. Original code were also patched to run well on Python 3. See :
 - PR #4, related to issue #3 (thanks to @virresh)

The resulting library is available on Pypi
> Note: the root module has name 'pysvg' to silently replace the original version on Python 3 environments. For that
reason, you should remove the original package before installing this one.

    pip uninstall pysvg
    pip install pysvg-py3
