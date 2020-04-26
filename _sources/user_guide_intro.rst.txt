.. _user-guide-intro:

===================
Introduction
===================

This user guide introduces various categories of  SPy functions in a tutorial
style.  If you would like to test the commands presented in the guide, you
should download the following sample data files, which are associated with a
well-studied AVIRIS hyperspectral image collected over Indiana in 1992.
[Landgrebe1998]_


.. list-table:: Sample Data Files
   :header-rows: 1
   :widths: 5, 30
   :class: center

   * - File Name
     - Description
   * - :download:`92AV3C.lan <data/92AV3C.lan>`
     - A small hyperspectral image chip (9.3 MB) in ERDAS/Lan format.  The chip
       is 145x145 pixels from an AVIRIS image and contains 220 spectral bands.
   * - :download:`92AV3GT.GIS <data/92AV3GT.GIS>`
     - A land-use ground-truth map for the hyperspectral image chip in ERDAS/Lan
       format.
   * - :download:`92AV3C.spc <data/92AV3C.spc>`
     - An AVIRIS-formatted band calibration file for the image chip.

Many of the examples presented in the guide are cumulative, with success of
commands issued depending on previous commands and module imports.  While it is
generally not a good idea to import the contents of entire module namespaces,
for brevity, the examples in the user guide assume that ``from spectral import *``
has been issued.

.. rubric:: References

.. [Landgrebe1998] Landgrebe, D. Multispectral data analysis: A signal theory
   perspective. School of Electr. Comput. Eng., Purdue Univ., West Lafayette, IN  (1998).
