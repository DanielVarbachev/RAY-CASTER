# if self.brr_dir_x == 1 and self.wall_right:
        #     self.x += TS
        #     self.brr_dir_x = self.dir_x
        
        # elif self.brr_dir_x == -1 and self.wall_left:
        #     self.x -= TS
        #     self.brr_dir_x = self.dir_x

        # elif self.brr_dir_y == 1 and self.wall_above:
        #     self.y += TS
        #     self.brr_dir_y = self.dir_y

        # elif self.brr_dir_y == -1 and self.wall_below:
        #     self.y -= TS
        #     self.brr_dir_y = self.dir_y
        
        # else:
        #     self.brr_dir_x = self.hagrid_x
        #     self.brr_dir_y = self.hagrid_y

        #     self.brr_dir_x = random.randint(-2,2)
        #     if self.brr_dir_x == -2 or 2:
        #         self.brr_dir_y = self.y_directions[random.randint(0,1)]
            
        #     if self.brr_dir_x == self.hagrid_x * -1 != self.brr_dir_x and self.hagrid_y == 0:
        #         self.brr_dir_y = self.y_directions[random.randint(0,1)]
            
        #     if self.brr_dir_y == self.hagrid_y * -1 != self.brr_dir_y and self.hagrid_x == 0:
        #         self.brr_dir_x = self.x_directions[random.randint(0,1)]
            

        

        # if self.dir_x == 1 and self.wall_right:
        #     number = random.randint(0,3)
        # elif self.dir_x == -1 and not self.wall_left:
        #     number = random.randint(0,3)
        # elif self.dir_y == 1 and not self.wall_below:
        #     number = random.randint(0,3)
        # elif self.dir_y == -1 and not self.wall_above:
        #     number = random.randint(0,3)