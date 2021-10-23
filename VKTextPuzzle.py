import time
import os.path
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = 'b84f589813f7e8fc320e12e6d913be3709bfb2f0ff80bc116c2e4f3ab0dabee6f230b063a125a54bf053f'
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 207875677)

dota_pick = ['Пудж', 'Течис', 'СФ']

def send_msg(id, message, keyboard=None):
    req = {'user_id': id, 'message': message, 'random_id': 0}
    if keyboard != None:
        req['keyboard'] = keyboard.get_keyboard()
    vk_session.method('messages.send', req)


def game(id, cmd):
    file = f'D:\VKTextGameBot\ID\ID{id}.txt'
    if os.path.exists(file):
        print(f'old -- {id}')
        with open(file, 'r') as f:
            split_text = f.read().split(' ')
            money = split_text[1]
            respect = split_text[3]
            lottery_check = split_text[5]
            brawl_check = split_text[7].split(';')

    else:
        print(f'NEW -- {id}')
        with open(file, 'w') as f:
            f.write(f'Деньги: 1600 Репутация: -10 Лотерея_чек: 0 Бравл_старс_герои: Шелли;Эдгар')
            money = 1600
            respect = -10
            lottery_check = '0'
            brawl_check = ['Шелли', 'Эдгар']
    money = int(money)
    respect = int(respect)

    if cmd == 'start':
        send_msg(id, 'Вы просыпаетесь. Время - 8:17')
        time.sleep(2)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Идти спaть', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Ебaшить в школу', VkKeyboardColor.POSITIVE)
        send_msg(id, '- ЕБАНАЯ КОЧЕРГА. МАТЬ ЕГО СУКА ЕБАЛ. ПИЗДОС НАХУЙ. Опять проспал\nААААААААААААААААААА', keyboard)
    elif cmd == 'Спать':
        send_msg(id, '- В пизду эту школу')
        time.sleep(2)
        send_msg(id, 'Время - 9:57')
        time.sleep(2)
        send_msg(id, 'Время - 11:32')
        time.sleep(2)
        send_msg(id, 'Время - 13:47')
        time.sleep(2)
        send_msg(id, '- Уффф, заебись поспал')
        time.sleep(2)
        game(id, 'Дом дела')
    elif cmd == 'Дом дела':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Поигрaть в дотку', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Поигрaть в дотку', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Так, чем бы заняться', keyboard)
    elif cmd == 'Дота':
        send_msg(id, 'Вы включаете компьютер')
        time.sleep(1)
        send_msg(id, 'Нажимаете на иконочку Dota 2')
        time.sleep(1)
        send_msg(id, 'Поиск игры...')
        time.sleep(3)
        send_msg(id, 'Поиск игры...')
        time.sleep(4)
        send_msg(id, '- ЗАЕБАЛО')
        time.sleep(1)
        send_msg(id, 'Благодаря вашему заклинанию игра была найдена')
        time.sleep(2)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Пудж', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Течис', VkKeyboardColor.POSITIVE)
        keyboard.add_button('СФ', VkKeyboardColor.POSITIVE)
        send_msg(id, '- Так, кого бы пикнуть...', keyboard)
    elif cmd in dota_pick:
        if cmd == 'Пудж':
            msg = f'Вы нахукались, набегались, напердели. Хата воняет говном. Обдристали своё кресло. Слили игру в салат. Счёт {random.randint(0, 4)}/{random.randint(14, 30)}/{random.randint(2, 8)}, стоит отметить, чуть лучше чем в последней катке'
            send_msg(id, msg)
            time.sleep(4)
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Вздрочнуть', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Поделать уроки', VkKeyboardColor.POSITIVE)
            send_msg(id, '- Чем бы еще заняться?', keyboard)
        elif cmd == 'Течис':
            msg = 'Вы пикаете эту трипл-ебало хуйню, засовываете огромный черный хуй в рот и катите телегу в лес.'
            send_msg(id, msg)
            time.sleep(3)
            send_msg(id, 'Играете 1-ый час')
            time.sleep(1)
            send_msg(id, 'Играете 3-ий час')
            time.sleep(1)
            send_msg(id, 'Играете 9-ый час')
            time.sleep(1)
            send_msg(id,
                     f'На 12-ом часу игры упал сервер. На конец игры счёт был {random.randint(5, 30)}/{random.randint(170, 340)}/{random.randint(15, 55)}')
            time.sleep(2)
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Идти спaть', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Ебaшить в школу', VkKeyboardColor.POSITIVE)
            send_msg(id, 'За окном утро', keyboard)
            time.sleep(3)
        elif cmd == 'СФ':
            msg = 'Включается [shadowraze - juggernaut]. Покупаете блинк, еул, бкб. Разносите всех и всё'
            send_msg(id, msg)
            time.sleep(4)
            send_msg(id, 'Прошла стадия лайнинга. Все матери союзников лежат дохлые в канаве')
            time.sleep(3)
            send_msg(id, 'Прошла стадия лейт гейма. Все матери врагов лежат поверх матерей союзников')
            time.sleep(3)
            send_msg(id,
                     f'Конец игры. MVP матча - ВЫ. Очередная победка. Счёт {random.randint(18, 35)}/{random.randint(0, 3)}/{random.randint(2, 8)}')
            time.sleep(3)
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Вздрочнуть', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Поделать уроки', VkKeyboardColor.POSITIVE)
            send_msg(id, '- Чем бы еще заняться?', keyboard)
    elif cmd == 'Дрочка':
        send_msg(id, 'Идете на похуях в ванну')
        time.sleep(2)
        send_msg(id, 'Включаете порнушку с бабушками')
        time.sleep(2)
        send_msg(id, 'На всю хату стоны бабулек лесбух')
        time.sleep(1)
        send_msg(id, '- БЛЯТЬ ЗВУК НЕ ВЫКЛЮЧИЛ')
        time.sleep(2)
        send_msg(id,
                 'Батя ломится в толкан\n- Сука, опять бабу Дусю включил, сколько раз говорил - она моя мать и мне пиздец как неприятно')
        time.sleep(3)
        send_msg(id, 'Выходите из толчка, получаете аплеуху от отца. Идете спать')
        time.sleep(3)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Идти спaть', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Ебaшить в школу', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Просыпаетесь, затылок болит. Додрачиваете на ту порнуху. Что дальше?', keyboard)
    elif cmd == 'Уроки':
        time.sleep(1)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Ебалаи, чо задали?', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Скажите пж домашку', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Заходите в чат своих балбесов (11"А")', keyboard)
    elif cmd == 'ДЗ.1':
        send_msg(id, '[Сообщение из беседы] Ты чо ахуел? Тебе ебало сломать?')
        time.sleep(2)
        send_msg(id, '[Вы] Заткнула рожу овца')
        time.sleep(2)
        send_msg(id, '...')
        time.sleep(1)
        send_msg(id, 'Больше ничего не написали')
        time.sleep(2)
        send_msg(id, '- Ну и похуй, пойду дрочить')
        time.sleep(2)
        game(id, 'Дрочка')
    elif cmd == 'ДЗ.2':
        send_msg(id,
                 f'[Сообщение из беседы] По русскому учбеник упражнение 19,20,23.\nНаписать сочинение по теме "Почему русский язык такой пиздатый"\nПо математике номера с {random.randint(400, 500)} по {random.randint(505, 600)}\nПо литературе...')
        time.sleep(6)
        send_msg(id, '[Ваши мысли] ЁБ ТВОЮ МАТЬ. ИДИТЕ НАХУЙ')
        time.sleep(2)
        send_msg(id, '[Сообщение от вас] Спасибо большое')
        time.sleep(2)
        send_msg(id, '- Да идите вы все в пизду, пойду дрочить')
        time.sleep(3)
        game(id, 'Дрочка')
    elif cmd == 'АУЕ':
        a = random.randint(20, 40)
        b = random.randint(20, 50)
        c = random.randint(20, 60)
        if a + b + c > money:
            a = money // 3
            b = a
            c = a
        send_msg(id, 'Вы задумались о сочной мамке своего друга и пропустили поворот')
        time.sleep(2)
        send_msg(id, '- ОПААА. Молодоой. Здравья желаю')
        time.sleep(2)
        send_msg(id, 'Да вы только посмотрите, это же вымирающий вид животных - ауешники')
        time.sleep(3)
        send_msg(id, '- НУ че, залётный, ща тебя обрабатывать будем')
        time.sleep(3)
        send_msg(id, '[Ногой в живот]')
        time.sleep(1)
        send_msg(id, f'[Статы] Деньги: {money} => {int(money) - a} (-{a})')
        money -= a
        time.sleep(2.3)
        send_msg(id, '[Левый хук в ебало]')
        time.sleep(1.8)
        send_msg(id, f'[Статы] Деньги: {money} => {int(money) - b} (-{b})')
        money -= b
        time.sleep(2.3)
        send_msg(id, '[Правый апперкорт]')
        time.sleep(1.8)
        send_msg(id, f'[Статы] Деньги: {money} => {int(money) - c} (-{c})')
        money -= c
        time.sleep(2.3)
        send_msg(id, '- Откисай, подзаборный')
        time.sleep(2)
        send_msg(id, '...')
        time.sleep(2)
        send_msg(id, '[Ваши мысли] БЛЯТЬ. Я до Ленинского доехал')
        time.sleep(2)
        send_msg(id, f'Пересчитываете бабки. В итоге у вас спиздили {a + b + c} рублей')
        time.sleep(3)
        send_msg(id, 'Ну хули делать. Едете в школу дальше')
        time.sleep(2)
        with open(file, 'w') as f:
            print(f'UPDATE {file} -- {money} / {respect}')
            f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
        game(id, 'Дорога в школу 2')
    elif cmd == 'Деньги':
        find_money = random.randint(3, 13)
        total_new_money = 50 * find_money
        send_msg(id, f'ЕБАНУТЬСЯ. На дороге вы нашли {total_new_money} цинковых')
        time.sleep(2.5)
        send_msg(id, f'[Статы] Деньги: {money} => {int(money) + total_new_money} (+{total_new_money})')
        money += total_new_money
        with open(file, 'w') as f:
            f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
        time.sleep(2)
        game(id, 'Дорога в школу 2')
    elif cmd == 'Лотерея':
        send_msg(id, 'Вы замечаете на дороге человека в черном плаще. Он что-то вам кричит')
        time.sleep(2)
        send_msg(id, 'Вы останавливаетесь')
        time.sleep(2)
        send_msg(id,'- Предлагаю тебе игру. Можешь и бабки поднять. А можешь и слить. Всё честно')
        game(id,'Лотерея. Чуть позже')
    elif cmd == 'Лотерея. Чуть позже':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Сыграем!', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Ехать дальше', VkKeyboardColor.POSITIVE)
        send_msg(id,
                 f'Играем?\nСтавка - 50\n[Статы] Деньги: {money}',
                 keyboard)
    elif cmd == 'Лотерея 1':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Угадай число', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Орёл - Решка', VkKeyboardColor.NEGATIVE)
        send_msg(id, 'Во что сыграем?', keyboard)


    elif cmd == 'Лотерея. Число':
        if money >= 50:
            send_msg(id, 'Деньги вперёд')
            send_msg(id, f'[Статы] Деньги: {money} => {money - 50} (-50)\n')
            money -= 50
            send_msg(id, 'Я загадал число от 1 до 10 (включительно)')
            time.sleep(1)
            lottery_num = random.randint(1, 10)
            with open(file, 'w') as f:
                f.write(
                    f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_num} Бравл_старс_герои: {";".join(brawl_check)}')
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('1 - 5', VkKeyboardColor.POSITIVE)
            keyboard.add_button('6 - 10', VkKeyboardColor.POSITIVE)
            send_msg(id, 'Угадай в какой половине оно находится', keyboard)
        else:
            send_msg(id, f'Ууу, Чел. У тебя {money} рублей. Нехватает на ставку. Пиздуй отсюда')
            time.sleep(2)
            game(id,'Дорога в школу 2')


    elif cmd == 'Лотерея. Число. 2':
        if lottery_check == '0':
            send_msg(id, '[От админа] Ты ахуел? Абузер ебаный. Пошел ты нахуй. минус полопвина бабок тебе')
            send_msg(id, f'[Статы] Деньги: {money} => {int(money / 2)} (-{money - int(money / 2)})')
            with open(file, 'w') as f:
                f.write(f'Деньги: {int(money / 2)} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
            money = int(money / 2)
            game(id, 'Дорога в школу 2')

        else:
            send_msg(id,f'Я загадал число {lottery_check}')
            if int(lottery_check) <= 5:
                if txt == '1 - 5':
                    send_msg(id, 'Поздравляю, епта. Ты выиграл')
                    time.sleep(1.5)
                    send_msg(id, f'[Статы] Деньги: {money} => {money + 100} (+100)')
                    money+=100
                else:
                    send_msg(id, 'Мои поздрваления... для меня. Ты слил')
                    time.sleep(1.5)
            elif int(lottery_check) > 5:
                if txt == '6 - 10':
                    send_msg(id, 'Поздравляю, епта. Ты выиграл')
                    time.sleep(1.5)
                    send_msg(id, f'[Статы] Деньги: {money} => {money + 100} (+100)')
                    money+=100
                else:
                    send_msg(id, 'Мои поздрваления... для меня. Ты слил')
                    time.sleep(1.5)
            with open(file, 'w') as f:
                f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: 0 Бравл_старс_герои: {";".join(brawl_check)}')
        time.sleep(3)

        game(id,'Лотерея. Чуть позже')
    elif cmd == 'Лотерея. Монета':
        if money >= 50:
            send_msg(id, 'Деньги вперёд')
            send_msg(id, f'[Статы] Деньги: {money} => {money - 50} (-50)\n')
            money -= 50
            send_msg(id, 'Человек в плаще кидает монету')
            time.sleep(1)
            send_msg(id, 'Ловит её и бьёт ею об другую руку')   
            time.sleep(1.7)
            lottery_monet = random.choice(['Орёл', 'Решка'])
            with open(file, 'w') as f:
                f.write(
                    f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_monet} Бравл_старс_герои: {";".join(brawl_check)}')
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Орёл', VkKeyboardColor.POSITIVE)
            keyboard.add_button('Решка', VkKeyboardColor.POSITIVE)
            send_msg(id, 'Угадай, что выпало?', keyboard)
        else:
            send_msg(id, f'Ууу, Чел. У тебя {money} рублей. Нехватает на ставку. Пиздуй отсюда')
            time.sleep(2)
            game(id,'Дорога в школу 2')

    elif cmd == 'Дорога в школу':
        send_msg(id, 'Вы запрыгиваете на велосипед и хуярите в школу')
        time.sleep(2)
        # random
        x = ['Лотерея', 'Деньги', 'АУЕ', 'Лотерея','','','','','','','']
        rnd = random.choice(x)
        if rnd == '':
            game(id, 'Дорога в школу 2')
        else:
            game(id, rnd)
    elif cmd == 'Дорога в школу 2':
        send_msg(id, 'Приезжаете, кидаете двухколесного на землю, у вас литература, забегаете в кабинет')
        time.sleep(2)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Извините за опоздание. Можно войти?', VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Вечер в хату, бродяги', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Нужно поздороваться', keyboard)








    elif cmd == 'Заход.1':
        send_msg(id,
                 '[Училка орёт] Какого, мать его, хера. Ты - маленький гавнюк опять опоздал на мой урок. Я УСТАЛА ПОВТОРЯТЬ...')
        time.sleep(3)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Кинуть 500 рублей на стол', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Дослушать высеры', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Дальнейшие действия?', keyboard)
        time.sleep(2)
    elif cmd == 'Заход.1.1':
        send_msg(id, 'Пока она орет какую - то хуйню вы пафосно достаете кошелек')
        time.sleep(2)
        if money >= 500:
            send_msg(id, 'Берете 500 рублей, кидаете ей на стол')
            time.sleep(2)
            send_msg(id, 'Она мгновенно затыкает свой хуеприемник')
            time.sleep(2.3)
            send_msg(id, 'Гордой походкой вы идете на свое место')
            time.sleep(2)
            rnd = random.randint(4, 10)
            send_msg(id,
                     f'[Статы] Деньги: {money} => {int(money) - 500} (-500)\n[Статы] Репутация: {respect} => {int(respect) + rnd} (+{rnd})')
            money -= 500
            respect += rnd
            with open(file, 'w') as f:
                print(f'UPDATE {file} -- {money} / {respect}')
                f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
            time.sleep(2)
            game(id, 'На уроке. Крутой')
        else:
            send_msg(id, f'БЛЯТЬ. В казне {money} рублей')
            time.sleep(2)
            send_msg(id, 'Училка уже была готова заткнуться. Но вы положили кошелек обратно')
            time.sleep(3)
            send_msg(id, 'Класс начал над тобой дико угарать')
            time.sleep(2)
            send_msg(id, 'Училка более яростно начала тебя хуесосить. Вы всё это выслушали и сели на место')
            time.sleep(3)
            rnd = random.randint(1, 3)
            send_msg(id, f'[Статы] Репутация: {respect} => {respect - rnd} (-{rnd})')
            respect -= rnd
            with open(file, 'w') as f:
                print(f'UPDATE {file} -- {money} / {respect}')
                f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
            time.sleep(2)
            game(id, 'На уроке. Не крутой')
    elif cmd == 'Заход.1.2':
        send_msg(id, 'Вас обхуесосили с пяток до печени')
        time.sleep(2)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Да пошла ты нахуй, карга ебучая', VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Можно пойти на место?', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Что скажите?', keyboard)
    elif cmd == 'Заход.2':
        send_msg(id, 'Учитель встал с места: ветер с тобой бродяга')
        time.sleep(2.4)
        send_msg(id, 'Вы на выебонах садитесь на своё место. Весь класс в ахуе, смотрит на тебя')
        time.sleep(4)
        game(id, 'На уроке. Крутой')
    elif cmd == 'На уроке. Крутой':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Зайти в Бравл Старс', VkKeyboardColor.POSITIVE)
        if respect>=40:
            keyboard.add_button('Позалипать на одноклассниц', VkKeyboardColor.POSITIVE)
        else:
            keyboard.add_button('Позалипать на одноклассниц 40+', VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Попиздиться', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Слушать урок', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Сегодня вы в ударе\n\nБля, чем бы заняться', keyboard)
    elif cmd == 'На уроке. Не крутой':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Зайти в Бравл Старс', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Слушать урок', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Бля, чем бы заняться', keyboard)
    elif cmd == 'Послать учителя':
        send_msg(id, '[Сообщение от Бога] Чувак, даже не думай, я и сам её боюсь. Лучше молча сядь на место')
        time.sleep(3)
        send_msg(id, 'Вы садитесь за свою парту')
        game(id, 'На уроке. Не крутой')
    elif cmd == 'Идти на место':
        send_msg(id, '"Можно" мать твою выебать, а если хочешь сесть, то "разрешите пожалуйста"')
        time.sleep(3)
        send_msg(id,
                 '[Ваши мысли] Плесень ебаная еще не знает что я всю ее семью от кошки до её отца мертвого перетрахал')
        time.sleep(3.4)
        send_msg(id, 'Садитесь на место')
        game(id, 'На уроке. Не крутой')
    elif cmd == 'Урок':
        send_msg(id, 'Пиздит')
        time.sleep(0.7)
        send_msg(id, 'Пиздит')
        time.sleep(0.7)
        send_msg(id, 'Пиздит')
        time.sleep(0.7)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Идти домой', VkKeyboardColor.POSITIVE)
        keyboard.add_line()

        x = random.choice(['','','','','','','','','','','','','','','','','','','','','','','','','','', 'Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Зачёт','Обстрел'])
        if x == '':
            if respect >= 50:
                keyboard.add_button('Погулять с одноклами', VkKeyboardColor.POSITIVE)
            else:
                keyboard.add_button('Погулять с одноклами 50+', VkKeyboardColor.NEGATIVE)
            send_msg(id, 'Мымра напизделась. Звонок. Уроки закончились', keyboard)
        elif x == 'Зачёт':
            send_msg(id, 'До конца урока 4 минуты')
            time.sleep(2)
            send_msg(id, '[Неожиданное происшествие] Эта хуета решила позадавать вопросы по уроку')
            time.sleep(3)
            send_msg(id,
                     'Какой длины хер был у Онегина в проивзедении Гоголя "Капитанская дочка"? И что это символизирует?')
            time.sleep(3)
            send_msg(id, 'Если нет желающих, то спрашиваю по списку')
            time.sleep(3)
            send_msg(id, 'Вы решили потянуть руку')
            time.sleep(2)
            send_msg(id,
                     'Выходите к доске. И начинаете пиздеть. Еле как, но смогли растянуть ответ прям до конца урока')
            time.sleep(3.7)
            send_msg(id, 'Весь класс, который пинал хуи, благодарен тебе')
            time.sleep(2)
            rnd = random.randint(2, 4)
            send_msg(id, f'[Статы] Репутация: {respect} => {int(respect) + rnd} (+{rnd})')
            respect += rnd
            time.sleep(3)
            with open(file, 'w') as f:
                print(f'UPDATE {file} -- {money} / {respect}')
                f.write(f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
            if respect >= 50:
                keyboard.add_button('Погулять с одноклами', VkKeyboardColor.POSITIVE)
            else:
                keyboard.add_button('Погулять с одноклами', VkKeyboardColor.NEGATIVE)
            send_msg(id, 'Напизделись. Уроки закончились', keyboard)
        elif x == 'Обстрел':
            print('АХУЕТЬ ВЫПАЛ ОБСТРЕЛЛ!!!')
            print(f'Умер {id}')
            send_msg(245210027,f'Умер человек с айди {id}')
            send_msg(id, '[Стук в дверь]')
            time.sleep(1)
            send_msg(id, 'Училка открывает дверь')
            time.sleep(1)
            send_msg(id, '[ВЫСТРЕЛ]')
            time.sleep(1)
            send_msg(id, 'Кровь этой твари размазалась по всем окнам и по отличнице с первой парты')
            time.sleep(3)
            send_msg(id, 'В класс входит голубоглазый блондин с M134 Minigun')
            time.sleep(2)
            keyboard = VkKeyboard(one_time=True)
            keyboard.add_button('Раздеться и начать дрочить', VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Идти на таран со столом', VkKeyboardColor.POSITIVE)
            send_msg(id, 'Что делать?',keyboard)



    elif cmd == 'Гулять':
        time.sleep(2)
        if respect >= 50:
            send_msg(id, 'Эту ветку я еще не доделал. ПОэтому мы идем пока что домой')
            time.sleep(2)
            game(id, 'Дом дела')
        else:
            send_msg(id, '[Нехватка репутации] Необходима репутация 50+')
            time.sleep(2)
            send_msg(id, 'Поэтому ты идёшь домой')
            time.sleep(2)
            game(id, 'Дом дела')
    elif cmd == 'Голый':
        send_msg(id, 'На ваших глазах он расстреливает весь класс')
        time.sleep(2)
        send_msg(id, 'Скидывает абмундирование и встает рядом с вами')
        time.sleep(2)
        send_msg(id, 'Теперь вы стоите спина к спине и оба дрочите')
        time.sleep(2)
        send_msg(id, 'Он ждет 10 секунд и отходит на три шага от вас')
        time.sleep(2)
        send_msg(id, 'Разворачивается...')
        time.sleep(2)
        send_msg(id, 'CumShot')
        time.sleep(2)
        send_msg(id, '[Вы умерли от прострела головы]')
        time.sleep(1)
        send_msg(id, '[Получено достижение: CumDead]')
        time.sleep(2)
        with open(file, 'w') as f:
            f.write(f'Деньги: 1600 Репутация: -10 Лотерея_чек: 0 Бравл_старс_герои: Шелли;Эдгар')
        send_msg(id,'[Статы обновлены] Деньги: 1600 Репутация: -10')
    elif cmd == 'Таран':
        send_msg(id, 'Вы хватаете стол в руки и бежите на него. С криками "АААААААААААААААААА"')
        time.sleep(2)
        send_msg(id, 'Мгновенно наступила тишина')
        time.sleep(2)
        send_msg(id, 'Все в ахуе от этого действия')
        time.sleep(2)
        send_msg(id, 'Блодин смотрит на вас с недоразумением')
        time.sleep(2)
        send_msg(id, 'Вы извиняетесь. Ставите стол на место')
        time.sleep(2)
        send_msg(id, 'Блондин кладет Миниган на пол и отходит немного от вас (вероятно, испугался)')
        time.sleep(3)
        send_msg(id, 'Всё. Это победа! Вы спасли школу ')
        time.sleep(6)
        send_msg(id, '[Блондин достает "Винторез"]')
        time.sleep(2)
        send_msg(id, '[Точечный еджиничный выстрел]')
        time.sleep(2)
        send_msg(id, '[Мгновенная смерть]')
        time.sleep(2)
        send_msg(id, '[Получено достижение: +420]')
        time.sleep(2)
        with open(file, 'w') as f:
            f.write(f'Деньги: 1600 Репутация: -10 Лотерея_чек: 0 Бравл_старс_герои: Шелли;Эдгар')
        send_msg(id,'[Статы обновлены] Деньги: 1600 Репутация: -10')
        time.sleep(5)
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('start', VkKeyboardColor.SECONDARY)
        send_msg(id,'Чтобы начать новую игру нажмите start',keyboard)
    elif cmd == 'Бравл Старс':
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Открыть ящик', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Сыграть ШД', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Слушать урок', VkKeyboardColor.POSITIVE)
        send_msg(id, 'Что дальше?', keyboard)
    elif cmd == 'Ящики':
        gifts=['250 монет', 'Мать котова', 'ЭЛЬ_ПРИМО', 'Эдгар', 'Шелли','10 гемов', '100 монет', 'Падж', 'Батины пантолоны', 'Труханы деда', 'Гаджет на шелли', '20 рублей', 'Хер моржа', 'Скин на Шелли', 'Пачка гандонов', 'Отбойный молоток', 'Прах прадеда']
        a = random.choice(gifts)
        gifts.remove(a)
        b = random.choice(gifts)
        gifts.remove(b)
        c = random.choice(gifts)
        if a in ['ЭЛЬ_ПРИМО', 'Эдгар', 'Шелли', 'Падж']:
            if a in brawl_check:
                a_text = f'1) {random.randint(10, 60)} очков силы {a}'
            else:
                a_text = f'1) НОВЫЙ СУКА ГЕРООООЙ ({a})!'
                brawl_check.append(a)
        else:
            a_text = f'1) {a}'

        if b in ['ЭЛЬ_ПРИМО', 'Эдгар', 'Шелли','Падж']:
            if b in brawl_check:
                b_text=f'2) {random.randint(10,60)} очков силы {b}'
            else:
                b_text=f'2) НОВЫЙ СУКА ГЕРООООЙ ({b})!'
                brawl_check.append(b)
        else:
            b_text=f'2) {b}'

        if c in ['ЭЛЬ_ПРИМО', 'Эдгар', 'Шелли','Падж']:
            if c in brawl_check:
                c_text=f'3) {random.randint(10,60)} очков силы {c}'
            else:
                c_text=f'3) НОВЫЙ СУКА ГЕРООООЙ ({c})!'
                brawl_check.append(c)
        else:
            c_text=f'3) {c}'

        send_msg(id, 'Ваш лут:')
        time.sleep(1.5)
        send_msg(id, a_text)
        time.sleep(1.5)
        send_msg(id, b_text)
        time.sleep(1.5)
        send_msg(id, c_text)
        time.sleep(1.5)
        if a == '20 рублей' or b == '20 рублей' or c == '20 рублей':
            send_msg(id,f'[Статы] Деньги: {money} ==> {money+20} (+20)')
            money += 20
        with open(file, 'w') as f:
            f.write(
                f'Деньги: {money} Репутация: {respect} Лотерея_чек: {lottery_check} Бравл_старс_герои: {";".join(brawl_check)}')
        game(id,'Бравл Старс')
    elif cmd == 'ШД':
        keyboard = VkKeyboard(one_time=True)
        i=0
        for hero in brawl_check:
            if i%2==0 and i!=0:
                keyboard.add_line()
                print('-----------------')
            keyboard.add_button(hero, VkKeyboardColor.POSITIVE)
            print(hero)
            i+=1
        print(keyboard)
        send_msg(id,'Выберите пик',keyboard)





# Бравл старс. Сундук. Игра для крутых. Игра для лохов
# Слушать урок +
# Пиздитьсят
# Позалипать на однокласниц
# Сделать больше рандома+
# Добавить рандом на событие в начало game() +
# Мужик предлагает игру сыграть в рулетку(больше 6 или меньше или равно) Выбери ставку +
# Вы нашли на улице деньги +
# АУЕшники докопались (можно добавить условие на нож) И условие на (первый раз или нет) +
# f'{money} {respect} {items} {AUE_check}'
# Да пошла ты нахуй, карга ебучая +
# Можно пойти на место? +
# Гулять

# Можно добавить магазин

'''
send_msg(id,'')
time.sleep(2)

'''

for event in longpoll.listen():
    if event.from_user:
        if event.type == VkBotEventType.MESSAGE_NEW:
            txt = event.object.message['text']
            id = event.object.message['from_id']
            if txt == 'start':
                send_msg(id,
                         'Игра основана на реальных событиях. Строго не рекомендуется повторять то, что увидите в квесте\n.\n.\nНачнем испытание\nВы - обычный школьник-девственник, ваша задача - заполучить внимание красавицы вашего класса и сделать с ней Джага Джага, Шпили Вилли...\nНу короче выебать её')
                time.sleep(5)
                game(id, 'start')
            elif txt == 'Идти спaть':
                game(id, 'Спать')
            elif txt == 'Поигрaть в дотку':
                game(id, 'Дота')
            elif txt in dota_pick:
                game(id, txt)
            elif txt == 'Вздрочнуть':
                game(id, 'Дрочка')
            elif txt == 'Поделать уроки':
                game(id, 'Уроки')
            elif txt == 'Ебалаи, чо задали?':
                game(id, 'ДЗ.1')
            elif txt == 'Скажите пж домашку':
                game(id, 'ДЗ.2')
            elif txt == 'Ебaшить в школу':
                game(id, 'Дорога в школу')
            elif txt == 'Извините за опоздание. Можно войти?':
                game(id, 'Заход.1')
            elif txt == 'Кинуть 500 рублей на стол':
                game(id, 'Заход.1.1')
            elif txt == 'Дослушать высеры':
                game(id, 'Заход.1.2')
            elif txt == 'Вечер в хату, бродяги':
                game(id, 'Заход.2')
            elif txt == 'Позалипать на одноклассниц':
                game(id, 'Пялиться')
            elif txt == 'Попиздиться':
                game(id, 'Пизделка')
            elif txt == 'Да пошла ты нахуй, карга ебучая':
                game(id, 'Послать учителя')
            elif txt == 'Можно пойти на место?':
                game(id, 'Идти на место')
            elif txt == 'Слушать урок':
                game(id, 'Урок')
            elif txt == 'Идти домой':
                game(id, 'Дом дела')
            elif txt == 'Погулять с одноклами':
                game(id, 'Гулять')
            elif txt == 'Ехать дальше':
                game(id, 'Дорога в школу 2')
            elif txt == 'Сыграем!':
                game(id, 'Лотерея 1')
            elif txt == 'Угадай число':
                game(id, 'Лотерея. Число')
            elif txt == 'Орёл - Решка':
                game(id,'Лотерея. Монета')
            elif txt == '1 - 5' or txt == '6 - 10':
                game(id, 'Лотерея. Число. 2')
            elif txt == 'Раздеться и начать дрочить':
                game(id, 'Голый')
            elif txt == 'Идти на таран со столом':
                game(id, 'Таран')
            elif txt == 'Зайти в Бравл Старс':
                game(id,'Бравл Старс')
            elif txt == 'Открыть ящик':
                game(id,'Ящики')
            elif txt == 'Позалипать на одноклассниц 40+':
                send_msg(id,'Нужна репутация 40+')
                time.sleep(1)
                game(id,'На уроке. Крутой')
            elif txt == 'Позалипать на одноклассниц':
                pass
            elif txt == 'Попиздиться':
                game(id,'Драка.1')
            elif txt == 'Сыграть ШД':
                game(id, 'ШД')
