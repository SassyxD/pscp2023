# '''Ejudge'''
# def main():
#     '''Phonenumber'''
#     number = str(input())
#     typeconnection = str(input())
#     if len(number) == 9:
#         if typeconnection == "Domestic":
#             print(int(i) for i in str(number))
#         elif typeconnection == "International":
#             print("+66"+int(i) for i in str(number))
#     elif len(number) == 10:
#         if typeconnection == "Domestic":
#             print(int(i) for i in str(number))
#         elif typeconnection == "International":
#             print("+66"+int(i) for i in str(number))
# main()

def format_phone_number(phone_number, format_type):
    if len(phone_number) == 10:
        formatted_number = f"{phone_number[:2]} {phone_number[2:5]} {phone_number[5:]}"
    elif len(phone_number) == 9:
        formatted_number = f"{phone_number[:1]} {phone_number[1:5]} {phone_number[5:]}"


    if format_type == "Domestic":
        return formatted_number
    elif format_type == "International":
        return f"+66 {formatted_number}"


# อ่านข้อมูลจาก input
phone_number = input().strip()
format_type = input().strip()

# เรียกใช้ฟังก์ชันและพิมพ์ผลลัพธ์
formatted_phone_number = format_phone_number(phone_number, format_type)
print(formatted_phone_number)
