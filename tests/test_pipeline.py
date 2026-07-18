import unittest

from scripts.check_availability import resolve_status


class AvailabilityStatusTests(unittest.TestCase):
    def test_first_failure_is_unknown(self):
        self.assertEqual(resolve_status(False, {"failure_count": 0}), ("unknown", 1))

    def test_second_failure_is_dead(self):
        self.assertEqual(resolve_status(False, {"failure_count": 1}), ("dead", 2))

    def test_success_clears_failure_count(self):
        self.assertEqual(resolve_status(True, {"failure_count": 4}), ("active", 0))


if __name__ == "__main__":
    unittest.main()
