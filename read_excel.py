import pandas
import re
import sys

def read_exce(_sheet):
    # df = pandas.read_excel('CASETA.xlsx', index_col=[0, 1, 2], skiprows=1, sheet_name='DANUBIO', )
    df = pandas.read_excel('DIRECCIONES.xlsx', usecols="A,B", skiprows=0, sheet_name=_sheet, )
    values = df.values

    # print(values)
    for row in values:
        print(f"Calle->{row[1]}, Numero->{row[0]}")
        # address = row[0]
        # address = address.split("#")
        # print(address)
        # if len(address) != 2:
        #     print("ERROR ")
        #     return
        # phone = row[1]
        # if phone:
        #     phone = str(phone)
        #     # print(f"{phone} tipo {type(phone)}")
        #     phone = re.sub("\D", "", phone)
        #     phone = phone[:10]
        #     print(phone)
        # print(row)


        # for element in row:
            # element[0]
            # element = element.split("#")
            # print(element)
            # if len(element) != 2:
            #     print("ERROR ")
            #     return
        print()
    # print(df)

    # df = pandas.read_excel('CASETA.xlsx', sheet_name='DANUBIO')
    # df = df.head()

    # df2 = df.to_dict()

    # df2 = df.to_csv()

    # for key,val in df2.items():
    #     print(f"K:{key}, Val{val}\n")

    # print(df2)

if __name__ == '__main__':
    sheet_name = sys.argv[1]
    read_exce(sheet_name)

    # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    #         print(a[i][j], end=' ')
    #     print()

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()