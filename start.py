import sys
import pygame as pg
from src import control

run_it = control.Control()
run_it.main_loop()
pg.quit()
sys.exit()
