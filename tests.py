import unittest
from app import count_commits


class TestCommitCountMethod(unittest.TestCase):

    # testing functioning repo
    def test_correctcount(self):
        self.assertEqual(count_commits('alimgee', 350), 126)

    # testing empty repo with no commits
    def test_no_commits(self):
        self.assertEqual(count_commits('test-user-user', 365), 0)
    
     # testing invalid username
    def test_invalid_user(self):
        self.assertEqual(count_commits('abcdefg123r', 365), 0)
    
     # testing days parameter is passed correctly
    def test_invalid_date_value(self):
        self.assertEqual(count_commits('alimgee', 'amg'), 0)
    
     # testing days parameter is greater than 0
    def test_date_value_less_than_1(self):
        self.assertEqual(count_commits('alimgee', 0), 0)

if __name__ == '__main__':
    unittest.main()
