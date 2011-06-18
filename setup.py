from setuptools import setup, find_packages

setup(
    name = "raytrace",
    version = "0.1",
    packages = find_packages(),
    scripts = ['test1.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['numpy>=1.5','PIL','pygame>=1.9'],
    test_suite = "test.test_all",
    package_data = {
    },

    # metadata for upload to PyPI
    author = "Stefano Borini",
    author_email = "stefano.borini@ferrara.linux.it",
    description = "A simple raytracer",
    license = "BSD 2",
    keywords = "raytrace raytracing",
    url = "https://github.com/stefanoborini/python-raytrace/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
