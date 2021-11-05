from setuptools import setup

from os import path

def get_long_description():
    with open(
        path.join(path.dirname(path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()
   

def get_requirements(fn='requirements.txt', nogit=True):
   """Get requirements."""
   if path.exists(fn):
      with open(fn, 'r') as f:
        requirements = [r.split()[0].strip() for r in f.read().splitlines() if r and not r.startswith('#')]
   else:
     requirements = []

   if nogit:
       requirements = [r for r in requirements if not 'git+' in r]
   return requirements
   
requirements = get_requirements()

print(f'Requirements: {requirements}')

setup(author='Tony Hirst',
    author_email='tony.hirst@open.ac.uk',
    description='Javascript diagrammers and magics for IPython and Jupyter notebooks',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/innovationOUtside/nb_js_diagrammers',
    version='0.0.1',
    name='nb-js-diagrammers',
    packages=['nb_js_diagrammers'],
    install_requires=requirements
)