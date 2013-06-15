"""
This file contains the unit tests for the :mod:`communication` app.

Since this app has no models there is only view tests:

* :class:`~communication.tests.FeedDetailViewTests` 

"""

from lab_website.tests import BasicTests

class CommunicationViewTests(BasicTests):
    '''This class tests the views associated with the :mod:`communication` app.'''
    
    
    def test_feed_details_view(self):
        """This tests the feed-details view, ensuring that templates are loaded correctly.  

        This view uses a user with superuser permissions so does not test the permission levels for this view."""
        
        test_response = self.client.get('/feeds')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'feed_details.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('google_calendar_id' in test_response.context)          
        
    def test_lab_rules_view(self):
        '''This tests the lab-rules view.
        
        The tests ensure that the correct template is used.
        It also tests whether the correct context is passed (if included).
        his view uses a user with superuser permissions so does not test the permission levels for this view.'''
        
        test_response = self.client.get('/contact/lab-rules')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'lab_rules.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('lab_rules' in test_response.context)    
        self.assertTrue('lab_rules_source' in test_response.context)    
        
    def test_twitter_view(self):
        '''This tests the twitter view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/twitter')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'twitter_timeline.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('timeline' in test_response.context)         
        
    def test_calendar_view(self):
        '''This tests the google-calendar view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/calendar')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'calendar.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('google_calendar_id' in test_response.context)                    
                                
        
    def test_wikipedia_view(self):
        '''This tests the google-calendar view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/wikipedia')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'wikipedia_edits.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('pages' in test_response.context)                                 
                                
    def test_news_view(self):
        '''This tests the lab-news view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/news')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'lab_news.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html') 
        self.assertTrue('statuses' in test_response.context) 
        self.assertTrue('links' in test_response.context)           
        self.assertTrue('milestones' in test_response.context) 
        
    def test_contact_page(self):
        '''This tests the contact-page view.
        
        Currently it just ensures that the template is loading correctly.
        '''
        test_response = self.client.get('/contact/')
        self.assertEqual(test_response.status_code, 200)       
        self.assertTemplateUsed(test_response, 'contact.html')
        self.assertTemplateUsed(test_response, 'base.html') 
        self.assertTemplateUsed(test_response, 'twitter_anywhere_script.html')
        self.assertTemplateUsed(test_response, 'jquery_script.html')                                           