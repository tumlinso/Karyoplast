"""Smoke tests for the initial importable package skeleton."""

import unittest

import karyoplast


class PackageSmokeTests(unittest.TestCase):
    def test_package_imports_with_expected_identity(self) -> None:
        self.assertEqual(karyoplast.__name__, "karyoplast")
        self.assertEqual(karyoplast.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
