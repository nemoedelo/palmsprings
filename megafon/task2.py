"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
  Функция должна принимать параметры как именованные аргументы.
  Реализовать вывод данных о пользователе одной строкой."""


# User is allowed to leave some arguments blank
def prettyPrintUser(name="", surname="", birth_date="", city="", email="", phone=""):
    print(f"name:{name}, surname:{surname}, birth_date:{birth_date}, city:{city}, email:{email}, phone:{phone}")


prettyPrintUser(name="Elena", surname="Miliutina")
