import unittest
from app import count_commits


class TestCommitCountMethod(unittest.TestCase):

    # testing functioning repo
    def test_correctcount(self):
        self.assertEqual(count_commits('alimgee', 350), 126)

    # testing empty repo with no commits
    def test_no_commits(self):
        self.assertEqual(count_commits('test-user-user', 365), 0)


if __name__ == '__main__':
    unittest.main()
