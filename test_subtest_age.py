import unittest

def get_category(age):
    if 0 <= age <= 9:
        return "is_child"
    elif 10 <= age <= 19:
        return "is_teen"
    elif age >= 20:
        return "is_adult"
    return None

class TestAgeCategories(unittest.TestCase):

    def test_child_age(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(get_category(age), "is_child")

    def test_teen_age(self):
        for age in range(10, 20):
            with self.subTest(age=age):
                print(f"{age} is considered as a teen.")
                self.assertEqual(get_category(age), "is_teen")

    def test_adult_age(self):
        for age in range(20, 26):
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(get_category(age), "is_adult")

if __name__ == '__main__':
    unittest.main()