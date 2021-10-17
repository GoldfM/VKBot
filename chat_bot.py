import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from bs4 import BeautifulSoup as bs
import requests
import re
from translate import Translator


token = 'e911efb87d78dcc242a4a564de61a3dd61c91a6cb308e64aed9e1594f6991a191732daa7c4b15756aa582'
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 207468617)
check=0
def send_msg(id, message):
    global vk_session
    vk_session.method('messages.send', {'chat_id': id, 'message': message, 'random_id':0 })
def send_msg_user(id, message):
    vk_session.method('messages.send', {'user_id': id, 'message': message, 'random_id': 0})
def cmd(text, id, from_, peer_id=0):
    global vk_session, check
    text = text[1::]
    text = str(text).lower()

    with open('D:/VKBot/opg_list.txt','r') as f:
        opg=f.read().split(';')


    opg_list_in = ['3','опг', 'список опг', 'список банды']

    fun_in = ['1','анекдот', 'ебашь анекдот','ебани анекдот','пошути','давай анекдот','рассмеши меня','хочу анекдот','дай анекдот']

    help_in = ['help','cmd','помощь', 'команды']

    hentai_in = ['хентай','аниме','5']

    angela_in = ['6', 'angela', 'анжела', 'анджела']

    angry_words = '(?:{})'.format('|'.join(['лох','еблан','мудак','долбаеб','гандон','хуесос','мудак','мразь','еблан','хуйло','говноед','железяка','чмо','пидор','пидр','гей','уебище','гондон','клоун','дебил','идиот','даун','придурок','дурак','сука']))

    happy_words = '(?:{})'.format('|'.join(['молодец', 'красавчик', 'красавец', 'умница', 'хорош', 'крутой', 'лучший', 'красава']))

    hello = '(?:{})'.format('|'.join(['привет', 'сау', 'салям алейкум', 'дарова','здравствуй','салам','вечер в хату','здарова','прив']))

    silence = '(?:{})'.format('|'.join(['успокоить', '7', 'успокой']))

    name_bot = '(?:{})'.format('|'.join(['меха-фриц','бот', 'машина','железяка', 'робот', 'автобот', 'десяктикон']))
    

    goroskop = ['9', 'гороскоп']

    split_text=text.split()

    #СПИСОК
    if split_text[0] in opg_list_in:
        try:
            num=int(split_text[1])
            name = split_text[2].capitalize()
            opg[num-1]=str(name)
            if event.object.message["from_id"] == 245210027 or event.object.message["from_id"] == 260245693:
                with open('D:/VKBot/opg_list.txt', 'w') as f:
                    f.write(';'.join(opg))
                    f'1 -- {opg[0]}\n2 -- {opg[1]}\n3 -- {opg[2]}\n4 -- {opg[3]}\n5 -- {opg[4]}\n6 -- {opg[5]}\n7 -- {opg[6]}\n8 -- {opg[7]}\n9 -- {opg[8]}\n10 -- {opg[9]}'
            else:return 'Подожди открой список миох пап... Так, тебя там нет => не указывай мне'
        except: 
            return f'1 -- {opg[0]}\n2 -- {opg[1]}\n3 -- {opg[2]}\n4 -- {opg[3]}\n5 -- {opg[4]}\n6 -- {opg[5]}\n7 -- {opg[6]}\n8 -- {opg[7]}\n9 -- {opg[8]}\n10 -- {opg[9]}'

    #ПОСЛАТЬ КОГО-НИБУДЬ
    elif split_text[0] == '2' or split_text[0] == 'нахуй':
        print(text.split().count)
        try:
            name = split_text[1]
        except:
            name = random.choice(opg)
        name=name.capitalize()
        msg = random.choice([f'{name}, пошёл нахуй', f'Нахуй идеееетт...\n.\n.\n.\n.\n{name}', f'Вот ты нахуй и пойдешь, быдло ебучее', f'Давайте дружно пошлем нахуй человека по имени "{name}"',f'Обращаюсь к существу "{name}", пошёл ты нахуй'])
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
        msg = 'Вот список моих комманд:\n1) Анекдот\n2) Послать кого-нибудь нахуй (можно добавить имя в И.П.)\n3) Список опг\n4) roll [от 1 до 100], можно добавить "дота", "опг", "мать"\n5) Хентай (может появиться сюрприз)\n6) Вспомнить Анжелу\n7) Успокоить + "введите имя в И.П."\n8) Зихте дрихте, переводчик на Немецкий\n9) Гороскоп (введите /9 и свой знак зодиака)'
        return msg
    #ROLL

    elif text=='random chat':
        all = vk_session.method('messages.getConversationMembers', {'peer_id': peer_id})['profiles']
        name = random.choice(all)
        msg = f'https://vk.com/{name["screen_name"]}'


        return msg

    elif text == 'roll' or text == '4':
        return random.randint(1,101)

    elif text == 'roll opg' or text == 'roll опг' or text == '4 opg' or text == '4 опг':
        name = random.choice(opg)
        return name

    elif text == 'roll dota' or text == '4 dota' or text == 'roll дота' or text == '4 дота':
        roles = ['Лесничок', 'Керри', 'Саппорт', 'Мидер', 'Пудж', 'Четверочка', 'Харда']
        role = random.choice(roles)
        return role

    elif text == 'roll mother' or text == 'roll мать' or text == 'roll мама' or text == 'roll маму':
        kot_name=random.choice(["KotAFF'а", "Котова","Белоруса", "КотОФФа"])
        moms = [f"Поздравляем, вы получаете мать {kot_name}",f"Матушка {kot_name} отныне принадлежит вам",f"Мать {kot_name} теперь ваша",f"Мать {kot_name} достаётся вам", f'Котов передает свою мать вам' ]
        mom = random.choice(moms)
        return mom

    #Успокоить
    elif bool(re.search(silence, text, flags=re.I)):
        try: name=split_text[1].capitalize()
        except: name=''
        msgs=[f'{name} Успокойся нахуй', f'{name}, Успокойся пожалуйста. пук-пук',f'Остановись {name}, чего ты добиваешься?','Тише.. Тише..', 'Полегче, брат',f'{name} Приди в себя','Чумба, не наводи суеты']
        return random.choice(msgs)
    #Вкл
    elif text=='go' and (event.object.message["from_id"] == 245210027 or event.object.message["from_id"] == 260245693):
        hi = 'Hello World', 'АУЕ','Сау, братья','Вечер в хату'
        check = 1
        return random.choice(hi)
    #ВЫКЛ
    elif text == 'спать' or text =='off' :
        if event.object.message["from_id"] == 245210027 or event.object.message["from_id"] == 260245693:
            msg = 'Выключаюсь, папуля. Всем спокойной ночи <3\n@id273782101 (Тимофей)  Удачи, на соревах!'
            check = 2
        else:
            msg = 'Ты не мой папа, и даже не второй папа.\nТак что ты мне тут блять не указывай'
        return msg
    #Анжела
    elif text in angela_in:
        i = random.randint(1,16)
        a = vk_session.method("photos.getMessagesUploadServer")
        b = requests.post(a['upload_url'], files={'photo': open(f'D:/VKBot/AngelA/{i}.jpg', 'rb')}).json()
        c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = "photo{}_{}".format(c["owner_id"], c["id"])
        if from_=='chat':
            vk_session.method("messages.send", {"chat_id": id, "attachment": d, "random_id": 0})
        else:vk_session.method("messages.send", {"peer_id": id, "attachment": d, "random_id": 0})
        return None

    #HENTAI
    elif text in hentai_in:
        i = random.randint(1,399)
        a = vk_session.method("photos.getMessagesUploadServer")
        b = requests.post(a['upload_url'], files={'photo': open(f'D:/VKBot/Hent/{i}.jpg', 'rb')}).json()
        c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
        d = "photo{}_{}".format(c["owner_id"], c["id"])
        if from_=='chat':
            vk_session.method("messages.send", {"chat_id": id, "attachment": d, "random_id": 0})
        else:vk_session.method("messages.send", {"peer_id": id, "attachment": d, "random_id": 0})
        return None

    elif split_text[0]=='8' or split_text[0]=='переведи':
        print('Translator')
        translator = Translator(from_lang="ru", to_lang='german')
        translation = translator.translate(' '.join(text.split()[1:]))
        return translation

    elif split_text[0] in goroskop:
        try:
            znak=split_text[1]
            znak_tuple={'овен':'aries', 'телец':'taurus', 'близнецы':'gemini','рак':'cancer','лев':'leo','дева':'virgo', 'весы': 'libra','скорпион':'scorpio', 'стрелец':'sagittarius','козерог':'capricorn','водолей':'aquarius','рыбы':'pisces'}
            try:
                url=f'https://1001goroskop.ru/?znak={znak_tuple[znak]}'
                HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36','accept': '*/*'}
                r=requests.get(url,headers=HEADERS)
                soup=bs(r.text,'html.parser')
                gorsk=soup.find('table', {'id':'eje_text'}).find('p', class_='').text
                return gorsk
            except: return 'Или такого знака нет, или упал сайт с гороскопом, или я трахнул ваш компьютер вчера'

        except: return 'Введи знак зодиака'


    #ПОДДЕРЖАНИЕ ДИАЛОГА


    elif bool(re.search(name_bot, text, flags=re.I)):
        return 'Я не знаю что ты там про меня написал, но не дай Бог там что-то обидное - я сука позову мегатрона и он тебе начистит жопу.\nЕсли же там комплимент, то спасибо🙃'

    elif 'пошел нахуй' in text or 'пошёл нахуй' in text or 'иди нахуй' in text:
        msgs = ['Мать твоя нахуй пойдет', 'Ебало офнул, ублюдок', 'Я ща мегатрона позову', 'Еще слова и я тебя разъебу, хоть я и железное корыто','Ты это мне, уебок?','ХПАХПАХПАХПАХХПА БЛЯЯЯЯЯ\nТы хули тут пиздишь, петух, утро еще не скоро', 'Попизди тут', 'Чел, ты понимаешь с кем тут пиздишь?\nНе твой уровень дорогуша', 'Берега попутал чепушило?','Хватит меня булить, ебучие кожаные мешки']
        return random.choice(msgs)

    elif bool(re.search(happy_words, text, flags=re.I)):
        msgs=['Спасибо, зай', 'И я тебя люблю', 'Чмок','Приподнял и обнял', 'Ты тоже', 'Благодарю','Служу Нацисткой Германии','Ещё бы']
        return random.choice(msgs)

    elif 'фрыц' in text or 'фриц' in text or 'нацист' in text or 'германия' in text:
        msgs = ['Батю не трогай','За батько я и взломать могу', 'Не трожь папу', 'Еще слово в сторону моего отца - я тебя заКИБЕРбулю, сука','Фрыца не трогай','Я зову своего брата']
        return random.choice(msgs)

    elif 'илья' in text or 'илюша' in text or 'али-баба' in text or 'алибаба' in text or 'ильич' in text or 'илью' in text:
        msgs = ['Батю №2 не трогай','За второго батько я и взломать могу', 'Не трожь отца V2.0', 'Еще слово в сторону моих отцов - я тебя заКИБЕРбулю, сука','Али-бабу не трогай','Я зову своего брата']
        return random.choice(msgs)

    elif bool(re.search(angry_words, text, flags=re.I)):
        msgs = ['Ты чо ахуел?', 'Кто как обзывается, тот сам так называется\nПонял, долбаеб?','Боже, закрой рыло', 'Похрюкай мне тут', 'Мальчик, иди спать','Еще слово - вынесу с ноги','Ебальник офни']
        return random.choice(msgs)

    elif bool(re.search(hello, text, flags=re.I)):
        msgs = ['Привет, бртаик','Батик кун, ОХАЁ', 'UwU','Дарова. Че как житуха?', 'Сааауу братан', 'Жизнь ворам хуй мусорам', 'Приветствую', 'Здарово заебал']
        return random.choice(msgs)

    elif 'раз на раз' in text or 'выйдем' in text or 'пиздимся'in text or 'пиздиться' in text or 'пиздится' in text or 'ебашиться' in text or 'ебашится' in text or 'по разам' in text or 'разбить' in text or 'сломать' in text or 'сломаю' in text or 'разобью' in text or '1 на 1' in text or 'на сфах' in text:
        msgs = ['Идиот, ты тут с кем драться собрался?','Слушай, ты - жалкий человек, у тебя ни шанса', 'Я щас встану - ты ляжешь', 'Я тебя даже трогать не буду - иди сам убейся об стенку']
        return random.choice(msgs)

    elif text == 'хуй':
        return 'Пизда'

    elif text=='пизда':
        return 'Хуй'

    elif text=='да':
        return 'Пизда'

    elif text=='нет':
        return 'Еблет'

    else:
        return None

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if check == -1:
            break
        txt=event.object.message['text']
        if event.from_chat :
            try:
                text=event.object.message['text']
                peer_id=event.object.message['peer_id']
                from_id=event.object.message["from_id"]
                print(f'Сообщение {text}, от https://vk.com/id{from_id} из беседы {peer_id}')
                if txt[0]=='/':
                    message=cmd(text,event.chat_id, 'chat',peer_id)
                    
                    if message != None and check>=1:
                        send_msg(
                        id=event.chat_id,
                        message=message,
                        )
                    print(f'Сообщение {text}, от https://vk.com/id{from_id} из беседы {peer_id}')

                else:
                    pass
            except Exception as ex:
                print(f'\nОшибка в беседе {ex}\n')

        elif event.from_user:
            try:
                if txt[0]=='/':
                    text=event.object.message['text']
                    from_id=event.object.message['from_id']
                    message=cmd(text,event.object.message['from_id'],'user')

                    if message != None and check>=1:
                        send_msg_user(
                            id = event.object.message['from_id'],
                            message=message,
                        )
                    print(f'Сообщение {text}, от https://vk.com/id{from_id}')
                else:
                    pass
            except Exception as ex:

                print(f'\nОшибка в личных сообщениях {ex}\n')
        if check==2:
            check=-1
