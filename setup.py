
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf_billing",
    version=__import__('drf_billing').__version__,
    author=__import__('drf_billing').__author__,
    author_email="pypidev@civilmachines.com",
    description="Billing APP for Django REST Framework with API Views",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=__import__('drf_billing').__license__,
    url="https://github.com/civilmachines/drf-billing",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read().split(),
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP'
    ),
)
