from setuptools import setup
from glob import glob
import os

package_name = "cube_petit_web_console"

def list_files_recursive(base_dir):
    paths = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            src = os.path.join(root, f)
            dst = os.path.join("share", package_name, root)
            paths.append((dst, [src]))
    return paths

data_files = [
    ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
    ("share/" + package_name, ["package.xml"]),
    (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
]

data_files += list_files_recursive("web_app")

setup(
    name=package_name,
    version="0.0.1",
    packages=[package_name],
    data_files=data_files,
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Airi Yokochi",
    maintainer_email="airi.yokochi@g.softbank.co.jp",
    description="Cube petit web console (Next.js + ROS bridge)",
    license="Apache-2.0",
)
