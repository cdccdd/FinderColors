from setuptools import setup, find_packages

setup(
    name="findercolors",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scikit-image>=0.18.0",
        "Pillow>=8.3.0",
    ],
    author="Churilo Maxim",
    author_email="cdccdd@example.com",
    description="A program for generating color combinations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cdccdd/FinderColors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "findercolors=main.main:main",
        ],
    },
) 