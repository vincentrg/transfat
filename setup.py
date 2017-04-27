from setuptools import setup

setup(
    name='trans-fat',
    version='0.1.0',
    description='Play audio files on your car stereo and maintain sanity',
    url='https://github.com/mwiens91/trans-fat',
    author='Matt Wiens',
    author_email='mwiens91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['transfat'],
    entry_points={
        'console_scripts': ['trans-fat = transfat.main:main'],
    },
)