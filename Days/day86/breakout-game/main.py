# python standard library
from abc import ABCMeta
from abc import abstractproperty
from collections import namedtuple
from copy import copy
import re
import string
import tkinter

BLUE = "#0000ff"
LAVENDER = "#aaaaff"
WHITE = "#ffffff"
NUMERIC = (int, float)

REVERSE_DIRECTION = -1
LEFT = -1
RIGHT = LEFT * REVERSE_DIRECTION
UP = -1
EDGE_OF_SCREEN = 0
NO_MOVEMENT = 0


Coordinates = namedtuple("Coordinates", ["top_left_x",
                                         "top_left_y",
                                         "bottom_right_x",
                                         "bottom_right_y"])


class BaseWidget(metaclass=ABCMeta):
    """base class for game object's

    Parameters
    ----------

    canvas: tkinter.Canvas
      canvas to draw on
    """
    @abstractproperty
    def item(self):
        """the canvas item"""
        return
    
    @property
    def position(self):
        """the coordinates of the object on the canvas

        Returns
        -------

        tuple: x0, y0, x1, y1
        """
        x0, y0, x1, y1 = self.canvas.coords(self.item)
        return Coordinates(top_left_x=x0,
                        top_left_y=y0,
                        bottom_right_x=x1,
                        bottom_right_y=y1)
    
    def move(self, horizontal_offset, vertical_offset):
        """move this object to the coordinates

            Parameters
            ----------

            horizontal_offset: int
            x-axis pixels to move
            vertical_offset: int
            y-axis pixels to move
            """
        self.canvas.move(self.item, horizontal_offset, vertical_offset)
        return
    
    def delete(self):
        """destroy this canvas item"""
        self.canvas.delete(self.item)
        return
    

class BaseSettings(metaclass=ABCMeta):
    """fluent interface"""
    _hex_pattern = None

    @abstractproperty
    def attributes(self):
        """list of attribute names
       This is used by the call to check the attributes
       """
        return
    
    @property
    def hex_pattern(self):
        """compiled regex to match hex-colors"""
        if BaseSettings._hex_pattern is None:
            hex_character = "\da-fA-f"
            base = "(?P<{{0}}[{0}])(?P={{0}})".format(hex_character)
            BaseSettings._hex_pattern = re.compile("#" +
                                                base.format("r") +
                                                base.format("g") +
                                                base.format("b"))
        return BaseSettings._hex_pattern
    
    def check_hex_color(self, value, identifier):
        """checks the color is a valid hex-code
        Parameters
        ----------
        value: string
        color-code to check
        identifier: string
        error-message identifier

        Raises
        ------
        TypeError: if string is malformed
        """
        if not re.match("#" + "[{0}]".format(string.hexdigits) * 6, value):
            raise TypeError("{0} must be a 6-digit hex string, not {1}".format(
                identifier, value))

        return
    

    def assert_positive_number(self, value, identifier):
        """checks the value

        Parameters
        ----------

        value: int or float
        value to check
        identifier: string
        something for the error message

        Raises
        ------
        TypeError if value is not a positive number
        """
        self.check_numeric(value, identifier)
        self.check_positive(value, identifier)
        return
    

    def check_positive(self, value, identifier):
        """check that value is greater than zero

            Parameters
            ----------

            value: numeric
            value to check

            identifier: str
            description for error messages

            Raises
            ------

            TypeError: if value is <= 0
            """
        if not value > 0:
            raise TypeError("{0} must be greater than 0 not {1}".format(
                identifier,
                value))
        return
    

    def check_type(self, thing, identifier, expected):
        """checks that the value is the correct type
        Parameters
        ----------

        thing:
        object to check
        identifier: string
        message to identify the thing
        expected: object
        what the thing is expected to be

        Raises
        ------

        TypeError: if thing isn't as expected
        """
        if not isinstance(thing, expected):
            raise TypeError("Expected {0} to be {1} not {2}".format(identifier,
                                                                    expected,
                                                                    thing))
        return
    

    def check_types(self, thing, identifier, expected):
        """check that thing is one of multiple types

        Parameters
        ----------

        thing: object
        thing to check
        identifier: string
        identifier for error message
        expected: collection
        types that thing might be

        Raises
        ------

        TypeError if type of thing not in expected
        """
        if not type(thing) in expected:
            raise TypeError("{0} should be one of {1}, not {2}".format(
                identifier,
                expected,
                thing))
        return
    

    def check_numeric(self, thing, identifier):
        """check if thing is int or float

        Parameters
        ----------

        thing: object
        thing to check if is numeric
        identifier: string
        identifier for error message

        Raises
        ------
        TypeError if thing is not numeric
        """
        self.check_types(thing, identifier, NUMERIC)
        return
    

    def __call__(self):
        """checks that everything was set
        Raises
        ------

        TypeError:
        if any attributes weren't set

        Returns
        -------

        GameSettings: this object
        """
        for attribute in self.attributes:
            if getattr(self, attribute) is None:
                raise TypeError("{0} attribute not set".format(attribute))
        return self
    

class BallDirections(object):
    """holds the current direction of the ball
    Parameters
    ----------

    horizontal: int
      positive to move left to right, negative otherwise
    vertical: int
      positive to move down, negative to move up
    """
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical
        return
    

class BallSettings(BaseSettings):
    """settings for the ball"""
    def __init__(self):
        self.x = None
        self.y = None
        self.radius = None
        self.direction = None
        self.speed = None
        self.fill = None
        self._attributes = None
        return

    @property
    def attributes(self):
        """required attributes"""
        if self._attributes is None:
            self._attributes = ("x",
                                "y",
                                "radius",
                                "direction",
                                "speed",
                                "fill")
        return self._attributes
    
    def x_position(self, x):
        """initial horizontal position

        Parameters
        ----------
        x: int or float
        pixels from the left of the canvas to start the ball
        """
        self.x = x
        self.assert_positive_number(x, "x")
        return self

    def y_position(self, y):
        """initial vertical position

        Parameters
        ----------

        y: int
        pixels from the top of the canvas
        """
        self.y = y
        self.assert_positive_number(y, "y")
        return self
    

    def circle_radius(self, radius):
        """radius of the ball
        Parameters
        ----------
        radius: int
        pixel width and height for the circle
        """
        self.radius = radius
        self.assert_positive_number(radius, "radius")
        return self
    
    def direction_vector(self, direction):
        """2-d vector for direction"""
        self.direction = direction
        self.check_type(direction, "ball direction", BallDirections)
        return self
    
    def velocity(self, speed):
        """speed of the ball
        Parameters
        ----------

        speed: number
        pixels per move
        """
        self.speed = speed
        self.assert_positive_number(speed, "speed")
        return self

    def color(self, fill):
        """fill color

        Parameters
        ----------
        fill: str
        hex-color to fill in the ball
        """
        self.fill = fill
        self.check_hex_color(fill, "fill")
        return self
    

class BallWidget(BaseWidget):
    """representation of the ball

    Parameters
    ----------

    canvas: tkinter.Canvas
      what to create the ball from

    settings: BallSettings
      initial ball settings
    """
    def __init__(self, canvas, settings):
        self.canvas = canvas
        self.settings = settings
        self._item = None
        self.direction = self.settings.direction
        self.speed = self.settings.speed
        return

    @property
    def item(self):
        """canvas item representing the ball"""
        if self._item is None:
            x, y = self.settings.x, self.settings.y
            radius = self.settings.radius
            self._item = self.canvas.create_oval(
                x-radius, y-radius,
                x+radius, y+radius,
                fill=self.settings.fill,
            )
        return self._item
    
    def update(self):
        """moves the ball
        if the ball hits something, reverses direction
        """
        ball = self.position
        width = self.canvas.winfo_width()
        if ball.top_left_x <= EDGE_OF_SCREEN or ball.bottom_right_x >= width:
            self.direction.horizontal *= REVERSE_DIRECTION
        if ball.top_left_y <= EDGE_OF_SCREEN:
            self.direction.vertical *= REVERSE_DIRECTION
        self.move(self.direction.horizontal * self.speed,
                self.direction.vertical * self.speed)
        

    def collide(self, others):
        """handles collisions

        Parameters
        ----------

        others: list
        collection of ther objects that the ball collided with
        """
        if len(others) > 1:
            self.direction.vertical *= REVERSE_DIRECTION
        elif len(others) == 1:
            ball = self.position
            x = (ball.top_left_x + ball.bottom_right_x)/2

            other = others[0].position
            if x > other.bottom_right_x:
                self.direction.horizontal = RIGHT
            elif x < other.top_left_x:
                self.direction.horizontal = LEFT
            else:
                self.direction.vertical *= REVERSE_DIRECTION
        for other in others:
            if isinstance(other, BrickWidget):
                other.hit()
        return
    

class PaddleSettings(BaseSettings):
    """settings for the player's paddle"""
    def __init__(self):
        self._attributes = None
        self.width = None
        self.height = None
        self.speed = None
        self.x = None
        self.y = None
        self.fill = None
        return

    @property
    def attributes(self):
        """list of required settings"""
        if self._attributes is None:
            self._attributes = ("width",
                                "height",
                                "speed",
                                "x",
                                "y",
                                "fill")
        return self._attributes
    

    def pixel_width(self, width):
        """width of the paddle
        Parameters
        ----------

        width: int
        pixel-width for the paddle
        """
        self.width = width
        self.check_type(width, "width", int)
        self.check_positive(width, "width")
        return self

    def pixel_height(self, height):
        """height of the paddle

        Parameters
        ----------

        height: int
        pixel-height of the paddle
        """
        self.height = height
        self.check_type(height, "height", int)
        self.check_positive(height, "height")
        return self
    
    def velocity(self, speed):
        """rate at which to move the paddle
        Parameters
        ----------

        speed: number
        amount to move paddle with each key stroke
        """
        self.speed = speed
        self.assert_positive_number(speed, "paddle speed")
        return self
    
    def x_position(self, x):
        """initial x-position
        Parameters
        ----------

        x: int
        pixels from the left of the canvas
        """
        self.x = x
        self.check_numeric(x, "x")
        self.check_positive(x, "x")
        return self

    def y_position(self, y):
        """initial y-position

        Parameters
        ----------

        y: int
        pixels from the top of the canvas
        """
        self.y = y
        self.check_numeric(y, 'y')
        self.check_positive(y, "y")
        return self
    
    def color(self, fill):
        """fill color for the rectangle

        Parameters
        ----------

        fill: str
        hex-code for the fill color
        """
        self.fill = fill
        self.check_hex_color(fill, "fill")
        return self
    


class PaddleWidget(BaseWidget):
    """the player's paddle
    Parameters
    ----------

    canvas: tkinter.Canvas
      the canvas to draw on
    settings: PaddleSettings
      initial settings for the paddle
    """
    def __init__(self, canvas, settings):
        self.canvas = canvas
        self.settings = settings
        self._item = None
        self.ball = None
        return

    @property
    def item(self):
        """the canvas item for the paddle"""
        if self._item is None:
            half_width = self.settings.width/2
            half_height = self.settings.height/2
            x, y = self.settings.x, self.settings.y
            self._item = self.canvas.create_rectangle(
                x - half_width, y - half_height,
                x + half_width, y + half_height,
                fill=self.settings.fill
            )
        return self._item
    

    def move(self, offset):
        """moves the paddle
        if has a ball, also moves the ball

        if already flush left or flush right, does nothing

        Parameters
        ----------

        offset: int
        amount to move the paddle and ball horizontally
        """
        coordinates = self.position
        width = self.canvas.winfo_width()
        if (coordinates.top_left_x + offset >= 0 and
            coordinates.bottom_right_x + offset <= width):  # noqa: E129
            super(PaddleWidget, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)


class BrickSettings(BaseSettings):
    """settings for the brick widget"""
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.colors = None
        self.tags = None
        self._attributes = None
        self._hits = None
        return

    @property
    def attributes(self):
        """list of required values"""
        if self._attributes is None:
            self._attributes = ("width",
                                "height",
                                "colors",
                                "tags",
                                "x",
                                "y",
                                "hits")
        return self._attributes
    

    @property
    def hits(self):
        """the number of hits each brick will take
        """
        if self._hits is None:
            self._hits = max(self.colors)
        return self._hits

    def maximum_hits(self, hits):
        """number of hits brick will take
        Parameters
        ----------

        hits: int
        number of hits before deleting bricks
        """
        self._hits = hits
        self.check_type(hits, "hits", int)
        self.check_positive(hits, "hits")
        return self
    

    def x_position(self, x):
        """horizontal position
        Parameters
        ----------
        x: int or float
        pixels from the left
        """
        self.x = x
        self.check_numeric(x, "x")
        self.check_positive(x, "x")
        return self

    def y_position(self, y):
        """vertical position
        Parameters
        ----------

        y: int or float
        pixels from the top
        """
        self.y = y
        self.check_numeric(y, "y")
        self.check_positive(y, "y")
        return self
    

    def pixel_width(self, width):
        """width of the brick
        Parameters
        ----------

        width: int
        pixel-width of the brick
        """
        self.width = width
        self.check_type(width, "width", int)
        self.check_positive(width, "width")
        return self

    def pixel_height(self, height):
        """height of the brick
        Parameters
        ----------

        height: int
        pixel-height of the brick
        """
        self.height = height
        self.check_type(height, "height", int)
        self.check_positive(height, "height")
        return self
    

    def level_colors(self, colors):
        """map of level to colors

        Parameters
        ----------
        colors: dict
        map of integers to colors
        """
        self.colors = colors
        for level in range(1, len(colors) + 1):
            if level not in colors:
                raise TypeError("colors keys must be range starting at 1")
        for level, color in colors.items():
            self.check_hex_color(color, "level {0} color".format(level))
        return self
    
    def label(self, tags):
        """string to tag bricks

        Parameters
        ----------

        tags: str
        identifier for bricks
        """
        self.tags = tags
        self.check_type(tags, "tags", str)
        return self
    

class BrickWidget(BaseWidget):
    """represents a single brick

    Parameters
    ----------

    canvas: tkinter.Canvas
      what to draw the brick on
    settings: BrickSettings
      initial settings for the brick
    """
    def __init__(self, canvas, settings):
        self.canvas = canvas
        self.settings = settings
        self.hits = self.settings.hits
        self._item = None
        return

    @property
    def item(self):
        """canvas rectangle"""
        if self._item is None:
            half_height = self.settings.height/2
            half_width = self.settings.width/2
            x, y = self.settings.x, self.settings.y
            self._item = self.canvas.create_rectangle(
                x - half_width, y - half_height,
                x + half_width, y + half_height,
                fill=self.settings.colors[self.hits],
                tags=self.settings.tags
            )
        return self._item
    
    def hit(self):
        """the brick has been hit event
        Decrements the counter and changes the color or deletes the brick
        """
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,
                                fill=self.settings.colors[self.hits])
        return
    

class FrameSettings(BaseSettings):
    """holds the settings for the game"""
    def __init__(self):
        self.width = None
        self.height = None
        self.color = None
        self.title = None
        self._attributes = None
        return

    @property
    def attributes(self):
        """list of required attributes"""
        if self._attributes is None:
            self._attributes = ("width",
                                "height",
                                "color",
                                "title")
        return self._attributes

    def window_width(self, width):
        """width of window
       Parameters
       ----------
       width: int
         pixel-width for the tkinter window

       Returns
       -------

       GameSettings: this object
       """
        self.width = width
        self.check_type(width, "width", int)
        self.check_positive(width, "width")
        return self

    def window_height(self, height):
        """height of window
       Parameters
       ----------

       height: int
         pixel height of the window

       Returns
       -------

       GameSettings: this object
       """
        self.height = height
        self.check_type(height, "height", int)
        self.check_positive(height, "height")
        return self

    def canvas_color(self, color):
        """background color

       Parameters
       ----------

       color: string
          hex-color for canvas background

       Returns
       -------

       GameSettings: this object
       """
        self.color = color
        self.check_hex_color(color, 'background color')
        return self

    def window_title(self, title):
        """title of the window
       Parameters
       ----------

       title: str
         name to give the title

       Returns
       -------

       GameSettings: this object
       """
        self.title = title
        self.check_type(title, "window title", str)
        return self
    

class BreakoutFrame(tkinter.Frame):
    """creates the breakout game

    Parameters
    ----------

    settings: GameSettings
      object with the settings
    parent: Tk
      parent window for this frame
    """
    def __init__(self, settings, parent):
        super(BreakoutFrame, self).__init__(parent)
        self.parent = parent
        self.parent.title(settings.title)
        self.settings = settings
        self._canvas = None
        self.height = settings.height
        return

    @property
    def canvas(self):
        """canvas to render images"""
        if self._canvas is None:
            self._canvas = tkinter.Canvas(self,
                                          width=self.settings.width,
                                          height=self.settings.height,
                                          bg=self.settings.color)
        return self._canvas

    def __call__(self):
        """runs the main-loop"""
        self.canvas.pack()
        self.pack()
        self.parent.mainloop()
        return
    

class GameSettings(BaseSettings):
    """settings for the game"""
    def __init__(self):
        self.lives = None
        self.text_x = None
        self.text_y = None
        self.text_size = None
        self.padding = None
        self._attributes = None
        return

    @property
    def attributes(self):
        """required attributes"""
        if self._attributes is None:
            self._attributes = ("lives",
                                "text_x",
                                "text_y",
                                "padding")
        return self._attributes

    def font_size(self, size):
        """text size in pixels
       Parameters
       ----------

       size: int
         size for fonts
       """
        self.text_size = size
        self.check_type(size, "text size", int)
        self.check_positive(size, "text size")
        return self

    def allowed_failures(self, lives):
        """number of times player can fail

       Parameters
       ----------

       lives: int
         number of failures per game
       """
        self.lives = lives
        self.check_type(lives, "lives", int)
        self.check_positive(lives, "lives")
        return self

    def text_horizontal_position(self, text_x):
        """pixel indent for text

       Parameters
       ----------

       text_x: int
         number of pixels from the left
       """
        self.text_x = text_x
        self.check_type(text_x, "text indent", int)
        self.check_positive(text_x, "text indent")
        return self

    def text_vertical_position(self, text_y):
        """pixel vertical position for text
       Parameters
       ----------

       text_y: int
          pixels from the top
       """
        self.text_y = text_y
        self.check_type(text_y, "text y", int)
        self.check_positive(text_y, "text y")
        return self

    def outer_padding(self, padding):
        """outer margins

       Parameters
       ----------

       padding: int
         pixels to put around the edge of the canvas
       """
        self.padding = padding
        self.check_type(padding, "padding", int)
        self.check_positive(padding, "padding")
        return self
    

class Game(object):
    """builds and holds the game

    Parameters
    ----------

    game_settings: GameSettings
      settings for the game overall

    frame_settings: FrameSettings
      settings to set-up the tkinter window

    paddle_settings: PaddleSettings
       settings to set-up the paddle_settings

    brick_settings: BrickSettings
       settings to set-up the bricks

    ball_settings: BallSettings
      settings to set-up the ball
    """
    def __init__(self, game_settings, frame_settings, paddle_settings,
                 brick_settings, ball_settings):
        self.game_settings = game_settings
        self.frame_settings = frame_settings
        self.paddle_settings = paddle_settings
        self.brick_settings = brick_settings
        self.ball_settings = ball_settings
        self.collidable = {}
        self.hud = None
        self._frame = None
        self._canvas = None
        self._paddle = None
        self._bricks = None
        self._ball = None
        return

    @property
    def frame(self):
        """the tkinter frame"""
        if self._frame is None:
            self._frame = BreakoutFrame(self.frame_settings, tkinter.Tk())
        return self._frame

    @property
    def canvas(self):
        """tkinter canvas to draw on"""
        if self._canvas is None:
            self._canvas = self.frame.canvas
        return self._canvas

    @property
    def paddle(self):
        """the paddle widget"""
        if self._paddle is None:
            (self.paddle_settings.x_position(self.frame_settings.width/2)
             .y_position(self.frame_settings.height -
                         self.game_settings.padding -
                         self.paddle_settings.height))
            self._paddle = PaddleWidget(self.canvas, self.paddle_settings)
        return self._paddle

    @property
    def ball(self):
        """the ball widget"""
        if self._ball is None:
            paddle = self.paddle.position
            (self.ball_settings
            .x_position((paddle.top_left_x + paddle.bottom_right_x)/2)
            .y_position(paddle.top_left_y - 2 * self.ball_settings.radius)
            .direction_vector(BallDirections(RIGHT, UP)))
            self._ball = BallWidget(self.canvas, self.ball_settings)
        return self._ball
    
    def add_brick(self, x, y, settings):
        """add a brick to items

        Parameters
        ----------

        x: int
        pixels from the left
        y: int
        pixels from the top
        """
        settings = (copy(settings)
                    .x_position(x)
                    .y_position(y))
        brick = BrickWidget(self.canvas, settings)
        self.collidable[brick.item] = brick
        return

    def add_bricks(self):
        """adds the bricks"""
        half_width = self.brick_settings.width/2
        first_row = 50
        second_row = first_row + self.brick_settings.height
        third_row = second_row + self.brick_settings.height
        first_settings = copy(self.brick_settings).maximum_hits(3)
        second_settings = copy(self.brick_settings).maximum_hits(2)
        third_settings = copy(self.brick_settings).maximum_hits(1)
        for x in range(5, self.frame_settings.width - 5, 75):
            this_x = x + half_width
            self.add_brick(this_x, first_row, first_settings)
            self.add_brick(this_x, second_row, second_settings)
            self.add_brick(this_x, third_row, third_settings)
        return
    

    def setup_canvas(self):
        """sets up some canvas settings"""
        self.canvas.focus_set()
        self.canvas.bind(
            "<Left>",
            lambda _: self.paddle.move(-self.paddle_settings.speed)
        )
        self.canvas.bind(
            "<Right>",
            lambda _: self.paddle.move(self.paddle_settings.speed)
        )
        self.canvas.bind("<space>", lambda _: self.start())
        return
    
    def draw_text(self, x, y, text):
        """draws the text

        Parameters
        ----------

        x: int
        left indent
        y: int
        right indent
        text: string
        what to output

        Returns
        -------
        text-object
        """
        font = ("Helvetica", self.game_settings.text_size)
        return self.canvas.create_text(x,
                                    y,
                                    text=text, font=font)

    def update_lives_text(self):
        """updates the text when a player fails"""
        text = "Lives: {0}".format(self.lives)
        if self.hud is None:
            self.hud = self.draw_text(self.game_settings.text_x,
                                    self.game_settings.text_y,
                                    text)
        else:
            self.canvas.itemconfig(self.hud, text=text)
        return

    def reset(self):
        """sets up the game after it's ended"""
        self.lives = self.game_settings.lives
        self.add_bricks()
        self.setup_canvas()
        self.ball.delete()
        self._ball = None
        self.paddle.ball = self.ball
        self.update_lives_text()
        return

    def set_up(self):
        """populates the collidable items dict"""
        self.lives = self.game_settings.lives
        self.collidable[self.paddle.item] = self.paddle
        self.add_bricks()
        self.setup_canvas()
        self.ball.delete()
        self._ball = None
        self.paddle.ball = self.ball
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to Start")
        return

    def set_up_in_between(self):
        """sets things up when the player still has lives"""
        self.ball.delete()
        self._ball = None
        self.paddle.ball = self.ball
        self.update_lives_text()
        self.setup_canvas()
        self.text = self.draw_text(300, 200, "Press Space to Start")
        return

    def start(self):
        """starts the game"""
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()
        return
    
    def game_loop(self):
        """runs the game"""
        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag("brick"))
        if num_bricks == 0:
            self.ball.speed = None
            self.text = self.draw_text(300, 200, "You Win. Whatever. (Hit the spacebar to restart)")
            self.reset()
        elif self.ball.position.bottom_right_y >= self.frame.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.text = self.draw_text(300, 200, "Loser (Hit the spacebar to restart)")
                self.reset()
            else:
                self.frame.after(1000, self.set_up_in_between)
        else:
            self.ball.update()
            self.frame.after(50, self.game_loop)
        return
    
    def check_collisions(self):
        """checks if the ball has collided with anything"""
        ball = self.ball.position
        items = self.canvas.find_overlapping(*ball)
        collisions = [self.collidable[item] for item in items
                    if item in self.collidable]
        self.ball.collide(collisions)
        return
    
    def __call__(self):
        """sets up the game"""
        self.set_up()
        self.frame()
        return
    


if __name__ == '__main__':
    frame_settings = (FrameSettings()
                      .window_width(600)
                      .window_height(400)
                      .canvas_color(WHITE)
                      .window_title("Breakout! Not Pong!")())
    ball_settings = (BallSettings()
                     .x_position(10)
                     .y_position(10)
                     .circle_radius(10)
                     .direction_vector(BallDirections(horizontal=NO_MOVEMENT,
                                                      vertical=UP))
                     .velocity(10)
                     .color(LAVENDER)())
    paddle_settings = (PaddleSettings()
                       .pixel_width(80)
                       .pixel_height(5)
                       .x_position(40)
                       .y_position(80)
                       .velocity(10)
                       .color(BLUE)
                       ())

    brick_settings = (BrickSettings()
                      .x_position(75)
                      .y_position(20)
                      .label("brick")
                      .pixel_width(75)
                      .pixel_height(20)
                      .level_colors({1: "#999999",
                                     2: "#555555",
                                     3: "#222222"})())

    game_settings = (GameSettings()
                     .allowed_failures(3)
                     .text_horizontal_position(50)
                     .text_vertical_position(20)
                     .font_size(15)
                     .outer_padding(20)()
                     )
    game = Game(game_settings, frame_settings, paddle_settings, brick_settings,
                ball_settings)
    game()