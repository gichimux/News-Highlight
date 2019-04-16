import unittest
from app.models import News

class TestNews(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_news_source = News('xyz','gichi','https://xyz.com/','xyz news is the true source', 'usa', 'general', 'xyz-news')
    
    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_news_source,News))
    
    def test_to_check_instance_variables(self):
       
        self.assertEquals(self.new_news_source.name,'xyz')
        self.assertEquals(self.new_news_source.author,'gichi')
        self.assertEquals(self.new_news_source.url,'https://xyz.com/')
        self.assertEquals(self.new_news_source.description,'xyz news is the true source')
        self.assertEquals(self.new_news_source.country,'usa')
        self.assertEquals(self.new_news_source.category,'general')
        self.assertEquals(self.new_news_source.id,'xyz-news')
        