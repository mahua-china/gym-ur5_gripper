from setuptools import setup, find_packages

setup(
    name='gym_ur5_gripper',
    version='0.1',
    packages=find_packages(include=['gym_ur5_gripper', 'gym_ur5_gripper.*']),
    install_requires=[
        'gym',
        'pybullet',
        'numpy',
    ],
)
