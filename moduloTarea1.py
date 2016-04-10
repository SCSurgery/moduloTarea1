# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer

class moduloTarea1():
  def __init__(self, parent):
    parent.title = "Tarea 1"
    parent.categories = ["Tareas"]
    parent.dependencies = []
    parent.contributors = ["Camilo Quiceno Q"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Este modulo sirve para cambiar el layout del slicer
    """
    parent.acknowledgementText = """
    Desarrollado por Camilo Quiceno 
    """ # replace with organization, grant and thanks.
    self.parent = parent

class moduloTarea1Widget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL'
    slicer.util.loadModel(path)
    print "Tornillo cargado"
