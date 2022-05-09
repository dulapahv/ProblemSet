def remove_at(string, index):
    ### BEGIN SOLUTION
    
    string[:index]
    
    return string[:index]
    ### END SOLUTION
    
string = 'ลองเคี้ยวหมากฝรั่งดูเผื่อหายง่วง'
index = int(input('ใส่เลข Index ของตัวอักษรที่ต้องการตัด: '))
print(remove_at(string, index))

# รันโค้ดต่อไปนี้ ถ้าได้ผลลัพธ์ 'True' 2 ครั้ง = 2 คะแนน (เต็ม)

string1 = 'ลองเคี้ยวหมากฝรั่งดูเผื่อหายง่วง'
string2 = 'ผมตกข่าวมากเลยครับ เกือบไม่ได้ไปดูงาน NIKON DAY 2006?'
print(string1.find('ก'))
print(string2.find('่'))

print(remove_at(string1, 12)=='ลองเคี้ยวหมาฝรั่งดูเผื่อหายง่วง')
print(remove_at(string2, 5)=='ผมตกขาวมากเลยครับ เกือบไม่ได้ไปดูงาน NIKON DAY 2006?')