import unittest
from app import count_commits
from app2 import calc_project_commits

class TestProjectCommitsMethod(unittest.TestCase):

    # testing functioning repo
    def test_calc_project_commits(self):
        self.assertEqual(calc_project_commits('https://github.com/alimgee/mollyrose--in-react', 50), 1)
    
    # testing missing repo
    def test_calc_project_commits_no_repo(self):
        self.assertEqual(calc_project_commits('https://github.com/alimgee/', 50), 0)
    
    # testing invalid repo
    def test_calc_project_commits_invalid_repo(self):
        self.assertEqual(calc_project_commits('https://github.com/alimgee/rrrrrrrrrr', 50), 0)
    
    # testing invalid user
    def test_calc_project_commits_invalid_user(self):
        self.assertEqual(calc_project_commits('https://github.com/alimgeee/', 50), 0)




class TestCommitCountMethod(unittest.TestCase):

    # testing functioning repo
    def test_correct_count(self):
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
