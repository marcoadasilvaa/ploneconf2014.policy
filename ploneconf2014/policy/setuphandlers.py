# -*- coding: utf-8 -*-

from plone import api
from ploneconf2014.policy.config import PROJECTNAME

import logging
logger = logging.getLogger(PROJECTNAME)

def remove_defaults_nav(portal):
    '''Remove defaults navegations and contents'''
    items_removable = ['news', 'events', 'Members', 'front-page']
    for item in items_removable:
        if hasattr(portal, item):
            try:
                api.content.delete(obj=portal[item])
                logger.info("Deleted {0} item".format(item))
            except AttributeError:
                logger.info("No {0} item detected. Hmm... strange. Continuing....".format(item))

def create_defaults_contents(portal):
    '''Create defaults navegations and contents'''
pass

def setupVarious(context):
    """ miscellaneous import steps for setup """
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('ploneconf2014.policy_various.txt') is None:
        return

    portal = api.portal.get()
    remove_defaults_nav(portal)
# create_defaults_contents(portal)