from unittest import TestCase


class TestBuild(TestCase):
    # check whether number or target cannot be null
    # check whether it number only not a string
    # check the value error
    # check_the_value_is_correct_or_not

    def test_check_whether_number_or_target_cannot_be_null(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")
        result = build(None,None)
        self.assertEqual(False,result)

    def test_check_whether_it_number_only_not_a_string(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")

        result = build("",1)
        self.assertEqual(False,result)

    def test_check_value_error(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")
        result = build([0],0)
        self.assertEqual(False,result)

    def test_check_the_value_is_correct_or_not(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import Failure")
        result = build([1,2,3],4)
        self.assertEqual([0,2], result)