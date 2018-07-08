#!/usr/bin/env python2

import re               # Regex Lib

TARGET                  = /home/mix-man/temp/Dest1/Facility Requests'

class FacilityRequest(object):
  def __init__(self):
    self.file = object


  def getDate(self):
    match   = re.search(r'\d{4}-d{2}-\d{2}', self)
    return match

  def GetDatesFromFile(self):
    match   = re.search(r'\d{4}-d{2}-\d{2}', self)
    return match

  def GetTimesFromFile(self):
    match   = re.search(r'\d{4}-\d{4}', self)
    return match


log.debug('Facility Request.py - Loaded!')