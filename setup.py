import setuptools

with open('README.md', "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "ML-Project-With-ML-Flow"
AUTHOR_USER_NAME = "Sujeet2003"
SRC_REPO = "MLProject"
AUTHOR_EMAIL = "sujeetsmpatel@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An End-to-End Python Project Using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"), 
)