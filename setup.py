from setuptools import setup, find_packages

from chained_selectbox import __version__

github_url = 'https://github.com/s-block/django-chained-selectbox'
long_desc = open('README.md').read()

setup(
    name='django-chained-selectbox',
    version='.'.join(str(v) for v in __version__),
    description='Ajax choice field widget for use with Django admin',
    long_description=long_desc,
    url=github_url,
    author='Josh Rowe',
    author_email='josh@s-block.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
