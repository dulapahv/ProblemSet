def fahrenheit(celcius):
    """ คืนค่ากลับเป็นอุณหภูมิองศาฟาเรนไฮต์ (F) """

    ### BEGIN SOLUTION

    fahrenheit=(celcius * 9/5 + 32)
    return fahrenheit


    ## END SOLUTION


celcius = int(input('ใส่อุณหภูมิในหน่วยองศาเซลเซียส (C):'))
print('อุณหภูมิในหน่วยองศาฟาเรนไฮต์คือ ', fahrenheit(celcius), 'F')