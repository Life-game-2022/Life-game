from ast import main
from calendar import c
from colorsys import yiq_to_rgb
from multiprocessing import Barrier
from multiprocessing.resource_sharer import stop
from pickle import NONE
from re import X
from tabnanny import check
from tkinter import ttk
from tkinter.messagebox import NO
from turtle import right, width
import pygame
import sys
import time
import random
import threading

###########플레이 시 유의 사항##############
'''
이미지 주소 경로를 바꿔주셔야 됩니다.
ex)
C:\Users\girookim\Desktop\전직\rlarlfn\고등학교\세특\2학년\동아리 수업\game_imagestart button.PNG 이 주소에서 맨 끝 사진 이름을 제외한
"C:\Users\girookim\Desktop\Life_game\game_image\game_image" 이 부분만큼을 선택하고 Ctrl + F2 키를 이용해 본인의 이미지 파일 경로로 한번에 변경 할 수 있습니다.

* 만약 이미지 경로 에러가 떴다면 백슬래시 (\) 를 두번 넣어주세요.

기능 확인을 위해 돈을 변경하고 싶다면 59번줄에 money 변수값을 바꿔주시면 됩니다.
'''


###########플레이 시 유의 사항##############








# 1.게임 초기화
pygame.init()       #init = 초기화

# 2.게임창 옵션 설정
stage_first = 0   # 처음화면
stage_story = 0  # 스토리
stage_home = 0  # 홈화면
stage_shop = 0  # 상점
stage_shop2 = 0 # 상점-분류
stage_work =0   # 일하기 창
stage_stutus =0 # 상태 창
stage_stock =0  # 주식 창
stage_work_businessman = 0 #회사원 창
stage_inventory = 0 #인벤토리 창
stage_teacher = 0 #교사 창
stage_cu = 0 #편의점 알바 창

sign = 0 #회사원 바 속도 신호
bar_x = 0 #회사원 바 첫 좌표
money = 400000 #돈

n = 1 #회사원 속도
ft = 0 #회사원 시간
st = 0 #주식 시간
tt = 60 #교사 시간
tvt = 0 #티비 시간
tvt2 = 0#큰 티비 시간
ra = 0 #교사 답 신호
m = 0 #편의점 신호
z = 0 #편의점 시간

first_num = 0 #교사 1번 숫자
second_num =0 #교사 2번 숫자
thrid_num = 0 #교사 3번 숫자
answer = 0 #교사 1+2+3 더한 값

s_ele = 210000 #전기 주가
s_fire = 130000 #열마트 주가
s_chemical =480000 #화학 주가
s_bigsla =1200000 #빅슬라 주가
s_pineapple =700000 #파인애플 주가

#구매 개수 
buystock1 = 0
buystock2 = 0
buystock3 = 0
buystock4 = 0
buystock5 = 0

#주식 개수
mystock1= 0
mystock2= 0
mystock3= 0
mystock4= 0
mystock5= 0

#판매 개수 
sellstock1 =0
sellstock2 =0
sellstock3 =0
sellstock4 =0
sellstock5 =0

#주식 판매 신호
sign1 =0
sign2 =0
sign3 =0 
sign4 =0 
sign5 =0 

#상태
hp_max =30    #최대 체력
hp =30        #체력 
mind_max = 30 #최대 정신력
mind =30      #정신력
IQ =40         #지식
py_IQ=0        #전문 지식

hp_max_cost=30000      #최대체력 증가 가격
mind_max_cost=30000   #최대정신력 증가 가격    
IQ_cost=1000000        #지식 가격
py_IQ_cost=5000000     #전문 지식 가격

chicken = 0 #치킨 개수
cup = 0 #컵라면 개수
coffee = 0 #커피 개수
pinephone = 0 #휴대폰 보유 여부
tv_1 = 0 #티비 보유 여부(싼=1,비싼=2
bed_1 = 0#침대 보유 여부


fps = 60    #프레임
fpsClock = pygame.time.Clock()
display_width, display_height = 360, 640    #창 사이즈
size = [360, 640]
screen = pygame.display.set_mode((display_width, display_height))   #게임창 사이즈 적용


title = "Life game"     #제목
pygame.display.set_caption(title)


#아이콘 이미지들  C:\\Users\\giruk\\game_image
si = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestart button.PNG")  #시작버튼
sci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestart button2.PNG") #클릭시 시작버튼
oi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageoption.PNG") #설정 버튼
oci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageoption2.PNG") #클릭시 설정 버튼
ei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageend.PNG") #종료 버튼
eci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageend2.PNG") #클릭시 종료 버튼
ni = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagenext.PNG") #다음 버튼(홈화면 가는)
nci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagenext2.PNG") #클릭시 다음 버튼
hbi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehbp.PNG") #설정 쇳바퀴 모양
hbci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehbp2.PNG")#클릭시 설정 쇳바퀴 모양
worki = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagewk.PNG")#일하기 버튼
workci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagewk2.PNG")#클릭시 일하기 버튼
shopi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagest.PNG")#상점 버튼
shopci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagest2.PNG")#클릭시 상점 버튼
stocki = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock.PNG")#주식 버튼
stockci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock2.PNG")#클릭시 주식 버튼
statusi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatus.PNG")#상태 버튼
statusci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatus2.PNG")#클릭시 상태 버튼
homei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehomeb.PNG")#홈화면 버튼
homeci =pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehomeb2.PNG")#클릭시 홈 화면 버튼
correcti = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecorr.PNG")#정답 버튼
correctci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecorr2.PNG")#클릭시 정답 버튼
errori = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageerror.PNG")#오답
errorci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageerror2.PNG")#클릭시 오답
mentali = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagemental.PNG")#정신력 이미지
healthi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealth.PNG")#체력 이미지
chickencheck = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechickencheck.PNG")#치킨 먹기 확인 이미지
ramencheck = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageramencheck.PNG")#라면 먹기 확인 이미지
coffeecheck = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecoffeecheck.PNG")#커피 먹기 확인 이미지

#직업 아이콘
business_mani = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebsm.PNG")#회사원 시작 아이콘 이미지
business_manci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebsm2.PNG")#회사원 클릭시 시작 아이콘 이미지
teacheri = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetea.PNG")#선생님 시작 아이콘 이미지
teacherci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetea2.PNG")#선생님 클릭시 시작 아이콘 이미지
cui = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecu.PNG")#편의점 시작 아이콘 이미지
cuci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecu2.PNG")#편의점 클릭시 시작 아이콘 이미지

savei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagesave.PNG")#저장 버튼 이미지
saveci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagesave2.PNG")#클릭시 저장 버튼 이미지
e2i = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagequit.PNG")#종료 버튼 이미지
e2ci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagequit2.PNG")#클릭시 종료 버튼 이미지
cashi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecash.PNG")#편의점 계산 이미지
cashci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecash2.PNG")#편의점 클릭시 계산 이미지
trashi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetrash.PNG")#편의점 청소 이미지
trashci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetrash2.PNG")#편의점 클릭시 청소 이미지
cleanupi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageclean.PNG")#편의점 재고정리 이미지
cleanupci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageclean2.PNG")#편의점 클릭시 재고정리 이미지



#상점아이콘들
moneyi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagemoney.PNG")#돈 이미지
m_homei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetohome.PNG")#홈 가기 버튼 이미지
m_clothesi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_clothes.PNG")#미니 옷 상점 가기 버튼
m_clothesci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_clothes2.PNG")#미니 클릭시 옷 상점 가기 버튼
m_tvi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_tv.PNG")#미니 티비 상점 가기 버튼
m_tvci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_tv2.PNG")#미니 클릭시 티비 상점 가기 버튼
m_phonei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_phone.PNG")#미니 휴대폰 상점 가기 버튼
m_phoneci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_phone2.PNG")#미니 클릭시 휴대폰 상점 가기 버튼
m_cari = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_car.PNG")#미니 차 상점 가기 버튼
m_carci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_car2.PNG")#미니 클릭시 차 상점 가기 버튼
m_foodi =pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_food.PNG")#미니 음식 상점 가기 버튼
m_foodci =pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_food2.PNG")#미니 클릭시 음식 상점 가기 버튼
m_item_replacei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_replace.PNG")
m_item_replaceci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_replace2.PNG")
m_item_cari = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_car.PNG")
m_item_carci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_car2.PNG")
m_item_roomi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_room.PNG")
m_item_roomci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_room2.PNG")
m_item_phonei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_phone.PNG")
m_item_phoneci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_phone2.PNG")
m_item_clothesi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_clothes.PNG")
m_item_clothesci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_clothes2.PNG")
m_item_foodi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_food.PNG")
m_item_foodci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_food2.PNG")
m_item_tvi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_tv.PNG")
m_item_tvci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageitem_tv2.PNG")
m_item_cupi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecup.PNG")
m_item_cupci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecup2.PNG")
m_item_chii = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechi.PNG")
m_item_chici = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechi2.PNG")
m_item_coffeei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecoffee.PNG")
m_item_coffeeci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecoffee2.PNG")
m_item_tv1i = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshoptv.PNG")
m_item_tv1ci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshoptv2.PNG")
m_item_tv2i = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshopbigtv.PNG")
m_item_tv2ci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshopbigtv2.PNG")
m_item_bedi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshopbed.PNG")
m_item_bedci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageshopbed2.PNG")
m_item_pinephonei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagepinephone.PNG")
m_item_pinephoneci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagepinephone2.PNG")
rameni = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageramen.PNG")
ramenci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageramen2.PNG")
chickeni = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechicken.PNG")
chickenci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechicken2.PNG")
coffeei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageicecoffee.PNG")
coffeeci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageicecoffee2.PNG")

muzinza = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagemuzinza.PNG")



#주식 이미지들
s_home = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_tohome.PNG")
s_buyi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_buy.PNG")
s_buyci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_buy2.PNG")
s_selli = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_sell.PNG")
s_sellci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_sell2.PNG")
s_canceli = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_cancel.PNG")
s_cancelci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_cancel2.PNG")
s_plusi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageplusi.PNG")
s_plusci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageplusi2.PNG")
s_minusi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageminusi.PNG")
s_minusci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageminusi2.PNG")
s_yesi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_yes.PNG")
s_yesci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_yes2.PNG")
icei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageice.PNG")
iceci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageice2.PNG")
moneyiw = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestore_money.PNG")
elei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageeleicon.PNG")
firei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagefireicon.PNG")
chi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagechicon.PNG")
bigi = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebigicon.PNG")
pinei = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagepineicon.PNG")
infori = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinforicon.PNG")
inforci = pygame.image.load("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinforicon2.PNG")








# 3.게임 내 설정

#minus_stock ~ 주식 개수가 0개 아래로 내려가지 않게하는 코드
#plus_stock ~ 주식 개수 증가 버튼

def plus_stock_number_1():
    global buystock1
    global sellstock1
    buystock1 += 1 #구매 수
    sellstock1 +=1 #판매 수
    
def minus_stock_number_1():
    global buystock1
    global sellstock1
    buystock1 -= 1
    sellstock1 -=1
    if buystock1 <0:
        buystock1 =0   
    if sellstock1 <0:
        sellstock1 =0
        
 
def plus_stock_number_2():
    global buystock2
    global sellstock2
    buystock2 += 1
    sellstock2 +=1
    
def minus_stock_number_2():
    global buystock2
    global sellstock2
    buystock2 -= 1
    sellstock2 -=1
    if buystock2 <0:
        buystock2 =0   
    if sellstock2 <0:
        sellstock2 =0
        

def plus_stock_number_3():
    global buystock3
    global sellstock3
    buystock3 += 1
    sellstock3 +=1
    
def minus_stock_number_3():
    global buystock3
    global sellstock3
    buystock3 -= 1
    sellstock3 -=1
    if buystock3 <0:
        buystock3 =0   
    if sellstock3 <0:
        sellstock3 =0
        

def plus_stock_number_4():
    global buystock4
    global sellstock4
    buystock4 += 1
    sellstock4 +=1
    
def minus_stock_number_4():
    global buystock4
    global sellstock4
    buystock4 -= 1
    sellstock4 -=1
    if buystock4 <0:
        buystock4 =0   
    if sellstock4 <0:
        sellstock4 =0
        

def plus_stock_number_5():
    global buystock5
    global sellstock5
    buystock5 += 1
    sellstock5 +=1
    
def minus_stock_number_5():
    global buystock5
    global sellstock5
    buystock5 -= 1
    sellstock5 -=1
    if buystock5 <0:
        buystock5 =0   
    if sellstock5 <0:
        sellstock5 =0



def timer_stock(): #타이머  import threading 이거 선언해야함
    global tt
    global st
    global tvt
    global tvt2
    global s_ele
    global s_fire
    global s_bigsla
    global s_chemical
    global s_pineapple
    global first_num
    global second_num
    global third_num
    global answer
    global hp
    global mind
    global tv_1
    global bed_1
    global ft
    ft +=1
    st +=1    #주식 시간
    tt -=1    #교사 시간
    tvt +=1   #티비 시간
    tvt2 +=1  #큰 티비 시간
    timer=threading.Timer(1,timer_stock)
    timer.start() #타이머 시작
    if tvt ==60:
        if bed_1==1:
            hp+=1
        if tv_1 ==1:
            mind+=1
        tvt -=60
    if tvt2==40:
        if tv_1 ==2:
            mind+=1
        tvt2-=40
    if st==60: #stock()에다
            #주식 가격 확률 조정 코드
            a = random.randint(1,10)
            b = random.randint(1,10)
            if a != 2:
                s_ele= random.randint(190000,230000)
                s_fire= random.randint(110000,150000)
                s_chemical= random.randint(450000,510000)
                s_bigsla= random.randint(1100000,1300000)
                s_pineapple= random.randint(600000,800000)
            if a == 2:
                if b == 1:
                    s_ele= random.randint(160000,260000)       #210000
                if b == 2:
                    s_fire= random.randint(80000,180000)      #130000
                if b == 3:
                    s_chemical= random.randint(400000,400000)  #480000
                if b == 4:
                    s_bigsla= random.randint(1000000,1400000)  #1200000
                if b == 5:
                    s_pineapple= random.randint(500000,500000) #700000
            st-=60

#스토리 출력 텍스트
clock = pygame.time.Clock()
color = ( 0, 0, 0)
text_color =(255, 255 ,255)
font = pygame.font.SysFont('malgungothic', 19)
fonts = pygame.font.SysFont('malgungothic',20)
s1_text = fonts.render("내 이름 김XX 나이는 2X", True, text_color)  
s2_text = fonts.render("군대를 갔다 대학을 어제 막 졸업했다.", True, text_color)
s3_text = fonts.render("부모님이 주신 작은 반지하 한칸 뿐...", True, text_color)
s4_text = fonts.render("아... 나도 ", True, text_color)  
s5_text = fonts.render("창문에 한강이 보이는 곳에 살고 싶다...", True, text_color)
money_text = font.render(f"{money}",True,(0,0,0))
rti = font.render(f"{ft}",True,(255,255,255))

# 4.코드 컴팩트를 위한 클래스 선언
def game_quit():
    
    pygame.quit()
    sys.exit()

#이미지 클래스
class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cx = 0
        self.cy = 0
    def put_image(self, address):       #기본 이미지
        if address[-3:] == "PNG":       # 만약 이미지 확장자가 PNG 라면
            self.img = pygame.image.load(address).convert_alpha() 
        else :      # PNG가 아닐 시
             self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()

        
    def change_size(self, sx, sy):      #기본 이미지 사이즈
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()  # 업데이트 된 이미지 크기 다시 받아와 저장
    def show(self):
        screen.blit(self.img, (self.x, self.y))
        

#버튼 클래스   
class mouse:           #클릭전 이미지 , x위치 ,y위치, 높이, 폭, 클릭시 이미지, 클릭시 x위치, 클릭시 y위치 , 버튼 누를시 시작되는 명령(함수)
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mp = pygame.mouse.get_pos() #마우스 포인터
        mc = pygame.mouse.get_pressed() # 마우스 클릭
        if x + width > mp[0] > x and y + height > mp[1] > y:
            screen.blit(img_act,(x, y))
            if mc[0] and action !=None:
                time.sleep(0.1)
                action()
        else:
            screen.blit(img_in, (x ,y))

# 바탕화면
bg = obj()  #배경 아이콘 컴팩트 선언
bg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebg.PNG") #아이콘 저장 위치
bg.change_size(360,640)  #아이콘사이즈


###############################################################################################################################3


#상점 - 자동차 
def shop_car():
    global money
    while stage_shop2 == 0:
        clock.tick(60)
        screen.fill(color)
        
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈

        car = obj()
        car.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_car2.PNG")
        car.change_size(72,70)
        car.x = 5
        car.y = 570
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        shoppg.show()
        car.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
           
        clothesButton = mouse(m_clothesi, 140, 570, 72, 70, m_clothesci, 140, 570, shop_clothes) #옷 상점 가는 버튼
        tvButton = mouse(m_tvi, 70, 570, 72, 70, m_tvci, 70, 570, shop_tv)                       #티비 상점 가는 버튼
        phoneButton = mouse(m_phonei, 210, 570, 72, 70, m_phoneci, 210, 570, shop_phone)         #휴대폰 상점 가는 버튼
        foodButton = mouse(m_foodi, 280, 570, 72, 70, m_foodci, 210, 570, shop_food)             #음식 상점 가는 버튼
        shop_mainButton = mouse(muzinza, 115, 8 , 110, 25, muzinza, 130, 20 , shop)              #상점 메인 화면 가는 버튼
        item_replaceButton = mouse(m_item_replacei, 20, 65, 85, 148, m_item_replaceci, 25, 65, None) #대기중 버튼
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
#휴대폰 -파인 폰
def pinephone_buy():
    global money
    global pinephone
    if money >= 1560000 and pinephone <1:
        money -=1560000
        pinephone +=1
        



#상점 -휴대폰
def shop_phone():
    global money
    while stage_shop2 == 0:
        clock.tick(60)
        screen.fill(color)
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈

        phone = obj()
        phone.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_phone2.PNG")
        phone.change_size(72,70)
        phone.x = 210
        phone.y = 570
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        shoppg.show()
        phone.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
        clothesButton = mouse(m_clothesi, 140, 570, 72, 70, m_clothesci, 140, 570, shop_clothes) #옷 상점 가는 버튼
        tvButton = mouse(m_tvi, 70, 570, 72, 70, m_tvci, 70, 570, shop_tv)                       #티비 상점 가는 버튼
        carButton = mouse(m_cari, 5, 570, 72, 70, m_carci, 5, 570, shop_car)                     #자동차 상점 가는 버튼
        foodButton = mouse(m_foodi, 280, 570, 72, 70, m_foodci, 210, 570, shop_food)             #음식 상점 가는 버튼
        shop_mainButton = mouse(muzinza, 115, 8 , 110, 25, muzinza, 130, 20 , shop)              #상점 메인 화면 가는 버튼
        pinephoneButton = mouse(m_item_pinephonei, 20, 65, 85, 148, m_item_pinephoneci, 25, 65, pinephone_buy) #대기중 버튼
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                
                
#가구-티비
def tv1_buy():
    global money
    global tv_1
    if money >= 600000 and tv_1 <1:
        money -=600000
        tv_1 =1
        
def tv2_buy():
    global money
    global tv_1
    if money >= 2000000 and tv_1 <2:
        money -=2000000
        tv_1 =2

def bed_buy():
    global money
    global bed_1
    if money >= 400000 and bed_1 <1:
        money -=400000
        bed_1 =1




#상점 -가구
def shop_tv():
    global money
    while stage_shop2 == 0:
        clock.tick(60)
        screen.fill(color)
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈

        tv = obj()
        tv.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_tv2.PNG")
        tv.change_size(72,70)
        tv.x = 70
        tv.y = 570
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        shoppg.show()
        tv.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
        clothesButton = mouse(m_clothesi, 140, 570, 72, 70, m_clothesci, 140, 570, shop_clothes) #옷 상점 가는 버튼
        carButton = mouse(m_cari, 5, 570, 72, 70, m_carci, 5, 570, shop_car)                     #자동차 상점 가는 버튼
        phoneButton = mouse(m_phonei, 210, 570, 72, 70, m_phoneci, 210, 570, shop_phone)         #휴대폰 상점 가는 버튼
        foodButton = mouse(m_foodi, 280, 570, 72, 70, m_foodci, 210, 570, shop_food)             #음식 상점 가는 버튼
        shop_mainButton = mouse(muzinza, 115, 8 , 110, 25, muzinza, 130, 20 , shop)              #상점 메인 화면 가는 버튼
        tv1Button = mouse(m_item_tv1i, 20, 65, 85, 148, m_item_tv1ci, 25, 65, tv1_buy) #티비 구매 버튼
        tv2Button = mouse(m_item_tv2i, 130, 65, 85, 148, m_item_tv2ci, 130, 65, tv2_buy) #큰 티비 구매 버튼
        bedButton = mouse(m_item_bedi, 240, 65, 85, 148, m_item_bedci, 240, 65, bed_buy) #침대 구매 버튼 
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()




#상점 -옷 
def shop_clothes():
    global money
    while stage_shop2 == 0:
        clock.tick(60)
        screen.fill(color)
        
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈

        clothes = obj()
        clothes.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_clothes2.PNG")
        clothes.change_size(72,70)
        clothes.x = 140
        clothes.y = 570
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        shoppg.show()
        clothes.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
        tvButton = mouse(m_tvi, 70, 570, 72, 70, m_tvci, 70, 570, shop_tv)                       #티비 상점 가는 버튼
        carButton = mouse(m_cari, 5, 570, 72, 70, m_carci, 5, 570, shop_car)                     #자동차 상점 가는 버튼
        phoneButton = mouse(m_phonei, 210, 570, 72, 70, m_phoneci, 210, 570, shop_phone)         #휴대폰 상점 가는 버튼
        foodButton = mouse(m_foodi, 280, 570, 72, 70, m_foodci, 210, 570, shop_food)             #음식 상점 가는 버튼
        shop_mainButton = mouse(muzinza, 115, 8 , 110, 25, muzinza, 130, 20 , shop)              #상점 메인 화면 가는 버튼
        item_replaceButton = mouse(m_item_replacei, 20, 65, 85, 148, m_item_replaceci, 25, 65, None) #대기중 버튼
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()

#음식 -치킨
def chicken_buy():
    global money
    global chicken
    if money >=30000:
        money-=30000
        chicken +=1
#음식 -라면
def cup_buy():
    global money
    global cup
    if money >=2000:
        money-=2000
        cup +=1

#음식 -라면
def coffee_buy():
    global money
    global coffee
    if money >=6000:
        money-=6000
        coffee +=1

#상점 -음식 
def shop_food():
    global money
    while stage_shop2 == 0:
        clock.tick(60)
        screen.fill(color)
        
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈

        food = obj()
        food.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_food2.PNG")
        food.change_size(72,70)
        food.x = 280
        food.y = 570
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        shoppg.show()
        food.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
        clothesButton = mouse(m_clothesi, 140, 570, 72, 70, m_clothesci, 140, 570, shop_clothes) #옷 상점 가는 버튼
        tvButton = mouse(m_tvi, 70, 570, 72, 70, m_tvci, 70, 570, shop_tv)                       #티비 상점 가는 버튼
        carButton = mouse(m_cari, 5, 570, 72, 70, m_carci, 5, 570, shop_car)                     #자동차 상점 가는 버튼
        phoneButton = mouse(m_phonei, 210, 570, 72, 70, m_phoneci, 210, 570, shop_phone)         #휴대폰 상점 가는 버튼
        shop_mainButton = mouse(muzinza, 115, 8 , 110, 25, muzinza, 130, 20 , shop)              #상점 메인 화면 가는 버튼
        
        cupButton = mouse(m_item_cupi, 130, 65, 85, 148, m_item_cupci, 130, 65, cup_buy) #컵라면 구매 버튼
        chiButton = mouse(m_item_chii, 20, 65, 85, 148, m_item_chici, 20, 65, chicken_buy) #치킨 구매 버튼 
        coffeeButton = mouse(m_item_coffeei, 240, 65, 85, 148, m_item_coffeeci, 240, 65, coffee_buy) #치킨 구매 버튼 
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()

#상점 홈 화면

def shop():
    global money
    stage_story -1
    while stage_shop ==0:
        clock.tick(60)
        screen.fill(color)
        shoppg = obj()  #배경 아이콘 컴팩트 선언
        shoppg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagem_home.PNG") #아이콘 저장 위치
        shoppg.change_size(360,640)  #아이콘사이즈
        
        
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        
        shoppg.show()
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)                        #홈가는 버튼
        clothesButton = mouse(m_clothesi, 140, 570, 72, 70, m_clothesci, 140, 570, shop_clothes) #옷 상점 가는 버튼
        tvButton = mouse(m_tvi, 70, 570, 72, 70, m_tvci, 70, 570, shop_tv)                       #티비 상점 가는 버튼
        carButton = mouse(m_cari, 5, 570, 72, 70, m_carci, 5, 570, shop_car)                     #자동차 상점 가는 버튼
        phoneButton = mouse(m_phonei, 210, 570, 72, 70, m_phoneci, 210, 570, shop_phone)         #휴대폰 상점 가는 버튼
        foodButton = mouse(m_foodi, 280, 570, 72, 70, m_foodci, 210, 570, shop_food)             #음식 상점 가는 버튼
        
        itemtvButton = mouse(m_item_tvi, 20, 230, 85, 148, m_item_tvci, 20, 230, shop_tv)       #티비 상점 가는 버튼
        itemcarButton = mouse(m_item_cari, 20, 65, 85, 148, m_item_carci, 20, 65, shop_car)     #자동차 상점 가는 버튼
        itemclothesButton = mouse(m_item_clothesi, 240, 65, 85, 148, m_item_clothesci, 240, 65, shop_clothes) #옷 상점 가는 버튼
        itemphoneButton = mouse(m_item_phonei, 130, 65, 85, 148, m_item_phoneci, 130, 65, shop_phone) #폰 상점 가는 버튼
        itemfoodButton = mouse(m_item_foodi,130, 230 , 85, 148, m_item_foodci, 130, 230 , shop_food) #음식 상점 가는 버튼
        screen.blit(moneyiw, (200, 40)) #돈 이미지 위치
        screen.blit(money_text, (260,35)) #돈 보유량
        
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()


                
gauge = obj()      #회사원 게이지 바
gauge.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagegauge.PNG")
gauge.change_size(320,45)
gauge.x = round (size[0]/2 - gauge.sx/2  )
gauge.y = size[1] -gauge.sy - 95

checkpoint = obj()    #회사원 체크포인트(돈 버는)
checkpoint.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecheckpoint.PNG")
checkpoint.change_size(40,37)
checkpoint.x = round (size[0]/2 - gauge.sx/2 + 15)
checkpoint.y = size[1] -gauge.sy - 91


def red_zone():      #체크포인트 위치 조정 + 이동 바 속도 조절
    if checkpoint.x+30>bar.x >=checkpoint.x-30:
        global money
        global bar_x
        global n
        if bar_x == 4:
            n+=1 #2
        if bar_x == 6:
            n+=1 #3
        if bar_x == 8:
            n+=1 #4
        if bar_x == 10:
            n+=1 #5
        if bar_x == 12:
            n+=1 #6
        bar_x +=2
        money +=500*n
        if bar_x==12:
            bar_x -=2
        checkpoint.x = round (random.randint(40,280))
    else:
        checkpoint.x = round (random.randint(40,280))
        if bar_x == 12:
            bar_x -= 10
            n=1
        if bar_x == 10:
            bar_x -= 8
            n=1
        if bar_x == 8:
            bar_x -= 6
            n=1
        if bar_x == 6:
            bar_x -= 4
            n=1
        if bar_x == 4: #2
            bar_x -= 2
            n=1
        if bar_x == 2:
            n=1
        

        
bar = obj()        #회사원 이동 바
bar.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebar.PNG")
bar.change_size(30,60)
bar.x = round (10)
bar.y = size[1] -gauge.sy - 102



        
#정답
def right(): #교사 정답 확인
    global ra #정답 나올 확률 변수
    global money #돈 
    global first_num #첫번째 숫자
    global second_num #두번째 숫자
    global third_num #세번째 숫자
    global answer #1+2+3번째 숫자 더한 것 또는 1+2+3+w(오답 범위) 숫자 더한 것
    global w #오답 만드는 변수
    global tt #교사 시간
    if 2<= ra <=3: #ra= 정답이 나올 확률 정해주는 것
        money += 10000 #돈 추가
        first_num= random.randint(1,99) #첫번째 숫자 랜덤으로 정하기
        second_num = random.randint(1,99) #두번째 숫자 랜덤으로 정하기
        third_num = random.randint(1,99) #세번째 숫자 랜덤으로 정하기
        ra = random.randint(1,6) #정답 확률  
        w = random.randint(1,9) #오답 범위 랜덤 함수
        if 2<= ra <=3:
            answer = first_num + second_num + third_num           #정답
        else:
            answer = first_num + second_num + third_num + w       #오답 
    else:
        first_num= random.randint(1,99)
        second_num = random.randint(1,99)
        third_num = random.randint(1,99)
        ra = random.randint(1,6)
        w = random.randint(1,9)
        if 2<= ra <=3:
            answer = first_num + second_num + third_num
        else:
            answer = first_num + second_num + third_num - w
        tt -=10

#오답
def wrong(): #교사 오답 확인
    global ra #정답 나올 확률 변수
    global money #돈 
    global first_num #첫번째 숫자
    global second_num #두번째 숫자
    global third_num #세번째 숫자
    global answer #1+2+3번째 숫자 더한 것 또는 1+2+3+w(오답 범위) 숫자 더한 것
    global w #오답 만드는 변수
    global tt #교사 시간
    if 2<= ra <=3: #ra= 정답이 나올 확률 정해주는 것
        money+=15000 #돈추가
        first_num= random.randint(1,99) #첫번째 숫자 랜덤으로 정하기
        second_num = random.randint(1,99) #두번째 숫자 랜덤으로 정하기
        third_num = random.randint(1,99) #세번째 숫자 랜덤으로 정하기
        ra = random.randint(1,6) #정답 확률  
        w = random.randint(1,9) #오답 범위 랜덤 함수
        if 2<= ra <=3:
            answer = first_num + second_num + third_num      #정답
        else:
            answer = first_num + second_num + third_num + w  #오답
    else:
        first_num= random.randint(1,99) #첫번째 숫자 랜덤으로 정하기
        second_num = random.randint(1,99) #두번째 숫자 랜덤으로 정하기
        third_num = random.randint(1,99) #세번째 숫자 랜덤으로 정하기
        ra = random.randint(1,6) #정답 확률  
        w = random.randint(1,9) #오답 범위 랜덤 함수
        if 2<= ra <=3:
            answer = first_num + second_num + third_num
        else:
            answer = first_num + second_num + third_num + w
    
        
    


#교사    
def work_teacher():
    global tt
    global first_num
    global second_num
    global third_num
    global answer
    global ra
    global mind
    global hp
    global money
    global moneyi
    global IQ
    global py_IQ
    if mind <70 or hp <70 or py_IQ <1:
            home()
    if mind >=70 and hp >=70 and py_IQ >=1:
        mind -=70
        hp -=70
        
    tt = 60 
    
    if tt==60:
        first_num= random.randint(1,99) #첫번째 숫자 랜덤으로 정하기
        second_num = random.randint(1,99) #두번째 숫자 랜덤으로 정하기
        third_num = random.randint(1,99) #세번째 숫자 랜덤으로 정하기
        ra = random.randint(1,6) #정답 확률  
        w = random.randint(1,9) #오답 범위 랜덤 함수
        if 2<= ra <=3:
            answer = first_num + second_num + third_num
        else:
            answer = first_num + second_num + third_num + w
    
    while stage_teacher ==0:
        clock.tick(60)
        screen.fill(color)
        teacherpg = obj()  #배경 아이콘 컴팩트 선언
        teacherpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imaget_bm_bg.PNG") #아이콘 저장 위치
        teacherpg.change_size(360,640)  #아이콘사이즈
        
        
        second_n_t = font.render(f"{second_num:.0f}",True,(0,0,0))
        first_n_t = font.render(f"{first_num:.0f}",True,(0,0,0))
        third_n_t = font.render(f"{third_num:.0f}",True,(0,0,0))
        answer_t = font.render(f"{answer:.0f}",True,(0,0,0))
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        tt_t = font.render(f"{tt:.0f}",True,(0,0,0))
        p_t = font.render("+",True,(0,0,0))
        s_t = font.render("=",True,(0,0,0))
        
        teacherpg.show()
        correctButton = mouse(correcti,60,530,110,60,correctci,60,530,right)
        errorButton = mouse(errori,180,530,110,60,errorci,180,530,wrong)
        screen.blit(first_n_t,(80,200))
        screen.blit(second_n_t,(140,200))
        screen.blit(third_n_t,(200,200))
        screen.blit(p_t,(115,200)) 
        screen.blit(p_t,(175,200))
        screen.blit(s_t,(235,200))
        screen.blit(answer_t,(260,200))
        screen.blit(tt_t,(170, 65))
        screen.blit(moneyi,(20,25))
        screen.blit(money_text,(80,20))
        pygame.display.update()
        if tt<=0:
            work()
            sys.exit()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#회사원
def work_businessman():
    
    global hp
    global hp_max
    global mind
    global mind_max
    stage_work -1 
    global sign
    global bar_x
    bar_x = 2
    global ft
    ft = 0
    if mind <20 or hp <50 or IQ<45:
        home()
    if mind >=20 and hp >=50 or IQ >= 45:
        mind -=20
        hp -=50
    while stage_work_businessman ==0:
        clock.tick(60)
        screen.fill(color)
        companybg = obj()   #company background (회사 배경)
        companybg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagew_bm_bg.PNG")
        companybg.change_size(360, 640)
        money_text = font.render(f"{money}",True,(0,0,0))
        rti = font.render(f"{ft}",True,(0,0,0))
        
        
        if sign == 0:
                bar.x += bar_x
                if bar.x == 320:    # 320이라 bar.x 가 안 나눠떨어지면 와리가리 안침, ex) bar.x += 3 이면 320 으로 안 나눠떨어져서 와리가리 X
                    sign = 1
                if bar.x == 321: 
                    sign = 1
                if bar.x == 322: 
                    sign = 1
                if bar.x == 323: 
                    sign = 1
                if bar.x == 324: 
                    sign = 1
                if bar.x == 325: 
                    sign = 1
                if bar.x == 326: 
                    sign = 1
                if bar.x == 327: 
                    sign = 1
                if bar.x == 328: 
                    sign = 1
                if bar.x == 329: 
                    sign = 1
                
            
                
        if sign == 1:
            bar.x -= bar_x
            if bar.x == 10:
                sign = 0
            if bar.x == 9:
                sign = 0
            if bar.x == 8:
                sign = 0
            if bar.x == 7:
                sign = 0 
            if bar.x == 6:
                sign = 0
            if bar.x == 5:
                sign = 0
            if bar.x == 4:
                sign = 0
            if bar.x == 3:
                sign = 0
            if bar.x == 2:
                sign = 0
            if bar.x == 1:
                sign = 0
            
            if ft==60:
                ft-=60
                home()
                sys.exit() #회사원
        
        
        companybg.show()
        gauge.show()
        checkpoint.show()
        bar.show()
        screen.blit(rti, (170,330))
        screen.blit(moneyi, (200,20))
        screen.blit(money_text, (255,15))
        saveButton = mouse(savei,125,570,110,60,saveci,130,570,red_zone)
       
        
        
        pygame.display.update()
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()




########################################################################################################################


def cu_t():
    global m
    global z
    z+=1
    m = random.randint(1,10)
    timer=threading.Timer(0.8,cu_t)
    timer.start() #타이머 시작
#편의점 돈 벌기 버튼들

def cu_cash():
    global money
    global m
    money +=3000
    m =  4
    
def cu_trash():
    global money
    global m
    money +=3000
    m = 4
    
def cu_clean():
    global money
    global m
    money+=3000
    m = 4

#편의점    
def work_cu():
    global mind
    global hp
    if mind <10 or hp <10:
            home()
    if mind >=10 and hp >=10:
        mind -=10
        hp -=10
    cu_t()
    global m
    global z
    global money
    global moneyi
    while stage_cu ==0:
        clock.tick(60)
        screen.fill(color)
        cupg = obj()  #배경 아이콘 컴팩트 선언
        cupg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecubg.PNG") #아이콘 저장 위치
        cupg.change_size(360,640)  #아이콘사이즈
        cupg.show()
        if m ==1:
            cahhButton = mouse(cashi,30,70,130,93,cashci,30,70,cu_cash)
        if m ==2:
            trashButton = mouse(trashi,60,500,130,93,trashci,60,500,cu_trash)
        if m ==3:
            cleanupButton = mouse(cleanupi,200,320,130,93,cleanupci,200,320,cu_clean)
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        z_text = font.render(f"{z:.0f}",True,(0,0,0))
        screen.blit(moneyi,(10,35))
        screen.blit(money_text,(70,30))
        screen.blit(z_text,(200,40))
        if z==60:
            z-=60
            home()
            sys.exit()
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()  
#일하기

def work():
    global hp_max
    global hp
    global mind
    global mind_max
    global hp_text
    global mind_text
    global money
    while stage_work ==0:
        clock.tick(60)
        screen.fill(color)
        workpg = obj()  #배경 아이콘 컴팩트 선언
        workpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagewhp.PNG") #아이콘 저장 위치
        workpg.change_size(360,640)  #아이콘사이즈\
        
        workpg.show()
        homeButton = mouse(homei, 105, 400, 150, 60, homeci, 105, 400, home)
        bamburgerButton = mouse(hbi, 0, 0, 15, 15, hbci, 0, 0, option)
        businessman = mouse(business_mani,30, 80, 70, 105, business_manci, 30, 80, work_businessman)
        teacher = mouse(teacheri, 110, 80, 70, 150, teacherci, 110, 80, work_teacher)
        cu = mouse(cui, 190, 80, 70, 105, cuci, 190, 80, work_cu)
        infor_Bm_Button = mouse(infori, 24, 183, 18, 18, inforci, 24, 183, None)
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0)) 
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        gauge.show
        
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()




######################################################################################### line1195

#판매 최종
def stock_sell_yes():
    global money
    global sellstock1
    global sellstock2
    global sellstock3
    global sellstock4
    global sellstock5
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global mystock1
    global mystock2
    global mystock3
    global mystock4
    global mystock5
    a = mystock1*s_ele
    b = mystock2*s_fire
    c = mystock3*s_chemical
    d = mystock4*s_bigsla
    e = mystock5*s_pineapple
    if mystock1 >= sellstock1 and sign1==1:
        money +=a
        mystock1 -= sellstock1
    
    if  mystock2 >=sellstock2 and sign2==1:
        money +=b
        mystock2 -= sellstock2
    
    if  mystock3 >=sellstock3 and sign3==1:
        money +=c
        mystock3 -= sellstock3
    
    if  mystock4 >=sellstock4 and sign4==1:
        money +=d
        mystock4 -= sellstock4
    
    if  mystock5 >=sellstock4 and sign5==1:
        money +=e
        mystock5 -= sellstock5
    stock()
#구매 최종
def stock_buy_yes():
    global money
    global buystock1
    global buystock2
    global buystock3
    global buystock4
    global buystock5
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global mystock1
    global mystock2
    global mystock3
    global mystock4
    global mystock5
    global sign1
    global sign2
    global sign3
    global sign4
    global sign5
    
    a = buystock1*s_ele
    b = buystock2*s_fire
    c = buystock3*s_chemical
    d = buystock4*s_bigsla
    e = buystock5*s_pineapple
    if money > a and sign1==1:
        money -=a
        mystock1 += buystock1
    
    if money > b and sign2==1:
        money -=b
        mystock2 += buystock2
    
    if money > c and sign3==1:
        money -=c
        mystock3 += buystock3
    
    if money > d and sign4==1:
        money -=d
        mystock4 += buystock4
    
    if money > e and sign5==1:
        money -=e
        mystock5 += buystock5
    stock()
#주식 확인창 판매
def stock_check_sell():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        s_check2 = obj()
        s_check2.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecheck2.PNG")
        s_check2.change_size(180,90)
        s_check2.x = round (size[0]/2 - s_check2.sx/2   )
        s_check2.y = size[1] -s_check2.sy - 270
        
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        s_check2.show()
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, stock_sell_yes)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, stock)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()



#주삭 확인창 구매
def stock_check_buy():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        s_check = obj()
        s_check.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagecheck.PNG")
        s_check.change_size(180,90)
        s_check.x = round (size[0]/2 - s_check.sx/2   )
        s_check.y = size[1] -s_check.sy - 270
        
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        s_check.show()
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, stock_buy_yes)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, stock)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 판매숫자 창             1번 전기
def stock_number_sell_ele():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock1
    global sign1
    sign1=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock1}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))

        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stocksellButton2 = mouse(s_selli, 115, 360, 50, 30, s_sellci, 115, 360, stock_check_sell)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_1)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_1)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit() 
#주식 판매숫자 창     2번열마트 
def stock_number_sell_fire():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock2
    global sign2
    sign2=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock2}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))

        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stocksellButton2 = mouse(s_selli, 115, 360, 50, 30, s_sellci, 115, 360, stock_check_sell)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_2)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_2)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 판매숫자 창       3번 화학
def stock_number_sell_chemical():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock3
    global sign3
    sign3=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock3}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))

        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stocksellButton2 = mouse(s_selli, 115, 360, 50, 30, s_sellci, 115, 360, stock_check_sell)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_3)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_3)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 판매숫자 창           4번 빅슬라
def stock_number_sell_bigsla():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock4
    global sign4
    sign4=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock4}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))

        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stocksellButton2 = mouse(s_selli, 115, 360, 50, 30, s_sellci, 115, 360, stock_check_sell)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_4)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_4)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 판매숫자 창         5번 파인애플
def stock_number_sell_pineapple():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock5
    global sign5
    sign5=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock5}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))

        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stocksellButton2 = mouse(s_selli, 115, 360, 50, 30, s_sellci, 115, 360, stock_check_sell)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_5)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_5)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#주식 구매숫자 창          1번 전기
def stock_number_buy_ele():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock1
    global sign1
    sign1=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)

        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock1}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stockbuyButton2 = mouse(s_buyi, 115, 360, 50, 30, s_buyci, 115, 360, stock_check_buy)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_1)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_1)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()

#주식 구매숫자 창   2번 열마트
def stock_number_buy_fire():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock2
    global sign2
    sign2=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)

        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock2}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stockbuyButton2 = mouse(s_buyi, 115, 360, 50, 30, s_buyci, 115, 360, stock_check_buy)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_2)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_2)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 구매숫자 창        3번  화학
def stock_number_buy_chemical():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock3
    global sign3
    sign3=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)

        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock3}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stockbuyButton2 = mouse(s_buyi, 115, 360, 50, 30, s_buyci, 115, 360, stock_check_buy)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_3)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_3)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 구매숫자 창           4번 bigsla
def stock_number_buy_bigsla():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock4
    global sign4
    sign4=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)

        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock4}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stockbuyButton2 = mouse(s_buyi, 115, 360, 50, 30, s_buyci, 115, 360, stock_check_buy)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_4)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_4)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식 구매숫자 창      5번 파인애플
def stock_number_buy_pineapple():
    global money_text
    global st
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global buystock5
    global sign5
    sign5=+1
    while stage_stock == 0:
        clock.tick(60)
        screen.fill(color)
        
        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list = obj()
        s_list.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list.change_size(350,70)
        s_list.x = round (size[0]/2 - s_list.sx/2   )
        s_list.y = size[1] -s_list.sy - 515
        
        s_number = obj()
        s_number.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_number.PNG")
        s_number.change_size(230,190)
        s_number.x = round (size[0]/2 - s_number.sx/2   )
        s_number.y = size[1] -s_number.sy - 230
        
        stock_number = font.render(f"{buystock5}",True,(255,255,255))
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        s_number.show()
        
        
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        screen.blit(stock_number,(180, 285))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, None)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, None)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, None)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, None)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, None)
        
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, None)
        
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, None)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, None)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, None)
        
        stockbuyButton2 = mouse(s_buyi, 115, 360, 50, 30, s_buyci, 115, 360, stock_check_buy)
        stockcancelButton = mouse(s_canceli, 205, 360, 50, 30, s_cancelci, 205, 360, stock)
        stockplusButton = mouse (s_plusi, 217, 288, 22, 22, s_plusci, 217, 288, plus_stock_number_5)
        stockminusButton = mouse (s_minusi, 239, 288, 22, 22, s_minusci, 239, 288, minus_stock_number_5)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#주식

def stock():
    global money_text
    global mystock1_text
    global mystock2_text
    global mystock3_text
    global mystock4_text
    global mystock5_text
    global st
    global s_ele
    global s_fire
    global s_chemical
    global s_bigsla
    global s_pineapple
    global stock1_text
    global stock2_text
    global stock3_text
    global stock4_text
    global stock5_text
    global s_list1
    global s_list2
    global s_list3
    global s_list4
    global s_list5
    global sts
    global sign1
    global sign2
    global sign3
    global sign4
    global sign5
    while stage_stock ==0 and pinephone ==1:
        clock.tick(60)
        screen.fill(color)
        sign1 =0
        sign2 =0
        sign3 =0 
        sign4 =0 
        sign5 =0 
        

        stockpg = obj()  #배경 아이콘 컴팩트 선언
        stockpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestock_bg.PNG") #아이콘 저장 위치
        stockpg.change_size(360,640)  #아이콘사이즈\
        
        s_list1 = obj()
        s_list1.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_ele.PNG")
        s_list1.change_size(350,70)
        s_list1.x = round (size[0]/2 - s_list1.sx/2   )
        s_list1.y = size[1] -s_list1.sy - 515
        
        s_list2 = obj()
        s_list2.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_fire.PNG")
        s_list2.change_size(350,70)
        s_list2.x = round (size[0]/2 - s_list2.sx/2   )
        s_list2.y = size[1] -s_list2.sy - 425
        
        s_list3 = obj()
        s_list3.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_chemical.PNG")
        s_list3.change_size(350,70)
        s_list3.x = round (size[0]/2 - s_list3.sx/2   )
        s_list3.y = size[1] -s_list3.sy - 335
        
        s_list4 = obj()
        s_list4.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_bigsla.PNG")
        s_list4.change_size(350,70)
        s_list4.x = round (size[0]/2 - s_list4.sx/2   )
        s_list4.y = size[1] -s_list4.sy - 245
        
        s_list5 = obj()
        s_list5.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_images_pineapple.PNG")
        s_list5.change_size(350,70)
        s_list5.x = round (size[0]/2 - s_list5.sx/2   )
        s_list5.y = size[1] -s_list5.sy - 155
        
        stockpg.show()
        s_list1.show()
        s_list2.show()
        s_list3.show()
        s_list4.show()
        s_list5.show()
        
        
        
        sts = font.render(f"{st}",True,(255,255,255))
        stock1_text = font.render(f"{s_ele:.0f}",True,(255,255,255))
        stock2_text = font.render(f"{s_fire:.0f}",True,(255,255,255))
        stock3_text = font.render(f"{s_chemical:.0f}",True,(255,255,255))
        stock4_text = font.render(f"{s_bigsla:.0f}",True,(255,255,255))
        stock5_text = font.render(f"{s_pineapple:.0f}",True,(255,255,255))
        money_text = font.render(f"{money:.0f}",True,(255,255,255))
        mystock1_text = font.render(f"{mystock1:.0f}",True,(255,255,255))
        mystock2_text = font.render(f"{mystock2:.0f}",True,(255,255,255))
        mystock3_text = font.render(f"{mystock3:.0f}",True,(255,255,255))
        mystock4_text = font.render(f"{mystock4:.0f}",True,(255,255,255))
        mystock5_text = font.render(f"{mystock5:.0f}",True,(255,255,255))
        
        #주식 가격
        screen.blit(stock1_text,(160,70))
        screen.blit(stock2_text,(160,160))
        screen.blit(stock3_text,(160,250))
        screen.blit(stock4_text,(160,340))
        screen.blit(stock5_text,(160,430))
        
        screen.blit(sts,(250,10))
        
        screen.blit(moneyiw, (32, 610))
        screen.blit(money_text, (84,605))
        screen.blit(elei, ( 27, 505))
        screen.blit(mystock1_text, (50,500))
        screen.blit(firei, ( 27, 525))
        screen.blit(mystock2_text, (50,520))
        screen.blit(chi, ( 27, 545))
        screen.blit(mystock3_text, (50,540))
        screen.blit(bigi, ( 27, 565))
        screen.blit(mystock4_text, (50,560))
        screen.blit(pinei, ( 27, 585))
        screen.blit(mystock5_text, (50,580))
        stockhomeButton = mouse(s_home, 12, 0, 48, 48, s_home, 12, 0, home)
        stockbuyButton = mouse(s_buyi, 240, 70, 50, 30, s_buyci, 240, 70, stock_number_buy_ele)
        stocksellButton = mouse(s_selli, 295, 70, 50, 30, s_sellci, 295, 70, stock_number_sell_ele)
        
        stockbuyButton = mouse(s_buyi, 240, 160, 50, 30, s_buyci, 240, 160, stock_number_buy_fire)
        stocksellButton = mouse(s_selli, 295, 160, 50, 30, s_sellci, 295, 160, stock_number_sell_fire)
        
        stockbuyButton = mouse(s_buyi, 240, 250, 50, 30, s_buyci, 240, 250, stock_number_buy_chemical)
        stocksellButton = mouse(s_selli, 295, 250, 50, 30, s_sellci, 295, 250, stock_number_sell_chemical)
        
        stockbuyButton = mouse(s_buyi, 240, 340, 50, 30, s_buyci, 240, 340, stock_number_buy_bigsla)
        stocksellButton = mouse(s_selli, 295, 340, 50, 30, s_sellci, 295, 340, stock_number_sell_bigsla)
        
        stockbuyButton = mouse(s_buyi, 240, 430, 50, 30, s_buyci, 240, 430, stock_number_buy_pineapple)
        stocksellButton = mouse(s_selli, 295, 430, 50, 30, s_sellci, 295, 430, stock_number_sell_pineapple)
        
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
                
                
################################################################################################################################ line2761
 

def plus_status_yes_1():
    global money
    global hp_max_cost
    global hp_max
    global hp
    if money > hp_max_cost:
        money -=hp_max_cost
        hp_max +=5
        hp_max_cost +=10000

def plus_status_yes_2():
    global money
    global mind_max_cost
    global mind_max
    global mind
    if money > mind_max_cost:
        money -=mind_max_cost
        mind_max +=1
        mind_max_cost +=10000

def plus_status_yes_3():
    global money
    global IQ_cost
    global IQ
    if money > IQ_cost:
        money -=IQ_cost
        IQ +=1
        IQ_cost +=100000

def plus_status_yes_4():
    global money
    global py_IQ_cost
    global py_IQ
    fail = obj()
    fail.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagefail.PNG")
    fail.x = round (size[0]/2 - fail.sx/2   )
    fail.y = size[1] -fail.sy - 240
    success = obj()
    success.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagenice.PNG")
    success.x = round (size[0]/2 - success.sx/2   )
    success.y = size[1] -success.sy - 240
    if money > py_IQ_cost:
        money -=py_IQ_cost
        x =random.randint(0,10)
        if 3>x>=2:
            py_IQ+=1
            success.show()
            pygame.display.update()
            time.sleep(1)
            status()
        if x>=3 or x<2:
            fail.show()
            pygame.display.update()
            time.sleep(1)
            status()
            
 
#상태 확인창 구매 111111111111111111111111111111111
def status_check_buy_1():
    global money_text
    global hp_max
    global mind_max
    global IQ
    global py_IQ
    
    global hp_max_text
    global mind_max_text
    global IQ_text
    global py_IQ_text
    
    global hp_max_cost
    global mind_max_cost
    global IQ_cost
    global py_IQ_cost
    
    global hp_max_cost_text
    global mind_max_cost_text
    global IQ_cost_text
    global py_IQ_cost_text
    
    global health
    global mind_maxi
    global IQi
    global py_IQi
    while stage_stutus == 0:
        clock.tick(60)
        screen.fill(color)
        stup =obj()
        stup.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatusup.PNG")
        stup.x = round (size[0]/2 - stup.sx/2   )
        stup.y = size[1] -stup.sy - 240
        
        health=obj()
        health.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealthbar.PNG")
        health.change_size(180,45)
        health.x = 0
        health.y = 97
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        #스텟
        hp_max_text = font.render(f"{hp_max:.0f}",True,(0,0,0))
        mind_max_text = font.render(f"{mind_max:.0f}",True,(0,0,0))
        IQ_text = font.render(f"{IQ:.0f}",True,(0,0,0))
        py_IQ_text = font.render(f"{py_IQ:.0f}",True,(0,0,0))
        #스텟 업 가격
        hp_max_cost_text = font.render(f"{hp_max_cost:.0f}",True,(0,0,0))
        mind_max_cost_text = font.render(f"{mind_max_cost:.0f}",True,(0,0,0))
        IQ_cost_text = font.render(f"{IQ_cost:.0f}",True,(0,0,0))
        py_IQ_cost_text = font.render(f"{py_IQ_cost:.0f}",True,(0,0,0))
        
        stutuspg.show()
        health.show()
        mind_maxi.show()
        IQi.show()
        py_IQi.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(hp_max_text,(50,95))
        screen.blit(mind_max_text,(230,95))
        screen.blit(IQ_text,(50,195))
        screen.blit(py_IQ_text,(230,195))
        
        screen.blit(hp_max_cost_text,(50,115))
        screen.blit(mind_max_cost_text,(230,115))
        screen.blit(IQ_cost_text,(50,215))
        screen.blit(py_IQ_cost_text,(230,215))
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, None)
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, None)
        statusplusButton = mouse (s_plusi, 155, 100, 22, 22, s_plusci, 155, 100, None)
        statusplusButton = mouse (s_plusi, 335, 100, 22, 22, s_plusci, 335, 100, None)
        statusplusButton = mouse (s_plusi, 155, 200, 22, 22, s_plusci, 155, 200, None)
        statusplusButton = mouse (s_plusi, 335, 200, 22, 22, s_plusci, 335, 200, None)
        stup.show()
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, plus_status_yes_1)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, status)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#상태 확인창 구매 22222222222222222222222222222
def status_check_buy_2():
    global money_text
    global hp_max
    global mind_max
    global IQ
    global py_IQ
    
    global hp_max_text
    global mind_max_text
    global IQ_text
    global py_IQ_text
    
    global hp_max_cost
    global mind_max_cost
    global IQ_cost
    global py_IQ_cost
    
    global hp_max_cost_text
    global mind_max_cost_text
    global IQ_cost_text
    global py_IQ_cost_text
    
    global health
    global mind_maxi
    global IQi
    global py_IQi
    while stage_stutus == 0:
        clock.tick(60)
        screen.fill(color)
        stup =obj()
        stup.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatusup.PNG")
        stup.x = round (size[0]/2 - stup.sx/2   )
        stup.y = size[1] -stup.sy - 240
        
        health=obj()
        health.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealthbar.PNG")
        health.change_size(180,45)
        health.x = 0
        health.y = 97
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        #스텟
        hp_max_text = font.render(f"{hp_max:.0f}",True,(0,0,0))
        mind_max_text = font.render(f"{mind_max:.0f}",True,(0,0,0))
        IQ_text = font.render(f"{IQ:.0f}",True,(0,0,0))
        py_IQ_text = font.render(f"{py_IQ:.0f}",True,(0,0,0))
        #스텟 업 가격
        hp_max_cost_text = font.render(f"{hp_max_cost:.0f}",True,(0,0,0))
        mind_max_cost_text = font.render(f"{mind_max_cost:.0f}",True,(0,0,0))
        IQ_cost_text = font.render(f"{IQ_cost:.0f}",True,(0,0,0))
        py_IQ_cost_text = font.render(f"{py_IQ_cost:.0f}",True,(0,0,0))
        
        stutuspg.show()
        health.show()
        mind_maxi.show()
        IQi.show()
        py_IQi.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(hp_max_text,(50,95))
        screen.blit(mind_max_text,(230,95))
        screen.blit(IQ_text,(50,195))
        screen.blit(py_IQ_text,(230,195))
        
        screen.blit(hp_max_cost_text,(50,115))
        screen.blit(mind_max_cost_text,(230,115))
        screen.blit(IQ_cost_text,(50,215))
        screen.blit(py_IQ_cost_text,(230,215))
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, None)
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, None)
        statusplusButton = mouse (s_plusi, 155, 100, 22, 22, s_plusci, 155, 100, None)
        statusplusButton = mouse (s_plusi, 335, 100, 22, 22, s_plusci, 335, 100, None)
        statusplusButton = mouse (s_plusi, 155, 200, 22, 22, s_plusci, 155, 200, None)
        statusplusButton = mouse (s_plusi, 335, 200, 22, 22, s_plusci, 335, 200, None)
        stup.show()
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, plus_status_yes_2)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, status)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#상태 확인창 구매 33333333333333333333333333
def status_check_buy_3():
    global money_text
    global hp_max
    global mind_max
    global IQ
    global py_IQ
    
    global hp_max_text
    global mind_max_text
    global IQ_text
    global py_IQ_text
    
    global hp_max_cost
    global mind_max_cost
    global IQ_cost
    global py_IQ_cost
    
    global hp_max_cost_text
    global mind_max_cost_text
    global IQ_cost_text
    global py_IQ_cost_text
    
    global health
    global mind_maxi
    global IQi
    global py_IQi
    while stage_stutus == 0:
        clock.tick(60)
        screen.fill(color)
        stup =obj()
        stup.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatusup.PNG")
        stup.x = round (size[0]/2 - stup.sx/2   )
        stup.y = size[1] -stup.sy - 240
        
        health=obj()
        health.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealthbar.PNG")
        health.change_size(180,45)
        health.x = 0
        health.y = 97
        
        money_text = font.render(f"{money:.0f}",True,(0,0,0))
        
        #스텟
        hp_max_text = font.render(f"{hp_max:.0f}",True,(0,0,0))
        mind_max_text = font.render(f"{mind_max:.0f}",True,(0,0,0))
        IQ_text = font.render(f"{IQ:.0f}",True,(0,0,0))
        py_IQ_text = font.render(f"{py_IQ:.0f}",True,(0,0,0))
        #스텟 업 가격
        hp_max_cost_text = font.render(f"{hp_max_cost:.0f}",True,(0,0,0))
        mind_max_cost_text = font.render(f"{mind_max_cost:.0f}",True,(0,0,0))
        IQ_cost_text = font.render(f"{IQ_cost:.0f}",True,(0,0,0))
        py_IQ_cost_text = font.render(f"{py_IQ_cost:.0f}",True,(0,0,0))
        
        stutuspg.show()
        health.show()
        mind_maxi.show()
        IQi.show()
        py_IQi.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(hp_max_text,(50,95))
        screen.blit(mind_max_text,(230,95))
        screen.blit(IQ_text,(50,195))
        screen.blit(py_IQ_text,(230,195))
        
        screen.blit(hp_max_cost_text,(50,115))
        screen.blit(mind_max_cost_text,(230,115))
        screen.blit(IQ_cost_text,(50,215))
        screen.blit(py_IQ_cost_text,(230,215))
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, None)
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, None)
        statusplusButton = mouse (s_plusi, 155, 100, 22, 22, s_plusci, 155, 100, None)
        statusplusButton = mouse (s_plusi, 335, 100, 22, 22, s_plusci, 335, 100, None)
        statusplusButton = mouse (s_plusi, 155, 200, 22, 22, s_plusci, 155, 200, None)
        statusplusButton = mouse (s_plusi, 335, 200, 22, 22, s_plusci, 335, 200, None)
        stup.show()
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, plus_status_yes_3)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, status)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#상태 확인창 구매 44444444444444444444
    
def status_check_buy_4():
    global money_text
    global hp_max
    global mind_max
    global IQ
    global py_IQ
    
    global hp_max_text
    global mind_max_text
    global IQ_text
    global py_IQ_text
    
    global hp_max_cost
    global mind_max_cost
    global IQ_cost
    global py_IQ_cost
    
    global hp_max_cost_text
    global mind_max_cost_text
    global IQ_cost_text
    global py_IQ_cost_text
    
    global health
    global mind_maxi
    global IQi
    global py_IQi
    while stage_stutus == 0:
        clock.tick(60)
        screen.fill(color)
        stup =obj()
        stup.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagestatusup.PNG")
        stup.x = round (size[0]/2 - stup.sx/2   )
        stup.y = size[1] -stup.sy - 240
        
        health=obj()
        health.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealthbar.PNG")
        health.change_size(180,45)
        health.x = 0
        health.y = 97
        
        money_text = font.render(f"{money}",True,(0,0,0))
        
        #스텟
        hp_max_text = font.render(f"{hp_max:.0f}",True,(0,0,0))
        mind_max_text = font.render(f"{mind_max:.0f}",True,(0,0,0))
        IQ_text = font.render(f"{IQ:.0f}",True,(0,0,0))
        py_IQ_text = font.render(f"{py_IQ:.0f}",True,(0,0,0))
        #스텟 업 가격
        hp_max_cost_text = font.render(f"{hp_max_cost:.0f}",True,(0,0,0))
        mind_max_cost_text = font.render(f"{mind_max_cost:.0f}",True,(0,0,0))
        IQ_cost_text = font.render(f"{IQ_cost:.0f}",True,(0,0,0))
        py_IQ_cost_text = font.render(f"{py_IQ_cost:.0f}",True,(0,0,0))
        
        stutuspg.show()
        stutuspg.show()
        health.show()
        mind_maxi.show()
        IQi.show()
        py_IQi.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(hp_max_text,(50,95))
        screen.blit(mind_max_text,(230,95))
        screen.blit(IQ_text,(50,195))
        screen.blit(py_IQ_text,(230,195))
        
        screen.blit(hp_max_cost_text,(50,115))
        screen.blit(mind_max_cost_text,(230,115))
        screen.blit(IQ_cost_text,(50,215))
        screen.blit(py_IQ_cost_text,(230,215))
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, None)
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, None)
        statusplusButton = mouse (s_plusi, 155, 100, 22, 22, s_plusci, 155, 100, None)
        statusplusButton = mouse (s_plusi, 335, 100, 22, 22, s_plusci, 335, 100, None)
        statusplusButton = mouse (s_plusi, 155, 200, 22, 22, s_plusci, 155, 200, None)
        statusplusButton = mouse (s_plusi, 335, 200, 22, 22, s_plusci, 335, 200, None)
        stup.show()
        stockyesButton = mouse(s_yesi, 115, 330, 50, 30, s_yesci, 115, 330, plus_status_yes_4)
        stockcancelButton = mouse(s_canceli, 195, 330, 50, 30, s_cancelci, 195, 330, status)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#치킨 먹기
def eat_chicken():
    global chicken
    global hp
    global hp_max
    global chicken_sign
    if  chicken >0 and hp <= hp_max:
        chicken -=1
        hp+=30
        if hp > hp_max:
            hp = hp_max
    icebox()
    
#컵라면 먹기
def eat_ramen():
    global cup
    global hp
    global hp_max
    if cup>0 and hp < hp_max:
        cup -=1
        hp+=5
        if hp > hp_max:
            hp  = hp_max
    icebox()

#커피 먹기
def eat_coffee():
    global coffee
    global hp
    global mind
    global hp_max
    global mind_max
    if coffee >0 and hp >6 and mind < mind_max:
        coffee -=1
        hp -=5
        mind +=10
        if mind > mind_max:
            mind = mind_max
    icebox()

#치킨 먹기 확인
def check_eat_chicken():
    global chicken
    global hp
    global mind
    while chicken > 0:
        clock.tick(60)
        screen.fill(color)
        ice=obj()
        ice.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinice.png")
        ice.show()
        
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0))
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))
        
        if chicken >0:
            chickeneatButton = mouse(chickeni, 10, 280 , 72, 70, chickenci, 10, 280, None)
        if cup >0:
            cupeatButton = mouse(rameni, 100, 280 , 72, 70, ramenci, 100, 280, None)
        if coffee >0:
            coffeeButton = mouse(coffeei, 190, 280 , 72, 70, coffeeci, 190, 280, None)
        
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        iceButton2 = mouse(iceci, 10, 55 , 30, 40, icei, 10, 55, status)
        screen.blit(chickencheck,(90,160))
        yesButton = mouse(s_yesi, 115, 210, 50, 30, s_yesci, 115, 210, eat_chicken)
        celButton = mouse(s_canceli, 195, 210, 50, 30, s_cancelci, 195, 210, icebox)
        
        pygame.display.update()
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#컵라면 먹기 확인
def check_eat_ramen():
    global cup
    global hp
    global mind
    while cup> 0:
        clock.tick(60)
        screen.fill(color)
        ice=obj()
        ice.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinice.png")
        ice.show()
        
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0))
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))
        
        if chicken >0:
            chickeneatButton = mouse(chickeni, 10, 280 , 72, 70, chickenci, 10, 280, None)
        if cup >0:
            cupeatButton = mouse(rameni, 100, 280 , 72, 70, ramenci, 100, 280, None)
        if coffee >0:
            coffeeButton = mouse(coffeei, 190, 280 , 72, 70, coffeeci, 190, 280, None)
        
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        iceButton2 = mouse(iceci, 10, 55 , 30, 40, icei, 10, 55, status)
        screen.blit(ramencheck,(90,160))
        yesButton = mouse(s_yesi, 115, 210, 50, 30, s_yesci, 115, 210, eat_ramen)
        celButton = mouse(s_canceli, 195, 210, 50, 30, s_cancelci, 195, 210, icebox)
        
        pygame.display.update()
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()

#커피면 먹기 확인
def check_eat_coffee():
    global coffee
    global hp
    global mind
    while coffee> 0:
        clock.tick(60)
        screen.fill(color)
        ice=obj()
        ice.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinice.png")
        ice.show()
        
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0))
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))
        
        if chicken >0:
            chickeneatButton = mouse(chickeni, 10, 280 , 72, 70, chickenci, 10, 280, None)
        if cup >0:
            cupeatButton = mouse(rameni, 100, 280 , 72, 70, ramenci, 100, 280, None)
        if coffee >0:
            coffeeButton = mouse(coffeei, 190, 280 , 72, 70, coffeeci, 190, 280, None)
        
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        iceButton2 = mouse(iceci, 10, 55 , 30, 40, icei, 10, 55, status)
        screen.blit(coffeecheck,(90,160))
        yesButton = mouse(s_yesi, 115, 210, 50, 30, s_yesci, 115, 210, eat_coffee)
        celButton = mouse(s_canceli, 195, 210, 50, 30, s_cancelci, 195, 210, icebox)
        
        pygame.display.update()
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()

        
#냉장고
def icebox():
    global chicken
    global cup
    global coffee
    while stage_stutus ==0:
        clock.tick(60)
        screen.fill(color)
        ice=obj()
        ice.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageinice.png")
        ice.show()
        
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0))
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))

        if chicken >0:
            chickeneatButton = mouse(chickeni, 10, 280 , 72, 70, chickenci, 10, 280, check_eat_chicken)
        if cup >0:
            cupeatButton = mouse(rameni, 100, 280 , 72, 70, ramenci, 100, 280, check_eat_ramen)
        if coffee >0:
            coffeeButton = mouse(coffeei, 190, 280 , 72, 70, coffeeci, 190, 280, check_eat_coffee)
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        iceButton2 = mouse(iceci, 10, 55 , 30, 40, icei, 10, 55, home)
        
        pygame.display.update()
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
                
#상태
def status():
    global stutuspg
    global money
    global money_text
    global hp_max
    global mind_max
    global IQ
    global py_IQ
    global hp_max_text
    global mind_max_text
    global IQ_text
    global py_IQ_text
    global hp_max_cost
    global mind_max_cost
    global IQ_cost
    global py_IQ_cost
    global hp_max_cost_text
    global mind_max_cost_text
    global IQ_cost_text
    global py_IQ_cost_text
    global health
    global mind_maxi
    global IQi
    global py_IQi
    
    while stage_stutus ==0:
        clock.tick(60)
        screen.fill(color)
        stutuspg = obj()  #배경 아이콘 컴팩트 선언
        stutuspg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageWhp.PNG") #아이콘 저장 위치
        stutuspg.change_size(360,640)  #아이콘사이즈
        
        health=obj()
        health.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehealthbar.PNG")
        health.change_size(180,45)
        health.x = 0
        health.y = 97
        
        IQi =obj()
        IQi.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imageiqbar.PNG")
        IQi.change_size(180,45)
        IQi.x = 0
        IQi.y = 197
        
        mind_maxi=obj()
        mind_maxi.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagemindbar.PNG")
        mind_maxi.change_size(180,45)
        mind_maxi.x = 180
        mind_maxi.y = 97
        
        py_IQi=obj()
        py_IQi.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagehighiqbar.PNG")
        py_IQi.change_size(180,45)
        py_IQi.x = 180
        py_IQi.y = 197
        
        
        #스텟
        hp_max_text = font.render(f"{hp_max:.0f}",True,(0,0,0))
        mind_max_text = font.render(f"{mind_max:.0f}",True,(0,0,0))
        IQ_text = font.render(f"{IQ:.0f}",True,(0,0,0))
        py_IQ_text = font.render(f"{py_IQ:.0f}",True,(0,0,0))
        #스텟 업 가격
        hp_max_cost_text = font.render(f"{hp_max_cost:.0f}",True,(0,0,0))
        mind_max_cost_text = font.render(f"{mind_max_cost:.0f}",True,(0,0,0))
        IQ_cost_text = font.render(f"{IQ_cost:.0f}",True,(0,0,0))
        py_IQ_cost_text = font.render(f"{py_IQ_cost:.0f}",True,(0,0,0))
        
        
        
        stutuspg.show()
        health.show()
        mind_maxi.show()
        IQi.show()
        py_IQi.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        
        screen.blit(hp_max_text,(50,95))
        screen.blit(mind_max_text,(230,95))
        screen.blit(IQ_text,(50,195))
        screen.blit(py_IQ_text,(230,195))
        
        screen.blit(hp_max_cost_text,(50,115))
        screen.blit(mind_max_cost_text,(230,115))
        screen.blit(IQ_cost_text,(50,215))
        screen.blit(py_IQ_cost_text,(230,215))
        homeButton = mouse(m_homei, 12, 0, 48, 48, m_homei, 210, 0, home)
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, icebox)
        statusplusButton = mouse (s_plusi, 155, 100, 22, 22, s_plusci, 155, 100, status_check_buy_1)
        statusplusButton = mouse (s_plusi, 335, 100, 22, 22, s_plusci, 335, 100, status_check_buy_2)
        statusplusButton = mouse (s_plusi, 155, 200, 22, 22, s_plusci, 155, 200, status_check_buy_3)
        statusplusButton = mouse (s_plusi, 335, 200, 22, 22, s_plusci, 335, 200, status_check_buy_4)
        
        
        
        
        
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
#설정

def option():
    
    while stage_stutus ==0:
        clock.tick(60)
        screen.fill(color)
        optionpg = obj()  #배경 아이콘 컴팩트 선언
        optionpg.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagewhp.PNG") #아이콘 저장 위치
        optionpg.change_size(360,640)  #아이콘사이즈\
        
        optionpg.show()
        homeButton = mouse(homei, 105, 400, 150, 60, homeci, 105, 400, home)
        quitButton = mouse(e2i, 125, 500, 283, 75, e2ci, 125, 500, game_quit)
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()

#메인 화면

def home():
    global money_text
    global stage_story
    stage_story = 1
    global money
    global moneyi
    global hp_text
    global mind_text
    global hp_max_text
    global mind_max_text
    global hp
    global mind
    global hp_max
    global mind_max
    global tv_1
    global tvt
    global bed_1

    while stage_home ==0:
        clock.tick(60)
        screen.fill(color)
        hpi = obj()  #배경 아이콘 컴팩트 선언
        hpi.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagewhp.PNG") #아이콘 저장 위치
        hpi.change_size(360,640)  #아이콘사이즈\
        
        
        room = obj()
        room.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagenormalroom.PNG")
        room.change_size(260,260)
        room.x = round (size[0]/2 - room.sx/2 + 0  )
        room.y = size[1] -room.sy - 250
        
        pinephonei = obj()
        pinephonei.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagephoneicon.PNG")
        pinephonei.change_size(42,73)
        pinephonei.x = 6
        pinephonei.y = 60
        
        normalbed = obj()
        normalbed.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebox1.PNG")
        normalbed.change_size(85,55)
        normalbed.x = 70
        normalbed.y = 277
        
        bed = obj()
        bed.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebed.PNG")
        bed.change_size(100,100)
        bed.x = 60
        bed.y = 232
        
                       
        tv = obj()
        tv.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetv1.PNG")
        tv.change_size(85,55)
        tv.x = 220
        tv.y = 240
        
        tv2 = obj()
        tv2.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagetv2.PNG")
        tv2.change_size(82,100)
        tv2.x = 212
        tv2.y = 205
        
        
        undertvbox2 = obj()
        undertvbox2.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagebox2.PNG")
        undertvbox2.change_size(85,55)
        undertvbox2.x = 220
        undertvbox2.y = 260
                
        money_text = font.render(f"{money}",True,(0,0,0))
        
        hp_text = font.render(f"{hp:.0f}",True,(0,0,0))
        mind_text = font.render(f"{mind:.0f}",True,(0,0,0))
        hp_if = font.render("체력",True,(255,0,0))
        mind_if = font.render("정신력",True,(0,0,255))
        
        effect1 = font.render("●60초마다 정신력 +1",True,(0,0,0))
        effect2 = font.render("●40초마다 정신력 +1",True,(0,0,0))
        effect3 = font.render("●60초마다 체력 +1",True,(0,0,0))
        effect4 = font.render("휴대폰이 필요합니다",True,(0,0,0))
        
        hpi.show()
        room.show()
        
        screen.blit(moneyi, (200, 6))
        screen.blit(money_text, (255,1))
        screen.blit(mentali, (25,35))
        screen.blit(healthi,(25,5))
        screen.blit(hp_text,(120,2))
        screen.blit(mind_text,(120,32))
        screen.blit(hp_if,(50,2))
        screen.blit(mind_if,(50,32))
        
        if pinephone == 0:
            screen.blit(effect4,(180,490))
        
        if pinephone ==1:
            pinephonei.show()
        
        if 2 > tv_1 :
            undertvbox2.show()
        if tv_1 == 1:
            tv.show()
            screen.blit(effect1,(30,400))
            
        if tv_1 == 2:
            tv2.show()
            screen.blit(effect2,(30,400))
            
        if bed_1 != 1:
            normalbed.show()
            
        if bed_1 ==1:
            bed.show()
            screen.blit(effect3,(30,380))
        
        iceButton = mouse(icei, 320,55 , 30, 40, iceci, 320, 55, icebox)
        bamburgerButton = mouse(hbi, 0, 0, 15, 15, hbci, 0, 0, option)
        workButton = mouse(worki, 0, 580, 180, 60, workci, 0, 580, work)
        shopButton = mouse(shopi, 0, 520, 180, 60, shopci, 0, 520, shop)
        coinButton = mouse(stocki, 180, 520, 180, 60, stockci, 180, 520, stock)
        statusButton = mouse(statusi, 180, 580, 180, 60, statusci, 180, 580, status)
        

        
        pygame.display.update()
        
        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()


#스토리

def story():
    global stage_first
    stage_first = 1

    while stage_story == 0:

        clock.tick(60)
        screen.fill(color)

        #스토리 이미지 출력
        sp = obj()
        sp.put_image("C:\\Users\\girookim\\Desktop\\Life_game\\game_image\\game_imagesp.PNG")
        sp.change_size(290,267)
        sp.x = round (size[0]/2 - sp.sx/2  )
        sp.y = size[1] -sp.sy - 315
        
        #텍스트 출력
        screen.blit(s1_text, (15, 325))
        screen.blit(s2_text, (15, 385))
        screen.blit(s3_text, (15, 405))
        screen.blit(s4_text, (135, 435))
        screen.blit(s5_text, (15, 470))
        

        nextButton = mouse(ni, 265, 0, 80, 50, nci, 265, 0, home)

        sp.show()

        pygame.display.update()

        # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()
        

# 5. 시작 페이지

def startp():   
    timer_stock()
    # stage = 0일 때 시작 화면                       
    while stage_first == 0:  # SB가 0이면 반복

 # FPS 설정
        clock.tick(60) #FPS(프레암)를 60으로 설정
   
     # 6.이미지
        screen.fill(color)
        bg.show() # 배경화면 출력
    #si.show()
    #sci.show() #클릭 이미지 출력
    
    #버튼 출력
        startButton = mouse(si, 40, 380, 283, 75, sci, 40, 380, story )   # 시작 버튼
        quitButton = mouse(ei, 40, 460, 283, 75, eci, 40, 460, game_quit)

    
    
    
        pygame.display.update() #이미지 계속 업로드 없으면 한 번 나오고 사라져서 안 나온 거 처럼 보임
    
            
    
 # 입력 감지
        for event in pygame.event.get():  # 키보드, 마우스 동작을 리스트 형태로 pygame.event.get에 저장
            if event.type == pygame.QUIT: # 입력된 행위가 QUIT라면
                pygame.quit()
                sys.exit()


startp()



# 7.업데이트
pygame.display.flip()
    
# 8.게임 종료
pygame.quit()