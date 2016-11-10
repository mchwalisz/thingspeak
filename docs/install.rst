Installation
============

This part of the documentation covers the installation of `thingspeak package <https://pypi.python.org/pypi/thingspeak/>`_.
The first step to using any software package is getting it properly installed.


Pip Install thingspeak API
--------------------------

To install thingspeak, simply run this simple command in your terminal of choice::

    $ pip install thingspeak

If you don't have `pip <https://pip.pypa.io>`_ installed (tisk tisk!),
`this Python installation guide <http://docs.python-guide.org/en/latest/starting/installation/>`_
can guide you through the process.

Get the Source Code
-------------------

Requests is developed on GitHub, where the code is
`always available <https://github.com/mchwalisz/thingspeak>`_.

You can either clone the public repository::

    $ git clone git@github.com:mchwalisz/thingspeak.git

Or, download the `tarball <https://github.com/mchwalisz/thingspeak/tarball/master>`_::

    $ curl -OL https://github.com/mchwalisz/thingspeak/tarball/master
      # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your own Python
package, or install it into your site-packages easily::

    $ python setup.py install
