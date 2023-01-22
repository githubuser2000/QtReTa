#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="QtReTa",
    version="0.5.0",
    description="reta as one website GUI",
    author="Jupiter 3.0 alias trace",
    packages=find_packages(include=["main.py"]),
    install_requires=[
        "PySide6",
        "zstd",
    ],
    package_data={
        ".": [
            "*.txt",
            "*.sh",
            "*.qm",
            "*.png",
            "*.ts",
            "*.json",
            "*.ui",
            "*.spec",
            "*.qml",
            "*.cfg",
        ]
    },
)
