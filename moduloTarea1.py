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

    labelSeleccionTornillo = qt.QLabel("Seleccione tornillo a mover: ") #Se crea label para seleccion de tornillo a manipular
    sample1FormLayout.addWidget(labelSeleccionTornillo) #Se añade label
 
    self.comboBoxSeleccionTornillo = qt.QComboBox() #Se crea comboBox para seleccionar tornillo
    self.comboBoxSeleccionTornillo.addItem("Tornillo 1") #Se añade opciones
    self.comboBoxSeleccionTornillo.addItem("Tornillo 2")
    sample1FormLayout.addWidget(self.comboBoxSeleccionTornillo) #Se añade al layout
    groupBoxTraslation = qt.QGroupBox() #Se crea un group box dentro del boton colapsable
    groupBoxTraslation.setTitle( 'Traslacion' ) #Se anade nombre al groupBox
    sample1FormLayout.addWidget(groupBoxTraslation) #Se añade el groupbox al layout del boton
    
    groupBoxTraslationLayout = qt.QFormLayout( groupBoxTraslation ) #Se crea formLayout al groupLayout
  
    groupBoxTraslationLayoutContenedor1 = qt.QFrame(sample1CollapsibleButton)
    groupBoxTraslationLayoutContenedor1.setLayout(qt.QHBoxLayout())
    groupBoxTraslationLayout.layout().addWidget(groupBoxTraslationLayoutContenedor1)

    labelEjex = qt.QLabel("Traslacion eje RL: ") #Se crea label
    groupBoxTraslationLayoutContenedor1.layout().addWidget(labelEjex) #Se añade label al layout

    self.barraTranslacionX = qt.QSlider(1) #Se crea un slicer 
    self.barraTranslacionX.setMinimum(-200) #Minimo del slider -200
    self.barraTranslacionX.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayoutContenedor1.layout().addWidget(self.barraTranslacionX) #Se añade slicer al layout
    self.barraTranslacionX.valueChanged.connect(self.onMoveTraslacionX) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxTraslacionX= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxTraslacionX.setMinimum(-200)
    self.spinBoxTraslacionX.setMaximum(200)

    groupBoxTraslationLayoutContenedor1.layout().addWidget(self.spinBoxTraslacionX)
    self.spinBoxTraslacionX.valueChanged.connect(self.onMoveTraslacionXspinBox)
#-----------------------------------------------------------------------------------------
   
    groupBoxTraslationLayoutContenedor2 = qt.QFrame(sample1CollapsibleButton)
    groupBoxTraslationLayoutContenedor2.setLayout(qt.QHBoxLayout())
    groupBoxTraslationLayout.layout().addWidget(groupBoxTraslationLayoutContenedor2)

    labelEjey = qt.QLabel("Traslacion eje PA: ") #Se crea label
    groupBoxTraslationLayoutContenedor2.layout().addWidget(labelEjey) #Se añade label al layout

    self.barraTranslacionY = qt.QSlider(1) #Se crea un slicer 
    self.barraTranslacionY.setMinimum(-200) #Minimo del slider -200
    self.barraTranslacionY.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayoutContenedor2.layout().addWidget(self.barraTranslacionY) #Se añade slicer al layout
    self.barraTranslacionY.valueChanged.connect(self.onMoveTraslacionY) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxTraslacionY= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxTraslacionY.setMinimum(-200)
    self.spinBoxTraslacionY.setMaximum(200)
    groupBoxTraslationLayoutContenedor2.layout().addWidget(self.spinBoxTraslacionY)
    self.spinBoxTraslacionY.valueChanged.connect(self.onMoveTraslacionYspinBox)


#---------------------------------------------------------------------------------------------------
    groupBoxTraslationLayoutContenedor3 = qt.QFrame(sample1CollapsibleButton)
    groupBoxTraslationLayoutContenedor3.setLayout(qt.QHBoxLayout())
    groupBoxTraslationLayout.layout().addWidget(groupBoxTraslationLayoutContenedor3)

    labelEjeZ = qt.QLabel("Traslacion eje SI: ") #Se crea label
    groupBoxTraslationLayoutContenedor3.layout().addWidget(labelEjeZ) #Se añade label al layout

    self.barraTranslacionZ = qt.QSlider(1) #Se crea un slicer 
    self.barraTranslacionZ.setMinimum(-200) #Minimo del slider -200
    self.barraTranslacionZ.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayoutContenedor3.layout().addWidget(self.barraTranslacionZ) #Se añade slicer al layout
    self.barraTranslacionZ.valueChanged.connect(self.onMoveTraslacionZ) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxTraslacionZ= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxTraslacionZ.setMinimum(-200)
    self.spinBoxTraslacionZ.setMaximum(200)
    groupBoxTraslationLayoutContenedor3.layout().addWidget(self.spinBoxTraslacionZ)
    self.spinBoxTraslacionZ.valueChanged.connect(self.onMoveTraslacionZspinBox)


#---------------------------------------------------------------------------------------------------
  def onApply(self): 

      print "Cargaste tornillo 1"

      path='C:\Users\Camilo_Q\Documents\MEGA\Trabajo_de_grado\moduloTarea1/Tornillo_1.STL' #Se obtiene direccion de la unbicación del tornillo
      slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d


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
    
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID())# Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4()  #Se crea matriz 4x4 para el tornillo
    
    valorTrasladoSlidex=self.barraTranslacionX.value  #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionX.setValue(valorTrasladoSlidex) #Se añade al SpinBox el valor modificado del slide

    transformada.GetMatrixTransformToParent(matriztornillo1)  #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

  def onMoveTraslacionY(self):
    
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID()) # Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4() #Se crea matriz 4x4 para el tornillo
    
    valorTrasladoSlidey=self.barraTranslacionY.value #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionY.setValue(valorTrasladoSlidey) #Se añade al SpinBox el valor modificado del slide

    transformada.GetMatrixTransformToParent(matriztornillo1) #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(1,3,valorTrasladoSlidey)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

  def onMoveTraslacionZ(self):
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID()) # Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4() #Se crea matriz 4x4 para el tornillo
    
    valorTrasladoSlidez=self.barraTranslacionZ.value   #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionZ.setValue(valorTrasladoSlidez) #Se añade al SpinBox el valor modificado del slide


    transformada.GetMatrixTransformToParent(matriztornillo1)  #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1)  # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

  def onMoveTraslacionXspinBox(self):
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID())# Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4()

    valorTrasladoSlidex=self.spinBoxTraslacionX.value
    self.barraTranslacionX.setValue(valorTrasladoSlidex)

    transformada.GetMatrixTransformToParent(matriztornillo1)  #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1)

  def onMoveTraslacionYspinBox(self):
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID())# Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4()

    valorTrasladoSlidey=self.spinBoxTraslacionY.value
    self.barraTranslacionY.setValue(valorTrasladoSlidey)

    transformada.GetMatrixTransformToParent(matriztornillo1)  #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(1,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1)

  def onMoveTraslacionZspinBox(self):
    tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
    transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
    transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
    slicer.mrmlScene.AddNode(transformada) #
    tornillo1.SetAndObserveTransformNodeID(transformada.GetID())# Se relaciona la trnasformada con el objeto tornillo
    matriztornillo1 = vtk.vtkMatrix4x4()

    valorTrasladoSlidez=self.spinBoxTraslacionZ.value
    self.barraTranslacionZ.setValue(valorTrasladoSlidez)

    transformada.GetMatrixTransformToParent(matriztornillo1)  #Se toma la matriz padre de movimiento
    matriztornillo1.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
    transformada.SetAndObserveMatrixTransformToParent(matriztornillo1)
