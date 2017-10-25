from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UserForm, LoginForm
from django.views import View
from django.contrib.auth import login, authenticate
import oauth2 as oauth
import cgi
from Network import settings
from .models import User
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy,json
global arrtwt
import sys
arrtwt = []
class listener(StreamListener):
    def __init__(self, api=None):
        super(listener, self).__init__()
        self.num_tweets = 0
        self.tweets = []
    def on_data(self, data):

        all_data = json.loads(data)
        tweetext = all_data.get('text')
        print(tweetext)
        self.num_tweets += 1
        print(self.num_tweets)
        if self.num_tweets < 20:
            arrtwt.append(tweetext)
        if(self.num_tweets >= 20):
            #return tweetext
            print("ohno")


        #print(all_data)
        #return(tweetext)

    def on_error(self, status):
        print(status)

class Home(View):
    def get(self, request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        form = UserForm(request.POST)
        return render(request, 'index.html', {'form' : form})

    def post(self, request):
        form = UserForm(request.POST)
        error = 0
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #print(request.POST.data)
            return redirect('/')
        else:
            error = 1
            #form = UserForm()

        return render(request, 'index.html', {'form': form, 'error': error})

class LogIn(View):
    def get(self,request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            try:
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return render(request, 'dashboard.html')
            except:
                pass

        return render(request, 'login.html', {'form': form, 'error': "Invalid Username & Password!"})

class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated():
            name = (request.user)
            return render(request, 'dashboard.html', {'username' : name})
        else:
            return redirect('/login/')

    #deal with ajax request submission for facebook/twitter
    def post(self, request):
        data = {'result': 'Okay'}
        return JsonResponse(data)

class TwitterLogIn(View):
    def get(self,request):
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        authenticate_url = 'https://api.twitter.com/oauth/authenticate'
        consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
        client = oauth.Client(consumer)

        resp, content = client.request(request_token_url, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response from Twitter.")
        #print(content)
    # {b'oauth_token': b'BDtMwQAAAAAA2TwPAAABXpFY5J0', b'oauth_token_secret': b'LZQn9dZbHkC2bhqEMvSBfw6mE8ay2fZX', b'oauth_callback_confirmed': b'true'}
    # Step 2. Store the request token in a session for later use.
        cont = dict(cgi.parse_qsl(content))
        #equest.session['request_token'] = dict(cgi.parse_qsl(content))
        oauth_token = str(cont.get(b'oauth_token'))

        #oauth_token_secret = bb.get(b'oauth_token_secret')
        toklen = len(oauth_token)
        oauth_token = oauth_token[2:toklen-1]
        request.session['request_token'] = oauth_token
        #request.session.save()
        #print(oauth_token_secret)
    # Step 3. Redirect the user to the authentication URL.
        url = "%s?oauth_token=%s" % (authenticate_url,
        oauth_token)
        print(url)
        return redirect(url)

class TwitterReg(View):
    def get(self, request):
        print("kek")
        username = (request.user)
        obj = User.objects.get(username=username)
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        token = oauth.Token(request.session['request_token'],request.session['request_token'])
        token.set_verifier(request.GET['oauth_verifier'])
        consumer = oauth.Consumer(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
        client = oauth.Client(consumer, token)
        print("TEST\n\n")
        # Step 2. Request the authorized access token from Twitter.
        resp, content = client.request(access_token_url, "GET")

        #print(request)
        #print(content)
        print("REQUEST: ", request)
        #print("\nCONTENT: ", content)
        arrc = content.decode().split('&')
        print("\n\nCONTENT: ", arrc)
        l = arrc[0].find('=')
        oauth_token = arrc[0][l+1:len(arrc[0])]
        k = arrc[1].find('=')
        oauth_token_secret= arrc[1][k+1:len(arrc[1])]
        obj.TwToken = oauth_token
        obj.SecTwToken = oauth_token_secret
        obj.save()
        #print(request.GET['oauth_verifier'])
        #print(request.session['request_token'])
        #print(request.GET['oauth_token'])
        #print(request.session.items())
        return redirect('/')
class TwitterAuth(View):
    def get(self, request):
        username = (request.user)
        obj = User.objects.get(username=username)
        if(obj.TwToken==''):
            return redirect('/twitter/')
        access_token = obj.TwToken
        access_token_secret = obj.SecTwToken
        auth = tweepy.OAuthHandler(settings.TWITTER_TOKEN, settings.TWITTER_SECRET)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        public_tweets = api.home_timeline(count=40,page=3)
        #print(public_tweets[0].user)

        #twitterStream = Stream(auth, listener())
       # bc = twitterStream.sample(async=False)
        print("REQUEST: ", request)
        #print("\nCONTENT: ", content)
        #print(request.GET['oauth_verifier'])
        #print(request.session['request_token'])
        #print(request.GET['oauth_token'])
        return render(request, 'twitterfeed.html', {'tweets' : public_tweets})
