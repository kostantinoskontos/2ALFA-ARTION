from setuptools import find_packages
from setuptools import setup


setup(
    name="2ALFA-ARTION",
    version="1.0.0",
    description="The basic blog app built in the Flask tutorial.",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)