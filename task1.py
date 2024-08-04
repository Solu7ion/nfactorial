class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name):
        user_id = self.next_id
        self.users[user_id] = name
        self.next_id += 1
        return user_id

    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def getAllUsers(self):
        return self.users

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

user_manager = UserManager()

# Меню
while True:
    print('-' * 100)
    print("1. Посмотреть всю таблицу")
    print("2. Зарегистрировать пользователя")
    print("3. Найти пользователя по имени")
    print("4. Найти пользователя по ID")
    print("5. Удалить пользователя по ID")
    print("6. Выйти")
    temp = input("Выберите опцию (1-6): ")
    if temp != int:
        temp = input("Выберите опцию (1-6): ")
    match int(temp):
        case 1:
            # Выводим всех пользователей
            users = user_manager.getAllUsers()
            if users:
                for user_id, name in users.items():
                    print(f"ID: {user_id}, Имя: {name}")
            else:
                print("Таблица пользователей пуста.")
        case 2:
            # Добавляем нового пользователя
            name = input("Введите имя пользователя: ")
            user_id = user_manager.addUser(name)
            print(f"Пользователь {name} добавлен с ID {user_id}.")
        case 3:
            # Поиск пользователей по имени
            name = input("Введите имя для поиска: ")
            user_ids = user_manager.findUserByName(name)
            if user_ids:
                print(f"Пользователи с именем {name}: ID {user_ids}")
            else:
                print(f"Пользователей с именем {name} не найдено.")
        case 4:
            # Поиск пользователя по идентификатору
            user_id = int(input("Введите идентификатор пользователя: "))
            user_name = user_manager.getUser(user_id)
            if user_name is not None:
                print(f"Пользователь с ID {user_id}: {user_name}")
            else:
                print(f"Пользователь с ID {user_id} не найден.")
        case 5:
            # Удаление пользователя по ID
            user_id = int(input("Введите ID пользователя для удаления: "))
            success = user_manager.deleteUser(user_id)
            if success:
                print(f"Пользователь с ID {user_id} был успешно удален.")
            else:
                print(f"Пользователь с ID {user_id} не найден.")
        case 6:
            print("Выход...")
            break
        case _:
            print("Неверная опция, попробуйте снова.")



