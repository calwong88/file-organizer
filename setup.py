from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file-organizer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python tool to automatically organize files by type",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/file-organizer",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/file-organizer/issues",
        "Source Code": "https://github.com/yourusername/file-organizer",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Filesystems",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    py_modules=["file_organizer_1_0"],
    python_requires=">=3.6",
    install_requires=[
        # No external dependencies - uses only standard library
    ],
    entry_points={
        "console_scripts": [
            "file-organizer=file_organizer_1_0:main",
        ],
    },
)
