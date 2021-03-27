import pygame
import sys

# 1단계 : 화면 설정, fps 설정
# 2단계 : 공룡, 공룡 점프
# 3단계 : 장애물

pygame.init()
pygame.display.set_caption('awesome_jumping_dino')
max_height = 400
max_width = 800

def main():
# 1단계 : 화면 설정 및 fps 설정
screen = pygame.display.set_mode((max_width,max_height))
fps = pygame.time.Clock()

# 2단계 : 공룡
dino1 = pygame.image.load('dinoimage1.png')
dino2 = pygame.image.load('dinoimage2.png')
dinoheight = dino1.get_size()[1]
dinobutton = max_height - dino_height
dino_x = 50
dino_y = dino_buttom
jump_top = 200
leg_swap = True
is_butoon = True
is_go_up = False

# 3단계 장애물
tree = pygame.image.load('treeimage1.png')
tree_height = tree.get_size()[1]
tree_x = max_width
tree_y = max_height - tree_height

while True:
screen.fill((255, 255, 255))

# 이벤트
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
sys.exit()
elif event.type == pygame.KEYDOWN:
if is_butoon:
is_go_up = True
is_butoon = False
# 2단계 : 공룡 - 움직임
if is_go_up:
dino_y -= 10.0
elif not is_go_up and not is_butoon:
dino_y += 10.0

# 2단계 : 공룡 - 움직임[top and bottom check]
if is_go_up and dino_y <= jump_top:
is_go_up = False
if not is_butoon and dino_y >= dino_bottom:
is_butoon = True
dino_y = dino_bottom

# 3단계 : 장애물 움직임
tree_x -= 12.0
if tree_x <= 0:
tree_x = max_width

# 3단계 : 장애물 구현
screen.blit(tree,(tree_x,tree_y))

# 2단계 : 공룡 구현
if leg_swap:
screen.blit(dino1,(dino_x,dino_y))
else:
screen.blit(dino2,(dino_x,dino_y))

# 마무리
pygame.display.update()
fps.tick(30)

if __name__ == ' __main__ ' :
main()