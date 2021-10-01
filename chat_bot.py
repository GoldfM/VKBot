import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from bs4 import BeautifulSoup as bs
import requests

token = 'e911efb87d78dcc242a4a564de61a3dd61c91a6cb308e64aed9e1594f6991a191732daa7c4b15756aa582'
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 207468617)
hent_urls = {}

def send_msg(id, message):
    vk_session.method('messages.send', {'chat_id': id, 'message': message, 'random_id':0 })
def send_msg_user(id, message):
    vk_session.method('messages.send', {'user_id': id, 'message': message, 'random_id': 0})
def cmd(text, id, from_):
    global hent_urls, vk_session
    #print(f'[INFO]  cmd - {text}')
    text=text[1::]

    opg=['Хозяин','Тефтеля','Чорт','Арматура','Алкаш','Правильный','Илюша','Нигорь','Кобан', 'Фрыц']

    opg_list_in=['3','опг','ОПГ','всё опг', 'список опг', 'список банды', 'вся банда', 'все мы','наш список', 'список нас', 'Всё опг', 'Список опг', 'Список банды', 'Вся банда', 'Все мы','Наш список', 'Список нас', 'Список','список']
    opg_list_out='1 -- Хозяин\n2 -- Тефтеля\n3 -- Чорт\n4 -- Арматура\n5 -- Алкаш\n6 -- Правильный\n7 -- Илюша\n8 -- Нигорь\n9 -- Кобан\n10 -- Фрыц'

    go_out_in=['2','ебани кого-нибудь','Ебани кого-нибудь','Ебани кого-нибудь','ебни кого-нибудь','кто идет нахуй?','пошли кого-нибудь','Пошли кого-нибудь','Пошли кого-нибудь нахуй','пошли кого-нибудь', 'Пошли нахуй','пошли нахуй']

    fun_in = ['1','Анекдот', 'анекдот','Ебашь анекдот','Ебани анекдот','Пошути','Давай анекдот','Рассмеши меня','Хочу анекдот','Дай анекдот']

    help_in=['help','cmd','помощь','Помощь', 'Команды', 'команды']

    hentai_in=['ХЕНТАЙ','хентай','Хентай','Аниме','5']

    lottery=[]
    game=[]
    #СПИСОК
    if text in opg_list_in:
        return opg_list_out
    #ПОСЛАТЬ КОГО-НИБУДЬ
    elif text in go_out_in:
        name= random.choice(opg)
        msg=random.choice([f'{name}, пошёл нахуй', f'Нахуй идеееетт...\n\n\n\n\n{name}', f'Вот ты нахуй и пойдешь, быдло ебучее', f'Давайте дружно пошлем нахуй человека по имени "{name}"',f'Обращаюсь к существу "{name}", пошёл ты нахуй'])
        return msg
    #АНЕКДОТ
    elif text in fun_in:
        try:
            HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'accept': '*/*'}
            r=requests.get('https://www.anekdot.ru/random/anekdot/',headers=HEADERS)
            soup=bs(r.text,'html.parser')
            joke=soup.find('div', class_='text').text
        except:
            joke='Сайт с анекдотами накрылся'
        return joke
    #ПОМОЩЬ
    elif text in help_in:
        msg='Вот список моих комманд:\n1) Анекдот\n2) Послать кого-нибудь нахуй\n3) Список опг\n4) roll [от 1 до 100]\n5) Хентай (может появиться сюрприз' \
            ')'
        return msg
    #ROLL
    elif text=='roll' or text=='4':
        return random.randint(1,101)
    #HENTAI
    elif text in hentai_in:
        i=random.randint(1,399)
        a = vk_session.method("photos.getMessagesUploadServer")
        b = requests.post(a['upload_url'], files={'photo': open(f'D:/Проект/{i}.jpg', 'rb')}).json()
        c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = "photo{}_{}".format(c["owner_id"], c["id"])
        if from_=='chat':
            vk_session.method("messages.send", {"chat_id": id, "attachment": d, "random_id": 0})
        else:vk_session.method("messages.send", {"peer_id": id, "attachment": d, "random_id": 0})

        return None

    elif 'Пошел нахуй' in text or 'пошел нахуй' in text or 'Пошёл нахуй' in text or 'пошёл нахуй' in text:
        msgs=['Мать твоя нахуй пойдет', 'Ебало офнул, ублюдок', 'Я ща мегатрона позову', 'Еще слова и я тебя разъебу, хоть я и железное корыто','Ты это мне, уебок?','ХПАХПАХПАХПАХХПА БЛЯЯЯЯЯ\nТы хули тут пиздишь, петух, утро еще не скоро', 'Попизди тут', 'Чел, ты понимаешь с кем тут пиздишь?\nНе твой уровень дорогуша', 'Берега попутал чепушило?','Хватит меня булить, ебучие кожаные мешки']
        return random.choice(msgs)

    elif 'ФРЫЦ' in text or 'Фрыц' in text or 'фрыц' in text or 'ФРИЦ' in text or 'Фриц' in text or 'фриц' in text or 'Нацисткая Германия' in text or 'Нацисткая германия' in text or 'нацисткая Германия' in text or 'нацисткая германия' in text:
        msgs = ['Батю не трогай','За батько я и взломать могу', 'Не трожь отца', 'Еще слово в сторону моего отца - я тебя заКИБЕРбулю, сука','Фрыца не трогай','Я зову своего брата']
        return random.choice(msgs)

    elif 'Клоун' in text or 'клоун' in text or 'Долбаеб' in text or 'долбаеб' in text or 'Долбаёб' in text or 'долбаёб' in text or 'Еблан' in text or 'еблан' in text or 'Мудак' in text or 'мудак' in text or 'Сука' in text or 'сука' in text or 'Железка' in text or 'железка' in text or 'Даун' in text or 'даун' in text or 'Мразь' in text or 'мразь' in text or 'Пидр' in text or 'пидр' in text:
        msgs = ['Ты чо ахуел?', 'Кто как обзывается, тот сам так называется\nПонял, долбаеб?','Боже, закрой рыло', 'Похрюкай мне тут', 'Мальчик, иди спать','Еще слово - вынесу с ноги']
        return random.choice(msgs)



    #ИГРА
    elif text in game:
        #создать БД с уровнем, валютой, очками
        #адаптировать под любую беседу с чтением участников
        pass




    else:
        return 'Я не ебу что ты высрал.\nМой создатель - конченый уебан, а потому и я такой же тупой'

for event in longpoll.listen():
    try: print(f'[MESSAGE]{event.object.message["from_id"]} - {event.object.message["text"]}\n')
    except: pass
    # Если пришло новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW :
        txt=event.object.message['text']
        if event.from_chat :
            try:
                if txt[0]=='/':
                    message=cmd(event.object.message['text'],event.chat_id, 'chat')
                    #print(type(message))
                    if message != None:
                        send_msg(  # Отправляем собщение
                        id=event.chat_id,
                        message=message,
                        )
                else:
                    pass
            except:
                pass
        elif event.from_user:
            try:
                if txt[0]=='/':
                    message=cmd(event.object.message['text'],event.object.message['from_id'],'user')
                    #print(type(message))
                    if message != None:
                        send_msg_user(  # Отправляем собщение
                            id = event.object.message['from_id'],
                            message=message,
                        )
                else:
                    pass
            except:
                pass
