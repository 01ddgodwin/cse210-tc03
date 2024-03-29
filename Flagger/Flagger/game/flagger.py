import arcade
from game import constants

setupShortcut = constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH, constants.SCREEN_TITLE, constants.GRAVITY, constants.JUMP_SPEED, constants.MOVEMENT_SPEED, constants.RIGHT_MARGIN, constants.VIEWPORT_MARGIN, constants.GRID_PIXEL_SIZE, constants.SPRITE_PIXEL_SIZE

class Flagger(arcade.Window):
    """ Flagger application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        super().__init__(width, height, title)

        # Sprite lists

        # We use an all-wall list to check for collisions.
        self.all_wall_list = None

        # Drawing non-moving walls separate from moving walls improves performance.
        self.static_wall_list = None
        self.moving_wall_list = None

        self.player_list = None       

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0
        self.end_of_map = 0
        self.game_over = False
        


    def setup(self, setupShortcut):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        arcade.play_sound(constants.BACKGROUND_MUSIC)
        self.all_wall_list = arcade.SpriteList()
        self.static_wall_list = arcade.SpriteList()
        self.moving_wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Set up the player
        # self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png", constants.SPRITE_SCALING)
        # self.player_sprite.center_x = 2 * constants.GRID_PIXEL_SIZE
        # self.player_sprite.center_y = 3 * constants.GRID_PIXEL_SIZE
        # self.player_list.append(self.player_sprite)

        # # Create floor
        # for i in range(50):
        #     wall = arcade.Sprite(":resources:images/tiles/bridgeB.png", constants.SPRITE_SCALING)
        #     wall.bottom = 0
        #     wall.center_x = i * constants.GRID_PIXEL_SIZE
        #     self.static_wall_list.append(wall)
        #     self.all_wall_list.append(wall)



        # self.physics_engine = \
        #     arcade.PhysicsEnginePlatformer(self.player_sprite,
        #                                    self.all_wall_list,
        #                                    gravity_constant=constants.GRAVITY)

        # # Set the background color
        # arcade.set_background_color(arcade.color.AMAZON)

        # # Set the viewport boundaries
        # # These numbers set where we have 'scrolled' to.
        # self.view_left = 0
        # self.view_bottom = 0

        # self.game_over = False

    # def on_draw(self):
    #     """
    #     Render the screen.
    #     """

    #     # This command has to happen before we start drawing
    #     arcade.start_render()

    #     # Draw the sprites.
    #     self.static_wall_list.draw()
    #     self.moving_wall_list.draw()
    #     self.player_list.draw()

    #     # Put the text on the screen.
    #     # Adjust the text position based on the viewport so that we don't
    #     # scroll the text too.
    #     distance = self.player_sprite.right
    #     output = f"Distance: {distance}"
    #     arcade.draw_text(output, self.view_left + 10, self.view_bottom + 20,
    #                      arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = constants.JUMP_SPEED
                arcade.play_sound(constants.JUMP_SOUND)
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = constants.MOVEMENT_SPEED

        #ADDED to restart the game.
        elif key == arcade.key.ESCAPE:
            self.setup(setupShortcut)


    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + constants.VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH - constants.RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT - constants.VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT + self.view_bottom)

