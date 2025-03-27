## 0.3.0 (March 27, 2025)
- Project configuration using the toml file.

## 0.2.3 (March 26, 2025)
- Added __fspath__ method to make path class os.PathLike.

## 0.2.2 (October 1, 2024)
- Added missing dependencies to setup config.

## 0.2.1 (September 29, 2024)
- Allow empty course string.
- File fetched automatically from PAX if it doesn't exists locally.
- Path class automatically imported into paxutils namespace.
- Added __repr__ method.

## 0.2.0 (September 9, 2024)
- New implementation based on delegation instead of inheritance, which is a much cleaner approach given the messy implementation of pathlib. (the previous version did not work with Python 3.12)

## 0.1.1 (September 8, 2024)
- Rebuild of 0.1.0.

## 0.1.0 (August 23, 2023)

- Fixed issue with methods that return a new path without calling the new operator (e.g. absolute).
- Removed fetch_from_pax method.
