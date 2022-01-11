from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="py-project",
    version="0.0.1",
    author="Khalid Saifullah",
    author_email="khalid@outlook.com.au",
    description="A small example package",
    entry_points={
        "console_scripts": [
            "task_a=package_a.main:main",
            "task_b=package_b.main:main",
        ],
    },
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brainstation-au/py-project",
    project_urls={
        "Bug Tracker": "https://github.com/brainstation-au/py-project/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
)
