from unittest import TestCase


class TestBuild(TestCase):
    def test_check_whether_number_or_target_cannot_be_null(self):
        try:
            from build import two_sum
        except ImportError:
            self.assertFalse("Import Failure")

        self.assertRaises(TypeError, two_sum, None, None)
        self.assertRaises(ValueError, two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(two_sum(nums, target), expected)