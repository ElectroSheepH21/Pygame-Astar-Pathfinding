import pygame
from CustomItems.BoxItem import BoxItem
from CustomItems.WallItem import WallItem
from CustomItems.ClosedItem import ClosedItem
from CustomItems.OpenItem import OpenItem
from CustomItems.PathItem import PathItem
from Pathfinding.Pathfinding import Pathfinding
from SpotGrid.SpotGrid import SpotGrid
from CustomItems.StartItem import StartItem
from CustomItems.TargetItem import TargetItem

# Window
WND_SIZE = (900, 900)

# Grid
GRID_SIZE = (420, 560)
SPOT_GRID_COLUMNS = 15
SPOT_GRID_ROWS = 20
GRID_COLOR = (0, 0, 0)


def redraw():
    screen.fill((255, 255, 255))
    spot_grid.draw()
    pygame.display.update()


if __name__ == '__main__':
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode(WND_SIZE)
    pygame.display.set_caption("Pygame A* Pathfinding")

    # Init spot grid
    offset = pygame.Vector2(69, 69)
    spot_grid = SpotGrid(SPOT_GRID_COLUMNS, SPOT_GRID_ROWS, screen, GRID_SIZE, offset)
    spot_grid.grid_color = (0, 0, 0)
    spot_grid.grid_on = True
    bg = pygame.image.load('images/grass.png')
    spot_grid.load_background(bg)

    start_item = StartItem()
    target_item = TargetItem()
    wall_item = WallItem()
    box_item = BoxItem()

    spot_grid.add_item(start_item)
    spot_grid.add_item(target_item)
    spot_grid.add_item(wall_item)
    spot_grid.add_item(box_item)

    # Init pathfinding
    path_item = PathItem()
    open_item = OpenItem()
    closed_item = ClosedItem()

    pf = Pathfinding(spot_grid)
    pf.set_debug_items(open_item, closed_item, path_item)
    pf.debug = True
    pf.set_as_not_walkable(wall_item)
    pf.set_as_not_walkable(box_item)
    pf.diagonal = False
    pf.set_redraw(redraw)

    # Init loop settings
    run = True
    curr_pen_id = 1
    setState = False
    clearState = False

    # Game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    curr_pen_id = start_item.id
                elif event.key == pygame.K_t:
                    curr_pen_id = target_item.id
                elif event.key == pygame.K_b:
                    curr_pen_id = box_item.id
                elif event.key == pygame.K_SPACE:
                    start_spot = spot_grid.find_spot(start_item)
                    target_spot = spot_grid.find_spot(target_item)
                    path = pf.find_path(start_spot, target_spot)
                    if path is not None:
                        print("Path available")
                    else:
                        print("No path available")
            elif event.type == pygame.KEYUP:
                curr_pen_id = wall_item.id
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    spot_grid.set_spot(pos, curr_pen_id)
                    setState = True
                elif event.button == 3:
                    spot_grid.clear_spot(pos)
                    clearState = True
            elif event.type == pygame.MOUSEBUTTONUP:
                setState = False
                clearState = False
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if setState:
                    spot_grid.set_spot(pos, curr_pen_id)
                elif clearState:
                    spot_grid.clear_spot(pos)
        redraw()
