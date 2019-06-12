from distutils.core import setup
setup(
  name = 'pplot',
  packages = ['pplot'],
  version = '0.1',
  license='MIT',
  description = 'Some neat plotting functions for ML',
  author = 'Patrick Schrempf',
  author_email = 'pschrempf@outlook.com',
  url = 'https://github.com/pschrempf/pplot',
  download_url = 'https://github.com/pschrempf/pplot/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['plot', 'machine-learning'],
  install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
          'itertools',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
