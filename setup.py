from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirements_file:
    requirements = list(map(lambda line: line.strip(), requirements_file.readlines()))
    requirements = list(filter(lambda line: (not line.startswith("#")) and len(line) > 0, requirements))

setup(name="libquantum",
      version="1.1.2",
      url='https://github.com/RedVoxInc/libquantum',
      license='Apache',
      author='RedVox',
      author_email='dev@redvoxsound.com',
      description='Library for implementing standardized time-frequency representations.',
      packages=find_packages(include=[
          "libquantum",
          "libquantum.plot_templates",
      ],
          exclude=['tests']),
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      install_requires=requirements,
      python_requires=">=3.6, <3.9")
