# Top-level Makefile for creating the Spectral Python (SPy) website

SPHINXDIR = sphinx
SPHINXOPTS = -W
PYTHON = python

# The name of a sample data file so we know whether to init/update the git submodule
IMAGE_FILE = $(SPHINXDIR)/data/92AV3C.lan

.PHONY:		sphinx-html, images, upload, clean, help, git-submodules

help:
	@echo "Build targets:"
	@echo "  sphinx-html      Makes Sphinx HTML files without creating externally"
	@echo "                   generated images (faster and useful for debugging)."
	@echo "  images           Makes external images referenced by Sphinx."
	@echo "  site             Builds all website content."
	@echo "  clean            Removes all generated content."
	@echo "  upload           Uploads web site content to server."
	@echo ""

sphinx-html:	$(IMAGE_FILE)
	@echo "Building Sphinx files..."
	$(MAKE) -C $(SPHINXDIR) html SPHINXOPTS=$(SPHINXOPTS)

images:
	@echo "Creating image files..."
	$(PYTHON) scripts/create_images.py -o $(SPHINXDIR)/images

$(IMAGE_FILE):	git-submodules

git-submodules:
	@echo "Retrieving sample data files from GitHub..."
	git submodule init
	git submodule update

site:		images sphinx-html

upload:
	@echo "Not yet implemented."

clean:
	$(MAKE) -C $(SPHINXDIR) clean
	rm -rf $(SPHINXDIR)/images

