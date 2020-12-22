import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plantParent",  # Replace with your own username
    version="0.1.1",
    author="Aryn Davis",
    author_email="arynlynn1@gmail.com",
    description="plantParent is a tool to help you keep track of relevant care instructions for various plants by using HuggingFace's Bert Question and Answering Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryndavis/plantParent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
