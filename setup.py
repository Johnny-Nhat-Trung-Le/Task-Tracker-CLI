from setuptools import setup

setup (
    name='tracker-of-tasks',
    version='0.0.0',
    description='CLI app to track your tasks',
    author='Trung',
    author_email='johnnynhattrungle@gmail.com',
    url='https://github.com/Johnny-Nhat-Trung-Le/Task-Tracker-CLI',
    package=['core'],
    entry_points={
        'console_scripts': [
            'core=core.cli:main',
        ],
    },
    install_requires=[
        "tabulate",
    ],
    tests_require=[
        "pytest",
    ],
)