from decouple import config

HOSTNAME = 'localhost'

SECRET_KEY = ''

DEBUG=True

PLATFORMS = {
    'telegram': {
        'ENGINE': 'bottery.platform.telegram',
        'OPTIONS': {
            'token': config('TELEGRAM_TOKEN'),
        }
    },
}
