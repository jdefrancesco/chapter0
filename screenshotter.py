#!/usr/bin/env python

import win32api
import win32ui
import win32con
import win32gui


# Grab a handle to main desktop window
hdesktop = win32gui.GetDesktopWindow()

# Determing dimension of screen
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

# Create device context to copy our bitmap to
desktop_dc  = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# Create a virtual (memory based) device context
mem_dc =  img_dc.CreateCompatibleDC()

# Create bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

# copy the screen into out memory device context
mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

screenshot.SaveBitmapFile(mem_dc, "c:\\WINDOWS\\Temp\\screenshot.bmp")

# Free objects
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())