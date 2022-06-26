def _get_result(item):
    # 1
    if (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <фарминг> и <спуфинг> и <метод обратной инженерии> и <osint> и <поддельные лэндинг-страницы> и <торрент-сервисы>  и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 2
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <фарминг> и  <спуфинг>  и <сообщение в досках объявлений>  и <поддельные лэндинг-страницы> и  <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 3
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <метод обратной инженерии> и <фарминг>  и  <спуфинг>  и <мессенджеры> и <торрент-сервисы>   и <osint> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 4
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <спуфинг> и <фарминг>   и <метод обратной инженерии> и <сообщение в досках объявлений> и <мессенджеры> и <osint> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО>  и <контроль со стороны опекунов>"
    # 5
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 6
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <фарминг> и  <спуфинг> и<торрент-сервисы>  <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 7
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <фарминг> и  <метод обратной инженерии> и <сообщение в досках объявлений> и  <торрент-сервисы> и <osint> и  <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 8
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг> и  <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО>"
    # 9
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>  и <сообщение в досках объявлений> и <поддельные лэндинг-страницы> и <торрент-сервисы>   и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов"
    # 10
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>  и  <сообщение в досках объявлений> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 11
    if (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>   и <сообщение в досках объявлений> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 12
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 13
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг>  и <фарминг> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 14
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и <торрент-сервисы>  и  <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов>"
    # 15
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и  <сообщение в досках объявлений> и <смс-рассылка> и<соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 16
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <смишинг> и <спуфинг> и  <фарминг>  и  <метод обратной инженерии> и <osint> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и  <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 17
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы>  и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 18
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и  <сообщение в досках объявлений> и <смс-рассылка> и<соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 19
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <трэшхантинг> и <телефонный звонок> и <мессенджеры> и  <сообщение в досках объявлений> и <смс-рассылка> и<соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 20
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <спуфинг> и <смишинг> и  <фарминг>   и <метод обратной инженерии> и <трэшхантинг> и <телефонный звонок> и <мессенджеры> и <смс-рассылка> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 21
    if (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 22
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <спуфинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и  <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 23
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <смишинг> и <фарминг> и <спуфинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <смс-рассылка> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 24
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <спуфинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 25
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <смишинг> и <спуфинг> и <трэшхантинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 26
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <спуфинг> и <телефонный звонок> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 27
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <смишинг>и <вишинг> и  <фарминг>  и <спуфинг> и <смс-рассылка> и  <телефонный звонок> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 28
    elif (
        (str(item.work) == "не работает")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <спуфинг> и <торрент-сервисы> и  <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <обучение основам ИБ> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <контроль со стороны опекунов> и <использование защиты почтового ящика>"
    # 29
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы>  и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 30
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>   и <сообщение в досках объявлений> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 31
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <фарминг> и <метод обратной инженерии> и<спуфинг> и <osint> и <интернет-разведка> и <торрент-сервисы>  и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 32
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <торрент-сервисы> и <сообщение в досках объявлений>   и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 33
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <сообщение в досках объявлений>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 34
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 35
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и  <поддельные лэндинг-страницы>  и <торрент-сервисы>  и <мессенджеры> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 36
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 37
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 38
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<устойчив к СИ-угрозам> "
    # 39
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>  и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 40
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и <сообщение в досках объявлений>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 41
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>   и <спуфинг> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 42
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 43
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 44
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и <спуфинг> и  <фарминг>  и <смишинг> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 45
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 46
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 47
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и  <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 48
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и  <фарминг>  и <спуфинг> и <смишинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 49
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 50
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 51
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 52
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 53
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 54
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 55
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 56
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "руководитель")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 57
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <сообщение/письмо от руководства> и <торрент-сервисы>  > и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 58
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 59
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <сообщение/письмо от руководства> и <торрент-сервисы>  > и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 60
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <торрент-сервисы> и <сообщение в досках объявлений>  и <сообщение/письмо от руководства> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 61
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <сообщение в досках объявлений>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 62
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и  <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 63
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <поддельные лэндинг-страницы>  и <торрент-сервисы> и <сообщение/письмо от руководства> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 64
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 65
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 66
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<устойчив к СИ-угрозам>"
    # 67
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>  и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 68
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и <сообщение в досках объявлений>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 69
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>   и <спуфинг> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 70
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 71
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и  <сообщение/письмо от руководства> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 72
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и <спуфинг> и  <фарминг>  и <смишинг> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и   <сообщение/письмо от руководства> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 73
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и<сообщение/письмо от руководства>и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 74
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <сообщение/письмо от руководства> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 75
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и  <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 76
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и  <фарминг>  и <спуфинг> и <смишинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 77
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <сообщение/письмо от руководства> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 78
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 79
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 80
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 81
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок>  и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 82
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 83
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 84
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "сотрудник отдела")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 85
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <сообщение/письмо от руководства> и <торрент-сервисы>  > и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 86
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 87
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <сообщение/письмо от руководства> и <торрент-сервисы>  > и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 88
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <торрент-сервисы> и <сообщение в досках объявлений>  и <сообщение/письмо от руководства> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 89
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и  <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 90
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и  <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 91
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <метод обратной инженерии> и <спуфинг> и <osint> и <интернет-разведка> и <поддельные лэндинг-страницы> и <торрент-сервисы> и <сообщение/письмо от руководства> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 92
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 93
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>  и <спуфинг> и <поддельные лэндинг-страницы> и <сообщение в досках объявлений и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 94
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<устойчив к СИ-угрозам>"
    # 95
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и  <фарминг>  и <поддельные лэндинг-страницы> и <сообщение в досках объявлений>  и <торрент-сервисы>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 96
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <спуфинг> и <сообщение в досках объявлений>  и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 97
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг>   и <спуфинг> и <поддельные лэндинг-страницы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 98
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "высокий и средний")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и  <фарминг> и <спуфинг> и <поддельные лэндинг-страницы> и <торрент-сервисы> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 99
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и  <сообщение/письмо от руководства> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 100
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <метод обратной инженерии> и <спуфинг> и  <фарминг>  и <смишинг> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и   <сообщение/письмо от руководства> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 101
    if (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <трэшхантинг> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и<сообщение/письмо от руководства>и <поддельные лэндинг-страницы> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 102
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <сообщение/письмо от руководства> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и <штрафные санкции>"
    # 103
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и  <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 104
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и  <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 105
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "не анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <сообщение/письмо от руководства> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 106
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <смишинг> и <osint> и <торрент-сервисы> и <интернет-разведка> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <смс-рассылка> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 107
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 108
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 109
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <трэшхантинг> и <сообщение в досках объявлений> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 110
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "активен")
        and (str(item.activity_on_online_trading_platforms) == "не активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 111
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "не активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <телефонный звонок> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
    # 112
    elif (
        (str(item.work) == "работает")
        and (str(item.position) == "обслуживающий персонал")
        and (str(item.level_of_awareness) == "низкий")
        and (str(item.activity_in_social_networks) == "активен")
        and (str(item.message_board_activity) == "не активен")
        and (str(item.activity_on_online_trading_platforms) == "активен")
        and (str(item.anonymity_on_the_internet) == "анонимен")
        and (str(item.use_of_reaction_enhancers) == "да")
    ):
        return "<фишинг> и <вишинг> и <фарминг> и <метод обратной инженерии> и <спуфинг> и <торрент-сервисы> и <телефонный звонок> и <мессенджеры> и <поддельные лэндинг-страницы> и <трэшхантинг> и <соблюдение рекомендаций по кибергигиене> и <использование антивирусного ПО, настройка функции антиспам антивирусного ПО> и <использование защиты почтового ящика> и <СИ-пентестинг: имитационный сценарий фишинга> и <СИ-пентестинг: имитационный сценарий вишинга> и <обучение с проверкой осведомленности> и  <штрафные санкции>"
