from setuptools import find_packages,setup
import setuptools




__version__ = "0.0.0"

REPO_NAME = "Brain-Tumor-Detection-Deep-Learning-Project"
AUTHOR_USER_NAME = "19Shradha"
SRC_REPO = "src"
AUTHOR_EMAIL = "shradhabhat1929@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=[]
)