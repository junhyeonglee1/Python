import qrcode

with open('Samples/site_list.txt','rt',encoding = 'UTF-8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip() #글자이외의 특수문자나 깔끔하게 정리
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + '.png')

        

