from setuptools import find_packages, setup

setup(
    name="milkstraw-client",
    version="0.0.1",
    description="",
    url="https://github.com/milkstrawai/milkstraw-python-client",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.9",
    install_requires=["requests==2.30.0"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
