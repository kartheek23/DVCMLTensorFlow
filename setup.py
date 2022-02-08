from setuptools import setup

with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="KartheekChalla",
    description="A small package for DVC with Tensorflow",
    long_description=long_description,
    url="https://github.com/kartheek23/DVCMLTensorFlow.git",
    author_email="challakartheek@gmail.com",
    packages=["src"],
    install_requires=[
         "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "PyYAML",
        "boto3" ,
    ]


)