import telebot
from telebot import types

bot = telebot.TeleBot('5982132443:AAH2GAR3QyF497FpkoSWkJhWFxoiaOtcSLM')

@bot.message_handler(commands=['start'])
def start(message):
    myphoto = open('catgeometric.png', 'rb')
    bot.send_sticker(message.chat.id, myphoto)
    mess = f'Привет {message.from_user.first_name} {message.from_user.last_name}👋, меня зовут Геометрик, я помогу тебе разобраться с геометрией.\nЕсли тебе надо узнать весь функционал бота и начать изучение геометрии, напиши ➡/help⬅'
    bot.send_message(message.chat.id,mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    stereometriya = types.KeyboardButton('🔻Планиметрия🔻')
    planimetriya = types.KeyboardButton('🛢Стереометрия🛢')
    tabl = types.KeyboardButton('📋Таблица синусов и косинусов📋')
    markup.add(stereometriya, planimetriya, tabl)
    bot.send_message(message.chat.id, 'Выбирай раздел, который тебя интересует:\n/Planimetry - Раздел "Планиметрия"\n/Stereometry - Раздел "Стереометрия"\n/sincostable - Таблица синусов и косинусов', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')


    elif message.text == "/Planimetry":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        p00 = types.KeyboardButton('Краткое введение.')
        p29 = types.KeyboardButton('Виды линий')
        p30 = types.KeyboardButton('Определения фигур')
        p31 = types.KeyboardButton('Фигуры')
        p01 = types.KeyboardButton('01. Аксиомы планиметрии.')
        p02 = types.KeyboardButton('02. Углы')
        p03 = types.KeyboardButton('03. Параллельные прямые. Перпендикулярные прямые. Перпендикуляр к прямой')
        p04 = types.KeyboardButton('04. Свойства сторон и углов треугольника')
        p05 = types.KeyboardButton('05. Равенство треугольников.')
        p06 = types.KeyboardButton('06. Медиана треугольника.')
        p07 = types.KeyboardButton('07. Биссектриса треугольника.')
        p08 = types.KeyboardButton('08. Высота треугольника')
        p09 = types.KeyboardButton('09. Средняя линия треугольника')
        p10 = types.KeyboardButton('10. Соотношение между элементами прямоугольного треугольника')
        p11 = types.KeyboardButton('11. Соотношение между сторонами и углами в произвольном треугольнике')
        p12 = types.KeyboardButton('12. Преобразование фигур. Движение')
        p13 = types.KeyboardButton('13. Преобразование подобия')
        p14 = types.KeyboardButton('14. Подобие треугольников.')
        p15 = types.KeyboardButton('15. Параллелограмм и его виды.')
        p16 = types.KeyboardButton('16. Трапеция')
        p17 = types.KeyboardButton('17. Окружность, хорды и дуги')
        p18 = types.KeyboardButton('18. Окружность. Касательные и секущие.')
        p19 = types.KeyboardButton('19. Взаимное расположение прямой и окружности. Взаимное расположение двух окружностей.')
        p20 = types.KeyboardButton('20. Общие касательные двух окружностей.')
        p21 = types.KeyboardButton('21. Углы в окружности.')
        p22 = types.KeyboardButton('22. Длина окружности и её частей. Площадь круга и его частей')
        p23 = types.KeyboardButton('23. Вписанный и описанный многоугольники. Вписанный и описанный четырехугольники. Прямоугольник. Трапеция и ромб. Квадрат.')
        p24 = types.KeyboardButton('24. Окружность, описанная около треугольника, и окружность, вписанная в треугольник.')
        p25 = types.KeyboardButton('25. Окружности, описанные и вписанные в правильные многоугольники')
        p26 = types.KeyboardButton('26. Площади треугольников.')
        p27 = types.KeyboardButton('27. Площади четырехугольников.')
        markup.add(back, p00, p29, p30,p31, p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27)
        bot.send_message(message.chat.id, 'Планиметрия - это раздел геометрии, который изучает геометрические фигуры на плоскости.', reply_markup=markup)
        planimetrya_photo = open('figure.jpg', 'rb')
        bot.send_photo(message.chat.id, planimetrya_photo)
        bot.send_message(message.chat.id,'Выбери тему:', parse_mode='html')

    elif message.text == "🔻Планиметрия🔻":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        p00 = types.KeyboardButton('Краткое введение.')
        p29 = types.KeyboardButton('Виды линий')
        p30 = types.KeyboardButton('Определения фигур')
        p31 = types.KeyboardButton('Фигуры')
        p01 = types.KeyboardButton('01. Аксиомы планиметрии.')
        p02 = types.KeyboardButton('02. Углы')
        p03 = types.KeyboardButton('03. Параллельные прямые. Перпендикулярные прямые. Перпендикуляр к прямой')
        p04 = types.KeyboardButton('04. Свойства сторон и углов треугольника')
        p05 = types.KeyboardButton('05. Равенство треугольников.')
        p06 = types.KeyboardButton('06. Медиана треугольника.')
        p07 = types.KeyboardButton('07. Биссектриса треугольника.')
        p08 = types.KeyboardButton('08. Высота треугольника')
        p09 = types.KeyboardButton('09. Средняя линия треугольника')
        p10 = types.KeyboardButton('10. Соотношение между элементами прямоугольного треугольника')
        p11 = types.KeyboardButton('11. Соотношение между сторонами и углами в произвольном треугольнике')
        p12 = types.KeyboardButton('12. Преобразование фигур. Движение')
        p13 = types.KeyboardButton('13. Преобразование подобия')
        p14 = types.KeyboardButton('14. Подобие треугольников.')
        p15 = types.KeyboardButton('15. Параллелограмм и его виды.')
        p16 = types.KeyboardButton('16. Трапеция')
        p17 = types.KeyboardButton('17. Окружность, хорды и дуги')
        p18 = types.KeyboardButton('18. Окружность. Касательные и секущие.')
        p19 = types.KeyboardButton('19. Взаимное расположение прямой и окружности. Взаимное расположение двух окружностей.')
        p20 = types.KeyboardButton('20. Общие касательные двух окружностей.')
        p21 = types.KeyboardButton('21. Углы в окружности.')
        p22 = types.KeyboardButton('22. Длина окружности и её частей. Площадь круга и его частей')
        p23 = types.KeyboardButton('23. Вписанный и описанный многоугольники. Вписанный и описанный четырехугольники. Прямоугольник. Трапеция и ромб. Квадрат.')
        p24 = types.KeyboardButton('24. Окружность, описанная около треугольника, и окружность, вписанная в треугольник.')
        p25 = types.KeyboardButton('25. Окружности, описанные и вписанные в правильные многоугольники')
        p26 = types.KeyboardButton('26. Площади треугольников.')
        p27 = types.KeyboardButton('27. Площади четырехугольников.')
        markup.add(back, p00, p29, p30,p31, p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27)
        bot.send_message(message.chat.id, 'Планиметрия - это раздел геометрии, который изучает геометрические фигуры на плоскости.', reply_markup=markup)
        planimetrya_photo = open('figure.jpg', 'rb')
        bot.send_photo(message.chat.id, planimetrya_photo)
        bot.send_message(message.chat.id,'Выбери тему:', parse_mode='html')

    elif message.text == "/sincostable":
       phototabl = open('tabl.PNG', 'rb')
       bot.send_message(message.chat.id, 'Таблица синусов и косинусов:', parse_mode='html')
       bot.send_photo(message.chat.id,phototabl)


    elif message.text == "/Stereometry":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        stereo1 = types.KeyboardButton('Прямые и плоскости')
        stereo2 = types.KeyboardButton('Призма')
        stereo3 = types.KeyboardButton('Пирамида')
        stereo4 = types.KeyboardButton('Цилиндр')
        stereo5 = types.KeyboardButton('Конус')
        stereo6 = types.KeyboardButton('Сфера и шар')
        stereo7 = types.KeyboardButton('Вписанные и описанные тела')
        stereo8 = types.KeyboardButton('Векторы и координаты')
        markup.add(back,stereo1,stereo2,stereo3,stereo4,stereo5,stereo6,stereo7,stereo8)
        bot.send_message(message.chat.id, 'Стереометрия — это раздел геометрии, изучающий пространственные фигуры и их свойства.', reply_markup=markup)
        stereometrya_photo = open('stereo.jpg', 'rb')
        bot.send_photo(message.chat.id, stereometrya_photo)
        bot.send_message(message.chat.id,'Выбери тему:', parse_mode='html')


    elif message.text == "🛢Стереометрия🛢":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        stereo1 = types.KeyboardButton('Прямые и плоскости')
        stereo2 = types.KeyboardButton('Призма')
        stereo3 = types.KeyboardButton('Пирамида')
        stereo4 = types.KeyboardButton('Цилиндр')
        stereo5 = types.KeyboardButton('Конус')
        stereo6 = types.KeyboardButton('Сфера и шар')
        stereo7 = types.KeyboardButton('Вписанные и описанные тела')
        stereo8 = types.KeyboardButton('Векторы и координаты')
        markup.add(back,stereo1,stereo2,stereo3,stereo4,stereo5,stereo6,stereo7,stereo8)
        bot.send_message(message.chat.id, 'Стереометрия — это раздел геометрии, изучающий пространственные фигуры и их свойства.', reply_markup=markup)
        stereometrya_photo = open('stereo.jpg', 'rb')
        bot.send_photo(message.chat.id, stereometrya_photo)
        bot.send_message(message.chat.id,'Выбери тему:', parse_mode='html')


    elif message.text == "Прямые и плоскости":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       stereo10 = types.KeyboardButton('Базовые понятия')
       stereo20 = types.KeyboardButton('Взаимное расположение прямых в пространстве')
       stereo30 = types.KeyboardButton('Взаимное расположение плоскостей в пространстве')
       stereo40 = types.KeyboardButton('Взаимное расположение прямой и плоскости в пространстве')
       stereo50 = types.KeyboardButton('Теорема о трех перпендикулярах')
       stereo60 = types.KeyboardButton('Углы в пространстве')
       stereo70 = types.KeyboardButton('Расчет расстояний в пространстве')
       markup.add(back, stereo10, stereo20, stereo30, stereo40, stereo50, stereo60, stereo70)
       bot.send_message(message.chat.id,'Выбери тему:',reply_markup=markup)

    elif message.text == "Базовые понятия":
       photoaa = open('aa.jpg', 'rb')
       photoaaa = open('aaa.jpg', 'rb')
       bot.send_message(message.chat.id, 'Базовые понятия:', parse_mode='html')
       bot.send_photo(message.chat.id, photoaa)
       bot.send_photo(message.chat.id, photoaaa)

    elif message.text == "Взаимное расположение прямых в пространстве":
       photobb = open('bb.jpg', 'rb')
       photobbb = open('bbb.jpg', 'rb')
       bot.send_message(message.chat.id, 'Взаимное расположение прямых в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photobb)
       bot.send_photo(message.chat.id, photobbb)

    elif message.text == "Взаимное расположение плоскостей в пространстве":
       photocc = open('cc.jpg', 'rb')
       photoccc = open('ccc.jpg', 'rb')
       photocccc = open('cccc.jpg', 'rb')
       photoccccc = open('ccccc.jpg', 'rb')
       bot.send_message(message.chat.id, 'Взаимное расположение плоскостей в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photocc)
       bot.send_photo(message.chat.id, photoccc)
       bot.send_photo(message.chat.id, photocccc)
       bot.send_photo(message.chat.id, photoccccc)


    elif message.text == "Взаимное расположение прямой и плоскости в пространстве":
       photodd = open('dd.jpg', 'rb')
       photoddd = open('ddd.jpg', 'rb')
       photodddd = open('dddd.jpg', 'rb')
       bot.send_message(message.chat.id, 'Взаимное расположение прямой и плоскости в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photodd)
       bot.send_photo(message.chat.id, photoddd)
       bot.send_photo(message.chat.id, photodddd)

    elif message.text == "Теорема о трех перпендикулярах":
       photoee = open('ee.jpg', 'rb')
       photoeee = open('eee.jpg', 'rb')
       photoeeee = open('eeee.jpg', 'rb')
       bot.send_message(message.chat.id, 'Теорема о трех перпендикулярах:', parse_mode='html')
       bot.send_photo(message.chat.id, photoee)
       bot.send_photo(message.chat.id, photoeee)
       bot.send_photo(message.chat.id, photoeeee)

    elif message.text == "Углы в пространстве":
       photoff = open('ff.jpg', 'rb')
       photofff = open('fff.jpg', 'rb')
       bot.send_message(message.chat.id, 'Углы в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff)
       bot.send_photo(message.chat.id, photofff)

    elif message.text == "Расчет расстояний в пространстве":
       photogg = open('gg.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет расстояний в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photogg)


    elif message.text == "Призма":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       www01 = types.KeyboardButton('ㅤОсновные определения')
       www02 = types.KeyboardButton('ㅤРасчет')
       www03 = types.KeyboardButton('Параллелепипед и куб')
       markup.add(back,www01,www02,www03)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "ㅤОсновные определения":
       photocs1 = open('cs1.jpg', 'rb')
       photocs2 = open('cs2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные определения:', parse_mode='html')
       bot.send_photo(message.chat.id, photocs1)
       bot.send_photo(message.chat.id, photocs2)


    elif message.text == "ㅤРасчет":
       photocs3 = open('cs3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photocs3)

    elif message.text == "Параллелепипед и куб":
       photocs10 = open('cs10.jpg', 'rb')
       photocs11 = open('cs11.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photocs10)
       bot.send_photo(message.chat.id, photocs11)

    elif message.text == "Пирамида":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       opp1 = types.KeyboardButton('Основные определенияㅤ')
       opp2 = types.KeyboardButton('Расчетㅤ')
       markup.add(back, opp1,opp2)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Основные определенияㅤ":
       photoapi1 = open('api5.jpg', 'rb')
       photoapi2 = open('api6.jpg', 'rb')
       photoapi6 = open('api7.jpg', 'rb')
       photoapi7 = open('api8.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные определения:', parse_mode='html')
       bot.send_photo(message.chat.id, photoapi1)
       bot.send_photo(message.chat.id, photoapi2)
       bot.send_photo(message.chat.id, photoapi6)
       bot.send_photo(message.chat.id, photoapi7)

    elif message.text == "Расчетㅤ":
       photoapi3 = open('api1.jpg', 'rb')
       photoapi4 = open('api2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photoapi3)
       bot.send_photo(message.chat.id, photoapi4)

    elif message.text == "Цилиндр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        opp3 = types.KeyboardButton('ㅤОсновные определенияㅤ')
        opp4 = types.KeyboardButton('ㅤРасчетㅤ')
        markup.add(back, opp3, opp4)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "ㅤОсновные определенияㅤ":
       photolol1 = open('lol1.jpg', 'rb')
       photolol2 = open('lol2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные определения:', parse_mode='html')
       bot.send_photo(message.chat.id, photolol1)
       bot.send_photo(message.chat.id, photolol2)

    elif message.text == "ㅤРасчетㅤ":
       photolol4 = open('lol4.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photolol4)

    elif message.text == "Конус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        opp5 = types.KeyboardButton('ㅤㅤОсновные определенияㅤㅤ')
        opp6 = types.KeyboardButton('ㅤㅤРасчетㅤㅤ')
        markup.add(back, opp5, opp6)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "ㅤㅤОсновные определенияㅤㅤ":
       photo900 = open('k02.jpg', 'rb')
       photo901 = open('k022.jpg', 'rb')
       photo920 = open('k0222.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные определения:', parse_mode='html')
       bot.send_photo(message.chat.id, photo900)
       bot.send_photo(message.chat.id, photo901)
       bot.send_photo(message.chat.id, photo920)

    elif message.text == "ㅤㅤРасчетㅤㅤ":
       photo902 = open('k01.jpg', 'rb')
       photo903 = open('k011.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photo902)
       bot.send_photo(message.chat.id, photo903)

    elif message.text == "Сфера и шар":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        opp7 = types.KeyboardButton('Основные определения')
        opp8 = types.KeyboardButton('Расчет')
        markup.add(back, opp7, opp8)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Основные определения":
       photo800 = open('6.jpg', 'rb')
       photo801 = open('66.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные определения:', parse_mode='html')
       bot.send_photo(message.chat.id,photo800)
       bot.send_photo(message.chat.id, photo801)

    elif message.text == "Расчет":
       photo802 = open('opp1.jpg', 'rb')
       photo803 = open('opp2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Расчет:', parse_mode='html')
       bot.send_photo(message.chat.id, photo802)
       bot.send_photo(message.chat.id, photo803)

    elif message.text == "Вписанные и описанные тела":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        opp10 = types.KeyboardButton('Цилиндр и призма')
        opp11 = types.KeyboardButton('Конус и пирамида')
        opp12 = types.KeyboardButton('Вписанный о описанный шар')
        opp13 = types.KeyboardButton('Другие комбинации вписанный и описанных тел')
        markup.add(back, opp10, opp11,opp12,opp13)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)\

    elif message.text == "Цилиндр и призма":
       photoser1 = open('ser1.jpg', 'rb')
       bot.send_message(message.chat.id, 'Цилиндр и призма:', parse_mode='html')
       bot.send_photo(message.chat.id, photoser1)


    elif message.text == "Конус и пирамида":
       photoser2 = open('ser2.jpg', 'rb')
       photoser3 = open('ser3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Конус и пирамида:', parse_mode='html')
       bot.send_photo(message.chat.id, photoser2)
       bot.send_photo(message.chat.id, photoser3)

    elif message.text == "Вписанный о описанный шар":
       photoser5 = open('ser5.jpg', 'rb')
       photoser6 = open('ser6.jpg', 'rb')
       photoser7 = open('ser7.jpg', 'rb')
       photoser8 = open('ser8.jpg', 'rb')
       photoser9 = open('ser9.jpg', 'rb')
       photoser10 = open('ser10.jpg', 'rb')
       bot.send_message(message.chat.id, 'Вписанный о описанный шар:', parse_mode='html')
       bot.send_photo(message.chat.id, photoser5)
       bot.send_photo(message.chat.id, photoser6)
       bot.send_photo(message.chat.id, photoser7)
       bot.send_photo(message.chat.id, photoser8)
       bot.send_photo(message.chat.id, photoser9)
       bot.send_photo(message.chat.id, photoser10)

    elif message.text == "Другие комбинации вписанный и описанных тел":
       photoars1 = open('ars1.jpg', 'rb')
       photoars2 = open('ars2.jpg', 'rb')
       photoars3 = open('ars3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Другие комбинации вписанный и описанных тел:', parse_mode='html')
       bot.send_photo(message.chat.id, photoars1)
       bot.send_photo(message.chat.id, photoars2)
       bot.send_photo(message.chat.id, photoars3)

    elif message.text == "Векторы и координаты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        opp15 = types.KeyboardButton('Координаты и длины')
        opp16 = types.KeyboardButton('Действия над векторами в пространстве')
        opp17 = types.KeyboardButton('🔥Метод координат🔥')
        markup.add(back, opp15, opp16,opp17)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Координаты и длины":
       photowot1 = open('wot1.jpg', 'rb')
       photowot2 = open('wot2.jpg', 'rb')
       photowot3 = open('wot3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Координаты и длины:', parse_mode='html')
       bot.send_photo(message.chat.id, photowot1)
       bot.send_photo(message.chat.id, photowot2)
       bot.send_photo(message.chat.id, photowot3)


    elif message.text == "Действия над векторами в пространстве":
       photomama1 = open('mama1.jpg', 'rb')
       photomama2 = open('mama2.jpg', 'rb')
       photomama3 = open('mama3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Действия над векторами в пространстве:', parse_mode='html')
       bot.send_photo(message.chat.id, photomama1)
       bot.send_photo(message.chat.id, photomama2)
       bot.send_photo(message.chat.id, photomama3)

    elif message.text == "🔥Метод координат🔥":
       photopapa1 = open('papa1.jpg', 'rb')
       photopapa2 = open('papa2.jpg', 'rb')
       photopapa3 = open('papa3.jpg', 'rb')
       photopapa4 = open('papa4.jpg', 'rb')
       bot.send_message(message.chat.id, '🔥Метод координат🔥:', parse_mode='html')
       bot.send_photo(message.chat.id, photopapa1)
       bot.send_photo(message.chat.id, photopapa2)
       bot.send_photo(message.chat.id, photopapa3)
       bot.send_photo(message.chat.id, photopapa4)


    elif message.text == "Вернуться в главное меню⬅":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        stereometriya = types.KeyboardButton('🔻Планиметрия🔻')
        planimetriya = types.KeyboardButton('🛢Стереометрия🛢')
        tabl = types.KeyboardButton('📋Таблица синусов и косинусов📋')
        markup.add(stereometriya, planimetriya, tabl)
        bot.send_message(message.chat.id, 'Выбирай раздел, который тебя интересует:\n/Planimetry - Раздел "Планиметрия"\n/Stereometry - Раздел "Стереометрия"\n/sincostable - Таблица синусов и косинусов', reply_markup=markup)


    elif message.text == "Краткое введение.":
       photo0 = open('BBedenie.jpg', 'rb')
       bot.send_message(message.chat.id, 'Краткое введение.', parse_mode='html')
       bot.send_photo(message.chat.id,photo0)

    elif message.text == "Виды линий":
       photo29 = open('28.png', 'rb')
       bot.send_message(message.chat.id, 'Виды линий', parse_mode='html')
       bot.send_photo(message.chat.id,photo29)

    elif message.text == "📋Таблица синусов и косинусов📋":
       phototabl = open('tabl.PNG', 'rb')
       bot.send_message(message.chat.id, 'Таблица синусов и косинусов:', parse_mode='html')
       bot.send_photo(message.chat.id,phototabl)

    elif message.text == "Определения фигур":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        allOpr = types.KeyboardButton('Все определения')
        d01 = types.KeyboardButton('Круг и Окружность')
        d02 = types.KeyboardButton('Квадрат')
        d03 = types.KeyboardButton('Треугольник')
        d04 = types.KeyboardButton('Прямоугольник')
        d05 = types.KeyboardButton('Трапеция')
        d06 = types.KeyboardButton('Ромб')
        d07 = types.KeyboardButton('Параллелограмм')
        d08 = types.KeyboardButton('Многоугольник')
        markup.add(back, allOpr, d01, d02, d03, d04, d05, d06, d07, d08,)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)


    elif message.text == "Все определения":
        bot.send_message(message.chat.id, 'Квадрат — правильный четырёхугольник, у которого все стороны и углы равны между собой.\n\nКруг — множество точек плоскости, удаленных от заданной точки этой плоскости (центр круга — o) на расстояние, не превышающее заданное (радиус круга) \n\nПрямоугольник - это четырехугольник у которого две противоположные стороны равны и все четыре угла одинаковы. Прямоугольники отличаются между собой только отношением длинной стороны к короткой, но все четыре угла у них прямые, то есть по 90 градусов. Длинную сторону прямоугольника называют длиной прямоугольника, а короткую - шириной прямоугольника.\n\nТреуго́льник (в евклидовом пространстве) — это геометрическая фигура, образованная тремя отрезками, которые соединяют три не лежащие на одной прямой точки. Три точки, образующие треугольник, называются вершинами треугольника, а отрезки — сторонами треугольника. Стороны треугольника образуют в вершинах треугольника три угла.\n\nТрапецией называется четырехугольник, у которого две стороны параллельны а две другие − нет.\n\nЧетырёхугольник, в котором все стороны равны, называется ромбом.\n\nПараллелограмм — это четырехугольник, у которого противоположные стороны попарно параллельны и равны.\n\nМногоугольник – фигура, состоящая из нескольких точек (больше двух) и соответствующего количества отрезков, которые их последовательно соединяют. Эти точки называются вершинами многоугольника, а отрезки – сторонами.',parse_mode='html')

    elif message.text == "Круг и Окружность":
       photo100 = open('Круг.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Круга и Окружности:', parse_mode='html')
       bot.send_photo(message.chat.id,photo100)

    elif message.text == "Квадрат":
       photo101 = open('Квадрат.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Квадрата:', parse_mode='html')
       bot.send_photo(message.chat.id, photo101)

    elif message.text == "Треугольник":
       photo102 = open('Треугольник.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Треугольника:\n\nТреуго́льник (в евклидовом пространстве) — это геометрическая фигура, образованная тремя отрезками, которые соединяют три не лежащие на одной прямой точки. Три точки, образующие треугольник, называются вершинами треугольника, а отрезки — сторонами треугольника. Стороны треугольника образуют в вершинах треугольника три угла.', parse_mode='html')
       bot.send_photo(message.chat.id, photo102)

    elif message.text == "Прямоугольник":
       photo103 = open('Прямоугольник.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Прямоугольника:\n\nПрямоугольник - это четырехугольник у которого две противоположные стороны равны и все четыре угла одинаковы. Прямоугольники отличаются между собой только отношением длинной стороны к короткой, но все четыре угла у них прямые, то есть по 90 градусов. Длинную сторону прямоугольника называют длиной прямоугольника, а короткую - шириной прямоугольника.', parse_mode='html')
       bot.send_photo(message.chat.id, photo103)

    elif message.text == "Трапеция":
        photo104 = open('Трапеция.png', 'rb')
        bot.send_message(message.chat.id, 'Определение Трапеции:', parse_mode='html')
        bot.send_photo(message.chat.id, photo104)

    elif message.text == "Ромб":
       photo105 = open('Ромб.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Ромба:', parse_mode='html')
       bot.send_photo(message.chat.id, photo105)

    elif message.text == "Параллелограмм":
       photo106 = open('параллелограмм.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Параллелограмма:', parse_mode='html')
       bot.send_photo(message.chat.id, photo106)

    elif message.text == "Многоугольник":
       photo107 = open('Многоугольник.png', 'rb')
       bot.send_message(message.chat.id, 'Определение Многоугольника:\n\nМногоугольник – фигура, состоящая из нескольких точек (больше двух) и соответствующего количества отрезков, которые их последовательно соединяют. Эти точки называются вершинами многоугольника, а отрезки – сторонами. При этом никакие две смежные стороны не лежат на одной прямой и никакие две несмежные стороны не пересекаются.', parse_mode='html')
       bot.send_photo(message.chat.id, photo107)

    elif message.text == "Фигуры":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       k01 = types.KeyboardButton('Круг и Окружностьㅤ')
       k02 = types.KeyboardButton('Квадратㅤ')
       k03 = types.KeyboardButton('Треугольникㅤ')
       k04 = types.KeyboardButton('Прямоугольникㅤ')
       k05 = types.KeyboardButton('Трапецияㅤ')
       k06 = types.KeyboardButton('Ромбㅤ')
       k07 = types.KeyboardButton('Параллелограммㅤ')
       k08 = types.KeyboardButton('Многоугольникиㅤ')
       k09 = types.KeyboardButton('Прямые и углы')
       k10 = types.KeyboardButton('Векторы')
       markup.add(back, k01, k02, k03, k04, k05, k06, k07, k08,k09,k10)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Круг и Окружностьㅤ":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       n01 = types.KeyboardButton('Основные определения')
       n02 = types.KeyboardButton('Длины и площади')
       n03 = types.KeyboardButton('Свойства углов на окружности')
       n04 = types.KeyboardButton('Свойства линий на окружности')
       n05 = types.KeyboardButton('Две окружности')
       markup.add(back, n01, n02, n03, n04, n05)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Основные определения":
       photoff01 = open('ff01.jpg', 'rb')
       photoff011 = open('ff01.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основыные определения:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff01)
       bot.send_photo(message.chat.id, photoff011)

    elif message.text == "Длины и площади":
       photoff02 = open('ff02.jpg', 'rb')
       bot.send_message(message.chat.id, 'Длины и площади:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff02)

    elif message.text == "Свойства углов на окружности":
       photoff03 = open('ff03.jpg', 'rb')
       photoff033 = open('ff033.jpg', 'rb')
       bot.send_message(message.chat.id, 'Свойства углов на окружности:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff03)
       bot.send_photo(message.chat.id, photoff033)

    elif message.text == "Свойства линий на окружности":
       photoff04 = open('ff04.jpg', 'rb')
       bot.send_message(message.chat.id, 'Свойства линий на окружности:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff04)

    elif message.text == "Две окружности":
       photoff05 = open('ff05.jpg', 'rb')
       photoff055 = open('ff055.jpg', 'rb')
       bot.send_message(message.chat.id, 'Две окружности:', parse_mode='html')
       bot.send_photo(message.chat.id, photoff05)
       bot.send_photo(message.chat.id, photoff055)

    elif message.text == "Квадратㅤ":
       photouu01 = open('uu01.jpg', 'rb')
       photouu02 = open('uu02.jpg', 'rb')
       bot.send_message(message.chat.id, 'Квадрат:', parse_mode='html')
       bot.send_photo(message.chat.id, photouu01)
       bot.send_photo(message.chat.id, photouu02)

    elif message.text == "Треугольникㅤ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        zxc1 = types.KeyboardButton('Произвольный треугольник')
        zxc2 = types.KeyboardButton('Вписанный и описанный треугольник')
        zxc3 = types.KeyboardButton('Замечательные линии треугольника')
        zxc4 = types.KeyboardButton('Равенство и подобие')
        zxc5 = types.KeyboardButton('Равнобедоенный треугольник')
        zxc6 = types.KeyboardButton('Равносторонний треугольник')
        zxc7 = types.KeyboardButton('Прямоугольный треугольник')
        zxc8 = types.KeyboardButton('Основные теоремы')
        markup.add(back, zxc1,zxc2,zxc3,zxc4,zxc5,zxc6,zxc7,zxc8)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Произвольный треугольник":
       photot1 = open('zxc1.jpg', 'rb')
       photot11 = open('zxc11.jpg', 'rb')
       bot.send_message(message.chat.id, 'Произвольный треугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photot1)
       bot.send_photo(message.chat.id, photot11)

    elif message.text == "Вписанный и описанный треугольник":
       photot2 = open('zxc2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Вписанный и описанный треугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photot2)

    elif message.text == "Замечательные линии треугольника":
       photot3 = open('zxc3.jpg', 'rb')
       photot33 = open('zxc33.jpg', 'rb')
       photot333 = open('zxc333.jpg', 'rb')
       photot3333 = open('zxc3333.jpg', 'rb')
       bot.send_message(message.chat.id, 'Замечательные линии треугольника:', parse_mode='html')
       bot.send_photo(message.chat.id, photot3)
       bot.send_photo(message.chat.id, photot33)
       bot.send_photo(message.chat.id, photot333)
       bot.send_photo(message.chat.id, photot3333)

    elif message.text == "Равенство и подобие":
       photot4 = open('zxc4.jpg', 'rb')
       bot.send_message(message.chat.id, 'Равенство и подобие:', parse_mode='html')
       bot.send_photo(message.chat.id, photot4)

    elif message.text == "Равнобедоенный треугольник":
       photot5 = open('zxc5.jpg', 'rb')
       bot.send_message(message.chat.id, 'Равнобедоенный треугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photot5)

    elif message.text == "Равносторонний треугольник":
       photot6 = open('zxc6.jpg', 'rb')
       photot66 = open('zxc66.jpg', 'rb')
       bot.send_message(message.chat.id, 'Равносторонний треугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photot6)
       bot.send_photo(message.chat.id, photot66)

    elif message.text == "Прямоугольный треугольник":
       photot7 = open('zxc7.jpg', 'rb')
       photot77 = open('zxc77.jpg', 'rb')
       photot777 = open('zxc777.jpg', 'rb')
       photot7777 = open('zxc7777.jpg', 'rb')
       photot77777 = open('zxc77777.jpg', 'rb')
       bot.send_message(message.chat.id, 'Прямоугольный треугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photot7)
       bot.send_photo(message.chat.id, photot77)
       bot.send_photo(message.chat.id, photot777)
       bot.send_photo(message.chat.id, photot7777)
       bot.send_photo(message.chat.id, photot77777)

    elif message.text == "Основные теоремы":
       photot8 = open('zxc8.jpg', 'rb')
       photot88 = open('zxc88.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные теоремы:', parse_mode='html')
       bot.send_photo(message.chat.id, photot8)
       bot.send_photo(message.chat.id, photot88)

    elif message.text == "Прямоугольникㅤ":
       photo300 = open('300.jpg', 'rb')
       photo301 = open('301.jpg', 'rb')
       bot.send_message(message.chat.id, 'Прямоугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photo300)
       bot.send_photo(message.chat.id, photo301)

    elif message.text == "Трапецияㅤ":
       photo400 = open('gang01.jpg', 'rb')
       photo401 = open('gang02.jpg', 'rb')
       photo403 = open('gang03.jpg', 'rb')
       photo404 = open('gang04.jpg', 'rb')
       bot.send_message(message.chat.id, 'Трапеция:', parse_mode='html')
       bot.send_photo(message.chat.id, photo400)
       bot.send_photo(message.chat.id, photo401)
       bot.send_photo(message.chat.id, photo403)
       bot.send_photo(message.chat.id, photo404)

    elif message.text == "Ромбㅤ":
       photoholo1 = open('holo1.jpg', 'rb')
       photoholo2 = open('holo2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Ромб:', parse_mode='html')
       bot.send_photo(message.chat.id, photoholo1)
       bot.send_photo(message.chat.id, photoholo2)

    elif message.text == "Параллелограммㅤ":
       photodota1 = open('dota1.jpg', 'rb')
       photodota2 = open('dota2.jpg', 'rb')
       photodota3 = open('dota3.jpg', 'rb')
       bot.send_message(message.chat.id, 'Параллелограмм:', parse_mode='html')
       bot.send_photo(message.chat.id, photodota1)
       bot.send_photo(message.chat.id, photodota2)
       bot.send_photo(message.chat.id, photodota3)


    elif message.text == "Многоугольникиㅤ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        back = types.KeyboardButton('Вернуться в главное меню⬅')
        gang1 = types.KeyboardButton('Произвольный многоугольник')
        gang2 = types.KeyboardButton('Правильный многоугольник')
        markup.add(back, gang1, gang2)
        bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Произвольный многоугольник":
       photogang01 = open('gang01.jpg', 'rb')
       photogang011 = open('gang02.jpg', 'rb')
       bot.send_message(message.chat.id, 'Произвольный многоугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photogang01)
       bot.send_photo(message.chat.id, photogang011)

    elif message.text == "Правильный многоугольник":
       photogang02 = open('gang03.jpg', 'rb')
       photogang022 = open('gang04.jpg', 'rb')
       bot.send_message(message.chat.id, 'Правильный многоугольник:', parse_mode='html')
       bot.send_photo(message.chat.id, photogang02)
       bot.send_photo(message.chat.id, photogang022)

    elif message.text == "Прямые и углы":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       ufo01 = types.KeyboardButton('Прямые')
       ufo02 = types.KeyboardButton('Углы на плоскости')
       markup.add(back, ufo01, ufo02,)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Прямые":
       photoufo1 = open('ufo1.jpg', 'rb')
       bot.send_message(message.chat.id, 'Прямые:', parse_mode='html')
       bot.send_photo(message.chat.id, photoufo1)

    elif message.text == "Углы на плоскости":
       photoufo2 = open('ufo2.jpg', 'rb')
       bot.send_message(message.chat.id, 'Углы на плоскости:', parse_mode='html')
       bot.send_photo(message.chat.id, photoufo2)

    elif message.text == "Векторы":
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
       back = types.KeyboardButton('Вернуться в главное меню⬅')
       rar01 = types.KeyboardButton('Основные свойства векторов')
       rar02 = types.KeyboardButton('Действия над векторами')
       rar03 = types.KeyboardButton('Координаты и длины')
       rar04 = types.KeyboardButton('Взаимное расположение векторов')
       markup.add(back, rar01, rar02, rar03, rar04)
       bot.send_message(message.chat.id, 'Выбери тему:', reply_markup=markup)

    elif message.text == "Основные свойства векторов":
       photo500 = open('500.jpg', 'rb')
       bot.send_message(message.chat.id, 'Основные свойства векторов:', parse_mode='html')
       bot.send_photo(message.chat.id,photo500)

    elif message.text == "Действия над векторами":
       photo501 = open('501.jpg', 'rb')
       photo5011 = open('5011.jpg', 'rb')
       bot.send_message(message.chat.id, 'Действия над векторами:', parse_mode='html')
       bot.send_photo(message.chat.id,photo501)
       bot.send_photo(message.chat.id, photo5011)

    elif message.text == "Координаты и длины":
       photo502 = open('502.jpg', 'rb')
       bot.send_message(message.chat.id, 'Координаты и длины:', parse_mode='html')
       bot.send_photo(message.chat.id,photo502)

    elif message.text == "Взаимное расположение векторов":
       photo503 = open('503.jpg', 'rb')
       photo5033 = open('5033.jpg', 'rb')
       bot.send_message(message.chat.id, 'Взаимное расположение векторов:', parse_mode='html')
       bot.send_photo(message.chat.id, photo503)
       bot.send_photo(message.chat.id, photo5033)


    elif message.text == "01. Аксиомы планиметрии.":
       photo1 = open('01.png', 'rb')
       bot.send_message(message.chat.id, '01. Аксиомы планиметрии.', parse_mode='html')
       bot.send_photo(message.chat.id,photo1)

    elif message.text == "02. Углы":
       photo2 = open('02.png', 'rb')
       bot.send_message(message.chat.id, '02. Углы', parse_mode='html')
       bot.send_photo(message.chat.id,photo2)

    elif message.text == "03. Параллельные прямые. Перпендикулярные прямые. Перпендикуляр к прямой":
        photo3 = open('03.png', 'rb')
        bot.send_message(message.chat.id, '03. Параллельные прямые. Перпендикулярные прямые. Перпендикуляр к прямой', parse_mode='html')
        bot.send_photo(message.chat.id, photo3)

    elif message.text == "04. Свойства сторон и углов треугольника":
        photo4 = open('04.png', 'rb')
        bot.send_message(message.chat.id, '04. Свойства сторон и углов треугольника', parse_mode='html')
        bot.send_photo(message.chat.id, photo4)

    elif message.text == "05. Равенство треугольников.":
        photo5 = open('05.png', 'rb')
        bot.send_message(message.chat.id, '05. Равенство треугольников.', parse_mode='html')
        bot.send_photo(message.chat.id, photo5)

    elif message.text == "06. Медиана треугольника.":
        photo6 = open('06.png', 'rb')
        bot.send_message(message.chat.id, '06. Медиана треугольника.', parse_mode='html')
        bot.send_photo(message.chat.id, photo6)

    elif message.text == "07. Биссектриса треугольника.":
        photo7 = open('07.png', 'rb')
        bot.send_message(message.chat.id, '07. Биссектриса треугольника.', parse_mode='html')
        bot.send_photo(message.chat.id, photo7)

    elif message.text == "08. Высота треугольника":
        photo8 = open('08.png', 'rb')
        bot.send_message(message.chat.id, '08. Высота треугольника', parse_mode='html')
        bot.send_photo(message.chat.id, photo8)

    elif message.text == "09. Средняя линия треугольника":
        photo9 = open('09.png', 'rb')
        bot.send_message(message.chat.id, '09. Средняя линия треугольника', parse_mode='html')
        bot.send_photo(message.chat.id, photo9)

    elif message.text == "10. Соотношение между элементами прямоугольного треугольника":
        photo10 = open('10.png', 'rb')
        bot.send_message(message.chat.id, '10. Соотношение между элементами прямоугольного треугольника', parse_mode='html')
        bot.send_photo(message.chat.id, photo10)

    elif message.text == "11. Соотношение между сторонами и углами в произвольном треугольнике":
        photo11 = open('11.png', 'rb')
        bot.send_message(message.chat.id, '11. Соотношение между сторонами и углами в произвольном треугольнике', parse_mode='html')
        bot.send_photo(message.chat.id, photo11)

    elif message.text == "12. Преобразование фигур. Движение":
        photo12 = open('12.png', 'rb')
        bot.send_message(message.chat.id, '12. Преобразование фигур. Движение', parse_mode='html')
        bot.send_photo(message.chat.id, photo12)

    elif message.text == "13. Преобразование подобия":
        photo13 = open('13.png', 'rb')
        bot.send_message(message.chat.id, '13. Преобразование подобия', parse_mode='html')
        bot.send_photo(message.chat.id, photo13)

    elif message.text == "14. Подобие треугольников.":
        photo14 = open('14.png', 'rb')
        bot.send_message(message.chat.id, '14. Подобие треугольников.', parse_mode='html')
        bot.send_photo(message.chat.id, photo14)

    elif message.text == "15. Параллелограмм и его виды.":
        photo15 = open('15.png', 'rb')
        bot.send_message(message.chat.id, '15. Параллелограмм и его виды.', parse_mode='html')
        bot.send_photo(message.chat.id, photo15)

    elif message.text == "16. Трапеция":
        photo16 = open('16.png', 'rb')
        bot.send_message(message.chat.id, '16. Трапеция', parse_mode='html')
        bot.send_photo(message.chat.id, photo16)

    elif message.text == "17. Окружность, хорды и дуги":
        photo17 = open('17.png', 'rb')
        bot.send_message(message.chat.id, '17. Окружность, хорды и дуги', parse_mode='html')
        bot.send_photo(message.chat.id, photo17)

    elif message.text == "18. Окружность. Касательные и секущие.":
        photo18 = open('18.png', 'rb')
        bot.send_message(message.chat.id, '18. Окружность. Касательные и секущие.', parse_mode='html')
        bot.send_photo(message.chat.id, photo18)

    elif message.text == "19. Взаимное расположение прямой и окружности. Взаимное расположение двух окружностей.":
        photo19 = open('19.png', 'rb')
        bot.send_message(message.chat.id, '19. Взаимное расположение прямой и окружности. Взаимное расположение двух окружностей.', parse_mode='html')
        bot.send_photo(message.chat.id, photo19)

    elif message.text == "20. Общие касательные двух окружностей.":
        photo20 = open('20.png', 'rb')
        bot.send_message(message.chat.id, '20. Общие касательные двух окружностей.', parse_mode='html')
        bot.send_photo(message.chat.id, photo20)

    elif message.text == "21. Углы в окружности.":
        photo21 = open('21.png', 'rb')
        bot.send_message(message.chat.id, '21. Углы в окружности.', parse_mode='html')
        bot.send_photo(message.chat.id, photo21)

    elif message.text == "22. Длина окружности и её частей. Площадь круга и его частей":
        photo22 = open('22.png', 'rb')
        bot.send_message(message.chat.id, '22. Длина окружности и её частей. Площадь круга и его частей', parse_mode='html')
        bot.send_photo(message.chat.id, photo22)

    elif message.text == "23. Вписанный и описанный многоугольники. Вписанный и описанный четырехугольники. Прямоугольник. Трапеция и ромб. Квадрат.":
        photo23 = open('23.png', 'rb')
        bot.send_message(message.chat.id, '23. Вписанный и описанный многоугольники. Вписанный и описанный четырехугольники. Прямоугольник. Трапеция и ромб. Квадрат.', parse_mode='html')
        bot.send_photo(message.chat.id, photo23)

    elif message.text == "24. Окружность, описанная около треугольника, и окружность, вписанная в треугольник.":
        photo24 = open('24.png', 'rb')
        bot.send_message(message.chat.id, '24. Окружность, описанная около треугольника, и окружность, вписанная в треугольник.', parse_mode='html')
        bot.send_photo(message.chat.id, photo24)

    elif message.text == "25. Окружности, описанные и вписанные в правильные многоугольники":
        photo25 = open('25.png', 'rb')
        bot.send_message(message.chat.id, '25. Окружности, описанные и вписанные в правильные многоугольники', parse_mode='html')
        bot.send_photo(message.chat.id, photo25)

    elif message.text == "26. Площади треугольников.":
        photo26 = open('26.png', 'rb')
        bot.send_message(message.chat.id, '26. Площади треугольников.', parse_mode='html')
        bot.send_photo(message.chat.id, photo26)

    elif message.text == "27. Площади четырехугольников.":
        photo27 = open('27.png', 'rb')
        bot.send_message(message.chat.id, '27. Площади четырехугольников.', parse_mode='html')
        bot.send_photo(message.chat.id, photo27)

    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю.\nНапиши ➡/help⬅ ', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Эта фотка мне не нравится...', parse_mode='html')


bot.polling(none_stop=True)