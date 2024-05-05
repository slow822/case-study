diem = 0
cauhoi = ['cau1', 'cau2', 
          'cau3', 'cau4', 
          'cau5', 'cau6', 
          'cau7', 'cau8', 
          'cau9', 'cau10']
def question(a):
    a=a-1
    global choncau
    global diem
    global cau
    global cauhoi
    if cau == cauhoi[0]:
        print("Câu hỏi: 1 + 1 bằng bao nhiêu")
        print("a) 1")
        print("b) 2")
        print("c) 3")
        print("d) 4")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'b':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
            
    if cau == cauhoi[1]:
        print("Trong 26 chữ cái của bảng chữ cái tiếng Anh, chữ cái nào đứng đầu tiên?")
        print("a) G")
        print("b) F")
        print("c) A")
        print("d) X")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'c':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
            
    if cau == cauhoi[2]:
        print("Ai là người phát minh ra đèn điện?")
        print("a) Thomas Edison")
        print("b) Nikola Tesla")
        print("c) Benjamin Franklin")
        print("d) Alexander Graham Bell")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'a':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
            
    if cau == cauhoi[3]:
        print("Câu hỏi: Ai là người đầu tiên đặt chân lên mặt trăng?")
        print("a) Neil Armstrong")
        print("b) Buzz Aldrin")
        print("c) Yuri Gagarin")
        print("d) John Glenn")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'a':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[4]:
        print("Câu hỏi: Mùa nào nóng nhất?")
        print("a) Mùa Xuân")
        print("b) Mùa Hè")
        print("c) Mùa Thu")
        print("d) Mùa Đông")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'b':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[5]:
        print("Câu hỏi: Ai là người đầu tiên đặt chân lên mặt trăng?")
        print("a) Bill Gates")
        print("b) Steve Jobs")
        print("c) Jeff Bezos")
        print("d) Mark Zuckerberg")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'd':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[6]:
        print("Câu hỏi: Màu của lá cây thường là gì?")
        print("a) trắng")
        print("b) tím")
        print("c) xanh lá")
        print("d) hồng")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'c':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[7]:
        print("Câu hỏi: Loại thú nhỏ nhất trong đây là gì?")
        print("a) Chuột")
        print("b) Kiến")
        print("c) Bò")
        print("d) cá heo")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'b':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[8]:
        print("Câu hỏi: Con người có bao nhiêu chân?")
        print("a) 2")
        print("b) 102")
        print("c) 33")
        print("d) 9")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'a':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    if cau == cauhoi[9]:
        print("Câu hỏi: Loài vật nào sau đây có khả năng bay cao nhất?")
        print("a) chim cánh cụt")
        print("b) đà điểu")
        print("c) gà")
        print("d) đại bàng")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        z = input()
        if z == 'd':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                    
        else:
            print('sai')
    else :
        print('----------------------------------------------------------------')
        print('xin hay nhap lai')
        print('----------------------------------------------------------------')
    
 
while True:     
    real = ' '.join(cauhoi)  
    print(real)
    choncau = int(input('chon cau: '))
    cau = 'cau'+str(choncau)
    print(cau)
    question(choncau)
            
