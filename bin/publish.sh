rm -rf build
rm -rf dist
rm -rf gslocalizator.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*