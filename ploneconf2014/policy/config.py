# -*- coding: utf-8 -*-

"""
Contains constants used by setuphandler.py
"""	

PROJECTNAME = 'ploneconf2014.policy'

DEPENDENCIES = [
    'plone.api',
	'plone.app.contenttypes',
	'collective.geo.bundle[dexterity]',
	'wildcard.foldercontents',
	'collective.plonetruegallery',
	'ploneconf2014.contenttypes',
	'ploneconf2014.theme',
    ]

"""
PRODUCT_DEPENDENCIES = [
    'plone.api',
	'plone.app.contenttypes',
	'collective.geo.bundle[dexterity]',
	'wildcard.foldercontents',
	'collective.plonetruegallery',
    ]

PACKAGE_DEPENDENCIES = [
	'ploneconf2014.contenttypes',
	'ploneconf2014.theme',
    ]

DEPENDENCIES = PRODUCT_DEPENDENCIES + PACKAGE_DEPENDENCIES
"""