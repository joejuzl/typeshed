from __future__ import print_function

import codecs
import os
import sys
from setuptools import setup

import typeshed


VERSION = typeshed.__version__
PROJECT_URL = "https://github.com/python/typeshed/"
ISSUES_URL = PROJECT_URL + "issues/"
SOURCE_URL = PROJECT_URL
_commit = typeshed.git_revision()
if _commit:
    SOURCE_URL += "commit/" + _commit


def get_long_description():
    current_dir = os.path.dirname(__file__)
    readme_md = os.path.join(current_dir, "README.md")
    with codecs.open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


setup(
    name="typeshed",
    version=VERSION,
    description="Collection of library stubs for Python, with static types",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license="MIT",
    url=PROJECT_URL,
    packages=["typeshed"],
    include_package_data=True,  # from MANIFEST.in
    project_urls={"Bug Tracker": ISSUES_URL, "Source Code": SOURCE_URL},
    install_requires=[],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=2.7",
    zip_safe=True,
)


if typeshed.is_dirty():
    print()
    print("WARNING: there are uncommitted changes.", file=sys.stderr)