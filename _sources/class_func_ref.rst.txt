.. _class-func-ref:

.. toctree::
    :maxdepth: 2

============================
Class/Function Documentation
============================

File I/O
========

open_image
----------

.. autofunction:: spectral.spectral.open_image

ImageArray
----------

.. autoclass:: spectral.image.ImageArray

SpyFile
-------

.. autoclass:: spectral.SpyFile
   :members: __str__, __getitem__, load

SpyFile Subclasses
~~~~~~~~~~~~~~~~~~

SpyFile is an abstract base class.  Subclasses of :class:`~spectral.io.spyfile.SpyFile`
(:class:`~spectral.io.bipfile.BipFile`, :class:`~spectral.io.bipfile.BilFile`,
:class:`~spectral.io.bsqfile.BsqFile`) all implement a common set of additional
methods. :class:`~spectral.io.bipfile.BipFile` is shown here but the other two are similar.

.. autoclass:: spectral.io.bipfile.BipFile
   :members: open_memmap, read_band, read_bands, read_pixel, read_subregion, read_subimage
	    


SubImage
--------

.. autoclass:: spectral.io.spyfile.SubImage
   :members: read_band, read_bands, read_pixel, read_subregion, read_subimage

File Formats
------------

AVIRIS
~~~~~~

.. automodule:: spectral.io.aviris
   :members: open, read_aviris_bands

ENVI
~~~~

.. automodule:: spectral.io.envi
   :members: open, SpectralLibrary

envi.create_image
-----------------

.. autofunction:: spectral.io.envi.create_image

envi.save_classification
------------------------

.. autofunction:: spectral.io.envi.save_classification

envi.save_image
---------------

.. autofunction:: spectral.io.envi.save_image

ERDAS/Lan
~~~~~~~~~

erdas.open
----------

.. automodule:: spectral.io.erdas
   :members: open

Graphics
========

ColorScale
----------

.. autoclass:: spectral.ColorScale
   :members: __init__, __call__, set_background_color, set_range

get_rgb
-------

.. autofunction:: spectral.graphics.graphics.get_rgb

ImageView
---------

.. autoclass:: spectral.graphics.spypylab.ImageView
   :members: __init__, set_data, set_classes, set_source, show, label_region, refresh, set_display_mode, class_alpha, interpolation, open_zoom, pan_to, format_coord, set_rgb_options

imshow
------

.. autofunction:: spectral.graphics.spypylab.imshow

save_rgb
--------

.. autofunction:: spectral.save_rgb

view
----

.. autofunction:: spectral.view

view_cube
---------

.. autofunction:: spectral.view_cube

view_indexed
------------

.. autofunction:: spectral.view_indexed

view_nd
-------

.. autofunction:: spectral.view_nd


Training Classes
================

create_training_classes
-----------------------

.. autofunction:: spectral.create_training_classes

TrainingClass
-------------

.. autoclass:: spectral.algorithms.algorithms.TrainingClass
   :members: __init__, __iter__, stats_valid, size, calc_stats, transform
   :special-members: __init__, __iter__

TraningClassSet
---------------

.. autoclass:: spectral.algorithms.algorithms.TrainingClassSet
   :members: add_class, transform, all_samples, __getitem__, __len__, __iter__

Spectral Classes/Functions
==========================

Adaptive Coherence/Cosine Estimator (ACE)
-----------------------------------------

.. autofunction:: spectral.algorithms.detectors.ace

AsterDatabase
-------------

.. autoclass:: spectral.database.AsterDatabase
   :members:

.. _spectral-band-info:

BandInfo
--------

.. autoclass:: spectral.BandInfo

BandResampler
-------------

.. autoclass:: spectral.algorithms.resampling.BandResampler
   :members: __init__, __call__

Bhattacharyya Distance
----------------------

.. autofunction:: spectral.algorithms.algorithms.bdist

.. note::

   Since it is unlikely anyone can actually remember how to spell
   "Bhattacharyya", this function has been aliased to "bdist"
   for convenience.

calc_stats
----------

.. autofunction:: spectral.calc_stats

covariance
----------

.. autofunction:: spectral.algorithms.algorithms.covariance

cov_avg
-------

.. autofunction:: spectral.algorithms.algorithms.cov_avg

EcostressDatabase
-----------------

.. autoclass:: spectral.database.EcostressDatabase
   :members:

FisherLinearDiscriminant
------------------------

.. autoclass:: spectral.algorithms.algorithms.FisherLinearDiscriminant

GaussianClassifier
------------------

.. autoclass:: spectral.algorithms.classifiers.GaussianClassifier
   :members: __init__, train, classify_spectrum
   :special-members: __init__
   :inherited-members: classify_image

GaussianStats
-------------

.. autoclass:: spectral.algorithms.algorithms.GaussianStats

kmeans
------

.. autofunction:: spectral.kmeans

linear_discriminant
-------------------

.. autofunction:: spectral.linear_discriminant

LinearTransform
---------------

.. autoclass:: spectral.algorithms.transforms.LinearTransform
   :members: __init__, __call__, chain
   :special-members: __init__, __call__

MahalanobisDistanceClassifier
-----------------------------

.. autoclass:: spectral.algorithms.classifiers.MahalanobisDistanceClassifier
   :members: __init__, train, classify_spectrum
   :special-members: __init__
   :inherited-members: classify_image

map_class_ids
-------------

.. autofunction:: spectral.algorithms.spatial.map_class_ids

map_classes
-----------

.. autofunction:: spectral.algorithms.spatial.map_classes

matched_filter
--------------

.. autofunction:: spectral.algorithms.detectors.matched_filter

MatchedFilter
-------------
.. autoclass:: spectral.algorithms.detectors.MatchedFilter
   :members: __init__, whiten
   :special-members: __init__, __call__
   
mean_cov
--------

.. autofunction:: spectral.algorithms.algorithms.mean_cov

Minimum Noise Fraction (MNF)
----------------------------

.. autofunction:: spectral.algorithms.algorithms.mnf

.. autoclass:: spectral.algorithms.algorithms.MNFResult
   :members: denoise, get_denoising_transform, reduce, get_reduction_transform, num_with_snr

msam
----

.. autofunction:: spectral.algorithms.algorithms.msam

ndvi
----

.. autofunction:: spectral.algorithms.algorithms.ndvi

noise_from_diffs
----------------

.. autofunction:: spectral.algorithms.algorithms.noise_from_diffs

orthogonalize
-------------

.. autofunction:: spectral.algorithms.algorithms.orthogonalize

PerceptronClassifier
--------------------

.. autoclass:: spectral.algorithms.classifiers.PerceptronClassifier
   :members: __init__, train, classify_spectrum
   :inherited-members: classify_image

Pixel Purity Index (PPI)
------------------------

.. autofunction:: spectral.algorithms.algorithms.ppi

principal_components
--------------------

.. autofunction:: spectral.principal_components

PrincipalComponents
-------------------

.. autoclass:: spectral.algorithms.algorithms.PrincipalComponents
   :members: reduce
   :inherited-members: transform

RX Anomaly Detector
-------------------

.. autofunction:: spectral.algorithms.detectors.rx

spectral_angles
---------------

.. autofunction:: spectral.algorithms.algorithms.spectral_angles

SpectralLibrary
---------------

.. autoclass:: spectral.io.envi.SpectralLibrary
   :members:

transform_image
---------------

.. autofunction:: spectral.io.spyfile.transform_image

Configuration
=============

SpySettings
-----------

.. autoclass:: spectral.config.SpySettings

Utilities
=========

iterator
--------

.. autofunction:: spectral.algorithms.algorithms.iterator


