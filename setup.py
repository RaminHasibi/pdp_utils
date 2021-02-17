

def pkg_setup():

    from setuptools import setup

    setup(name='pdp_utils',
          version='.'.join(map(str, [1, 0, 1])),
          author="Ramin Hasibi",
          author_email="Ramin.Hasibi@uib.no",
          description='Utils needed for solving pickup and delivery problems for course INF273 UiB',
          # url=url,
          # download_url=url,
          include_package_data=True,
          install_requires=['numpy'],
          packages=['pdp_utils'],
          )


if __name__ == '__main__':
    pkg_setup()
