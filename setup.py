import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="glg_jupyter_notebook_utils",  # Replace with your own username
    version="0.0.1",
    author="Amit Segal",
    author_email="asegal@glgroup.com.com",
    description="Utility functions for glg jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glg/glg-jupyter-notebook-utils",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
