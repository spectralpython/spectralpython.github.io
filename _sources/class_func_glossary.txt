.. toctree::
    :maxdepth: 2

.. _class-func-glossary:

========================
Class/Function Glossary
========================

File Input/Output
=================

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :func:`~spectral.database.AsterDatabase`
     - Create/Query a spectral database generated from the ASTER Spectral Library
   * - :func:`aviris.open <spectral.io.aviris.open>`
     - Open an AVIRIS image file
   * - :func:`aviris.read_aviris_bands <spectral.io.aviris.read_aviris_bands>`
     - Read an AVIRIS band calibration file
   * - :func:`envi.open <spectral.io.envi.open>`
     - Open a data file (image, classification, or spectral library) that has
       an ENVI header
   * - :func:`envi.create_image <spectral.io.envi.create_image>`
     - Open a new (empty) image file with an ENVI header
   * - :func:`envi.save_classification <spectral.io.envi.save_classification>`
     - Save classification labels to a file with a corresponding ENVI header
   * - :func:`envi.save_image <spectral.io.envi.save_image>`
     - Save image data to a file with a corresponding ENVI header
   * - :func:`envi.SpectralLibrary <spectral.io.envi.SpectralLibrary>`
     - Class to create/save spectral libraries in ENVI format
   * - :func:`erdas.open <spectral.io.erdas.open>`
     - Open an Erdas LAN image file
   * - :func:`~spectral.spectral.open_image`
     - Generic function for opening multiple hyperspectral image file formats

|

Display/Visualization
=====================

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :class:`~spectral.ColorScale`
     - Create color scales for use with data display functions
   * - :func:`~spectral.graphics.graphics.get_rgb`
     - Produce RGB array suitable for display from image data
   * - :func:`~spectral.graphics.spypylab.ImageView`
     - Class for interacting with image displays (returned by :func:`~spectral.graphics.spypylab.imshow`)
   * - :func:`~spectral.graphics.spypylab.imshow`
     - Primary function for displaying raster views of image data (an extension of matplotlib's `imshow` providing overlays and interactivity)
   * - :func:`~spectral.algorithms.algorithms.ppi`
     - Display Pixel Purity Index values while :func:`ppi` function executes.
   * - :func:`~spectral.save_rgb`
     - Saves image data in common RGB image formats (e.g., JPEG, PNG)
   * - :func:`~spectral.view_cube`
     - View an interactive 3D image cube
   * - :func:`~spectral.view_nd`
     - Display an interactive N-D visualization of image pixel data

|

Dimensionality Reduction
========================

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :func:`~spectral.linear_discriminant`
     - Computes Fisher's Linear Discriminant for a set of classes
   * - :func:`~spectral.algorithms.algorithms.mnf`
     - Minimum Noise Fraction
   * - :func:`~spectral.algorithms.algorithms.ppi`
     - Calculates Pixel Purity Index (PPI)
   * - :func:`~spectral.principal_components`
     - Calculates principal components of an image

|

Target Detection
================

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :func:`~spectral.algorithms.detectors.ace`
     - Adaptive Coherence/Cosine Estimator
   * - :func:`~spectral.algorithms.detectors.matched_filter`
     - Applies a linear matched filter detector for a given target
   * - :func:`~spectral.algorithms.algorithms.msam`
     - Modified Spectral Angle Mapper (MSAM)
   * - :func:`~spectral.algorithms.detectors.rx`
     - RX anomaly detector
   * - :func:`~spectral.algorithms.algorithms.spectral_angles`
     - Spectral Angle Mapper (SAM)

|

Classification
==============

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :func:`~spectral.create_training_classes`
     - Creates a :class:`TrainingClassSet <spectral.algorithms.algorithms.TrainingClassSet>` object from image data and ground truth
   * - :class:`~spectral.algorithms.classifiers.GaussianClassifier`
     - Gaussian Maximum Likelihood Classifier (GMLC)
   * - :func:`~spectral.kmeans`
     - Unsupervised image classification via k-means clustering
   * - :class:`~spectral.algorithms.classifiers.MahalanobisDistanceClassifier`
     - A classifier using Mahalanobis distance
   * - :func:`~spectral.algorithms.algorithms.msam`
     - Modified Spectral Angle Mapper (MSAM)
   * - :func:`~spectral.algorithms.classifiers.PerceptronClassifier`
     - A Multi-Layer Perceptron (MLP) Artificial Neural Network (ANN) classifier
   * - :func:`~spectral.algorithms.algorithms.spectral_angles`
     - Spectral Angle Mapper (SAM)
   * - :class:`~spectral.algorithms.algorithms.TrainingClassSet`
     - Object returned from :func:`spectral.create_training_classes`
       (used by some classifiers)

|

Spectral Transforms
===================

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :class:`~spectral.BandInfo`
     - Container for spectral band discretization/calibration data
   * - :class:`~spectral.algorithms.resampling.BandResampler`
     - Class for performing band resampling
   * - :class:`FisherLinearDiscriminant <spectral.algorithms.algorithms.FisherLinearDiscriminant>`
     - Object returned by :func:`~spectral.linear_discriminant` to transform image data into linear discriminant space.
   * - :class:`~spectral.algorithms.transforms.LinearTransform`
     - A callable linear transform that can be applied to image data
   * - :class:`MNFResult <spectral.algorithms.algorithms.MNFResult>`
     - Object returned by :func:`~spectral.algorithms.algorithms.mnf` to reduce dimensionality via Minimum Noise Fraction (MNF)
   * - :func:`~spectral.algorithms.algorithms.ndvi`
     - Normalized Difference Vegetation Index (NDVI)
   * - :class:`PrincipalComponents <spectral.algorithms.algorithms.PrincipalComponents>`
     - Object returned by :func:`~spectral.principal_components`. Transforms data into PCA space and - optionally - reduces dimensionality.

|

Math/Statistics
===============

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :func:`~spectral.algorithms.algorithms.bdist`
     - Bhattacharyya distance
   * - :func:`~spectral.calc_stats`
     - Calculates Gaussian statistics for image data
   * - :func:`~spectral.algorithms.algorithms.covariance`
     - Calculates image data covariance
   * - :func:`~spectral.algorithms.algorithms.cov_avg`
     - Calculates covariance averaged over a set of ground truth classes
   * - :func:`noise_from_diffs <spectral.algorithms.algorithms.noise_from_diffs>`
     - Estimate image noise statistics from a homogeneous region
   * - :func:`~spectral.algorithms.algorithms.orthogonalize`
     - Performs Gram-Schmidt orthogonalization on a set of vectors
   * - :func:`~spectral.principal_components`
     - Calculates principal components of an image
   * - :func:`~spectral.io.spyfile.transform_image`
     - Applies a linear transform to image data

Miscellaneous
=============

.. list-table::
   :header-rows: 1
   :widths: 15, 30
   :class: center

   * - Class/Function
     - Description
   * - :obj:`settings <spectral.spectral.SpySettings>`
     - Object for controlling SPy configuration options
   * - :func:`algorithms.algorithms.iterator <spectral.algorithms.algorithms.iterator>`
     - Function returning an iterator over image pixels
