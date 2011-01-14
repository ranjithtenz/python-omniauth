from omniauth.provider.twitter import Twitter

def main():
    twitter = Twitter()
    print twitter.config('Oi!')

if __name__ == '__main__':
    main()
