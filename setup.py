from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.policy',
      version=version,
      description="plone policy for Plonecof2014 demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='policy demo plone4',
      author='Marco Da Silva',
      author_email='markmarco16@hotmial.com',
      url='https://github.com/markmarco16/ploneconf2014.policy/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'plone.app.contenttypes',
          'collective.geo.bundle[dexterity]',
          'wildcard.foldercontents',
          'collective.plonetruegallery',
          'ploneconf2014.theme',
          'ploneconf2014.contenttypes',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': ['plone.app.testing'],
       },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
