diem = 0
count = 0
import random
cauhoi = ['cau1', 'cau2', 
          'cau3', 'cau4', 
          'cau5', 'cau6', 
          'cau7', 'cau8', 
          'cau9', 'cau10']
help = ['1:50/50','2:sai tru dung cong them']
help1 = True
help2 = True 
print(help[0])

def question(a):
    a=a-1
    global help1
    global help2
    global count
    global choncau
    global diem
    global cau
    global cauhoi
    global help
    global strhelp
    done = True
    help21 = False
    if cau == cauhoi[0]:
        count += 1
        list1 = ['a/ 1','c/ 3','d/ 4']
        print("Câu hỏi: 1 + 1 bằng bao nhiêu")
        print(list1[0])
        print("b) 2")
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        while done == True:
         if z == 'b':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 1:
                print(aa)
                print("b/ 2")   
            else:
                print('b/ 2')
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            done = False
            
    elif cau == cauhoi[1]:
        count += 1
        list1 = ['B) Z','C) M','D) F']
        print(" Trong 26 chữ cái của bảng chữ cái tiếng Anh, chữ cái nào đứng đầu tiên?")
        
        print("A) A")
        print(list1[0])
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        while done == True:
         if z == 'a':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 0:
                print(aa)
                print("A/ A")   
            else:
                print("A/ A")
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            done = False
    elif cau == cauhoi[2]:
        count += 1
        list1 = ['B) Nikola Tesla','C) Benjamin Franklin','D) Alexander Graham Bell']
        print("Ai là người phát minh ra đèn điện?")
        
        print("A) Thomas Edison")
        print(list1[0])
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        while done == True:
         if z == 'a':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 0:
                print(aa)
                print("A) Thomas Edison")   
            else:
                print("A) Thomas Edison")
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            done = False
    elif cau == cauhoi[3]:
        count += 1
        list1 = ["b) Buzz Aldrin","c) Yuri Gagarin","d) John Glenn"]
        print("Câu hỏi: Ai là người đầu tiên đặt chân lên mặt trăng?")
        print("a) Neil Armstrong")
        print(list1[0])
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        
        while done == True:
         if z == 'a':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 0:
                print(aa)
                print("A/ Neil Armstrong")   
            else:
                print('A/ Neil Armstrong')
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            help2 = False
            done = False
    elif cau == cauhoi[4]:
        list1 =  ["a) Mùa Xuân","c) Mùa Thu","d) Mùa Đông"]
        count += 1
        print("Câu hỏi: Mùa nào nóng nhất?")
        print(list1[0])
        print("b) Mùa Hè")
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        while done == True:
         if z == 'b':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 1:
                print(aa)
                print("b) Mùa Hè")   
            else:
                print("b) Mùa Hè")
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            done = False
    elif cau == cauhoi[5]:
        count += 1
        list1 = ["a) Bill Gates","b) Steve Jobs","c) Jeff Bezos"]
        print("Câu hỏi: Ai là người tạo ra facebook")
        print(list1[0])
        print(list1[1])
        print(list1[2])
        print("d) Mark Zuckerberg")
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()
        
        while done == True:
         if z == 'd':
            diem+=1
            if help21 == True:
                diem+=1
            print("chuc mung,ban dang co",diem,'diem') 
            done=False
        
         elif z == '1':
          if help1 == True:      
            help.remove('1:50/50') 
            help.insert(int(z)-1,'        ')
            aa = random.choice(list1)
            if list1.index(aa) < 4:
                print(aa)
                print("d) Mark Zuckerberg")   
            else:
                print("d) Mark Zuckerberg")
                print(aa)
            help1 = False
          else: 
              print('ban da dung tro giup nay roi') 
          z = input('nhap : ') 
         elif z == '2':
            if help2 == True:
                help.remove('2:sai tru dung cong them') 
                help.insert(int(z)-1,'        ')
                help21 = True
            else:
                print('ban da dung tro giup nay roi') 
            help2 = False
            z = input('nhap : ')
         else:
            print('sai')
            if help21 == True:
                diem = diem-1
            done = False
    elif cau == cauhoi[6]:
        count += 1
        list1 = ["A) Trắng","C) Tím","D) Hồng"]
        print("Câu hỏi: Màu của lá cây thường là gì?")
        print(list1[0])
        print("B) Xanh")
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()

        while done == True:
            if z == 'b':
                diem+=1
                if help21 == True:
                    diem+=1
                print("Chúc mừng, bạn đã có",diem,'điểm') 
                done=False

            elif z == '1':
                if help1 == True:      
                    help.remove('1:50/50') 
                    help.insert(int(z)-1,'        ')
                    aa = random.choice(list1)
                    if list1.index(aa) < 1:
                        print(aa)
                        print("B) Xanh")   
                    else:
                        print("B) Xanh")
                        print(aa)
                    help1 = False
                else: 
                    print('Bạn đã dùng trợ giúp này rồi') 
                z = input('Nhập : ') 
            elif z == '2':
                if help2 == True:
                    help.remove('2:sai tru dung cong them') 
                    help.insert(int(z)-1,'        ')
                    help21 = True
                else:
                    print('Bạn đã dùng trợ giúp này rồi') 
                help2 = False
                z = input('Nhập : ')
            else:
                print('Sai')
                if help21 == True:
                    diem = diem-1
                done = False
            
    elif cau == cauhoi[7]:
        count += 1
        list1 = ["A) Chuột","C) Cá heo","D) Bò"]
        print("Câu hỏi: Loại thú nhỏ nhất trong đây là gì?")
        print(list1[0])
        print("B) Kiến")
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()

        while done == True:
            if z == 'b':
                diem+=1
                if help21 == True:
                    diem+=1
                print("Chúc mừng, bạn đã có",diem,'điểm') 
                done=False

            elif z == '1':
                if help1 == True:      
                    help.remove('1:50/50') 
                    help.insert(int(z)-1,'        ')
                    aa = random.choice(list1)
                    if list1.index(aa) < 1:
                        print(aa)
                        print("B) Kiến")   
                    else:
                        print("B) Kiến")
                        print(aa)
                    help1 = False
                else: 
                    print('Bạn đã dùng trợ giúp này rồi') 
                z = input('Nhập : ') 
            elif z == '2':
                if help2 == True:
                    help.remove('2:sai tru dung cong them') 
                    help.insert(int(z)-1,'        ')
                    help21 = True
                else:
                    print('Bạn đã dùng trợ giúp này rồi') 
                help2 = False
                z = input('Nhập : ')
            else:
                print('Sai')
                if help21 == True:
                    diem = diem-1
                done = False
                
    elif cau == cauhoi[8]:
        count += 1
        list1 = ["B) 3","C) 4","D) 5"]
        print("Câu hỏi: Con người có bao nhiêu chân?")
        print("A) 2")
        print(list1[0])
        print(list1[1])
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()

        while done == True:
            if z == 'a':
                diem+=1
                if help21 == True:
                    diem+=1
                print("Chúc mừng, bạn đã có",diem,'điểm') 
                done=False

            elif z == '1':
                if help1 == True:      
                    help.remove('1:50/50') 
                    help.insert(int(z)-1,'        ')
                    aa = random.choice(list1)
                    if list1.index(aa) < 0:
                        print(aa)
                        print("A) 2")   
                    else:
                        print("A) 2")
                        print(aa)
                    help1 = False
                else: 
                    print('Bạn đã dùng trợ giúp này rồi') 
                z = input('Nhập : ') 
            elif z == '2':
                if help2 == True:
                    help.remove('2:sai tru dung cong them') 
                    help.insert(int(z)-1,'        ')
                    help21 = True
                else:
                    print('Bạn đã dùng trợ giúp này rồi') 
                help2 = False
                z = input('Nhập : ')
            else:
                print('Sai')
                if help21 == True:
                    diem = diem-1
                done = False
                
    elif cau == cauhoi[9]:
        count += 1
        list1 = ["A) Vịt","B) Chim sáo","D) Sâu bướm"]
        print("Câu hỏi: Loài vật nào có khả năng bay cao nhất?")
        print(list1[0])
        print(list1[1])
        print("C) Đại bàng")
        print(list1[2])
        cauhoi.remove(cau) 
        cauhoi.insert(a,'    ')
        print(strhelp)
        z = input()

        while done == True:
            if z == 'c':
                diem+=1
                if help21 == True:
                    diem+=1
                print("Chúc mừng, bạn đã có",diem,'điểm') 
                done=False

            elif z == '1':
                if help1 == True:      
                    help.remove('1:50/50') 
                    help.insert(int(z)-1,'        ')
                    aa = random.choice(list1)
                    if list1.index(aa) < 2:
                        print(aa)
                        print("C) Đại bàng")   
                    else:
                        print("C) Đại bàng")
                        print(aa)
                    help1 = False
                else: 
                    print('Bạn đã dùng trợ giúp này rồi') 
                z = input('Nhập : ') 
            elif z == '2':
                if help2 == True:
                    help.remove('2:sai tru dung cong them') 
                    help.insert(int(z)-1,'        ')
                    help21 = True
                else:
                    print('Bạn đã dùng trợ giúp này rồi') 
                help2 = False
                z = input('Nhập : ')
            else:
                print('Sai')
                if help21 == True:
                    diem = diem-1
                done = False
    else :
        print('----------------------------------------------------------------')
        print('xin hay nhap lai')
        print('----------------------------------------------------------------')
    print('-----------------------     tiep tuc     -----------------------')
    
print('10 câu, mỗi câu 4 đáp án, đúng sẽ được cộng')
print('bạn có 2 quyền trợ giúp')
while True:
    if count == 10:
        print('kết quả',diem,'điểm')  
        break   
    real = ' '.join(cauhoi)  
    strhelp = ' '.join(help)
    print(real)
    choncau = int(input('chon cau: '))
    cau = 'cau'+str(choncau)
    print(cau)
    question(choncau)
            
