translations = {
    'ru': {
        'choose_option': 'Выберите одно из следующих!\n\n\n',
        'choose_language': 'выберем язык обслуживания!',
        'back_to_menu': 'Вы вернулись в главное меню',
        'language_set': 'Язык установлен на русский',
        'products': 'Продукты',
        'my_orders': 'Мои заказы',
        'language_settings': 'Язык(ru/uz)',
        'send_phone_prompt': 'Привет! Нажмите на кнопку ниже, чтобы отправить свой номер телефона.',
        'phone_received': 'Спасибо за предоставленный номер телефона ({0}). ',
        'send_location_prompt': 'Теперь нажмите на кнопку ниже, чтобы отправить свою локацию.',
        'location_received': 'Локация получена: ({}, {})',
        'street_name': 'Название улицы: {}',
        'choose_option_location': 'Пожалуйста, выберите опцию:',
        'back': 'Назад',
        'send_phone': 'Отправить мой номер',
        'send_location': 'Отправить мою локацию',
        'support': 'Вы можете связаться с администратором. Пожалуйста, опишите вашу проблему сюда - @secdeee1',
        'buy': "Здесь вы можете купить наши продукты!"
    },
    'uz': {
        'choose_option': 'Quyidagi variantlardan birini tanlang!\n\n\n',
        'choose_language': 'Xizmat tilini tanlang!',
        'back_to_menu': 'Asosiy menyuga qaytdingiz',
        'language_set': 'Til o‘rnatildi: o‘zbekcha',
        'products': 'Mahsulotlar',
        'my_orders': 'Buyurtmalarim',
        'language_settings': 'Til(ru/uz)',
        'send_phone_prompt': 'Salom! Telefon raqamingizni yuborish uchun quyidagi tugmani bosing.',
        'phone_received': 'Berilgan telefon raqamingiz uchun rahmat ({0}).',
        'send_location_prompt': 'Endi joylashuvingizni yuborish uchun quyidagi tugmani bosing.',
        'location_received': 'Локация получена: ({}, {})',
        'street_name': 'Название улицы: {}',
        'choose_option_location': 'Пожалуйста, выберите опцию:',
        'back': 'Ortga',
        'send_phone': 'Telefon raqamimni yuborish',
        'send_location': 'Mening joylashuvimni yuborish',
        'support': 'Siz administratorga murojaat qilishingiz mumkin. Muammoingizni shu yerda tasvirlab bering - @secdeee1',
        'buy': "Bu yerda siz bizning mahsulotlarimizni xarid qilishingiz mumkin!"
    }
}


def get_translation(key, language):
    return translations.get(language, {}).get(key, key)
