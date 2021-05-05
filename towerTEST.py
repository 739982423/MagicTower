import sys, pygame
import pygame.freetype


Firstfloor_list2D =[
[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,  1],

[-1, 0, 0, 0, 0, -1,1,  10,0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  8, 0, 0, 2, 0, 1, 9, 5, 0, 1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 18,0, 1, 0, 1, 9, 8, 0, 1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  1, 2, 1, 1, 75, 1, 1, 1, 2, 1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  5, 0, 0, 1, 0, 2, 13,14,15,1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 17,0, 1, 0, 1, 1, 1, 1, 1, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 1, 1, 2, 1, 1, 1, 2, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  8, 0, 5, 1, 5, 0, 5, 1, 0, 15,0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  8, 9, 5, 1, 0, 0, 0, 1, 19,9,16 ,  1],

[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,  1]

]
Secondfloor_list2D = [
[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,  1],

[-1, 0, 0, 0, 0, -1,1,  11,0, 3, 0, 0, 0, 0, 0, 0, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 1, 1, 0, 34,0, 34,0, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 5, 5, 1, 0, 0, 0, 1, 0, 75,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 5, 0, 12,0, 0, 0, 12,0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 74,0, 1, 0, 0, 0, 1, 0, 73,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 0, 0, 12,0, 0, 0, 12,0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 1, 1, 1, 0 ,0, 0, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 1, 9, 0, 1, 0, 0, 0, 1, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  10,1, 9, 0, 12,0, 0, 0, 12,0, 0 ,  1],

[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,  1]

]
thirdfloor_list2D =[
[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   1],

[-1, 0, 0, 0, 0, -1,1,  5, 5, 1, 5, 5, 5, 1, 0, 1, 0, 8 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 8, 1, 8, 0, 5, 1, 0, 2, 17,0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  29,0, 1, 8, 0, 6, 1, 0, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  2, 1, 1, 1, 0, 1, 1, 0, 1, 0, 75,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 22,0, 0, 0, 13,0, 0, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  2, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  22,0, 1, 1, 0, 1, 1, 0, 1, 0, 8 ,  1],
[-1, 0, 0, 0, 0, -1,1,  0, 5, 1, 0, 0, 0, 1, 0, 2, 29,5 ,  1],
[-1, 0, 0, 0, 0, -1,1,  8, 5, 1, 0, 0, 0, 1, 0, 1, 1, 1 ,  1],
[-1, 0, 0, 0, 0, -1,1,  1, 1, 1, 1, 0, 1, 1, 13,1, 0, 0 ,  1],
[-1, 0, 0, 0, 0, -1,1,  11,0, 0, 0, 0, 0, 1, 0, 2, 0, 10,  1],

[-1,-1,-1,-1,-1,-1 ,1,  1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1,   1]

]
fourthfloor_list2D = [
[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1],

[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11,  1],

[-1,-1,-1,-1,-1,-1 ,1,  1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1,  1]

]
finalfloor_list2D = [
[-1,-1,-1,-1,-1, -1,1,  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1],

[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,   1],
[-1, 0, 0, 0, 0, -1,1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11,  1],

[-1,-1,-1,-1,-1,-1 ,1,  1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1,  1]

]
maps_detail_list = [Firstfloor_list2D,Secondfloor_list2D,thirdfloor_list2D,fourthfloor_list2D,finalfloor_list2D]
height = 115
text_display_flag = 0

def attr_display(health = "1000", attack = "40", defence = "10", coin = "0", exp = "0", yk = "0", bk = "0", rk = "0"):
    for i in range(1,5):
        for j in range(1,12):
            screen.blit(ground11_image,(32 * i, 32 * j))
    WHITE = 255, 255, 255
    f1 = pygame.freetype.Font("C://Windows//Fonts//simhei.ttf")
    f2 = pygame.font.Font("C://Windows//Fonts//simhei.ttf",28)
    f2.set_italic(True)

    #title__fontrect = f1.render_to(screen, (60, 48), "魔 塔", fgcolor=WHITE, size=30)
    #设置标题
    title__fontrect = f2.render("魔 塔",True,WHITE)
    screen.blit(title__fontrect,(60,48))
    #设置人物属性
    lv_fontrect = f1.render_to(screen, (95, 105), "Lv 1", fgcolor=WHITE, size=20)
    health_fontrect = f1.render_to(screen, (55, 140), "生命:", fgcolor=WHITE, size=20)
    attack_fontrect = f1.render_to(screen, (55, 165), "攻击:", fgcolor=WHITE, size=20)
    defence_fontrect = f1.render_to(screen, (55, 190), "防御:", fgcolor=WHITE, size=20)
    defence_fontrect = f1.render_to(screen, (55, 215), "金币:", fgcolor=WHITE, size=20)
    defence_fontrect = f1.render_to(screen, (55, 240), "经验:", fgcolor=WHITE, size=20)
    #设置道具数值
    health_value_fontrect = f1.render_to(screen, (110, 142), health, fgcolor=WHITE, size=20)
    attack_value_fontrect = f1.render_to(screen, (110, 167), attack, fgcolor=WHITE, size=20)
    defence_value_fontrect = f1.render_to(screen, (110, 192), defence, fgcolor=WHITE, size=20)
    coin_value_fontrect = f1.render_to(screen, (110, 217), coin, fgcolor=WHITE, size=20)
    exp_value_fontrect = f1.render_to(screen, (110, 242), exp, fgcolor=WHITE, size=20)
    yellowkey_value_fontrect = f1.render_to(screen, (110, 285), yk, fgcolor=WHITE, size=20)
    bluekey_value_fontrect = f1.render_to(screen, (110, 317), bk, fgcolor=WHITE, size=20)
    redkey_value_fontrect = f1.render_to(screen, (110, 349), rk, fgcolor=WHITE, size=20)

    screen.blit(items_image.subsurface(1 * 32, 1 * 32, 32, 32), (50, 275))
    screen.blit(items_image.subsurface(2 * 32, 1 * 32, 32, 32), (50, 307))
    screen.blit(items_image.subsurface(3 * 32, 1 * 32, 32, 32), (50, 339))
    screen.blit(hero_image.subsurface(0, 0, 32, 32), (50, 88))

    pygame.display.update()

def text_update():
    for i in range(19,25):
        for j in range(13):
            screen.blit(wall_image.subsurface(0, 3 * 32, 32 ,32),(i * 32 , j * 32))
    pygame.display.update()

def text_display(str,num):
    text_update()
    height = 145
    talktext_bg_image.set_alpha(0)

    my_font = pygame.font.Font("C://Windows//Fonts//simhei.ttf",19)
    my_font.set_italic(True)
    lines = str.strip().splitlines()
    for line in lines:
        text = my_font.render(line.strip(),True,(255,255,0))
        r = text.get_rect()
        r.midtop = 710,height
        screen.blit(text,r)
        height += my_font.get_linesize()
    if num == 62:
        screen.blit(npc_image.subsurface(0, 0, 32 ,32),(690,100))
    pygame.display.flip()

props_num_dict = {
    'yellow_key':0,
    'blue_key':0,
    'red_key':0
}
monster_attr_dict = {
        '0': {  # 绿色史莱姆
            'name':'绿色史莱姆',
            'health': '100',
            'attack': '10',
            'defence': '5'
        },
        '1': {  # 红色史莱姆
            'name':'红色史莱姆',
            'health': '150',
            'attack': '15',
            'defence': '5'
        },
        '2': {  # 黑色史莱姆
            'name':'黑色史莱姆',
            'health': '600',
            'attack': '20',
            'defence': '10'
        },
        '3': {  # 巨型史莱姆
            'name':'巨型史莱姆',
            'health': '850',
            'attack': '30',
            'defence': '45'
        },
        '4': {  # 小蝙蝠
            'name':'小蝙蝠',
            'health': '200',
            'attack': '20',
            'defence': '10'
        },
            '5': {  # 巨型史莱姆
            'name':'大蝙蝠',
            'health': '500',
            'attack': '45',
            'defence': '10'
        },
        '6': {  # 巨型史莱姆
            'name':'红蝙蝠',
            'health': '1200',
            'attack': '120',
            'defence': '35'
        },
        '7': {  # 吸血鬼
            'name':'吸血鬼',
            'health': '1800',
            'attack': '150',
            'defence': '100'
        },
        '8': {  # 巨型史莱姆
            'name':'骷髅怪',
            'health': '300',
            'attack': '25',
            'defence': '15'
        },
        '9': {  # 巨型史莱姆
            'name':'骷髅卫兵',
            'health': '480',
            'attack': '28',
            'defence': '15'
        },
        '10': {  # 巨型史莱姆
            'name':'骷髅队长',
            'health': '950',
            'attack': '50',
            'defence': '45'
        },
        '11': {  # 巨型史莱姆
            'name':'鬼战士',
            'health': '1000',
            'attack': '110',
            'defence': '65'
        },
        '999': {  # Hero
            'name':'Hero',
            'health': 1000,
            'attack': 40,
            'defence':10
        }
    }
current_numofprops = 13
monster_image_swtichtime = 250
class attributes():

    def __init__(self,num):
        self.name = 0
        self.health = 0
        self.attack = 0
        self.defence = 0
        self.yellow_key_num = 0
        self.blue_key_num = 0
        self.red_key_num = 0
        self.coin = 0
        self.num = num

        attr_default = {'name': ' 0 ', 'health': ' 0 ', 'attack': ' 0 ', 'defence': ' 0 '}
        self.name = monster_attr_dict.get(str(self.num),attr_default).get('name')
        self.health = monster_attr_dict.get(str(self.num),attr_default).get('health')
        self.attack = monster_attr_dict.get(str(self.num),attr_default).get('attack')
        self.defence = monster_attr_dict.get(str(self.num),attr_default).get('defence')

    def set_health_attr(self,health):
        self.health = health

    def set_attack_attr(self, attack):
        self.attack = attack

    def set_attack_attr(self, defence):
        self.defence = defence

    def get_monster_attr(self,num):
        return self.name,self.health,self.attack,self.defence

    def set_props_attr(self,prop_name,option):
        if option == 1:
         props_num_dict[str(prop_name)] += 1
         if prop_name == 'yellow_key' or 'blue_key' or 'red_key':
             temp_dict = {'yellow_key':'黄钥匙','blue_key':'蓝钥匙','red_key':'红钥匙',}
             tips = "获得了一把{}".format(temp_dict[prop_name])
             text_display(tips,0)
        elif option == -1:
         props_num_dict[str(prop_name)] -= 1
         if prop_name == 'yellow_key' or 'blue_key' or 'red_key':
             temp_dict = {'yellow_key': '黄钥匙', 'blue_key': '蓝钥匙', 'red_key': '红钥匙', }
             tips = "使用了一把{}".format(temp_dict[prop_name])
             text_display(tips, 0)

    def get_props_attr(self,prop_name):
        return props_num_dict[str(prop_name)]

class enemys(pygame.sprite.Sprite):
    def __init__(self,num,dest_x,dest_y,serial_number):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = enemys_image                  #导入怪物集合贴图
        self.image = ground11_image
        self.x = dest_x
        self.y = dest_y
        self.rect = (32 * self.x, 32 * self.y, 32 ,32)    #用来表示怪物所在地图中的位置
        self.num = num                                    #用来表示怪物的类型
        self.flag = 0                                     #用来标志当前怪物的贴图是哪一种，当t满足条件时则将贴图显示切换至另一种
        self.t = 0                                        #用来判断当前是否应改变怪物贴图的显示（因为每个怪物的贴图有两种，所以需要不断切换来得到动态的效果）
        self.monster_attr = attributes(num)
        self.serial_num = serial_number

    def update(self,key,hero_flag):
        self.t += clock.get_time()
        if self.t >= monster_image_swtichtime and self.flag == 0:
            self.image = self.master_image.subsurface((32, 32 * self.num, 32, 32))
            self.flag = 1
            self.t = 0
        elif self.t >= monster_image_swtichtime and self.flag == 1:
            self.image = self.master_image.subsurface((0, 32 * self.num, 32, 32))
            self.t = 0
            self.flag = 0





class maps():
    def __init__(self,list2D):
        self.list2D = list2D
        self.enemys_list = []
        self.n = 0
        self.n2 = 0
        self.enemys_list_combat = []

    def creat_monsters(self,num,i,j):
        self.enemys_list.append(enemys(num, j, i, self.n))
        self.n += 1

    def creat_props(self,i,j):
        if self.list2D[i][j] == 0:    # items:地板
            screen.blit(ground11_image, (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == -1:
            screen.blit(attrtext_wall_image, (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 1:  # items:墙
            screen.blit(wall_image.subsurface(0 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 2:  # items:黄色门
            screen.blit(items_image.subsurface(6 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 3:  # items:蓝色门
            screen.blit(items_image.subsurface(7 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 4:  # items:红色门
            screen.blit(items_image.subsurface(8 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 5:  # items:黄色钥匙
            screen.blit(items_image.subsurface(1 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 6:  # items:蓝色钥匙
            screen.blit(items_image.subsurface(2 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 7:  # items:红色钥匙
            screen.blit(items_image.subsurface(3 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 8:  # items:红色血瓶
            screen.blit(items_image.subsurface(6 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 9:  # items:蓝色血瓶
            screen.blit(items_image.subsurface(7 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 10:  # items:上楼梯
            screen.blit(items_image.subsurface(5 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 11:  # items:下楼梯
            screen.blit(items_image.subsurface(4 * 32, 0 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        elif self.list2D[i][j] == 12:  # items:栅栏
            screen.blit(items_image.subsurface(0 * 32, 1 * 32, 32, 32), (j * 32, i * 32, 32, 32))
        else : pass

    def creat_items(self):
        for i in range(len(self.list2D)):
            for j in range(len(self.list2D[i])):
                self.creat_props(i,j)
                if self.list2D[i][j] >= current_numofprops:
                 self.creat_monsters(self.list2D[i][j] - current_numofprops,i,j)
        for k in range(self.n):
            sprites.add(self.enemys_list[k])

    def creat_after_combat(self):
        for i in range(0,13):
            for j in range(6,19):
                self.creat_props(i, j)
                if self.list2D[i][j] >= current_numofprops:
                    self.creat_monsters(self.list2D[i][j] - current_numofprops, i, j)

    def map_update(self,x,y):
        for l in range(self.n):
            if self.enemys_list[l].x == y and self.enemys_list[l].y == x:
                #print(self.n)
                sprites.remove(self.enemys_list[l])
                self.list2D[x][y] = 0
        self.creat_after_combat()
        pygame.display.update()

    def all_sprites_remove(self):
        for l in  range(self.n):
            sprites.remove(self.enemys_list[l])

    '''
    def stairs_update(self,new_reach_flag,key):
        if new_reach_flag == 1:
         for i in range(len(self.list2D)):
            for j in range(len(self.list2D[i])):
                if self.list2D[i][j] == 10 or 11:
                    if key == pygame.K_RIGHT:
                     screen.blit(items_image.subsurface(5 * 32, 0 * 32, 32, 32), ((j-1) * 32, i * 32, 32, 32))
                     screen.blit(items_image.subsurface(4 * 32, 0 * 32, 32, 32), ((j-1) * 32, i * 32, 32, 32))
                    elif key == pygame.K_LEFT:
                     screen.blit(items_image.subsurface(5 * 32, 0 * 32, 32, 32), ((j+1) * 32, i * 32, 32, 32))
                     screen.blit(items_image.subsurface(4 * 32, 0 * 32, 32, 32), ((j+1) * 32, i * 32, 32, 32))
                    elif key == pygame.K_UP:
                     screen.blit(items_image.subsurface(5 * 32, 0 * 32, 32, 32), (j * 32, (i+1) * 32, 32, 32))
                     screen.blit(items_image.subsurface(4 * 32, 0 * 32, 32, 32), (j * 32, (i+1) * 32, 32, 32))
                    elif key == pygame.K_DOWN:
                     screen.blit(items_image.subsurface(5 * 32, 0 * 32, 32, 32), (j * 32, (i-1) * 32, 32, 32))
                     screen.blit(items_image.subsurface(4 * 32, 0 * 32, 32, 32), (j * 32, (i-1) * 32, 32, 32))


        return 0
    '''

    def update(self):
         self.creat_items()

         pygame.display.update()

class Heros(pygame.sprite.Sprite):
    def __init__(self,current_map):
        pygame.sprite.Sprite.__init__(self)
        # 角色总贴图
        self.master_image = hero_image

        # 角色初始贴图
        self.image = self.master_image.subsurface((0, 0, 32, 32))

        # 角色所在位置的外切矩形对象
        self.rect = self.master_image.get_rect()
        # 角色初始位置
        self.rect.top += 11 * 32
        self.rect.left += 11 * 32

        # 角色所在地图
        self.current_map = current_map
        self.current_map_list = current_map.list2D
        self.current_floor = 0
        # 角色所在坐标
        self.current_x = 11
        self.current_y = 11

        # 角色当前属性
        self.hero_attr = attributes(999)

        self.stairs_judge_flag = 0

    def hero_combat(self,num):

        global text_display_flag
        monster_num = num
        if num == 62:
            print("display")
            text_display('''我这里有本怪物手
                            册，你可以使用快 
                            捷键H来使用它，它
                            能帮你预测怪物对
                            你的伤害''',num)
            text_display_flag = 1
            return  False
        current_monster_attr = attributes(monster_num)

        # attributes类的get_monster_attr函数将返回一个元组(name,health,attack,defence)
        monster_name = current_monster_attr.get_monster_attr(monster_num)[0]
        monster_health = int(current_monster_attr.get_monster_attr(monster_num)[1])
        monster_attack = int(current_monster_attr.get_monster_attr(monster_num)[2])
        monster_defence = int(current_monster_attr.get_monster_attr(monster_num)[3])
        tips = '''遇到了{},
               属性: health:{}
               attack:{}
               defence:{}'''.format(monster_name,monster_health,monster_attack,monster_defence)
        text_display(tips,0)
        #print("遇到了{},属性: health:{}  attack:{}  defence:{}".format(monster_name,monster_health,monster_attack,monster_defence))

        hero_health = int(self.hero_attr.get_monster_attr(999)[1])
        hero_attack = int(self.hero_attr.get_monster_attr(999)[2])
        hero_defence = int(self.hero_attr.get_monster_attr(999)[3])



        if hero_attack > monster_defence:
             hero_each_damage = hero_attack - monster_defence
        else:
            hero_each_damage = 0

        if monster_attack > hero_defence:
             monster_each_damage = monster_attack - hero_defence
        else:
            monster_each_damage = 0

        if (hero_each_damage > 0):
            hero_health_init = hero_health
            while (monster_health > 0):
             monster_health -= hero_each_damage
             hero_health -= monster_each_damage
            if(hero_health > 0):

             # 战斗界面显示
             self.combat_display(num)

            #刷新战斗后数据
             self.hero_attr.set_health_attr(hero_health)
             print("本次战斗消耗生命：{}".format(hero_health_init - hero_health))
             print("当前hero属性是：health:{}  attack:{}  defence:{}".format(hero_health,hero_attack,hero_defence))
             self.display_hero_attr()

             tips = '''战胜了{}'''.format(monster_name)
             text_display(tips, 0)

             return True
            else:
                print("你打不过这只怪物")
                text_display("你打不过这只怪物",0)
                return False
        else:
            tips = '''你的攻击小于
                      {}的防御
                      无法对其造成伤害'''.format(monster_name)
            text_display(tips,0)
            return False


    def combat_display(self,num):
        combat_font = pygame.font.Font("C://Windows//Fonts//simhei.ttf", 20)
        combat_font.set_italic(True)

        monster_num = num
        current_monster_attr = attributes(monster_num)


        hero_health = int(self.hero_attr.get_monster_attr(999)[1])
        hero_attack = int(self.hero_attr.get_monster_attr(999)[2])
        hero_defence = int(self.hero_attr.get_monster_attr(999)[3])

        monster_name = current_monster_attr.get_monster_attr(monster_num)[0]
        monster_health = int(current_monster_attr.get_monster_attr(monster_num)[1])
        monster_attack = int(current_monster_attr.get_monster_attr(monster_num)[2])
        monster_defence = int(current_monster_attr.get_monster_attr(monster_num)[3])
        img_hero1 = hero_image.subsurface((0,0,32,32))
        img_hero2 = hero_image.subsurface((32,0,32,32))
        img_monster1 = enemys_image.subsurface((32, 32 * num, 32, 32))
        img_monster2 = enemys_image.subsurface((0, 32 * num, 32, 32))
        combat_background = ground11_image
        if hero_attack > monster_defence:
            hero_each_damage = hero_attack - monster_defence
        else:
            hero_each_damage = 0

        if monster_attack > hero_defence:
            monster_each_damage = monster_attack - hero_defence
        else:
            monster_each_damage = 0

        if (hero_each_damage > 0):
            hero_health_init = hero_health
            sprites.draw(screen)

            for i in range(4,9):
                for j in range(6,18):
                    screen.blit(combat_background,(j*32+20,i*32-20))

            pygame.draw.rect(screen, (155, 255, 255), (6 * 32 + 20, 4 * 32 - 20, 12 * 32 , 5 * 32), 4)

            screen.blit(img_monster2, (13 * 32 + 20,  7 * 32 - 20))
            screen.blit(combat_font.render('生命:' + str(monster_health), 1, (253, 215, 6)), (420, 120))
            screen.blit(combat_font.render('攻击:' + str(monster_attack), 1, (253, 215, 6)), (420, 145))
            screen.blit(combat_font.render('防御:' + str(monster_defence), 1, (253, 215, 6)), (420, 170))

            while (monster_health > 0):
                for i in range(4, 9):
                    for j in range(6, 12):
                        screen.blit(combat_background, (j * 32 + 20, i * 32 - 20))

                pygame.draw.rect(screen, (155, 255, 255), (6 * 32 + 20, 4 * 32 - 20, 12 * 32 , 5 * 32), 4)


                screen.blit(ground11_image, (13 * 32 + 20,  7 * 32 - 20))
                screen.blit(img_monster2, (13 * 32 + 20,  7 * 32 - 20))
                screen.blit(img_hero1, (7 * 32 + 20,  7 * 32 - 20))
                screen.blit(combat_font.render('生命:' + str(hero_health), 1, (253, 215, 6)), (245, 120))
                screen.blit(combat_font.render('攻击:' + str(hero_attack), 1, (253, 215, 6)), (245, 145))
                screen.blit(combat_font.render('防御:' + str(hero_defence), 1, (253, 215, 6)), (245, 170))
                hero_health -= monster_each_damage
                pygame.display.update()

                pygame.time.wait(200)

                for i in range(4, 9):
                    for j in range(12, 18):
                        screen.blit(combat_background, (j * 32 + 20, i * 32 - 20))
                pygame.draw.rect(screen, (155, 255, 255), (6 * 32 + 20, 4 * 32 - 20, 12 * 32 , 5 * 32), 4)

                screen.blit(ground11_image,(7 * 32 + 20,  7 * 32 - 20))
                screen.blit(img_hero2,(7 * 32 + 20,  7 * 32 - 20))
                screen.blit(img_monster1, (13 * 32 + 20,  7 * 32 - 20))

                screen.blit(combat_font.render('生命:' + str(monster_health), 1, (253, 215, 6)), (420, 120))
                screen.blit(combat_font.render('攻击:' + str(monster_attack), 1, (253, 215, 6)), (420, 145))
                screen.blit(combat_font.render('防御:' + str(monster_defence), 1, (253, 215, 6)), (420, 170))
                monster_health -= hero_each_damage
                pygame.display.update()

                pygame.time.wait(100)
        else:
            pass

    def display_hero_attr(self):
        hero_health = str(self.hero_attr.get_monster_attr(999)[1])
        hero_attack = str(self.hero_attr.get_monster_attr(999)[2])
        hero_defence = str(self.hero_attr.get_monster_attr(999)[3])
        hero_yk = str(self.hero_attr.get_props_attr('yellow_key'))
        hero_bk = str(self.hero_attr.get_props_attr('blue_key'))
        hero_rk = str(self.hero_attr.get_props_attr('red_key'))
        attr_display(hero_health,hero_attack,hero_defence,yk = hero_yk,bk = hero_bk,rk = hero_rk)


    def items_judge(self,num,x,y):
        #门道具类判断
        if  num < 5:
            if num == 0:
                return  True
            elif num == 2 :
                if self.hero_attr.get_props_attr('yellow_key') >= 1:
                    self.hero_attr.set_props_attr("yellow_key", -1)
                    maplist[self.current_floor].list2D[y][x] = 0
                    self.display_hero_attr()
                    return True
                else:
                    text_display("你没有黄钥匙！",0)
                    return False
            elif num == 3:
                if self.hero_attr.get_props_attr('blue_key') >= 1:
                    self.hero_attr.set_props_attr("blue_key",-1)
                    maplist[self.current_floor].list2D[y][x] = 0
                    self.display_hero_attr()
                    return True
                else:
                    text_display("你没有蓝钥匙！",0)
                    return False
            elif num == 4:
                if self.hero_attr.get_props_attr('red_key') >= 1:
                    self.hero_attr.set_props_attr("red_key", -1)
                    maplist[self.current_floor].list2D[y][x] = 0
                    self.display_hero_attr()
                    return True
                else:
                    text_display("你没有红钥匙！",0)
                    return False
        #其他道具判断
        elif num < current_numofprops:
            if num == 5:
                self.hero_attr.set_props_attr("yellow_key",1)
                maplist[self.current_floor].list2D[y][x] = 0
                self.display_hero_attr()
            elif num == 6:
                self.hero_attr.set_props_attr("blue_key",1)
                maplist[self.current_floor].list2D[y][x] = 0
                self.display_hero_attr()
            elif num == 7:
                self.hero_attr.set_props_attr("red_key",1)
                maplist[self.current_floor].list2D[y][x] = 0
                self.display_hero_attr()
            elif num == 8:
                self.hero_attr.set_health_attr(self.hero_attr.get_monster_attr(999)[1]+150)
                maplist[self.current_floor].list2D[y][x] = 0
                text_display('''获得了红血瓶
                                生命+150
                                当前生命为：{}'''.format(self.hero_attr.get_monster_attr(999)[1]),0)
                self.display_hero_attr()
            elif num == 9:
                self.hero_attr.set_health_attr(self.hero_attr.get_monster_attr(999)[1]+500)
                maplist[self.current_floor].list2D[y][x] = 0
                text_display('''获得了蓝血瓶
                                生命+500
                                当前生命为：{}'''.format(self.hero_attr.get_monster_attr(999)[1]),0)
                self.display_hero_attr()
            elif num == 10:
                #print(self.current_floor)
                print('当前是第{}层'.format(self.current_floor + 1))
                maplist[self.current_floor].all_sprites_remove()                          #maplist是map类对象的列表，self.currentfloor是记录hero所在层的变量，先调用当前层的map对象的all_sprites_remove函数
                self.current_floor += 1                                                   #再将所在层加1
                maplist[self.current_floor] = maps(maps_detail_list[self.current_floor])  #再创建一个新的map对象作为下一层的map对象
                self.current_map = maplist[self.current_floor]
                self.current_map_list = maplist[self.current_floor].list2D                     #再将hero类中的current_map更新至新层的list_2D
                maplist[self.current_floor].update()                                      #最后调用新层map对象的update函数，实现画面更新
                self.stairs_judge_flag = 1
                self.display_hero_attr()
                return True
            elif num == 11:
                maplist[self.current_floor].all_sprites_remove()
                self.current_floor -= 1
                maplist[self.current_floor] = maps(maps_detail_list[self.current_floor])
                self.current_map = maplist[self.current_floor]
                self.current_map_list = maplist[self.current_floor].list2D
                maplist[self.current_floor].update()
                print('当前是第{}层'.format(self.current_floor + 1))
                self.stairs_judge_flag = 1
                self.display_hero_attr()
                return True

            else:
                pass
                '''其他道具'''
            return True


    def stairs_judge(self,stair_x,stair_y,key):
        if self.current_map_list[stair_y][stair_x + 1] == 0:
            print("选择右侧")
            if key == pygame.K_UP:
             self.rect.top -= 32
             self.rect.left += 32
             self.current_x = stair_x + 1
             self.current_y = stair_y
            elif key == pygame.K_DOWN:
             self.rect.top += 32
             self.rect.left += 32
             self.current_x = stair_x + 1
             self.current_y = stair_y
            elif key == pygame.K_LEFT:
                pass
            elif key == pygame.K_RIGHT:
             self.rect.left += 32 * 2
             self.current_x = stair_x + 1
        elif self.current_map_list[stair_y][stair_x - 1] == 0:
            print("选择左侧")
            if key == pygame.K_UP:
             self.rect.top -= 32  #
             self.rect.left -= 32
             self.current_x = stair_x - 1
             self.current_y = stair_y
            elif key == pygame.K_DOWN:
             self.rect.top += 32
             self.rect.left -= 32
             self.current_x = stair_x - 1
             self.current_y = stair_y
            elif key == pygame.K_LEFT:
             self.rect.left -= 32 * 2
             self.current_x = stair_x - 1
            elif key == pygame.K_RIGHT:
             pass
        elif self.current_map_list[stair_y - 1][stair_x] == 0:
            print("选择上方")
            if key == pygame.K_UP:
             self.rect.top -= 32 * 2
             self.current_y = stair_x - 1
            elif key == pygame.K_DOWN:
             pass
            elif key == pygame.K_LEFT:
             self.rect.left -= 32
             self.rect.top -= 32
             self.current_x = stair_x
             self.current_y = stair_y - 1
            elif key == pygame.K_RIGHT:
             self.rect.left += 32
             self.rect.top -= 32
             self.current_x = stair_x
             self.current_y = stair_y - 1
             pass
        elif self.current_map_list[stair_y + 1][stair_x] == 0:
            print("选择下方")
            if key == pygame.K_UP:
             pass
            elif key == pygame.K_DOWN:
             self.rect.top += 32 * 2
             self.current_y = stair_x + 1
            elif key == pygame.K_LEFT:
             self.rect.left -= 32
             self.rect.top += 32
             self.current_x = stair_x
             self.current_y = stair_y + 1
            elif key == pygame.K_RIGHT:
             self.rect.left += 32
             self.rect.top += 32
             self.current_x = stair_x
             self.current_y = stair_y + 1
        self.image = self.master_image.subsurface((0, 0, 32, 32))


    def hero_move(self, event_key, hero_flag ,enermy_flag = 0):
        global text_display_flag
        next_y = self.current_y - 1
        next_x = self.current_x
        num = self.current_map_list[next_y][next_x]

        if event_key == pygame.K_s:
            if text_display_flag == 1:
                #blit右侧对话框
                text_display_flag1 = 0

        if event_key == pygame.K_UP:
            if hero_flag == 0:
                if self.current_y > 0 :
                    if  num != 1 and num != -1 :
                        if num >= current_numofprops:
                           combat_judge = self.hero_combat(num - current_numofprops)
                           if combat_judge:
                            maplist[self.current_floor].map_update(next_y,next_x)
                            self.rect.top -= 32
                            self.current_y -= 1
                            self.image = self.master_image.subsurface((0, 96, 32, 32))
                        elif self.items_judge(num,next_x,next_y):
                            if self.stairs_judge_flag:
                                self.stairs_judge(next_x,next_y,event_key)
                                self.stairs_judge_flag = 0
                            else:
                             self.rect.top -= 32
                             self.current_y -= 1
                             self.image = self.master_image.subsurface((0, 96, 32, 32))
                             print("当前位置：({},{})".format(next_x - 5,next_y + 1))
                    else :
                        print("上方是墙，无法移动")
                else:
                    print("上方超出地图范围")
            elif hero_flag == 1:
                self.image = self.master_image.subsurface((32, 96, 32, 32))
            elif hero_flag == 2:
                self.image = self.master_image.subsurface((0, 96, 32, 32))

        elif event_key == pygame.K_DOWN:
            next_y = self.current_y + 1
            next_x = self.current_x
            num = self.current_map_list[next_y][next_x]
            if hero_flag == 0:
                if self.current_y < 12:
                     if num != 1 and num != -1 :
                         if num >= current_numofprops:
                             combat_judge = self.hero_combat(num - current_numofprops)
                             if combat_judge:
                                maplist[self.current_floor].map_update(next_y, next_x)
                                self.rect.top += 32
                                self.current_y += 1
                                self.image = self.master_image.subsurface((0, 0, 32, 32))
                         elif self.items_judge(num,next_x,next_y):
                             if self.stairs_judge_flag:
                                 self.stairs_judge(next_x, next_y,event_key)
                                 self.stairs_judge_flag = 0
                             else:
                              self.rect.top += 32
                              self.current_y += 1
                              self.image = self.master_image.subsurface((0, 0, 32, 32))
                              print("当前位置：({},{})".format(next_x - 5,next_y + 1))
                     else:
                        print("下方是墙，无法移动")
                else:
                    print("下方超出地图范围")
            elif hero_flag == 1:
             self.image = self.master_image.subsurface((32, 0, 32, 32))
            elif hero_flag == 2:
             self.image = self.master_image.subsurface((0, 0, 32, 32))

        elif event_key == pygame.K_LEFT:
            next_y = self.current_y
            next_x = self.current_x - 1
            num = self.current_map_list[next_y][next_x]
            if hero_flag == 0:
                if self.current_x > 5 :
                    if num != 1 and num != -1 :
                        if num >= current_numofprops:
                            combat_judge = self.hero_combat(num - current_numofprops)
                            if combat_judge:
                              maplist[self.current_floor].map_update(next_y, next_x)
                              self.rect.left -= 32
                              self.current_x -= 1
                              self.image = self.master_image.subsurface((0, 32, 32, 32))
                        elif self.items_judge(num,next_x,next_y):
                            if self.stairs_judge_flag:
                                self.stairs_judge(next_x, next_y,event_key)
                                self.stairs_judge_flag = 0
                            else:
                             self.rect.left -= 32
                             self.current_x -= 1
                             self.image = self.master_image.subsurface((0, 32, 32, 32))
                             print("当前位置：({},{})".format(next_x - 5,next_y + 1))
                    else:
                        print("左侧是墙，无法移动")
                else:
                    print("左侧超出地图范围")
            elif hero_flag == 1:
                self.image = self.master_image.subsurface((32, 32, 32, 32))
            elif hero_flag == 2:
                self.image = self.master_image.subsurface((0, 32, 32, 32))

        elif event_key == pygame.K_RIGHT:
            next_y = self.current_y
            next_x = self.current_x + 1
            num = self.current_map_list[next_y][next_x]
            if hero_flag == 0:
                if self.current_x <18:
                    if num != 1 and num != -1 :
                        if num >= current_numofprops:
                            combat_judge = self.hero_combat(num - current_numofprops)
                            if combat_judge:
                              maplist[self.current_floor].map_update(next_y, next_x)
                              self.rect.left += 32
                              self.current_x += 1
                              self.image = self.master_image.subsurface((0, 64, 32, 32))
                        elif self.items_judge(num,next_x,next_y):
                            if self.stairs_judge_flag:
                                self.stairs_judge(next_x, next_y,event_key)
                                self.stairs_judge_flag = 0
                            else:
                             self.rect.left += 32
                             self.current_x += 1
                             self.image = self.master_image.subsurface((0, 64, 32, 32))
                             print("当前位置：({},{})".format(next_x - 5,next_y + 1))
                    else:
                        print("右侧是墙，无法移动")
                else:
                    print("右侧超出地图范围")
            elif hero_flag == 1:
                self.image = self.master_image.subsurface((32, 64, 32, 32))
            elif hero_flag == 2:
                self.image = self.master_image.subsurface((0, 64, 32, 32))
        else:
           pass

    def update(self, event_key, hero_flag ,enermy_flag = 0):
        self.hero_move(event_key, hero_flag)

    ''' def move_display(self,key):
        sprites.clear(screen, clear_callback)
        sprites.update(key,0)
        updates = sprites.draw(screen)
        pygame.display.update()

        sprites.clear(screen, clear_callback)
        sprites.update(key,1)
        updates = sprites.draw(screen)
        pygame.display.update()

        pygame.time.wait(100)
        sprites.clear(screen, clear_callback)
        sprites.update(key,2)
        updates = sprites.draw(screen)
        pygame.display.update()'''

#Group对象的clear方法所需的回调函数，可清除上次绘制的所有精灵对象
def clear_callback(surf, rect):
    surf.blit(ground11_image,rect)


#初始化及图片导入
pygame.init()
screen_size =800,416

pygame.display.set_mode(screen_size)

ground33_image = pygame.image.load('pictures/ground33(96p).jpg')
ground33_image_rect = ground33_image.get_rect()
hero_image = pygame.image.load("pictures/hero.png")
hero1_image = pygame.image.load("pictures/hero1.png")
ground11_image = pygame.image.load("pictures/ground.png")
wall_image = pygame.image.load("pictures/walls.png")
items_image = pygame.image.load("pictures/items.jpg")
enemys_image = pygame.image.load("pictures/enemys2.png")
attrtext_wall_image = wall_image.subsurface(0, 2 * 32, 32 ,32)
talktext_bg_image = pygame.image.load("pictures/textbg.png")
npc_image = pygame.image.load("pictures/npc.png")
clock = pygame.time.Clock()
screen = pygame.display.get_surface()
screen_rect = screen.get_rect()
sprites = pygame.sprite.RenderUpdates()                 #生成group对象



#生成地图，并在生成地图过程中建立enermy精灵对象，再将enermy精灵对象加入精灵group
maplist =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
maplist[0] = maps(maps_detail_list[0])
maplist[0].update()                                     #手动调用map类的update，刷新初始地图
hero1 = Heros(maplist[0])                #建立角色精灵
sprites.add(hero1)                                      #将角色精灵加入精灵group

#文字+属性显示
attr_display()
text_update()

#group类中调用各个精灵update函数时，先add入group的精灵先执行其update，后add的精灵后执行
#其结果就是后导入的精灵贴图会显示在前导入精灵的贴图的上层（遮挡了前导入精灵的贴图）


#主循环
const_event_type = None
while True:
        clock.tick(60)                                  #设定画面刷新帧数
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                const_event_type = event.key

        sprites.clear(screen, clear_callback)           #sprites.clear 用来清除上次sprites.draw中绘制的精灵对象
        sprites.update(const_event_type,0)              #sprites.update 可自动调用精灵group中每个精灵所属类别的update函数
        const_event_type = None                         #刷新按键信息
        updates = sprites.draw(screen)                  #sprites.draw 可绘制所有与上次绘制时状态改变的精灵，并返回一个屏幕需要改变显示的区域信息
        pygame.display.update(updates)                  #使用pygame.display.update刷新屏幕显示，因为传入了参数updates所以只刷新需要改变的区域（有助于提升性能）

