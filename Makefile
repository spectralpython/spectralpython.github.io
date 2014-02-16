# Top-level Makefile for creating the Spectral Python (SPy) website

SPHINXDIR = sphinx
SPHINXOPTS = -W
PYTHON = python

.PHONY:		sphinx-html, images, upload, clean, help

help:
	@echo "Build targets:"
	@echo "  sphinx-html      Makes Sphinx HTML files without creating externally"
	@echo "                   generated images (faster and useful for debugging)."
	@echo "  images           Makes external images referenced by Sphinx."
	@echo "  site             Builds all website content."
	@echo "  clean            Removes all generated content."
	@echo "  upload           Uploads web site content to server."
	@echo ""

sphinx-html:
	$(MAKE) -C $(SPHINXDIR) html SPHINXOPTS=$(SPHINXOPTS)

images:
	$(PYTHON) scripts/create_images.py -o $(SPHINXDIR)/images

site:		images sphinx-html

upload:
	@echo "Not yet implemented."

clean:
	$(MAKE) -C $(SPHINXDIR) clean
	rm -rf $(SPHINXDIR)/images

