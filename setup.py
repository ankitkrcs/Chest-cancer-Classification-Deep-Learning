import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-cancer-Classification-MlFlow-DVC"
AUTHOR_USER_NAME = "ankitkrcs"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Ankit Maddheshiya",
    author_email="amaddheshiya637@gmail.com",
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{ankitkrcs}/{Chest-cancer-Classification-MlFlow-DVC}",
    project_urls={
        "Bug Tracker": f"https://github.com/{ankitkrcs}/{Chest-cancer-Classification-MlFlow-DVC}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)