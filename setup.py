from setuptools import setup, find_packages

VERSION = '0.1.10'

setup(
    name="mkdocs-ringcentral",
    version=VERSION,
    url='https://github.com/byrnereese/mkdocs-ringcentral/',
    description='RingCentral theme for MkDocs',
    author='Byrne Reese',
    author_email='byrne.reese@ringcentral.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.1',
        'mkdocs-ringcentral-api-index>=0.1.2',
        'mkdocs-moonstone>=0.1.17'
    ],
    python_requires='>=3.0',
    entry_points={
        'mkdocs.themes': [
            'ringcentral = mkdocs_ringcentral',
        ]
    },
    zip_safe=False
)
