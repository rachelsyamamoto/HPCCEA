import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="central-gender-database", # Replace with your own username
    version="0.0.1",
    author="Meghan Utter and Nisha Prabhakar",
    author_email="utter2@llnl.gov",
    description="centralized notde attribute database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LLNL/HPCCEA/tree/gendersteam/2020/Genders",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
