import vk_api
from vk_api import utils
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from bs4 import BeautifulSoup as bs
import requests

token = 'e911efb87d78dcc242a4a564de61a3dd61c91a6cb308e64aed9e1594f6991a191732daa7c4b15756aa582'
vk_session = vk_api.VkApi(token=token)
longpoll=VkBotLongPoll(vk_session, 207468617)

def send_msg(id, message):
    vk_session.method('messages.send', {'chat_id': id, 'message': message, 'random_id':0 })
def send_msg_user(id,message):
    vk_session.method('messages.send', {'user_id': id, 'message': message, 'random_id': 0})
def cmd(text):
    print(f'[INFO]  cmd - {text}')
    text=text[1::]

    opg=['Хозяин','Тефтеля','Чорт','Арматура','Алкаш','Правильный','Илюша','Нигорь','Кобан', 'Фрыц']

    opg_list_in=['3','опг','ОПГ','всё опг', 'список опг', 'список банды', 'вся банда', 'все мы','наш список', 'список нас', 'Всё опг', 'Список опг', 'Список банды', 'Вся банда', 'Все мы','Наш список', 'Список нас', 'Список','список']
    opg_list_out='1 -- Хозяин\n2 -- Тефтеля\n3 -- Чорт\n4 -- Арматура\n5 -- Алкаш\n6 -- Правильный\n7 -- Илюша\n8 -- Нигорь\n9 -- Кобан\n10 -- Фрыц'

    go_out_in=['2','ебани кого-нибудь','Ебани кого-нибудь','Ебани кого-нибудь','ебни кого-нибудь','кто идет нахуй?','пошли кого-нибудь','Пошли кого-нибудь','Пошли кого-нибудь нахуй','пошли кого-нибудь']

    fun_in = ['1','Анекдот', 'анекдот','Ебашь анекдот','Ебани анекдот','Пошути','Давай анекдот','Рассмеши меня','Хочу анекдот','Дай анекдот']

    help_in=['help','cmd','помощь','Помощь', 'Команды', 'команды']

    if text in opg_list_in:
        return opg_list_out

    elif text in go_out_in:
        name= random.choice(opg)
        msg=random.choice([f'{name}, пошёл нахуй', f'Нахуй идеееетт...\n\n\n\n\n{name}', f'Вот ты нахуй и пойдешь, быдло ебучее', f'Давайте дружно пошлем нахуй человека по имени "{name}"'])
        return msg

    elif text in fun_in:
        HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            'accept': '*/*'}
        r=requests.get('https://www.anekdot.ru/random/anekdot/',headers=HEADERS)
        soup=bs(r.text,'html.parser')
        joke=soup.find('div', class_='text').text
        return joke
    elif text in help_in:
        msg='Вот список моих комманд:\n1) Анекдот\n2) Послать кого-нибудь нахуй\n3) Список опг\n4) roll [от 1 до 100]'
        return msg
    elif text=='roll' or text=='4':
        return random.randint(1,101)
    else:
        return 'Я не ебу что ты высрал.\nМой создатель - уебан, а потому и я такой же тупой'


print(longpoll.listen())
for event in longpoll.listen():
    print(event)
    # Если пришло новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW :
        txt=event.object.message['text']
        if event.from_chat:
            if txt[0]=='/':
                send_msg(  # Отправляем собщение
                id=event.chat_id,
                message=cmd(event.object.message['text'])
                )
            else:
                print(event.object.message['text'])
        elif event.from_user:
            if txt[0]=='/':
                send_msg_user(  # Отправляем собщение
                    id = event.object.message['from_id'],
                    message=cmd(event.object.message['text'])
                )
            else:
                print(event.object.message['text'])
