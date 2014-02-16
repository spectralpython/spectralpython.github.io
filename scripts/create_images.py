'''Creates dynamic images needed for Sphinx documentation.'''

import sys
import os
import numpy as np
import spectral as spy

image = spy.open_image('92AV3C.lan').load()
gt = spy.open_image('92AV3GT.GIS').read_band(0)

def view_image(outdir='.'):
    spy.save_rgb(os.path.join(outdir, 'view_image_default.jpg'), image)
    spy.save_rgb(os.path.join(outdir, 'view_image_rgb.jpg'), image, [29, 19, 9])
    spy.save_rgb(os.path.join(outdir, 'view_image_g.jpg'), image, [19])
    spy.save_rgb(os.path.join(outdir, 'view_gt.jpg'), gt, colors=spy.spy_colors)

def create_clusters(outdir='.'):
    import matplotlib.pyplot as plt
    plt.ioff()
    (m, c) = spy.cluster(image, 20)
    spy.save_rgb(os.path.join(outdir, 'cluster20.jpg'), m, colors=spy.spy_colors)
    
    (m, c) = spy.kmeans(image, 20, 30)
    spy.save_rgb(os.path.join(outdir, 'kmeans_20_30.jpg'), m, colors=spy.spy_colors)
    plt.figure()
    plt.hold(1)
    for i in range(c.shape[0]):
        plt.plot(c[i])
    plt.savefig(os.path.join(outdir, 'kmeans_20_30_centers.png'))
    
def create_supervised(outdir='.'):
    classes = spy.create_training_classes(image, gt)
    gmlc = spy.GaussianClassifier(classes)
    clmap = gmlc.classify_image(image)
    spy.save_rgb(os.path.join(outdir, 'gmlc.jpg'), clmap, colors=spy.spy_colors)
    clmap_training = clmap * (gt != 0)
    spy.save_rgb(os.path.join(outdir, 'gmlc_training.jpg'), clmap_training, colors=spy.spy_colors)
    spy.save_rgb(os.path.join(outdir, 'gmlc_errors.jpg'), clmap_training * (clmap_training != gt), colors=spy.spy_colors)

def create_dimensionality(outdir='.'):
    pc = spy.principal_components(image)
    spy.save_rgb(os.path.join(outdir, 'covariance.jpg'), pc.cov)
    pc_0999 = pc.reduce(fraction=0.999)
    image_pc = pc_0999.transform(image)
    spy.save_rgb(os.path.join(outdir, 'pc3.jpg'), image_pc[:,:,:3], stretch_all=True)

    classes = spy.create_training_classes(image_pc, gt)
    gmlc = spy.GaussianClassifier(classes)
    clmap = gmlc.classify_image(image_pc)
    clmap_training = clmap * (gt != 0)
    spy.save_rgb(os.path.join(outdir, 'gmlc2_training.jpg'), clmap_training, colors=spy.spy_colors)
    training_errors = clmap_training * (clmap_training != gt)
    spy.save_rgb(os.path.join(outdir, 'gmlc2_errors.jpg'), training_errors, colors=spy.spy_colors)

    classes = spy.create_training_classes(image, gt)
    fld = spy.linear_discriminant(classes)
    image_fld = fld.transform(image)
    spy.save_rgb(os.path.join(outdir, 'fld3.jpg'), image_fld[:,:,:3], colors=spy.spy_colors)
    
    classes.transform(fld.transform)
    gmlc = spy.GaussianClassifier(classes)
    clmap = gmlc.classify_image(image_fld)
    clmap_training = clmap * (gt != 0)
    spy.save_rgb(os.path.join(outdir, 'gmlc_fld_training.jpg'), clmap_training, colors=spy.spy_colors)
    fld_errors = clmap_training * (clmap_training != gt)
    spy.save_rgb(os.path.join(outdir, 'gmlc_fld_errors.jpg'), fld_errors, colors=spy.spy_colors)
    
def create_lib_plots(outdir='.'):
    import spectral.io.aviris as aviris
    db = spy.AsterDatabase('aster_lib.db')
    s = db.get_signature(2436)
    import matplotlib.pyplot as plt
    plt.ioff()
    f = plt.figure()
    plt.plot(s.x, s.y)
    plt.title(s.sample_name)
    plt.grid(1)
    plt.savefig(os.path.join(outdir, 'limestone.png'))

    bands = aviris.read_aviris_bands('92AV3C.spc')
    bands.centers = [x / 1000. for x in bands.centers]
    bands.bandwidths = [x / 1000. for x in bands.bandwidths]

    rows = db.query('SELECT SpectrumID FROM Samples, Spectra ' +
		    'WHERE Samples.SampleID = Spectra.SampleID AND ' +
		    'Name LIKE "%stone%" AND ' +
		    'MinWavelength <= 0.4 AND MaxWavelength >= 2.5')
    ids = [r[0] for r in rows]
    
    lib = db.create_envi_spectral_library(ids, bands)

    f = plt.figure()
    plt.plot(s.x, s.y, label='original')
    plt.hold(1)
    plt.plot(bands.centers, lib.spectra[-1], color='red', label='resampled')
    plt.grid(1)
    plt.legend(loc='upper left')
    plt.xlim(0, 3)
    f.set_size_inches(8, 4)
    plt.title('Resampled %s spectrum' % lib.names[-1])
    plt.savefig(os.path.join(outdir, 'limestone_resampled.png'))
    
def create_ndvi(outdir='.'):
    ndvi = spy.ndvi(image, 21, 43)
    spy.save_rgb(os.path.join(outdir, 'ndvi.jpg'), ndvi)  
    
    classes = spy.create_training_classes(image, gt, True)
    means = np.zeros((len(classes), image.shape[2]), float)
    for (i, c) in enumerate(classes):
        means[i] = c.stats.mean
    angles = spy.spectral_angles(image, means)
    c = np.argmin(angles, 2)
    spy.save_rgb(os.path.join(outdir, 'spectral_angles_training.jpg'),
                 (c + 1) * (gt != 0), colors=spy.spy_colors)

def create_all(outdir='.'):
    view_image(outdir)
    create_clusters(outdir)
    create_supervised(outdir)
    create_dimensionality(outdir)
    create_lib_plots(outdir)
    create_ndvi(outdir)

if __name__ == '__main__':
    import argparse
    import sys
    import os
    parser = argparse.ArgumentParser(description='Creates dynamic images ' \
                                     'for Sphinx documentation.')
    parser.add_argument('--outdir', '-o', default='.',
                        help='directory in which to create the images')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    spy.settings.show_progress = args.verbose
    stdout = sys.stdout
    if not args.verbose:
        sys.stdout = open(os.devnull, 'w')
    try:
        create_all(args.outdir)
    finally:
        sys.stdout = stdout
