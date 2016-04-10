# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer

class moduloTarea1():
  def __init__(self, parent):
    parent.title = "Tarea 1"
    parent.categories = ["Tareas"]
    parent.dependencies = []
    parent.contributors = ["Camilo Quiceno Q y Nicolas Buitrago Roldan"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Aprender a mover el tornillo en el espacio
    """
    parent.acknowledgementText = """
    Desarrollado por Camilo Quiceno Y Nicolas Buitrago
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
    path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL' #Se obtiene direccion de la unbicación del tornillo
    slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d
    tornillo1=slicer.util.getNode('Tornillo_1')
    transformada=slicer.vtkMRMLLinearTransformNode()
    transformada.SetName('Transformada')
    slicer.mrmlScene.AddNode(transformada)
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID())