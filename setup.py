from skbuild import setup

setup(
    name="eigen",
    version="3.3.8",
    description="Eigen3 C++ template library for linear algebra",
    author="Eigen3 team",
    license="MPL2",
    package_dir={"eigen": "src"},
    packages=["eigen"],
)
