import pyodbc

nome = input('Digite o nome: ') + '%'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='srv-vibpan01',
    Database='sistemas'
)
cursor = conn.cursor()
cursor.execute("SELECT * from usuario WHERE login like '%s'" % nome)
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
    

id = input('Digite o id: ')
mes = input('Digite o mês: ')
dia = input('Digite o dia: ')

cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
    row = cursor.fetchone()

esc = input('Digite o numero da opção: 1 - primeiro horario, 2 - segundo horario, 3 - terceiro horario, 4 - quarto horario, 5 - primeiro e segundo horario, 6 - segundo e terceiro horario, 7 - terceiro e quarto horario: ')


if esc == '1':
    esc2 = input("Insira 's' para inserir horario ou 'n' para valores nulos: ")
    if esc2 == 's':
        id1 = input('Digite o id da data: ')
        print('Ex: 2018-05-24 07:25:07.340')
        data = input('Digite o horario: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data1 = '%s' where id = '%s'" % (data,id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
    if esc2 == 'n':
        id1 = input('Digite o id da data: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data1 = null where id = '%s'" % (id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close

    
if esc == '2':
    esc2 = input("Insira 's' para inserir horario ou 'n' para valores nulos: ")
    if esc2 == 's':
        id1 = input('Digite o id da data: ')
        print('Ex: 2018-05-24 11:30:07.340')
        data = input('Digite o horario: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data2 = '%s' where id = '%s'" % (data,id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
    if esc2 == 'n':
        id1 = input('Digite o id da data: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data2 = null where id = '%s'" % (id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close

if esc == '3':
    esc2 = input("Insira 's' para inserir horario ou 'n' para valores nulos: ")
    if esc2 == 's':
        id1 = input('Digite o id da data: ')
        print('Ex: 2018-05-24 12:30:07.340')
        data = input('Digite o horario: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data3 = '%s' where id = '%s'" % (data,id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
    if esc2 == 'n':
        id1 = input('Digite o id da data: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data3 = null where id = '%s'" % (id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
        
if esc == '4':
    esc2 = input("Insira 's' para inserir horario ou 'n' para valores nulos: ")
    if esc2 == 's':
        id1 = input('Digite o id da data: ')
        print('Ex: 2018-05-24 12:30:07.340')
        data = input('Digite o horario: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data4 = '%s' where id = '%s'" % (data,id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
    if esc2 == 'n':
        id1 = input('Digite o id da data: ')
        cursor.execute("BEGIN TRANSACTION")
        cursor.execute("UPDATE registro set  data4 = null where id = '%s'" % (id1)) 
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
    
            des = input('Digite (S) para confirmar e commitar: ')
            if des == 's':
                conn.commit() 
                cursor.commit()
                cursor.execute('COMMIT TRANSACTION')
                print('Commit enviado com sucesso')
                cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
                row = cursor.fetchone()
            conn.close
    

if esc == '5':
    id1 = input('Digite o id da data: ')
    print('Ex: 2018-05-24 07:25:07.340')
    data = input('Digite o horario: ')
    data1 = input('Digite o horario: ')
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("UPDATE registro set  data1 = '%s', data2 = '%s' where id = '%s'" % (data,id1,id2))
    cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
        row = cursor.fetchone()

    des = input('Digite (S) para confirmar e commitar: ')
    if des == 's':
        conn.commit() 
        cursor.commit()
        cursor.execute('COMMIT TRANSACTION')
        print('Commit enviado com sucesso')
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
        conn.close

if esc == '6':
    id1 = input('Digite o id da data: ')
    print('Ex: 2018-05-24 07:25:07.340')
    data2 = input('Digite o horario: ')
    data3 = input('Digite o horario: ')
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("UPDATE registro set  data2 = '%s', data3 = '%s' WHERE id = '%s'" % (data2,data3,id1))
    cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
        row = cursor.fetchone()

    des = input('Digite (S) para confirmar e commitar: ')
    if des == 's':
       conn.commit() 
       cursor.commit()
       cursor.execute('COMMIT TRANSACTION')
       print('Commit enviado com sucesso')
       cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
       row = cursor.fetchone()
       while row:
           print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
           row = cursor.fetchone()
       conn.close

if esc == '7':
    id1 = input('Digite o id da data: ')
    print('Ex: 2018-05-24 07:25:07.340')
    data = input('Digite o horario: ')
    data1 = input('Digite o horario: ')
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("UPDATE registro set  data3 = '%s', data4 = '%s' where id = '%s'" % (data,id1,id2))
    cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
        row = cursor.fetchone()

    des = input('Digite (S) para confirmar e commitar: ')
    if des == 's':
        conn.commit() 
        cursor.commit()
        cursor.execute('COMMIT TRANSACTION')
        print('Commit enviado com sucesso')
        cursor.execute("SELECT * FROM registro WHERE YEAR(data) = 2018 AND MONTH(data) = '%s' AND DAY(data) = '%s' AND usuario_id = '%s'" % (mes,dia,id))
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]))
            row = cursor.fetchone()
        conn.close


if esc == '0':
    print ('cancelado')
