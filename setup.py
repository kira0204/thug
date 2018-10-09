#!/usr/bin/env python

import os
import glob
from setuptools import setup, find_packages  # Always prefer setuptools over distutils

os.environ['BUILD_LIB'] = '1'

import thug

personalities_path = os.path.join(thug.__configuration_path__, "personalities")
rules_path         = os.path.join(thug.__configuration_path__, "rules")
scripts_path       = os.path.join(thug.__configuration_path__, "scripts")
plugins_path       = os.path.join(thug.__configuration_path__, "plugins")
hooks_path         = os.path.join(thug.__configuration_path__, "hooks")

html_rules_path    = os.path.join(rules_path, "htmlclassifier")
js_rules_path      = os.path.join(rules_path, "jsclassifier")
vbs_rules_path     = os.path.join(rules_path, "vbsclassifier")
url_rules_path     = os.path.join(rules_path, "urlclassifier")
sample_rules_path  = os.path.join(rules_path, "sampleclassifier")
text_rules_path    = os.path.join(rules_path, "textclassifier")
html_filter_path   = os.path.join(rules_path, "htmlfilter")
js_filter_path     = os.path.join(rules_path, "jsfilter")
vbs_filter_path    = os.path.join(rules_path, "vbsfilter")
url_filter_path    = os.path.join(rules_path, "urlfilter")
sample_filter_path = os.path.join(rules_path, "samplefilter")
text_filter_path   = os.path.join(rules_path, "textfilter")

setup(
    name="thug",
    version=thug.__version__,
    author="Angelo Dell'Aera",
    author_email="angelo.dellaera@honeynet.org",
    description="Low-interaction honeyclient Thug",
    license="GPLv2",
    long_description=open("README.rst").read(),
    url="http://buffer.github.io/thug/",
    download_url="https://github.com/buffer/thug/",
    platforms=["Linux", ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2.7",
        "Topic :: Security",
    ],
    package_data={
           "": ["*.js"],
           },
    packages=find_packages(),
    data_files=[
        (thug.__configuration_path__, ["thug/Analysis/honeyagent/honeyagent.conf.sample",
                                       "thug/Analysis/virustotal/virustotal.conf.default",
                                       "thug/Logging/logging.conf.default"]),
        (personalities_path         , glob.glob("thug/DOM/personalities/*.json")),
        (rules_path                 , glob.glob("thug/Classifier/rules/*.yar")),
        (scripts_path               , ["thug/DOM/thug.js",
                                       "thug/DOM/storage.js",
                                       "thug/DOM/date.js",
                                       "thug/DOM/eval.js",
                                       "thug/DOM/write.js",
                                       "thug/Debugger/d8.js"]),
        (plugins_path               , []),
        (hooks_path                 , []),
        (html_rules_path            , glob.glob("thug/Classifier/rules/htmlclassifier/*.yar")),
        (js_rules_path              , glob.glob("thug/Classifier/rules/jsclassifier/*.yar")),
        (vbs_rules_path             , glob.glob("thug/Classifier/rules/vbsclassifier/*.yar")),
        (url_rules_path             , glob.glob("thug/Classifier/rules/urlclassifier/*.yar")),
        (sample_rules_path          , glob.glob("thug/Classifier/rules/sampleclassifier/*.yar")),
        (text_rules_path            , glob.glob("thug/Classifier/rules/textclassifier/*.yar")),
        (html_filter_path           , glob.glob("thug/Classifier/rules/htmlfilter/*.yar")),
        (js_filter_path             , glob.glob("thug/Classifier/rules/jsfilter/*.yar")),
        (vbs_filter_path            , glob.glob("thug/Classifier/rules/vbsfilter/*.yar")),
        (url_filter_path            , glob.glob("thug/Classifier/rules/urlfilter/*.yar")),
        (sample_filter_path         , glob.glob("thug/Classifier/rules/samplefilter/*.yar")),
        (text_filter_path           , glob.glob("thug/Classifier/rules/textfilter/*.yar")),

    ],
    install_requires=[
        "PySocks==1.6.8",
        "beautifulsoup4==4.6.3",
        "cchardet==2.1.1",
        "cssutils==1.0.2",
        "elasticsearch==6.3.1",
        "esprima==4.0.1",
        "html5lib==1.0.1",
        "lxml==4.2.5",
        "networkx==2.2",
        "pefile==2018.8.8",
        "pygraphviz==1.5",
        "pylibemu==0.5.8",
        "pymongo==3.7.1",
        "python-magic==0.4.15",
        "rarfile==3.0",
        "requests==2.19.1",
        "six==1.11.0",
        "ssdeep==3.2",
        "yara-python==3.8.1",
        "zope.interface==4.5.0",
    ],
    extras_require={
        'dev': [
            "codecov==2.0.15",
            "mock==2.0.0",
            "mongomock>=3.12.0,<3.13.0",
            "pytest==3.8.2",
            "pytest-timeout==1.3.2",
            "pytest-cov==2.6.0",
            "tox==3.5.2"
        ]
    },
    entry_points={
        "console_scripts": [
            "thug = thug.thug:main",
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/buffer/thug/issues',
        'Funding': 'https://buffer.github.io/thug/',
        'Source': 'https://github.com/buffer/thug/',
    },
)
