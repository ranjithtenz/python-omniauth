from provider import PROVIDER_LIST

class Client():


    def __init__(self, provider, consumer_key, consumer_secret):

        if provider not in PROVIDER_LIST
            raise Exception("You may choose one of these providers: %s" % str(PROVIDER_LIST))

        exec "from provider.%s import *" % provider

        Auth()

        self.provider = provider
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
