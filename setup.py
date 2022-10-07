from setuptools import setup, find_namespace_packages
import re
import os.path


CURDIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(CURDIR, "sphinx_tsn_theme", "__init__.py")) as f:
    VERSION = re.search(r'__version__\s+=\s+"(.*)"', f.read()).group(1)

with open(os.path.join(CURDIR, "requirements.txt")) as requirements:
    REQUIREMENTS = requirements.read().splitlines()


setup(
    name="sphinx-tsn-theme",
    version=VERSION,
    license="MIT",
    url="https://www.tiac-systems.net",
    author="TiaC Systems Network",
    author_email="info@tiac-systems.net",
    description="TiaC Systems Network (TSN) theme for Sphinx",
    long_description=open("README.rst", encoding="utf-8").read(),
    packages=find_namespace_packages(),
    package_data={
        "sphinx_tsn_theme": [
            "theme.conf",
            "*.html",
            "static/**/*",
        ]
    },
    include_package_data=True,
    entry_points={
        "sphinx.html_themes": [
            "sphinx_tsn_theme = sphinx_tsn_theme",
        ]
    },
    install_requires=REQUIREMENTS,
    classifiers=[
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
