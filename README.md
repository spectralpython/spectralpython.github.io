spectralpython.github.io
========================

This repository contains source code for the Spectral Python (SPy)
[web site](http://spectralpython.sourceforge.net).

## Build dependencies

Building the site requires the [Spectral Python](https://github.com/spectralpython/spectral)
module (and its dependencies), [Sphinx](http://sphinx-doc.org/), and git
(to retrieve submodules).

In addition to the software components listed above, building the site also
requires a copy of the [ASTER Spectral Library](http://speclib.jpl.nasa.gov/),
converted to the SPy-recognized format, located in a file named "aster_lib.db"
in either the `sphinx` subdirectory or a directory included in the
`SPECTRAL_DATA` environment variable. The data on the CD provided by JPL can
be converted to the appropriate format with the following python commands:

    >>> import spectral
    >>> db = spectral.AsterDatabase.create("aster_lib.db", "/CDROM/ASTER2.0/data")

## Building the site content

The site content is created from the top-level directory with

    make site

This will create the HTML content in the `sphinx/_build/html` subdirectory.
An internet connection is required the first time the site is built because
the git submodule in `sphinx/data` will be automatically retrieved, if it is
not present.

If the SPy module has not been modified since the last time the `site` target
was built, the site can be built faster by building the `sphinx-html` target
instead. This simply skips the step of building the `images` target, which can
be handy when debugging or testing Sphinx ReST code.

## Deploying the site

The web site is currently hosted on sourceforge.net. Eventually, the site
will be moved elsewhere and a simple build rule will be added to the Makefile.
But for now, the site content is uploaded with the following commands:

    ssh-add
    ssh -t tboggs,spectralpython@shell.sourceforge.net create

Then, in a separate shell:

    rsync -aiv --delete sphinx/_build/html/ tboggs,spectralpython@web.sourceforge.net:htdocs

Obviously, if you are not `tboggs`, replace the username above with your own.
