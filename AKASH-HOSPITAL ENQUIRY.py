import pickle
import random
import os
class HOSPITAL:
    def __init__(self):
        self.hid=0
        self.hname=''
        self.hadd=''
        self.hdist=''
        self.hdisease=[]
        self.hmob_no=0
        self.doct_mno=[]
        self.num_docts=0
        self.doct_name=[]
        self.doct_eduqual=[]
        self.icu_num=0
        self.ccu_num=0
        self.num_beds=0
        self.email=''
        self.hcategory=''
        self.pas=''
        self.hos=''
        self.pname=''
        self.pdisease=''
        self.page=0
        self.pmobno=0
        self.pfname=''
        self.padd=''
        self.meal_chrg=0
        self.bed={}
        self.s=0
        
    
    def INPUT(self):
        self.hid=random.randint(1,100)
        print("______________________________________________________________________")
        self.hname=raw_input("ENTER HOSPITAL NAME::-->")
        print("______________________________________________________________________")
        self.hadd=raw_input("ENTER HOSPITAL ADDRESS::-->")
        print("______________________________________________________________________")
        self.hdist=raw_input("ENTER THE DISTRICT IN WHICH HOSPITAL IS SITUATED::-->")
        print("______________________________________________________________________")
        self.hmob_no=input("ENTER THE MOBILE NUMBER OF THE HOSPITAL::-->")
        print("______________________________________________________________________")
        self.email=raw_input("ENTER THE EMAIL ID OF THE HOSPITAL::-->")
        print("______________________________________________________________________")
        
        print("ENTER THE DISEASES THAT CAN BE CURED ONE")
        print("AND IF YOU ARE DONE PRESS 'N'::-->")
        while 1:#disease
            a=raw_input()
            if a in['n','N']:
                break
            self.hdisease.append(a)
        print("___________________________________________________________________________________")
        self.pas=raw_input("ENTER THE PASSWORD YOU HAVE TO ASSIGN::-->")#password
        self.num_docts=input("ENTER THE NUMBER OF DOCTORS CURRENTLY WORKING IN THE HOSOPITAL::-->")
        for i in range(self.num_docts):#doctor,name,mobno,eduqual
            print("ENTER THE DETAILS OF",i+1,"DOCTOR::-->")
            n=raw_input("ENTER THE NAME OF THE DOCTOR::-->")
            self.doct_name.append(n)
            m=input("ENTER THE MOBILE NUMBER OF THE DOCTOR::-->")
            self.doct_mno.append(m)
            print("ENTER THE EDUCATIONAL QUALIFICATION OF THE DOCTOR BY USING COMMA \nWHEN YOU ARE DONE PRESS ENTER::-->")
            a=raw_input()
            self.doct_eduqual.append(a)
        print("___________________________________________________________________________________")
        self.icu_num=input("ENTER NUMBER OF ICU IN HOSPITAL::-->>")
        print("___________________________________________________________________________________")
        self.ccu_num=input("ENTER NUMBER OF CCU IN HOSPITAL::-->>")
        print("___________________________________________________________________________________")
        self.num_beds=input("ENTER NUMBER OF BEDS IN HOSPITAL::-->>")
        print("______________________________________________________________________")
        self.hcategory=raw_input("ENTER SECTOR OF HOSPITAL(PVT OR GOVT. )")
        print("______________________________________________________________________")
        self.s=input("ENTER NO. OF CATEGORIES OF BEDS/ROOMS::-->>")
        print("______________________________________________________________________")
        for i in range(self.s):
            a=raw_input("ENTER THE CATEGORY OF BED/ROOM::-->>")
            b=input("ENTER THE CHARGE FOR THE SAME CATEGORY::-->>")
            self.bed[a]=b
        self.meal_chrg=input("ENTER THE COMMON MEAL CHARGE::-->>")
    def OUTPUT(self):
        print("HOSPITAL ID::-->",self.hid)
        print("______________________________________________________________________")
        print('NAME OF THE HOSPITAL::-->',self.hname)
        print("______________________________________________________________________")
        print('ADDRESS OF THE HOSPITAL::-->',self.hadd)
        print("______________________________________________________________________")
        print("DISTRICT ::-->",self.hdist)
        print("______________________________________________________________________")
        print("DISEASES CURED::-->>")
        for i in self.hdisease:
            print("*",i)
        print()
        print("MOBILE NUMBER OF THE HOSPITAL::-->",self.hmob_no)
        print("______________________________________________________________________")
        print("EMAIL ID OF THE HOSPITAL::-->",self.email)
        print("______________________________________________________________________")
        for i in range(self.num_docts):
            print("NAME OF THE DOCTOR::-->",self.doct_name[i])
            print("DOCTOR'S MOBILE NUMBER::-->",self.doct_mno[i])
            print("DOCTOR'S EDUCATIONAL QUALIFICATION::-->")
            L=self.doct_eduqual[i].split(",")
            for j in L:
                print("*",j)
            print("___________________________________________________________________________________")
        print("NUMBER OF ICU IN THE HOSPITAL::-->>",self.icu_num)
        print("___________________________________________________________________________________")
        print("NUMBER OF CCU IN THE HOSPITAL::-->>",self.ccu_num)
        print("___________________________________________________________________________________")
        print("NUMBER OF BEDS IN THE HOSPITAL::-->>",self.num_beds)
        print("_________________________________________________________________________")
        print("HOSPITAL'S SECTOR::-->>",self.hcategory)
        print("___________________________________________________________________________________")
        print("\n")
    def FORM(self,n):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("                                           APPOINTMENT FORM")
        print("                                           HOSPITAL::-->>",n)
        self.hos=n
        print("_________________________________________________________________________________________________________")
        print("ENTER NAME OF THE PATIENT::______")
        self.pname=raw_input()
        print("________________________________________________________________________________________________________")
        print("ENTER DISEASE WITH WHICH PATIENT IS SUFFERING::_________")
        self.pdisease=raw_input()
        print("_________________________________________________________________________________________________________")
        print("ENTER THE AGE OF PATIENT::_____")
        self.page=input()
        print("________________________________________________________________________________________________________")
        print("ENTER THE MOBILE NUMBER OF THE PATIENT::_____")
        self.pmobno=input()
        print("_________________________________________________________________________________________________________")
        print("ENTER PATIENT'S FATHER NAME::___")
        self.pfname=raw_input()
        print("_________________________________________________________________________________________________________")
        print("ENTER THE ADDRESS OF PATIENT::_____")
        self.padd=raw_input()
        print("_________________________________________________________________________________________________________")
        print("THANKS FOR GIVING THE DETAILS.....")
        print("TIMINGS AND SERIAL NO. WILL BE SENT TO YOUR MOBILE NUMBER::::::")
        print("______________________________________________________________________________________________________")
    def RATE(self):
        for i in self.bed:
            print("* BED/ROOM CATEGORY:",i,"::-->>",self.bed[i])
        print("COMMON MEAL CHARGE::-->>",self.meal_chrg)
def WRITEREC():
    fout=open("ENQUIRY.TXT","a")
    ob=HOSPITAL()
    print("ENTER THE DETAILS OF THE HOSPITAL::-->")
    ob.INPUT()
    pickle.dump(ob,fout)
    print("############RECORD ADDED SUCCESSFULLY###############")
    fout.close()
def READREC():
    fin=open("ENQUIRY.TXT","r")
    ob=HOSPITAL()
    try:
        print("@@@@@@@@@@       HOSPITAL DETAILS ARE...  @@@@@@@@@@@@")
        while True:
            ob=pickle.load(fin)
            ob.OUTPUT()
            print("HOSPITAL CHARGES:::")
            ob.RATE()
            print("\n")
    except EOFError:
        fin.close()
def SEARCH_DISE(disea):
    fin=open("ENQUIRY.TXT","r")
    ob=HOSPITAL()
    try:
        print("HOSPITALS WITH DETAILS OF DISEASE",disea,"ARE::-->")
        while True:
            ob=pickle.load(fin)
            if disea in ob.hdisease:
                ob.OUTPUT()
    except EOFError:
        fin.close()
def DELETE(regd,pdcode):
    fin=open("ENQUIRY.TXT","r")
    fout=open("DELT.TXT","w")
    ob=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==regd:
                if pdcode==ob.pas:
                    flag==True
                    print("DETAILS OF",ob.hname,"DELETED SUCCESSFULLY::->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("NO SUCH HOSPITAL RECORD EXIST")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("DELT.TXT","ENQUIRY.TXT")
def MODIFY(regm,pmcode):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","w")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==regm:
                if ob.pas==pmcode:
                    flag=True
                    print("NOW You are READY to modify the Hospital Details::-->")
                    print("ENTER FRESH DETAILS ::-->")
                    ob1.INPUT()
                    pickle.dump(ob1,fout)
                    print("DETAILS OF HOSPITAL SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("NO SUCH HOSPITAL RECORD EXIST::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def SEARCH_HOS(hos):
    fin=open("ENQUIRY.TXT","r")
    ob=HOSPITAL()
    flag=False
    try:
        print("*******\n******\n*****\n****")
        while True:
            ob=pickle.load(fin)
            if hos==ob.hname:
                flag=True
                ob.OUTPUT()
    except EOFError:
        if not flag:
            print("NO SUCH HOSPITAL RECORD EXIST::::\n")
        fin.close()
def SEARCH_ADD(add):
     fin=open("ENQUIRY.TXT","r")
     ob=HOSPITAL()
     try:
         print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
         print("HOSPITALS WITH ADDRESS,IN THE GIVEN DISTRICT")
         while True:
             ob=pickle.load(fin)
             if add==ob.hdist:
                 ob.OUTPUT()
     except EOFError:
         fin.close()
def FORM_FILL(n):
    fin=open("ENQUIRY.TXT","r")
    ob=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hname==n:
                flag=True
    except EOFError:
        if flag:
            ob.FORM(n)
        else:
            print("NO SUCH HOSPITAL RECORD EXIST :::\n")
def SEARCH_DOC(n):
     fin=open("ENQUIRY.TXT","r")
     ob=HOSPITAL()
     flag=False
     try:
         while True:
            ob=pickle.load(fin)
            if n in ob.doct_name:
                flag=True
                ob.OUTPUT()
     except EOFError:
         if not flag:
             print("NO SUCH DOCTOR IS WORKING IN ANY HOSPITAL :::\n")
         fin.close()
def MODIFY_PAS(r,p):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==r:
                if ob.pas==p:
                    flag=True
                    print("ENTER NEW PASSWORD,FOR ASSIGNING TO THE HOSPITAL::-->>")
                    ob1=ob
                    ob1.pas=raw_input()
                    pickle.dump(ob1,fout)
                    print("PASSWORD SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def MOB_MODIFY(i,s):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==i:
                if ob.pas==s:
                    flag=True
                    print("ENTER NEW MOBILE NUMBER,FOR ASSIGNING TO THE HOSPITAL::-->>")
                    ob1=ob
                    ob1.hmob_no=raw_input()
                    pickle.dump(ob1,fout)
                    print("MOBILE NUMBER SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def MODIFY_ADDRESS(i,s):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==i:
                if ob.pas==s:
                    flag=True
                    print("ENTER NEW ADDRESS FOR ASSIGNING TO THE HOSPITAL::-->>")
                    ob1=ob
                    ob1.hadd=raw_input()
                    pickle.dump(ob1,fout)
                    print("ADDRESS SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def MODIFY_DISEASES(i,s):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==i:
                if ob.pas==s:
                    flag=True
                    print("ENTER THE DISEASES THAT CAN BE CURED ONE")
                    print("AND IF YOU ARE DONE PRESS 'N'::-->")
                    ob1=ob
                    ob1.hdisease=[]
                    while 1:
                        a=raw_input()
                        if a in ['N','n']:
                            break
                        ob1.hdisease.append(a)
                    pickle.dump(ob1,fout)
                    print("DISEASES SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")

def MODIFY_STAFF(r,p):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==r:
                if ob.pas==p:
                    flag=True
                    print("ENTER NEW NUMBER OF STAFFS FOR THE HOSPITAL::-->>")
                    ob1=ob
                    ob1.num_docts=0
                    ob1.doct_name=[]
                    ob1.doct_eduqual=[]
                    ob1.doct_mno=[]
                    ob1.num_docts=input()
                    for i in range(ob1.num_docts):#doctor,name,mobno,eduqual
                        print("ENTER THE DETAILS OF",i+1,"DOCTOR::-->")
                        n=raw_input("ENTER THE NAME OF DOCTOR::-->")
                        ob1.doct_name.append(n)
                        m=input("ENTER THE MOBILE NUMBER OF DOCTOR::-->")
                        ob1.doct_mno.append(m)
                        print("ENTER THE EDUCATIONAL QUALIFICATION OF THE DOCTOR BY USING COMMA \nWHEN YOU ARE DONE PRESS ENTER::-->")
                        a=raw_input()
                        ob1.doct_eduqual.append(a)
                    pickle.dump(ob1,fout)
                    print("STAFFS MODIFIED SUCCESSFULLY ::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def SEARCH_CATEG(cate):
    fin=open("ENQUIRY.TXT","r")
    ob=HOSPITAL()
    try:
        print("HOSPITALS IN THE SPECIFIED SECTOR ARE::-->")
        while True:
            ob=pickle.load(fin)
            if cate in ob.hcategory:
                ob.OUTPUT()
    except EOFError:
        fin.close()
def MODIFY_INFRA(i,s):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==i:
                if ob.pas==s:
                    flag=True
                    print("ENTER FRESH DETAILS OF INFRASTRUCTURE::-->>")
                    ob1=ob
                    ob1.icu_num=input("ENTER NUMBER OF ICU IN HOSPITAL::-->>")
                    print("___________________________________________________________________________________")
                    ob1.ccu_num=input("ENTER NUMBER OF CCU IN HOSPITAL::-->>")
                    print("___________________________________________________________________________________")
                    ob1.num_beds=input("ENTER NUMBER OF BEDS IN HOSPITAL::-->>")
                    pickle.dump(ob1,fout)
                    print("INFRASTRUCTURE SUCCESSFULLY MODIFIED::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def MODIFY_CHARGES(r,p):
    fin=open("ENQUIRY.TXT","r")
    fout=open("MODT.TXT","a")
    ob=HOSPITAL()
    ob1=HOSPITAL()
    flag=False
    try:
        while True:
            ob=pickle.load(fin)
            if ob.hid==r:
                if ob.pas==p:
                    flag=True
                    print("ENTER NEW CHARGES FOR THE HOSPITAL::-->>")
                    ob1=ob
                    ob1.bed={}
                    ob1.s=input("ENTER NO. OF CATEGORIES OF BEDS/ROOMS::-->>")
                    for i in range(ob1.s):
                        a=raw_input("ENTER THE CATEGORY OF BED/ROOM::-->>")
                        b=input("ENTER THE CHARGE FOR THE SAME CATEGORY::-->>")
                        ob1.bed[a]=b
                    ob1.meal_chrg=input("ENTER THE COMMON MEAL CHARGE::-->>")
                    pickle.dump(ob1,fout)
                    print("CHARGES MODIFIED SUCCESSFULLY ::-->")
            else:
                pickle.dump(ob,fout)
    except EOFError:
        if not flag:
            print("ENTER CORRECT PASSWORD AND HOSPITAL ID::\n")
    fin.close()
    fout.close()
    os.remove("ENQUIRY.TXT")
    os.rename("MODT.TXT","ENQUIRY.TXT")
def SEARCH_EMAIL(n):
     fin=open("ENQUIRY.TXT","r")
     ob=HOSPITAL()
     flag=False
     try:
         while True:
            ob=pickle.load(fin)
            if n==ob.email:
                flag=True
                ob.OUTPUT()
     except EOFError:
         if not flag:
             print("NO HOSPITAL WITH SUCH EMAIL:::\n")
         fin.close()

#Main Program
while True:
     print("#####################################################################################")
     print("_______________________________________________________________________________________________________")
     print("       @@@          &&&       &&&       &&&&         &&&&     &&&&&&&&&&  &&&    &&&&&&&&&         &&&          &&&  ")
     print("       @@@          &&&       &&&    &&&    &&&   &&&    &&&  &&&      &  &&&       &&&          &&&  &&&       &&&    ")
     print("  @@@@@@@@@@@@      &&&&&&&&&&&&&  &&&       &&&  &&&         &&&&&&&&&&  &&&       &&&         &&&    &&&      &&& ")
     print("  @@@@@@@@@@@@      &&&&&&&&&&&&&  &&&       &&&     &&&      &&&         &&&       &&&        &&&&&&&&&&&&     &&&                     ")
     print("       @@@          &&&       &&&    &&&    &&&   &&&   &&&   &&&         &&&       &&&       &&&        &&&    &&&&&&&&&&&             ")
     print("       @@@          &&&       &&&       &&&&         &&&      &&&         &&&       &&&      &&&          &&&   &&&&&&&&&&&          ")
     print("________________________________________________________________________________________________________")
     print("                        &&&&&&&&&&    &&&&&&       &&&            &&&             &&&       &&&   &&&   &&&&&&&&&&    &&&       &&&        @@@            ")  
     print("                        &&&&&&&&&&    &&& &&&      &&&         &&&    &&&         &&&       &&&   &&&   &&&      &      &&&    &&&         @@@            ")
     print("                        &&&           &&&  &&&     &&&      &&&         &&&       &&&       &&&   &&&   &&&      &       &&&  &&&          @@@             ")
     print("                        &&&&&&&       &&&   &&&    &&&     &&&            &&&     &&&       &&&   &&&   &&&&&&&&&&         &&&       @@@@@@@@@@@@@@@@             ")
     print("                        &&&&&&&       &&&    &&&   &&&     &&&&           &&&     &&&       &&&   &&&   &&&&               &&&       @@@@@@@@@@@@@@@@               ")
     print("                        &&&           &&&     &&&  &&&       &&&     &&   &&&     &&&       &&&   &&&   &&& &              &&&             @@@              ")
     print("                        &&&&&&&&&&    &&&      &&& &&&         &&&     &&&         &&&&&&&&&&     &&&   &&&  &&&           &&&             @@@            ")
     print("                        &&&&&&&&&&    &&&       &&&&&&            &&&   & &         &&&&&&&&      &&&   &&&   &&&&         &&&             @@@          ")
     print("____________________________________________________________________________________________________________")
     print("#####################################################################################")
     print("1. INPUT Details of hospital:")
     print("============================================================================================================")
     print("2. Get the Details of all the hospitals:")
     print("============================================================================================================")
     print("3. SEARCH for hospitals on the basis of DISEASES CURED:")
     print("============================================================================================================")
     print("4. DELETE Details of a particular hospital:")
     print("============================================================================================================")
     print("5. MODIFY Details of a particular hospital:")
     print("============================================================================================================")
     print("6. SEARCH with HOSPITAL NAME:")
     print("============================================================================================================")
     print("7. SEARCH HOSPITALS in a DISTRICT:")
     print("============================================================================================================")
     print("8. FILL the FORM for hospital:")
     print("============================================================================================================")
     print("9. SEARCH for a DOCTOR and show details of hospital he's working in:")
     print("============================================================================================================")
     print("10. MODIFY  PASSWORD for the hospital::-->>")
     print("============================================================================================================")
     print("11. MODIFY  MOBILE NUMBER of a hospital::-->>")
     print("===========================================================================================================")
     print("12. MODIFY  ADDRESS of a hospital::-->>")
     print("===========================================================================================================")
     print("13. MODIFY   DISEASES CURED in a hospital::-->>")
     print("============================================================================================================")
     print("14. MODIFY STAFFS in a hospital::-->>")
     print("============================================================================================================")
     print("15. SEARCH by HOSPITAL SECTOR (PVT or GOVT)::-->>")
     print("============================================================================================================")
     print("16. MODIFY  INFRASTRUCTURE of the hospital ::-->>")
     print("===========================================================================================================")
     print("17. MODIFY  CHARGES of the hospital ::-->>")
     print("============================================================================================================")
     print("18. SEARCH by HOSPITAL EMAIL::-->>")
     print("============================================================================================================")
     print("19. EXIT")
     print("============================================================================================================")
     print("PRESS THE NUMBER FOR CARRYING THE TASK:::-->")
     ch=input()
     if ch==1:
         WRITEREC()
     elif ch==2:
         READREC()
     elif ch==3:
         disea=raw_input("Enter the disease to be searched for:")
         SEARCH_DISE(disea)
     elif ch==4:
         regn=input("Enter the hospital id::")
         pacode=raw_input("Enter the password::")
         DELETE(regn,pacode)
     elif ch==5:
         reg=input("Enter the hospital id::")
         pcode=raw_input("Enter the password::")
         MODIFY(reg,pcode)
     elif ch==6:
         h=raw_input("Enter the hospital name to be searched::__")
         SEARCH_HOS(h)
     elif ch==7:
         d=raw_input("Enter the district in which hospital is to be searched for::-->>")
         SEARCH_ADD(d)
     elif ch==8:
         n=raw_input("ENTER THE HOSPITAL NAME,FOR WHICH FORM IS TO BE FILLED::___")
         FORM_FILL(n)
     elif ch==9:
         n=raw_input("ENTER the name of doctor to be searched for::-->>")
         SEARCH_DOC(n)
     elif ch==10:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_PAS(i,c)
     elif ch==11:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MOB_MODIFY(i,c)
     elif ch==12:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_ADDRESS(i,c)
     elif ch==13:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_DISEASES(i,c)
     elif ch==14:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_STAFF(i,c)
     elif ch==15:
         c=raw_input("Enter hospital's sector(PVT or GOVT)::-->>>")
         SEARCH_CATEG(c)
     elif ch==16:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_INFRA(i,c)
     elif ch==17:
         i=input("Enter the hospital id::")
         c=raw_input("Enter the password::")
         MODIFY_CHARGES(i,c)
     elif ch==18:
         n=raw_input("ENTER EMAIL ID TO BE SEARCHED::-->>")
         SEARCH_EMAIL(n)
     elif ch==19:
         print("GIVE US MORE CHANCES TO SERVE YOU")
         break
     else:
         print("INVALID INPUT")

        
        
        
    
                    
        
                
                
                                                                
                                
    
