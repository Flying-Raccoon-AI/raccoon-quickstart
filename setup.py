from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'raccoon-quickstart',
    version = '0.0.1',
    author = 'Raccoon AI',
    author_email = 'team@flyingraccoon.tech',
    license = 'MIT',
    description = 'Raccoon quickstart generator',
    long_description_content_type = "text/markdown",
    url = 'https://github.com/Flying-Raccoon-AI/raccoon-quickstart',
    py_modules = ['raccoon', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        raccoon-quickstart=raccoon:cli
    '''
)
