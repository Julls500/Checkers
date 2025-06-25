class Checkers:

  def __init__(self):
    self.init_board()

  def init_board(self):
    self.board = {}
    for col in 'ABCDEFGH':
      self.board[col] = []
      col_index = self.col_index(col)
      for row in range(8):
        if (col_index + row) % 2 != 0 and row < 3:
          color = 'O'
          self.board[col].append(Chip(color))  
        elif (col_index + row) % 2 != 0 and row > 4:
          color = '@'
          self.board[col].append(Chip(color))
        else:
          self.board[col].append('*')
    return self.board
  
  def col(self, p):
    return str(p[0]) # это ключ
  
  def row(self, p):
    return int(p[1]) - 1 # это индекс
  
  def col_index(self, p):
    return list(self.board).index(p[0]) + 1 # это порядковый номер колонки
  
  def get_cell(self, p):
    return self.board[self.col(p)][self.row(p)]
    
  def col_dif(self, f, t):
    return self.col_index(t) - self.col_index(f)
  
  def row_dif(self, f, t):
    return self.row(t) - self.row(f)
  
  def chip_remove(self, f):
    removed_chip = self.get_cell(f)
    self.board[self.col(f)][self.row(f)] = '*'
    return removed_chip
  
  def chip_move(self, f, t):
    moving_chip = self.chip_remove(f) 
    print('ход', moving_chip, 'c', f, 'на', t)
    self.board[self.col(t)][self.row(t)] = moving_chip

  def chip_to_eat(self, f, t):
    if self.row_dif(f, t) > 0:
      if self.col_dif(f, t) > 0 :
        chip_col = chr(ord(self.col(f)) + 1)
        chip_row = self.row(f) + 1
      else:
        chip_col = chr(ord(self.col(f)) - 1)
        chip_row = self.row(f) + 1
    else:
      if self.col_dif(f, t) > 0:
        chip_col = chr(ord(self.col(f)) + 1)
        chip_row = self.row(f) - 1
      else:
        chip_col = chr(ord(self.col(f)) - 1)
        chip_row = self.row(f) - 1
    coord = str(chip_col) + str(chip_row + 1) # координаты как на доске
    return coord

  def print_board(self):
    print('   A  B  C  D  E  F  G  H')
    for row in '87654321':
      print(row, end='')
      for col in 'ABCDEFGH':
        print(' ', checkers.get_cell(col + row), end='')
      print()

  def move(self, f, t):
    if self.row(t) not in range(8) or self.col(t) not in 'ABCDEFGH':
      print(f'ход {f}->{t} вы за пределами доски')
    else:
      cell_to = self.get_cell(t)
      cell_from = self.get_cell(f)
      chip_to_eat_coord = self.chip_to_eat(f, t)
      chip_to_eat = self.get_cell(chip_to_eat_coord)
      row_step = abs(self.row_dif(f, t))
      col_step = abs(self.col_dif(f, t))      
      if cell_to != '*':
        print(f'ход {f}->{t} клетка занята')
      elif cell_from == '*':
        print(f'ход {f}->{t} не выполнен, пустая клетка')
      elif row_step > 2 or col_step > 2:
        print(f'ход {f}->{t} так нельзя, ход может быть только на 1 или 2 клетки')
      elif row_step == 0 or col_step == 0 or row_step - col_step !=0:
        print(f'ход {f}->{t} так нельзя, ходить нужно по диагонали')
      elif chip_to_eat != '*' and chip_to_eat.color == cell_from.color:
        print(f'ход {f}->{t} так нельзя, своих не едят')
      else:
        if row_step == 1:
          self.chip_move(f, t)
        elif row_step == 2 and chip_to_eat != '*' :
          self.chip_move(f, t)
          print(f'ход {f}->{t} шашка', chip_to_eat, chip_to_eat_coord, 'съедена')
          self.chip_remove(chip_to_eat_coord)
        else:
          print(f'ход {f}->{t} так нельзя, ход должен быть на 1 клетку')
    self.print_board()

class Chip:

  def __init__(self, col = '*'):
    self.color = col

  def color(self):
    return self.color
  
  def __str__(self):
    return self.color
  
checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('A7', 'C5')
checkers.move('H6', 'F4')
checkers.move('F6', 'E5')