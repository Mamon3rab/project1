import pygame 
from pygame.locals import*
import pygame.mixer
import sys
pygame.init()
screenwidth=800
screenhight=800
screen = pygame.display.set_mode([screenwidth, screenhight])
pygame.display.set_caption('Two-Player')
font = pygame.font.Font('freesansbold.ttf', 20)
check_king_sound = pygame.mixer.Sound("switch22.ogg")
piece_click_sound = pygame.mixer.Sound("click2.ogg")
music_game=pygame.mixer.Sound("ggs.mp3")
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0),(1, 0),(2, 0),(3, 0),(4, 0),(5, 0),(6, 0),(7, 0),
                   (0, 1),(1, 1),(2, 1),(3, 1),(4, 1),(5, 1),(6, 1),(7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7),(1, 7),(2, 7),(3, 7),(4, 7),(5, 7),(6, 7),(7, 7),
                   (0, 6),(1, 6),(2, 6),(3, 6),(4, 6),(5, 6),(6, 6),(7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class MainMenu:
    def __init__(self, screen, width, height):

        self.screen = screen
        self.width = width
        self.height = height
        # إعداد نافذة العرض
        window_size = (800, 800)


        # تهيئة الخط
        self.font = pygame.font.Font(None, 36)

        # تهيئة الأزرار
        button_width = 200
        button_height = 50
        button_margin = 20

        # توسيط الأزرار في الشاشة
        horizontal_spacing = window_size[0] // 2 - button_width // 2
        vertical_spacing = window_size[1] // 2 - (2 * button_height + button_margin) // 2

        # تهيئة مستطيلات الأزرار
        self.start_button_rect = pygame.Rect(horizontal_spacing, vertical_spacing, button_width, button_height)
        self.options_button_rect = pygame.Rect(horizontal_spacing, vertical_spacing + button_height + button_margin, button_width, button_height)
        self.quit_button_rect = pygame.Rect(horizontal_spacing, vertical_spacing + 2 * (button_height + button_margin), button_width, button_height)

        button_click_sound = pygame.mixer.Sound('click5.ogg')
        self.button_click_sound = button_click_sound
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(event.pos):
                    self.on_start_button_click()

                if self.options_button_rect.collidepoint(event.pos):
                    self.on_options_button_click()

                if self.quit_button_rect.collidepoint(event.pos):
                    self.on_quit_button_click()

    def on_start_button_click(self):
        global is_in_main_menu
        is_in_main_menu=False
        print("start")
        
        # تشغيل الصوت عند النقر على زر Start
        self.button_click_sound.play()
        
        # اكتب الإجراء الذي يحدث عند النقر على زر Start هنا

    def on_options_button_click(self):
        print("Options button clicked")

        # تشغيل الصوت عند النقر على زر options
        self.button_click_sound.play()
        # اكتب الإجراء الذي يحدث عند النقر على زر Options هنا

    def on_quit_button_click(self):
        print("Quit button clicked")
        pygame.quit()
        sys.exit()
    
    

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, self.start_button_rect)
        pygame.draw.rect(self.screen, WHITE, self.options_button_rect)
        pygame.draw.rect(self.screen, WHITE, self.quit_button_rect)

        start_text = self.font.render("Start", True, BLACK)
        options_text = self.font.render("Options", True, BLACK)
        quit_text = self.font.render("Quit", True, BLACK)

        self.screen.blit(start_text, (self.start_button_rect.x + self.start_button_rect.width // 2 - start_text.get_width() // 2, self.start_button_rect.y + self.start_button_rect.height // 2 - start_text.get_height() // 2))
        self.screen.blit(options_text, (self.options_button_rect.x + self.options_button_rect.width // 2 - options_text.get_width() // 2, self.options_button_rect.y + self.options_button_rect.height // 2 - options_text.get_height() // 2))
        self.screen.blit(quit_text, (self.quit_button_rect.x + self.quit_button_rect.width // 2 - quit_text.get_width() // 2, self.quit_button_rect.y + self.quit_button_rect.height // 2 - quit_text.get_height() // 2))

        pygame.display.flip()

    def run(self):
        global is_in_main_menu

        #while True:
        if is_in_main_menu:
            self.handle_events()
            self.draw()
# إنشاء كائن MainMenu وتشغيله
menu = MainMenu(screen, screenwidth, screenhight)
is_in_main_menu =True
# load in game piece image
class item():
    def __init__(self,path,width,height):
        self.path=path
        self.width=width
        self.height=height
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
    def set_data(self,path,width,height):
        self.path=path
        self.width=width
        self.height=height
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))

    def blit(self,i):
        screen.blit(self.image, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
    

wiedth = 80
height = 80
black_queen= item('images/black queen.png',wiedth,height)
black_king= item('images/black king.png',wiedth,height)
black_rook= item('images/black rook.png',wiedth,height)
black_bishop= item('images/black bishop.png',wiedth,height)
black_knight= item('images/black knight.png',wiedth,height)
black_pawn= item('images/black pawn.png',wiedth-15,height-15)


white_queen = item('images/white queen.png', wiedth, height)
white_king = item('images/white king.png', wiedth, height)  # تم تحديد صورة مختلفة للملك الأبيض
white_rook = item('images/white rook.png', wiedth, height)  # تم تحديد صورة مختلفة للقلعة البيضاء
white_bishop = item('images/white bishop.png', wiedth, height)
white_knight = item('images/white knight.png', wiedth, height)
white_pawn = item('images/white pawn.png', wiedth-15, height-15)  # تم تحديد صورة مختلفة للبيدق الأبيض
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

class ChessBoard:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def draw_board(self):
        for i in range(32):
            column = i % 4
            row = i // 4
            if row % 2 == 0:
                pygame.draw.rect(self.screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
            else:
                pygame.draw.rect(self.screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
            for i in range(9):
                pygame.draw.line(self.screen, 'black', (0, 100 * i), (800, 100 * i), 2)
                pygame.draw.line(self.screen, 'black', (100 * i, 0), (100 * i, 800), 2)
board = ChessBoard(screen, screenwidth, screenhight)


# رسم القطع على اللوحة
def draw_pieces():
  # رسم قطع اللاعب الأبيض
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        screen.blit(white_images[index].image, (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)
     
 # رسم قطع اللاعب الأسود
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        screen.blit(black_images[index].image, (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)
                

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# الدالة لفحص حركات الملك الممكنة
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    
    # 8 مربعات لفحص حركات الملك، حيث يمكنه التحرك مربع واحد في أي اتجاه
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    
    return moves_list



# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list



def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    
    for i in range(len(moves)):
        pygame.draw.circle(screen, "RED", (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)
        
# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
                        check_king_sound.play()
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)
                        check_king_sound.play()
                        
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))
                    
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')          
music_game.play(-1)  
RUN =True
while RUN:
    screen.fill(BLACK)

    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    if is_in_main_menu == True:# متغير اذا مان في الفائمة الرئيسية
        menu.run()
    else:
            board.draw_board()
            draw_pieces()
            draw_check()
    
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pygame.event.get():
        if event.type == QUIT:
            RUN = False    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            piece_click_sound.play()
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                check_king_sound.play()
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.update()

pygame.quit()