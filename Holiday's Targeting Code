# tartest.py -- Test of a targeting system which locates a piece of reflective tape
# 2017-11-4 HP

import cv2
import numpy as np
from winclass import Window

# Target Specs:
# Height to width:
htw1 = [1.9, 2.1] 
htw2 = [.30, .60]


def tar1(cons):
  goodcons = []
  for con in cons:
    cen, wh, ang = cv2.minAreaRect(con)
    try:
      h_w = wh [1]/wh [0]
      # Note: W/H = Extent
      if h_w > htw1 [0] and h_w < htw1 [1]:
        area = cv2.contourArea(con)
        if area > 480 and area < 700:
          goodcons.append(con)
          hull = cv2.convexHull(con)
            
          sol = area/cv2.contourArea(hull)
          if sol > .94:
            arc = cv2.arcLength(con, True)
            
            if arc > 90 and arc < 105:
              
              print("Angle :", ang)
              print('Width :', wh [0], "Height :", wh [1])
              print('Area :', area)
              print('Arc Length:', cv2.arcLength(con, True))
              print('Solidity:', sol)
              
              goodcons.append(con)
              
    except ZeroDivisionError:
      pass
  return goodcons
  
def tar2(cons):
  goodcons = []
  for con in cons:
    cen, wh, ang = cv2.minAreaRect(con)
    try:
      h_w = wh [1]/wh [0]
      if h_w > htw2 [0] and h_w < htw2 [1]:
        area = cv2.contourArea(con)
        if area > 480 and area < 700:
          if ang > -30 and ang < 30:
            goodcons.append(con)
            
            hull = cv2.convexHull(con)
            
            sol = area/cv2.contourArea(hull)
            
            if sol > .94:
              
              arc = cv2.arcLength(con, True)
              
              if arc > 95 and arc < 115:
                print("Angle :", ang)
                print('Width :', wh [0], "Height :", wh [1])
                print('Area :', area)
                print('Arc Length:', arc)
                print('Solidity:', sol)
                
                goodcons.append(con)
                
    except ZeroDivisionError:
      pass
  return goodcons
  
def tar3(cons):
  goodcons = []
  for con in cons:
    cen, wh, ang = cv2.minAreaRect(con)
    try:
      h_w = wh [1]/wh [0]
      if h_w > .95 and h_w < 1.28:
        if wh [1] > 10 and wh [0] > 10:
          area = cv2.contourArea(con)
          if area > 190 and area < 700:
            hull = cv2.convexHull(con)
            
            sol = area/cv2.contourArea(hull)
            
            if sol > .85:
            
              arc = cv2.arcLength(con, True)
              if arc > 65 and arc < 75:
                
                ret, tri = cv2.minEnclosingTriangle(con)
                
              
                print("Angle :", ang)
                print('Width :', wh [0], "Height :", wh [1])
                print('Area :', area)
                print('Arc Length:', cv2.arcLength(con, True))
                print('Solidity:', sol)
                
                goodcons.append(con)
                
                
                print(tri)
                
    except ZeroDivisionError:
      pass
  return goodcons
  
"""
def tar4(cons):
 goodcons = []
  for con in cons:
    cen, wh, ang = cv2.minAreaRect(con)
    try:
      h_w = wh [1]/wh [0]
      if h_w > .95 and h_w < 1.5:
        if wh [1] > 10 and wh [0] > 10:
          area = cv2.contourArea(con)
          if area > 180 and area < 250:
            hull = cv2.convexHull(con)
            
            sol = area/cv2.contourArea(hull)
            
            if sol > .85:
            
              arc = cv2.arcLength(con, True)
              if arc > 65 and arc < 75:
                
                ret, tri = cv2.minEnclosingTriangle(con)
              
              
                print("Angle :", ang)
                print('Width :', wh [0], "Height :", wh [1])
                print('Area :', area)
                print('Arc Length:', cv2.arcLength(con, True))
                print('Solidity:', sol)
                
                goodcons.append(con)
                
                
                print(tri)
                
    except ZeroDivisionError:
      pass
  return goodcons
"""
def none(null):
  pass

def custom(self):
  try:
    self.d = self.d
  except:
    self.d = 100
    self.set = 0
  self.passed = False
  self.now = 0
  self.last = 0
  
  """
  # ------
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HLS)
  self.uptracks()
  self.e = self.trackpos ['v']
  
  # ------
  """
  
  self.uptracks()
  
  impure = self.frame.copy()
  
  lum = self.frame [:, :, 1]
  flum = np.float32(lum)
  flum *= self.d/ 100
  lum = np.int32(flum)
  lum [lum < 0] = 0
  
  self.frame [:, :, 1] = lum.copy()
  
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_HLS2RGB)
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
  
  # self.frame = cv2.inRange(self.frame, (0), (255))
  # Thresholds the frame
  # This needs to change depending on enviornment
  
  res, self.frame = cv2.threshold(self.frame, 150, 255, cv2.THRESH_BINARY)
  
  
  # -------- Comment this out if it doesn't work 
  # while not self.passed:
  passing = self.frame [: :].sum()/307200
  
  
  if passing > 100:
    
    self.frame = impure.copy()
    
    self.d -= 3
    
    lum = self.frame [:, :, 1]
    flum = np.float32(lum)
    flum *= self.d/100
    lum = np.int32(flum)
    lum [lum <= 0] = 0
    
    self.frame [:, :, 1] = lum.copy()
    
    self.frame = cv2.cvtColor(self.frame, cv2.COLOR_HLS2RGB)
    self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)

    res, self.frame = cv2.threshold(self.frame, 240, 255, cv2.THRESH_BINARY)
  else:
    if self.set <= 10 or passing < 20:
      self.d += 1
    
    if abs(self.now - self.last) < 1:
      self.set += 1
    else:
      self.set = 0
    
        
    print(self.d, passing)
  
  # --------
  
  
  _, cons, _ = cv2.findContours(self.frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  
  """
  while not passed:
    
    if len(cons) > 10:
      self.d += 1
      
      self.frame = impure.copy()
      # self.frame = cv2.inRange(self.frame, (d), (255))
      res, self.frame = cv2.threshold(self.frame, self.d, 360, cv2.THRESH_BINARY)
      _, cons, _ = cv2.findContours(self.frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    else:
      passed = True
  """
  
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_GRAY2BGR)
  cons = sense (cons, self.trackpos ['tar'] + 1).copy()
  
  for con in cons:
    cv2.drawContours(self.frame, cons, -1, (255, 0, 0), 3)
    M = cv2.moments(con)
    cx = int(M ['m10']/M ['m00'])
    cy = int(M ['m01']/M ['m00'])
    cen = str(cx) + ', ' + str(cy)
    print(cen)
    cv2.line(self.frame, (cx - 40, cy), (cx + 40, cy), (0, 0, 255), 5)
    cv2.line(self.frame, (cx, cy - 40), (cx, cy + 40), (0, 0, 255), 5)

def test(self):
  # self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HLS)
  
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2HLS)
  self.uptracks()
  self.d = self.trackpos ['v']
  
  lum = self.frame [:, :, 1]
  
  flum = np.float32(lum)
  flum *= self.d/ 100
  lum = np.int32(flum)
  
  print(lum.sum()/307200)
  
  # lum [lum <= 0] = 0
  
  self.frame [:, :, 1] = lum
  
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_HLS2RGB)
  self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
  
def tar():
  
  win = Window("Window", 0)
  win.makewin()
  win.newtracks(['v', 1, 100, none], ['tar', 1, 2, none])
  win.makecustom(custom)
  win.display()
  
  nwin = Window("Winny", 0)
  nwin.makecustom(test)
  nwin.makewin()
  nwin.newtracks(['v', 1, 100, none])
  nwin.display()
  nwin.cam.release()
  
  
def sense(cons, tar):
  goodcons = []
  areas = {}
  ret = []
  ind = 0
  
  # Target type:
  # 1 = Upright Rect
  # 2 = Side Rect
  # 3 = Top Left Triangle
  # 4 = Bottom Right Triangle
  
  # Works from about 2 yards away
  
  if tar == 1:
    goodcons = tar1(cons)
  elif tar == 2:
    goodcons = tar2(cons)
  elif tar == 3:
    goodcons = tar3(cons)
  elif tar == 4:
    goodcons = tar4(cons)
    
  """
  for con in goodcons:
    area [ind] = cv2.contourArea(con)
    ind += 1
  
  areas = sorted(areas, reverse = True)
  """
  
  return goodcons
