# winclass.py -- Class test which generates a window with variable properities
# 2017-11-2 HP

import cv2
import numpy as np
import palform

class Window:
  def __init__(self, name, src, draws = [], esc = "q"):
    """
    Creates a window which stores one image or camera source
    """
    
    # Initiates member variables
    
    self.name = name  # Window's name, string
    self.src = src
    
    """
    self.draws = draws
    # {"type": type, ... "color": (r, g, b)}
    # Format will vary depending on drawing type
    """
    
    self.tracks = []
    # {"name": name, "min": min, "max": max}
    
    # Dictionary of trackbar positions
    
    self.trackpos = {}
    # {trackbar1name: trackbar1pos, trackbar2name: trackbar2pos ... trackbarXname: trackbarXpos}
    
    # Sets escape key for window
    
    self.esc = esc
    
    # Sets the mode of the window:
    # 0 = image
    # 1 = camera
    
    self.cam = None
    
    self.setsrc(src)
    
    # Sets null custom function
    
    self.custom = self.null
    
    # Draws drawings on the source
    
    # self.draw()
    
    
  def null(self, null):
    pass
  
  def makewin(self):
    """
    Makes a window with the name of the object
    """
    cv2.namedWindow(self.name)
    
  def upframe(self):
    """
    Updates the frame for a camera input
    """
    
    self.ret, self.frame = self.cam.read()
  
  """
  def draw(self):
    \"""
    Draws a specified drawing on the source
    Works with:
    Lines
    Circles
    Text
    Contours
    \"""
    
    draws = palform.tuplist(self.draws)
    
    for draw in draws:
      # Exception Tracker
      
      excepts = 0
      
      if draw ['type'] == 'line':
        try:
          if not excepts:
            cv2.line(self.frame, (draw ['x1'], draw ['y1']), (draw ['x2'], draw ['y2']), draw ['color'], draw ['thick'], draw ['type'])
          elif excepts == 1:
            cv2.line(self.frame, (draw ['x1'], draw ['y1']), (draw ['x2'], draw ['y2']), draw ['color'], draw ['thick'])
          elif excepts == 2:
            cv2.line(self.frame, (draw ['x1'], draw ['y1']), (draw ['x2'], draw ['y2']), draw ['color'])
          else:
            continue
        except KeyError:
          excepts += 1
      elif draw ['type'] == 'circle':
        try:
          if not excepts:
            cv2.circle(self.frame, (draw ['x'], draw ['y']), draw ['rad'], draw ['color'], draw ['thick'], draw ['type'])
          elif excepts == 1:
            cv2.circle(self.frame, (draw ['x'], draw ['y']), draw ['rad'], draw ['color'], draw ['thick'])
          elif excepts == 2:
            cv2.circle(self.frame, (draw ['x'], draw ['y']), draw ['rad'], draw ['color'])
          else:
            continue
        except KeyError:
          excepts += 1
      elif draw ['type'] == 'text':
        try:
          if not excepts:
            cv2.putText(self.frame, draw ['text'], (draw ['x'], draw ['y']), draw ['font'], draw ['scale'], draw ['color'], draw ['thick'], draw ['type'])
          elif excepts == 1:
            cv2.putText(self.frame, draw ['text'], (draw ['x'], draw ['y']), draw ['font'], draw ['scale'], draw ['color'], draw ['thick'])
          elif excepts == 2:
            cv2.putText(self.frame, draw ['text'], (draw ['x'], draw ['y']), draw ['font'], draw ['scale'], draw ['color'])
          else:
            continue
        except KeyError:
          excepts += 1
      elif draw ['type'] == 'cons':
        try:
          if not excepts:
            cv2.drawContours(self.frame, draw ['cons'], -1, draw ['color'], draw ['thick'], draw ['type'])
          elif excepts == 1:
            cv2.drawContours(self.frame, draw ['cons'], -1, draw ['color'], draw ['thick'])
          elif excepts == 2:
            cv2.drawContours(self.frame, draw ['cons'], -1, draw ['color'])
          else:
            continue
        except KeyError:
          excepts += 1
      # elif draw ['type'] == 'line':
    """
    
  def newtracks(self, *tracks):
    """
    Creates a trackbar on the window with the specified settings
    """
    
    tracks = palform.tuplist(tracks)
    
    for trackbar in tracks:
      cv2.createTrackbar(trackbar [0], self.name, trackbar [1], trackbar [2], trackbar [3])
      self.tracks.append(trackbar [0])
    
  def uptracks(self):
    """
    Updates all trackbar positions
    """
    
    for trackbar in self.tracks:
      self.trackpos [trackbar] = cv2.getTrackbarPos(trackbar, self.name)
      
  def display(self):
    """
    Displays the frame image depending on the mode
    """
    
    if self.mode == 0:
      self.imdisplay()
    elif self.mode == 1:
      self.camdisplay()
    
    
  def imdisplay(self):
    """
    Displays the frame if the window is in image mode
    """
    
    while True:
      self.custom(self)
      cv2.imshow(self.name, self.frame)
      if cv2.waitKey(1) & 0xFF == ord(self.esc):
        break
    cv2.destroyAllWindows()
    
  def camdisplay(self):
    """
    Displays the frame if the window is in camera mode
    """
    
    while True:
      self.upframe()
      self.custom(self)
      cv2.imshow(self.name, self.frame)
      if cv2.waitKey(1) & 0xFF == ord(self.esc):
        break
    cv2.destroyAllWindows()
    
  def pure(self):
    """
    Makes a deep copy of the frame called 'pure'
    """
    
    self.pure = self.frame.copy()
    
  def makecustom(self, func):
    """
    Sets the custom logic while the source video is being displayed
    """
    
    self.custom = func
  
  def setsrc(self, src):
    """
    Sets the source of the image in the window
    """
    
    try:
      self.cam.release()
    except AttributeError:
      pass
    
    print(src)
    
    if type(src) == str:
      self.mode = 0
      self.frame = cv2.imread(src)
    elif type(src) == int:
      self.mode = 1
      self.cam = cv2.VideoCapture(src)
      self.frame = self.upframe()

    
# Test
def priself(self):
  pass
  
"""
win = Window("win", 0)
win.makewin()
win.makecustom(priself)
win.display()
"""
