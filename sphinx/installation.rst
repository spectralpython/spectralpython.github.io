.. _installation:

********************************
Installing SPy
********************************

.. toctree::
    :maxdepth: 2
    
SPy Dependencies
================

SPy requires Python and depends on several other freely available Python
modules. Prior to installing SPy, you should make sure its dependencies are met.
While you can use SPy to process hyperspectral data with just Python and NumPy,
there are several other modules you will need if you want to use any of SPy's
graphical capabilities.

.. list-table:: SPy Dependencies
   :header-rows: 1
   :widths: 20, 25
   :class: center

   * - Dependency
     - Requirement
   * - `Python 2.6+ <http://www.python.org>`_
     - Required (Note that SPy does not work with Python 3.x)
   * - `NumPy <http://numpy.scipy.org/>`_
     - Required
   * - `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/>`_
     - Required if displaying or saving images
   * - `wxPython <http://www.wxpython.org/>`_
     - Required if displaying images
   * - `matplotlib <http://matplotlib.sourceforge.net/>`_
     - Required if plotting spectra interactively
   * - `IPython <http://ipython.org/>`_
     - Required for interactive, non-blocking GUI windows
   * - `PyOpenGL <http://pyopengl.sourceforge.net/>`_
     - Required if calling
       :func:`~spectral.view_cube` or
       :func:`~spectral.view_nd`

As of SPy version 0.10, IPython is used to provide interactive GUI windows.
To use SPy with IPython, you will need to start IPython in "pylab"
(see :ref:`starting_ipython`)

Installing from a distribution package
======================================

SPy is distributed as a Python source distribution, which can be downloaded from
the `SPy Download Page <https://sourceforge.net/projects/spectralpython/files>`_
on `Sourceforge.net <http://sourceforge.net>`_.  Both ``.zip`` and ``.tar.gz``
formats are available.  The source distribution will unpack to a directory with
a name like ``spectral-x.y``, where ``x.y`` is the SPy version number.  To
install SPy, open a console in the unpacked directory and type the following:

.. code::

    python setup.py install

Note that if you are on a unix-based system, you will either need to be logged
in as root or preface the above command with "sudo" (unless you use the -d
option to install it to a local directory).

Installing with pip or Distribute
=================================

If you have `Distribute <http://pypi.python.org/pypi/distribute/>`_ (or the
deprecated Setuptools) or `pip <http://pypi.python.org/pypi/pip>`_ installed on
your system, there is no need to download the latest SPy version explicitly.
If you have Distribute installed, simply type

.. code::

    easy_install spectral

or using pip, type

.. code::

    pip install spectral

Note that your pip binary may be named differently (e.g., "pip-python"). And
again, you may need to be logged in as root or use "sudo" if you are on a
unix-based system.

Installing from the Git source code repository
==============================================

The latest version of the SPy source code resides in the Sourceforge Git
repository.  While the latest source code may be less stable than the most
recent release, it often has newer features and bug fixes.  To download the
latest version of SPy from the Git repository, ``cd`` to the directory
where you would like to check out the source code and type the following::

    git clone git://git.code.sf.net/p/spectralpython/repo code

.. note::

    SPy migrated from Subversion to Git for source code management as of SPy
    version 0.9.  If you have been using subversion, it is recommended you
    delete the Subversion copy and clone the SPy Git repository because future
    code changes will only be updated in the Git repository.

Configuring SPy
===============

Because hyperspectral data files can be quite large, you might store all your
HSI data in one or several specific directories.  To avoid having to type
absolute path names whenever you attempt to open an HSI file in SPy, you can
define a ``SPECTRAL_DATA`` environment variable, which SPy will use to find
image files (if they are not found in the current directory).  ``SPECTRAL_DATA``
should be a colon-delimited list of directory paths.

.. seealso::

    :class:`~spectral.spectral.SpySettings`
