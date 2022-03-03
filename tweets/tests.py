from django.contrib.auth.models import User
from django.test import TestCase
from tweets.models import Tweet
from datetime import timedelta
from utils.time_helpers import utc_now

# Create your tests here.

class TweetTest(TestCase):

    def test_hours_to_now(self):
        jim = User.objects.create_user(username='jim')
        tweet = Tweet.objects.create(user=jim, content='Jim always have great ideas!')
        tweet.created_at = utc_now() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_to_now, 10)