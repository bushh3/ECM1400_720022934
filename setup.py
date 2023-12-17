from setuptools import setup, find_packages

setup(
    # project name
    name='ECM1400_720022934',
    # final release version
    version='1.0.0',
    # descriptions of project
    description='A Battleship Game versus AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # project location
    url='https://github.com/bushh3/ECM1400_720022934',  # Adjust the URL based on your project's repository
    # author details
    author='Henry (Harry) James Hardy Bush',
    author_email='harryjhbush@icloud.com',
    # license type
    license='MIT',
    # classifiers for the project
    classifiers=[
        # how mature the project is
        'Development Status :: 5 - Production/Stable',
        # who the project is for
        'Intended Audience :: Examiners',
        'Topic :: Software Development :: Coursework',
        # license used
        'License :: OSI Approved :: MIT License',
        # versions of python supported
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    # keywords describing this project
    keywords = 'battleships, game, AI',
    # list all packages used
    packages=find_packages(where='src'),
    # requirements for the project to run
    py_modules=['components', 'game_engine', 'mp_game_engine', 'main'],
    install_requires=[
        'Flask>=1.0',
    ],
    python_requires='>=3, <4',
    package_data={
        'battleships_game': [
            '*.txt', 
            '*.json',
            '*.html',
        ],
    },
    # entry point for the project
    entry_points={
        'console_scripts': [
            'start_game=battleships_game.main:main',
        ],
    },
    # url locations for essential parts of the project
    project_urls={
    'Documentation': 'https://github.com/bushh3/ECM1400_720022934/blob/main/README.md',
    'Source': 'https://github.com/bushh3/ECM1400_720022934/tree/main/src/battleships_game',
    'Tests': 'https://github.com/bushh3/ECM1400_720022934/tree/main/tests',
    },
)
