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


    #Path para camilo= path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL'
    #Path para Nicolas = ...

#---------------------------------------------------------------------------------------------------

    sampleCollapsibleButton = ctk.ctkCollapsibleButton() #Se crea boton colapsable
    sampleCollapsibleButton.text = "Creacion de tornillos" #Se asigna label del boton colapsable
    sampleCollapsibleButton.collapsed = True #Aparecen sin colapsar
    self.layout.addWidget(sampleCollapsibleButton) #Se crea layout dentro del boton colapsable

#-------------------------------------------------------------------------------------------------

    sample1CollapsibleButton = ctk.ctkCollapsibleButton()  #Se crea boton colapsable
    sample1CollapsibleButton.text = "Movimiento de tornillo" #Se asigna label del boton colapsable
    sample1CollapsibleButton.collapsed = True #Aparecen sin colapsar
    self.layout.addWidget(sample1CollapsibleButton) #Se crea layout dentro del boton colapsable

#------------------------------------------------------------------------------------------------
    #Click boton "Cargar tornillo"
    sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)

    layout1Button = qt.QPushButton("Cargar tornillo 1") #Se crea boton pulsable, con texto "Apply"
    layout1Button.toolTip = "Al presionar aparecerá un tornillo en la scena" #Información que aparece si dejas el mouse encima
    sampleFormLayout.addWidget(layout1Button) #Se añade el boton al layout del boton colapsable
    layout1Button.connect('clicked(bool)',self.onApply)

    layout2Button = qt.QPushButton("Cargar tornillo 2") #Se crea boton pulsable, con texto "Apply"
    layout2Button.toolTip = "Al presionar aparecerá un tornillo en la scena" #Información que aparece si dejas el mouse encima
    sampleFormLayout.addWidget(layout2Button) #Se añade el boton al layout del boton colapsable
    layout2Button.connect('clicked(bool)',self.onApply2)

#-----------------------------------------------------------------------------------------------

    sample1FormLayout = qt.QFormLayout(sample1CollapsibleButton) #Se anada QformLayout al boton colapsable

    groupBoxTraslation = qt.QGroupBox() #Se crea un group box dentro del boton colapsable
    groupBoxTraslation.setTitle( 'Traslacion' ) #Se anade nombre al groupBox
    sample1FormLayout.addWidget(groupBoxTraslation) #Se añade el groupbox al layout del boton
    
    groupBoxTraslationLayout = qt.QFormLayout( groupBoxTraslation ) #Se crea formLayout al groupLayout
    labelEjex = qt.QLabel("Traslacion eje x: ") #Se crea label
    groupBoxTraslationLayout.layout().addWidget(labelEjex) #Se añade label al layout
    self.barraTranslacionX = qt.QSlider(1) #Se crea un slicer 
    self.barraTranslacionX.setMinimum(-200) #Minimo del slider -200
    self.barraTranslacionX.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayout.layout().addWidget(self.barraTranslacionX) #Se añade slicer al layout
    self.barraTranslacionX.valueChanged.connect(self.onMoveTraslacionX) #Se crea metodo para saber cuando se mueve el slider


#---------------------------------------------------------------------------------------------------
  def onApply(self): 

      print "Cargaste tornillo 1"

      path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL' #Se obtiene direccion de la unbicación del tornillo
      slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d
      tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
      transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
      transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
      slicer.mrmlScene.AddNode(transformada) #
      tornillo1.SetAndObserveTransformNodeID(transformada.GetID()) # Se relaciona la trnasformada con el objeto tornillo

  def onApply2(self): 

      print "Cargaste tornillo 2"

      path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL' #Se obtiene direccion de la unbicación del tornillo
      slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d
      tornillo2=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
      transformada2=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
      transformada2.SetName('Transformada Tornillo 2') #Se asigna nombre a la transformada
      slicer.mrmlScene.AddNode(transformada2) #
      tornillo2.SetAndObserveTransformNodeID(transformada2.GetID()) # Se relaciona la trnasformada con el objeto tornillo
      
      matriztornillo2 = vtk.vtkMatrix4x4() #Se crea matriz 4x4 para el tornillo 2
      transformada2.GetMatrixTransformToParent(matriztornillo2) # a la matriz de tornillo 2 se toma como padre la matriz de movimiento
      matriztornillo2.SetElement(0,3,5) #Se modifica la matriz del tornillo
      transformada2.SetAndObserveMatrixTransformToParent(matriztornillo2) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

  def onMoveTraslacionX(self):
    print "Trasladando en x"

  