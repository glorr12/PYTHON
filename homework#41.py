
import pymysql
import os


cfg = {'host': os.getenv('DB_HOST'),
       'user': os.getenv('DB_USER'),
       'password': os.getenv('DB_PASSWORD'),
       'database': os.getenv('DB_NAME'),
       }

connect = pymysql.connect(**cfg)
if connect.open:
    print('Connected to database')

    cursor = connect.cursor()
    cursor.execute("""
                    select name from world.country
                   """)
    row = cursor.fetchall()

    world_countries = {}

    for _id, (country,) in enumerate(row, start=1):
        print(f"{_id}. {country}")
        world_countries[_id] = country



    input_us = input("Введите страну или её номер: ").strip().capitalize()
    if connect.open:
        print('Connected to database')
    request = """
    SELECT 
        ci.name AS city_name, 
        ci.population AS city_population
    FROM 
        city AS ci
    JOIN 
        country AS co ON ci.CountryCode = co.code
    WHERE 
        co.name = %s
    ORDER BY 
        ci.population DESC
"""

    if input_us.isdigit():
        input_us = int(input_us)
        if 0 >= input_us < len(row):
            print("out of range")

        for _id, country in world_countries.items():
            if _id == input_us:
                input_us = country


    with connect.cursor() as cursor:
        cursor.execute(request, (input_us,))

        result = cursor.fetchall()

    for index, row in enumerate(result, start=1):
        print(f"{index}. {row[0]} - {row[1]}")