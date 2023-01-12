import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-cli-sample",
    version="0.0.1",
    author="ivis-tsukioka",
    author_email="cmtaro@example.com",
    license='MIT',
    description="Sample code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivis-OTS/kl_python_cli.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)