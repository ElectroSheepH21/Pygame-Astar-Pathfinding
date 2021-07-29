class Pathfinding:
    def __init__(self, spot_grid):
        self.redraw = None
        self.open_spots = []
        self.closed_spots = []
        self._debug = False
        self._diagonal = False
        self.spot_grid = spot_grid
        self.debug_spots = []
        self.path_id = 4
        self.open_id = 5
        self.closed_id = 6
        self.not_walkable_ids = []

    def find_path(self, start_spot, target_spot):
        # Reset debug spots
        for spd in self.debug_spots:
            if spd.id not in self.not_walkable_ids:
                spd.id = -1
        self.redraw()
        self.debug_spots = []

        # Reset open and closed spots
        self.open_spots = []
        self.closed_spots = []
        self.open_spots.append(start_spot)

        # Init spots
        for r in range(self.spot_grid.get_rows()):
            for c in range(self.spot_grid.get_cols()):
                sp = self.spot_grid.get_spot(c, r)
                sp.g_cost = float("inf")
                sp.update_f_cost()
                sp.came_from = None
        start_spot.g_cost = 0
        start_spot.h_cost = self.spot_grid.get_distance(start_spot, target_spot)
        start_spot.update_f_cost()

        # While open spots are available
        while len(self.open_spots) > 0:
            # Show debug spots
            if self.debug:
                for spo in self.open_spots:
                    if spo is not start_spot and spo is not target_spot:
                        spo.id = self.open_id
                        self.debug_spots.append(spo)
                for spc in self.closed_spots:
                    if spc.id not in self.not_walkable_ids and spc is not start_spot and spc is not target_spot:
                        spc.id = self.closed_id
                self.redraw()

            curr_spot = min(self.open_spots)  # Get lowest f cost

            # Path found
            if curr_spot == target_spot:
                return self.get_path(start_spot, target_spot)

            # Move the current spot from open spots to closed spots
            self.open_spots.remove(curr_spot)
            self.closed_spots.append(curr_spot)

            neighbors = self.spot_grid.get_neighbors(curr_spot, self.diagonal)
            for n in neighbors:
                if n in self.closed_spots:  # Skip if neighbor is already in closed spots
                    continue
                if n.id in self.not_walkable_ids:  # Skip if neighbor is not walkable
                    self.closed_spots.append(n)
                    continue
                temp_g_cost = curr_spot.g_cost + self.spot_grid.get_distance(curr_spot, n)  # Temp g-cost + distance to compare/choose the cheaper way
                if temp_g_cost < n.g_cost:  # If the temp g-cost is smaller than the neighbor g-cost
                    n.came_from = curr_spot  # Add the current spot as path-spot/came-from-spot to the neighbor

                    # Update neighbor costs
                    n.g_cost = temp_g_cost
                    n.h_cost = self.spot_grid.get_distance(n, target_spot)
                    n.update_f_cost()

                    # Add the neighbor to open spots if it is not not already in
                    if n not in self.open_spots:
                        self.open_spots.append(n)
        return None

    def get_path(self, start_spot, target_spot):
        # Generate path
        path = [target_spot]
        curr_spot = target_spot
        while curr_spot.came_from is not None:
            path.append(curr_spot.came_from)
            curr_spot = curr_spot.came_from
        path.reverse()

        # Show path if debug
        if self.debug:
            for sp in path:
                if sp is not start_spot and sp is not target_spot:
                    sp.id = self.path_id
                    self.debug_spots.append(sp)
            print("Path found")
        return path

    def set_redraw(self, redraw):
        self.redraw = redraw

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value

    @property
    def diagonal(self):
        return self._diagonal

    @diagonal.setter
    def diagonal(self, value):
        self._diagonal = value

    def set_debug_items(self, open_item, closed_item, path_item):
        self.open_id = open_item.id
        self.closed_id = closed_item.id
        self.path_id = path_item.id
        self.spot_grid.add_item(path_item)
        self.spot_grid.add_item(open_item)
        self.spot_grid.add_item(closed_item)

    def set_as_not_walkable(self, not_walkable_item):
        if not_walkable_item.id not in self.not_walkable_ids:
            self.not_walkable_ids.append(not_walkable_item.id)
