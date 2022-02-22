def sayLove():
    print('上邪，我欲与君相知，长命无绝衰。山无陵，江水为竭。冬雷震震，夏雨雪。天地合，乃敢与君绝。')


sayLove()
sayLove.__call__()


class SayLove:
    def __init__(self, content):
        self.content = content

    def __call__(self, name):
        print(name + self.content)


t = SayLove(", I love you.")
t('Ning')
