from setuptools import setup

setup(  name='date_simple',
        version='0.1',
        description = "This module simplifies the interface to Python's datetime module  the user.",
        url='https://github.com/jose112624120/date_simple',
        author='jose112624120',
        author_email='jose112624120@gmail.com',
        license='MIT',
        packages=['date_simple'],
        install_requires=[ ],
        test_suite='pytest',
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        zip_safe=False )