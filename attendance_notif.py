import shared
import mysql.connector


def take_values(employee_id, attendance_id, date, time_in, time_out):
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="minimumM4.",
                    database="employees"
        )

    cursor1 = mydb.cursor()
    cursor1.execute(f"SELECT * FROM employees WHERE id_number={employee_id}")
    res1 = cursor1.fetchall()

    print(attendance_id, date, time_in, time_out)

    shared.the_date = date
    shared.the_time_in = time_in
    shared.the_time_out = time_out

    for i in res1:
        shared.name = i[0]

