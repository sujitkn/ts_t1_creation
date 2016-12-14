# ts_t1_creation

Installation and Dependencies:

git clone git@github.com:sujitkn/ts_t1_creation.git
 
 
# In your virtual envrionment use pip to install python packages listed in the requirements.txt file by entering the following command in your shell:

virtualenv venv


. ./venv/bin/activate


pip install -r requirements.txt --extra-index-url 'https://pi.mediamath.com:9002/simple/'


Running the tests is straightforward with nosetest. For example, I can run tests in this repo by entering the following command in my shell:


nosetests -v tests/test_t1_creation.py

Adding Tests


To add a test, simply create a module with all desired test functions in it. Place this file in the tests directory for auto-detection by nosetest.
	
	# saved in tests/test_t1_creation.py

	def test_generate_campaign():
	    """This demonstrates a sample test function for your test case purposes"""
	    import terminalone
    	    t1 = terminalone.T1(user_name, pass_word, api_key=api_key, api_base=api_url, auth_method="cookie" )
    	    campaign=generate_campaign(generate_advertiser, t1)
	    assert 1 == 1


Page Objects

The page objects would normally contain the implementation logic for interactions with test.

Let's go ahead and create a pages directory and place page file in it,, call it ts_t1_creation.py

	
	def generate_campaign(generate_advertiser, api):
    """
    Creates a campaign if one doesn't already exist via api
    """
    advertiser = generate_advertiser
    try:
        campaign = list(api.find("campaign", "name", "==", "Test Bulk-Edit-Campaign", full=True))[0]
    except:
        .....
    return campaign
