from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory  / "README.md").read_text()

setuptools.setup(
    name="streamlit-smart-text-input",
    version="1.0.9",
    author="Ankit Guria",
    author_email="ankitguria142@gmail.com",
    description="A Streamlit component that allows you to select from a list of options or enter a custom value.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=["streamlit_smart_text_input"],
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    install_requires=[
        "streamlit >= 1.25",
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.39.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    },
)
