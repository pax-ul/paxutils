## 0.2.0 (September 9, 2024)
- New implementation based on delegation instead of inheritance, which is a much cleaner approach given the messy implementation of pathlib. (the previous version did not work with Python 3.12)

## 0.1.1 (September 8, 2024)
- Rebuild of 0.1.0.

## 0.1.0 (August 23, 2023)

- Fixed issue with methods that return a new path without calling the new operator (e.g. absolute).
- Removed fetch_from_pax method.
