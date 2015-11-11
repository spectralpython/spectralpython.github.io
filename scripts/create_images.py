'''Creates dynamic images needed for Sphinx documentation.'''

import sys
import os
import numpy as np
import spectral as spy

image = spy.open_image('92AV3C.lan').load()
gt = spy.open_image('92AV3GT.GIS').read_band(0)

def view_image(outdir='.'):
    spy.save_rgb(os.path.join(outdir, 'view_image_rgb.jpg'), image, [29, 19, 9])
    spy.save_rgb(os.path.join(outdir, 'view_gt.jpg'), gt, colors=spy.spy_colors)

def create_clusters(outdir='.'):
    import matplotlib.pyplot as plt
    plt.ioff()
    
    (m, c) = spy.kmeans(image, 20, 30)
    spy.save_rgb(os.path.join(outdir, 'kmeans_20_30.jpg'), m, colors=spy.spy_colors)
    plt.figure()
    plt.hold(1)
    for i in range(c.shape[0]):
        plt.plot(c[i])
    plt.savefig(os.path.join(outdir, 'kmeans_20_30_centers.png'))
    
def create_all(outdir='.'):
    view_image(outdir)
    create_clusters(outdir)

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
