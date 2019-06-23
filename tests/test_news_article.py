import unittest
class TestNewsArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = NewsArticles('Smith','The Singularity','AI will eventually become more intelligent than human life','https://techtoday.com','https://techtoday.com/images','2019-06-21T14:50:05Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticles))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'Smith')
        self.assertEquals(self.new_article.title,'The Singularity')
        self.assertEquals(self.new_article.description,'AI will eventually become more intelligent than human life')
        self.assertEquals(self.new_article.url,'https://techtoday.com')
        self.assertEquals(self.new_article.urlToImage,'https://techtoday.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-06-21T14:50:05Z')