import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timestamps",
    version="1.0.0",
    author="Jordan Leppert",
    author_email="jordanleppert@gmail.com",
    description="CLI tool to prefix lines of output with a timestamp.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JordanL2/Timestamps",
    packages=setuptools.find_packages() + setuptools.find_namespace_packages(include=['timestamps.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {'console_scripts': [
        'timestamps=timestamps.cli:main',
        ], },
)
