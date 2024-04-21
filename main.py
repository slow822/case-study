diem = 0
cauhoi = ['cau1', 'cau2', 
          'cau3', 'cau4', 
          'cau5', 'cau6', 
          'cau7', 'cau8', 
          'cau9', 'cau10']
def question(a):
    global choncau
    global diem
    global cau
    global cauhoi
    if a == 1:
        print("Câu hỏi: 1 + 1 bằng bao nhiêu")
        print("a) 1")
        print("b) 2")
        print("c) 3")
        print("d) 4")
        z = input()
        if z == 'b':
            diem+=1
            print("chuc mung,ban dang co",diem,'diem')  
                     
        else:
            print('sai')
    cauhoi.remove(cau)
real = ' '.join(cauhoi)   
while True:     
    print(real)
    choncau = int(input('chon cau: '))
    cau = 'cau'+str(choncau)
    print(cau)
    question(choncau)
            