### ✅ Описание функциональности:
****
#### Название бота: ChatGuardBot

##### Описание функциональности:

###### 2.1. Удаление ссылок на другие чаты и каналы Telegram:

- Бот должен отслеживать все сообщения, отправленные участниками чата.
- Если сообщение содержит ссылку на другой чат или канал Telegram, бот должен удалить это сообщение автоматически.
- В случае удаления сообщения бот должен отправлять уведомление в чат о том, что ссылка была удалена.

###### 2.2. Предупреждение о нарушении правил:

- Если участник чата отправляет ссылку на другой чат или канал Telegram, бот должен отправлять уведомление о нарушении правил.
- Уведомление должно содержать информацию о том, что при повторном нарушении будет применена блокировка на 24 часа.

###### 2.3. Блокировка участника чата:

- Если участник чата второй раз отправляет ссылку на другой чат или канал Telegram, бот должен блокировать этого участника на 24 часа.
- Во время блокировки участник не сможет отправлять сообщения в чат.
- После истечения 24 часов бот должен автоматически снять блокировку с участника.
- Бот должен отправлять уведомление в чат о блокировке и разблокировке участника.

###### 2.4. Приветственное сообщение для новых участников:

- При добавлении нового участника в чат, бот отправляет приветственное сообщение в чат / группу.
- Приветственное сообщение должно содержать текст, предоставленный в задании:
 
      Привет, @имя!
      Добро пожаловать в чат подружки.
      Чат создан для общения и встреч.
      Ознакомься, пожалуйста, с правилами чата.
      Если заскучала, предлагай встречу.
      Или приходи на те, которые предлагают девчонки в чате.