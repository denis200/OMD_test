# OMD OD TEST

## Installation

```
git clone https://github.com/denis200/OMD_test/
```

Для начала переименуйте  ".env.example"  - > ".env" 

После создайте базу данных postgres и в данный файл введите соответствующие поля.
```
POSTGRES_DB=#db credentials
POSTGRES_PASSWORD=#db credentials
```
Чтобы поднять контейнер, выполните команду:
```
docker-compose up --build
```

## Пояснения к работе проекта

### Запрос на регистрацию:
```
POST http://localhost:8000/auth/users/
```
```
{
  "username":
  "email":
  "password":
}
```
После регистрации пользователя через сигнал автоматически создается таблица пользователя, в которой в будущем будут храниться данные.

### Запрос на авторизацию
```
POST http://localhost:8000/auth/jwt/create/
```
```
{
  "username":
  "password":
}
```

Присылается токен авторизации, который в будущем нужно использовать для запросов

### Запрос на добавление данных
```
POST http://localhost:8000/curve/
```
Можно добавить как одну запись так и массив.Старые данные удаляются

```
[
    {
        "unit": 10000,
        "reach": [9.39, 2.88, 1.71, 1.48, 1.05, 0.83, 0.66, 0.53, 0.44, 0.4]
    },
    {
        "unit": 20000,
        "reach": [17.13, 6.68, 4.37, 2.97, 2.13, 1.68, 1.34, 1.08, 0.9, 0.8]
    }
]
```
Валидация данных происходит в основном во встроенных методах полей сериализатора, хотя это можно исправить. Кастомная валидация написана для поля reach.

### Запрос на получение данных пользователя
```
GET http://localhost:8000/curve/
```
## Ошибки
### Если больше или меньше 10 элементов в массиве
```
"reach": [
            "Ensure this field has no more than 10 elements."
        ]
```
```
"reach": [
            "Ensure this field has at least 10 elements."
        ]
```
### Если отправить строку 

```
"A valid number is required."
```
### Если число больше 100 или меньше нуля
```
"Ensure this value is less than or equal to 100."
```
```
"Ensure this value is greater than or equal to 0."
```
### Если массив не отсортирован
```
"reach": [
            "The array must be sorted in descending order"
        ]
```




