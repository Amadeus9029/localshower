import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="localshower-amadeus",
  version="0.0.1",
  author="Amadeus9029",
  author_email="965720890@qq.com",
  description="An image local detail shower",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Amadeus9029/localshower",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)