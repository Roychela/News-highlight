import unittest
class NewsSourceTest(unittest.TestCase):
    '''
    Test case to test the behavior of the NewsSource class
    '''
    def setUp(self):
        '''
        Setup function that will run before every test
        '''
        self.new_source = NewsSource('xyznews','Todays bulletin','Breaking news','https://tomorrowtoday.com','general','gb')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))

    def test_to_check_instance_variables(self):
        '''
        Test function to check instance variables
        '''
        self.assertEquals(self.new_source.id,'xyznews')
        self.assertEquals(self.new_source.name,'Todays bulletin')
        self.assertEquals(self.new_source.description,'Breaking News')
        self.assertEquals(self.new_source.url,'https://tomorrowtoday.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'gb')
