# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer
import math

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

    #Path para camilo= C:\Users\Camilo_Q\Documents\GitHub\moduloTarea1/Tornillo_1.STL
    #Path para Nicolas = ...

    path1='C:\Users\Camilo_Q\Documents\GitHub\moduloTarea1/stlcolumna.stl' #Se obtiene direccion de la unbicación del tornillo
    slicer.util.loadModel(path1)
    layoutManager = slicer.app.layoutManager() 
    threeDWidget = layoutManager.threeDWidget(0)
    threeDView = threeDWidget.threeDView()
    threeDView.resetFocalPoint()

    layoutManager.setLayout(9)
  
    sample2CollapsibleButton = ctk.ctkCollapsibleButton() #Se crea boton colapsable
    sample2CollapsibleButton.text = "Planear trayectoria" #Se asigna label del boton colapsable
    sample2CollapsibleButton.collapsed = False #Aparecen sin colapsar
    self.layout.addWidget(sample2CollapsibleButton) #Se crea layout dentro del boton colapsable

#---------------------------------------------------------------------------------------------------

    sampleCollapsibleButton = ctk.ctkCollapsibleButton() #Se crea boton colapsable
    sampleCollapsibleButton.text = "Creacion de tornillos" #Se asigna label del boton colapsable
    sampleCollapsibleButton.collapsed = False #Aparecen sin colapsar
    self.layout.addWidget(sampleCollapsibleButton) #Se crea layout dentro del boton colapsable

#-------------------------------------------------------------------------------------------------

    sample1CollapsibleButton = ctk.ctkCollapsibleButton()  #Se crea boton colapsable
    sample1CollapsibleButton.text = "Movimiento de tornillo" #Se asigna label del boton colapsable
    sample1CollapsibleButton.collapsed = False #Aparecen sin colapsar
    self.layout.addWidget(sample1CollapsibleButton) #Se crea layout dentro del boton colapsable

    #---------------------------------------------------------------------------------------------------

   
    #Click boton "Cargar tornillo"
    sample2FormLayout = qt.QFormLayout(sample2CollapsibleButton)

    layout2Button = qt.QPushButton("Inicio trayectoria") #Se crea boton pulsable, con texto "Apply"
    layout2Button.toolTip = "Al presionar aparecerá un tornillo en la scena" #Información que aparece si dejas el mouse encima
    sample2FormLayout.addWidget(layout2Button) #Se añade el boton al layout del boton colapsable
    layout2Button.connect('clicked(bool)',self.onApply3)

    layout2Button = qt.QPushButton("Fin trayectoria") #Se crea boton pulsable, con texto "Apply"
    layout2Button.toolTip = "Al presionar aparecerá un tornillo en la scena" #Información que aparece si dejas el mouse encima
    sample2FormLayout.addWidget(layout2Button) #Se añade el boton al layout del boton colapsable
    layout2Button.connect('clicked(bool)',self.onApply4)

#--------------------------------------------------------------------------------------------------
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
    self.comboBoxSeleccionTornillo.currentIndexChanged.connect(self.onMoveComboBox)
   
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
    self.spinBoxTraslacionX.setSuffix(".00mm")
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
    self.spinBoxTraslacionY.setSuffix(".00mm")
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
    self.barraTranslacionZ.setMinimum(-2000) #Minimo del slider -200
    self.barraTranslacionZ.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayoutContenedor3.layout().addWidget(self.barraTranslacionZ) #Se añade slicer al layout
    self.barraTranslacionZ.valueChanged.connect(self.onMoveTraslacionZ) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxTraslacionZ= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxTraslacionZ.setSuffix(".00mm")
    self.spinBoxTraslacionZ.setMinimum(-2000)
    self.spinBoxTraslacionZ.setMaximum(200)
    groupBoxTraslationLayoutContenedor3.layout().addWidget(self.spinBoxTraslacionZ)
    self.spinBoxTraslacionZ.valueChanged.connect(self.onMoveTraslacionZspinBox)
#---------------------------------------------------------------------------------------------------
    groupBoxTraslationLayoutContenedor4 = qt.QFrame(sample1CollapsibleButton)
    groupBoxTraslationLayoutContenedor4.setLayout(qt.QHBoxLayout())
    groupBoxTraslationLayout.layout().addWidget(groupBoxTraslationLayoutContenedor4)

    labelEjeEje = qt.QLabel("Traslacion eje tornillo: ") #Se crea label
    groupBoxTraslationLayoutContenedor4.layout().addWidget(labelEjeEje) #Se añade label al layout

    self.barraTranslacionEje = qt.QSlider(1) #Se crea un slicer 
    self.barraTranslacionEje.setMinimum(-200) #Minimo del slider -200
    self.barraTranslacionEje.setMaximum(200) #Maximo de slider 200
    groupBoxTraslationLayoutContenedor4.layout().addWidget(self.barraTranslacionEje) #Se añade slicer al layout
    self.barraTranslacionEje.valueChanged.connect(self.onMoveTraslacionEje) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxTraslacionEje= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxTraslacionEje.setSuffix(".00mm")
    self.spinBoxTraslacionEje.setMinimum(-200)
    self.spinBoxTraslacionEje.setMaximum(200)
    groupBoxTraslationLayoutContenedor4.layout().addWidget(self.spinBoxTraslacionEje)
    self.spinBoxTraslacionEje.valueChanged.connect(self.onMoveTraslacionEjespinBox)
#---------------------------------------------------------------------------------------------------
    groupBoxRotation = qt.QGroupBox() #Se crea un group box dentro del boton colapsable
    groupBoxRotation.setTitle( 'Rotacion' ) #Se anade nombre al groupBox
    sample1FormLayout.addWidget(groupBoxRotation)

    groupBoxRotationLayout = qt.QFormLayout( groupBoxRotation ) #Se crea formLayout al groupLayout
  
    groupBoxRotationLayoutContenedor1 = qt.QFrame(sample1CollapsibleButton)
    groupBoxRotationLayoutContenedor1.setLayout(qt.QHBoxLayout())
    groupBoxRotationLayout.layout().addWidget(groupBoxRotationLayoutContenedor1)

    labelRotationEjex = qt.QLabel("Rotacion Eje x ") #Se crea label
    groupBoxRotationLayoutContenedor1.layout().addWidget(labelRotationEjex) #Se añade label al layout

    self.barraRotacionX = qt.QSlider(1) #Se crea un slicer 
    self.barraRotacionX.setMinimum(0) #Minimo del slider -200
    self.barraRotacionX.setMaximum(360) #Maximo de slider 200
    groupBoxRotationLayoutContenedor1.layout().addWidget(self.barraRotacionX) #Se añade slicer al layout
    self.barraRotacionX.valueChanged.connect(self.onMoveRotacionX) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxRotacionX= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxRotacionX.setSuffix(" Grados")
    self.spinBoxRotacionX.setMinimum(0)
    self.spinBoxRotacionX.setMaximum(360)

    groupBoxRotationLayoutContenedor1.layout().addWidget(self.spinBoxRotacionX)
    self.spinBoxRotacionX.valueChanged.connect(self.onMoveRotacionXspinBox)
#---------------------------------------------------------------------------------------------------
    groupBoxRotationLayoutContenedor2 = qt.QFrame(sample1CollapsibleButton)
    groupBoxRotationLayoutContenedor2.setLayout(qt.QHBoxLayout())
    groupBoxRotationLayout.layout().addWidget(groupBoxRotationLayoutContenedor2)

    labelRotationEjey = qt.QLabel("Rotacion Eje y ") #Se crea label
    groupBoxRotationLayoutContenedor2.layout().addWidget(labelRotationEjey) #Se añade label al layout

    self.barraRotacionY = qt.QSlider(1) #Se crea un slicer 
    self.barraRotacionY.setMinimum(0) #Minimo del slider -200
    self.barraRotacionY.setMaximum(360) #Maximo de slider 200
    groupBoxRotationLayoutContenedor2.layout().addWidget(self.barraRotacionY) #Se añade slicer al layout
    self.barraRotacionY.valueChanged.connect(self.onMoveRotacionY) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxRotacionY= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxRotacionY.setSuffix(" Grados")
    self.spinBoxRotacionY.setMinimum(0)
    self.spinBoxRotacionY.setMaximum(360)

    groupBoxRotationLayoutContenedor2.layout().addWidget(self.spinBoxRotacionY)
    self.spinBoxRotacionY.valueChanged.connect(self.onMoveRotacionYspinBox)
#--------------------------------------------------------------------------------
    groupBoxRotationLayoutContenedor3 = qt.QFrame(sample1CollapsibleButton)
    groupBoxRotationLayoutContenedor3.setLayout(qt.QHBoxLayout())
    groupBoxRotationLayout.layout().addWidget(groupBoxRotationLayoutContenedor3)

    labelRotationEjez = qt.QLabel("Rotacion Eje z ") #Se crea label
    groupBoxRotationLayoutContenedor3.layout().addWidget(labelRotationEjez) #Se añade label al layout

    self.barraRotacionZ = qt.QSlider(1) #Se crea un slicer 
    self.barraRotacionZ.setMinimum(0) #Minimo del slider -200
    self.barraRotacionZ.setMaximum(360) #Maximo de slider 200
    groupBoxRotationLayoutContenedor3.layout().addWidget(self.barraRotacionZ) #Se añade slicer al layout
    self.barraRotacionZ.valueChanged.connect(self.onMoveRotacionZ) #Se crea metodo para saber cuando se mueve el slider

    self.spinBoxRotacionZ= qt.QSpinBox() #Se crea Qspinbox
    self.spinBoxRotacionZ.setSuffix(" Grados")
    self.spinBoxRotacionZ.setMinimum(0)
    self.spinBoxRotacionZ.setMaximum(360)

    groupBoxRotationLayoutContenedor3.layout().addWidget(self.spinBoxRotacionZ)
    self.spinBoxRotacionZ.valueChanged.connect(self.onMoveRotacionZspinBox)
#--------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
  def onApply(self): 

      print "Cargaste tornillo 1"

      path='C:\Users\Camilo_Q\Documents\GitHub\moduloTarea1\Tornillo_1.STL' #Se obtiene direccion de la unbicación del tornillo
      slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d
      self.tornillo1=slicer.util.getNode('Tornillo_1') #Se obtiene la informacion del tonillo cargado
      self.transformada=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
      self.transformada.SetName('Transformada Tornillo 1') #Se asigna nombre a la transformada
      slicer.mrmlScene.AddNode(self.transformada) #
      self.tornillo1.SetAndObserveTransformNodeID(self.transformada.GetID())# Se relaciona la trnasformada con el objeto tornillo
      self.matriztornillo1 = vtk.vtkMatrix4x4()  #Se crea matriz 4x4 para el tornillo

  def onApply2(self): 

      print "Cargaste tornillo 2"

      path='C:\Users\Camilo_Q\Documents\GitHub\moduloTarea1/Tornillo_2.STL' #Se obtiene direccion de la unbicación del tornillo
      slicer.util.loadModel(path) #Se carga el tornillo al espacio 3d
      
      self.tornillo2=slicer.util.getNode('Tornillo_2') #Se obtiene la informacion del tonillo cargado
      self.transformada2=slicer.vtkMRMLLinearTransformNode() #Se crea una transformada lineal
      self.transformada2.SetName('Transformada Tornillo 2') #Se asigna nombre a la transformada
      slicer.mrmlScene.AddNode(self.transformada2) #
      self.tornillo2.SetAndObserveTransformNodeID(self.transformada2.GetID()) # Se relaciona la trnasformada con el objeto tornillo
      
      self.matriztornillo2 = vtk.vtkMatrix4x4() #Se crea matriz 4x4 para el tornillo 2
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2) # a la matriz de tornillo 2 se toma como padre la matriz de movimiento
      self.matriztornillo2.SetElement(0,3,50) #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

  def onApply3(self):
    print "Inicio trayectoria"
    placeModePersistence = 0
    a=slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)

  def onApply4(self):
     
    placeModePersistence = 0
    b=slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)
    print "Fin de trayectoria" 

  def onMoveTraslacionX(self):

    valorTrasladoSlidex=self.barraTranslacionX.value  #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionX.setValue(valorTrasladoSlidex)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2) 
      
  def onMoveTraslacionY(self):

    valorTrasladoSlidey=self.barraTranslacionY.value #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionY.setValue(valorTrasladoSlidey) #Se añade al SpinBox el valor modificado del slide
    
    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1) #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(1,3,valorTrasladoSlidey)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(1,3,valorTrasladoSlidey)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveTraslacionZ(self):

    valorTrasladoSlidez=self.barraTranslacionZ.value   #Se obtiene el valor del slide modificado
    self.spinBoxTraslacionZ.setValue(valorTrasladoSlidez) #Se añade al SpinBox el valor modificado del slide
    
    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1)  # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)
    
  def onMoveTraslacionXspinBox(self):

    valorTrasladoSlidex=self.spinBoxTraslacionX.value
    self.barraTranslacionX.setValue(valorTrasladoSlidex)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:
      
      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1)

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(0,3,valorTrasladoSlidex)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveTraslacionYspinBox(self):

    valorTrasladoSlidey=self.spinBoxTraslacionY.value
    self.barraTranslacionY.setValue(valorTrasladoSlidey)
    
    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(1,3,valorTrasladoSlidey)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1)

    else:
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(1,3,valorTrasladoSlidey)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveTraslacionZspinBox(self):

    valorTrasladoSlidez=self.spinBoxTraslacionZ.value
    self.barraTranslacionZ.setValue(valorTrasladoSlidez)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:
    
      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      self.matriztornillo1.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1)

    else:
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      self.matriztornillo2.SetElement(2,3,valorTrasladoSlidez)  #Se modifica la matriz del tornillo
      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  

  def onMoveRotacionX(self):

    self.valorRotacionSlidex=self.barraRotacionX.value  #Se obtiene el valor del slide modificado
    self.valorRotacionSlidey=self.barraRotacionY.value
    self.valorRotacionSlidez=self.barraRotacionZ.value

    self.spinBoxRotacionX.setValue(self.valorRotacionSlidex)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.gradoX1=self.valorRotacionSlidex

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:

      self.gradoX2=self.valorRotacionSlidex
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2) 

  def onMoveRotacionXspinBox(self):

    self.valorRotacionSlidex=self.spinBoxRotacionX.value
    self.barraRotacionX.setValue(self.valorRotacionSlidex)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2) 

  def onMoveRotacionY(self):
    self.valorRotacionSlidex=self.barraRotacionX.value  #Se obtiene el valor del slide modificado
    self.valorRotacionSlidey=self.barraRotacionY.value
    self.valorRotacionSlidez=self.barraRotacionZ.value
    self.spinBoxRotacionY.setValue(self.valorRotacionSlidey)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.gradoY1=self.valorRotacionSlidey

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:

      self.gradoY2=self.valorRotacionSlidey
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveRotacionYspinBox(self):
    self.valorRotacionSlidey=self.spinBoxRotacionY.value
    self.barraRotacionY.setValue(self.valorRotacionSlidey)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveRotacionZ(self):

    self.valorRotacionSlidex=self.barraRotacionX.value  #Se obtiene el valor del slide modificado
    self.valorRotacionSlidey=self.barraRotacionY.value
    self.valorRotacionSlidez=self.barraRotacionZ.value
    self.spinBoxRotacionZ.setValue(self.valorRotacionSlidez)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.gradoZ1=self.valorRotacionSlidez

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))
      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1)

    else:

      self.gradoZ2=self.valorRotacionSlidez
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveRotacionZspinBox(self):

    self.valorRotacionSlidez=self.spinBoxRotacionZ.value
    self.barraRotacionZ.setValue(self.valorRotacionSlidez)

    if self.comboBoxSeleccionTornillo.currentIndex == 0:

      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo1.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo1.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo1.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo1.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo1.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada.SetAndObserveMatrixTransformToParent(self.matriztornillo1) # Se añade la matriz del tornillo modificada a la matriz padre de movimientos

    else:
      
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
     
      self.matriztornillo2.SetElement(0,0,math.cos(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(0,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))+(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(0,2,(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))-(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(1,0,-math.cos(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(1,1,(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidez*0.017453292519943))-(math.sin(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )
      self.matriztornillo2.SetElement(1,2,(math.cos(self.valorRotacionSlidez*0.017453292519943)*math.sin(self.valorRotacionSlidex*0.017453292519943))+(math.cos(self.valorRotacionSlidex*0.017453292519943)*math.sin(self.valorRotacionSlidey*0.017453292519943)*math.sin(self.valorRotacionSlidez*0.017453292519943)) )

      self.matriztornillo2.SetElement(2,0,math.sin(self.valorRotacionSlidey*0.017453292519943))  #Se modifica la matriz del tornillo
      self.matriztornillo2.SetElement(2,1,-math.sin(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943)) 
      self.matriztornillo2.SetElement(2,2,math.cos(self.valorRotacionSlidex*0.017453292519943)*math.cos(self.valorRotacionSlidey*0.017453292519943))

      self.transformada2.SetAndObserveMatrixTransformToParent(self.matriztornillo2)

  def onMoveComboBox(self):
    if self.comboBoxSeleccionTornillo.currentIndex == 1:
      print "Actualiza matriz del tornillo 2"
      self.transformada2.GetMatrixTransformToParent(self.matriztornillo2)  #Se toma la matriz padre de movimiento
      x=self.matriztornillo2.GetElement(0,3) #Se toman los valores actuales de la matriz
      y=self.matriztornillo2.GetElement(1,3)
      z=self.matriztornillo2.GetElement(2,3)


      self.barraTranslacionX.setValue(x) # Se actualizan los slides y spins al valor de la matriz
      self.spinBoxTraslacionX.setValue(x)
      self.barraTranslacionY.setValue(y)
      self.spinBoxTraslacionY.setValue(y)
      self.barraTranslacionZ.setValue(z)
      self.spinBoxTraslacionZ.setValue(z)

      try:
        self.barraRotacionX.setValue(self.gradoX2)
        self.barraRotacionY.setValue(self.gradoY2)
        self.barraRotacionZ.setValue(self.gradoZ2)
      except (AttributeError):
        self.barraRotacionX.setValue(0)
        self.barraRotacionY.setValue(0)
        self.barraRotacionZ.setValue(0)

    else:
      self.transformada.GetMatrixTransformToParent(self.matriztornillo1)  #Se toma la matriz padre de movimiento
      x=self.matriztornillo1.GetElement(0,3)  #Se toman los valores actuales de la matriz
      y=self.matriztornillo1.GetElement(1,3)
      z=self.matriztornillo1.GetElement(2,3)

      self.barraTranslacionX.setValue(x) # Se actualizan los slides y spins al valor de la matriz
      self.spinBoxTraslacionX.setValue(x)
      self.barraTranslacionY.setValue(y)
      self.spinBoxTraslacionY.setValue(y)
      self.barraTranslacionZ.setValue(z)
      self.spinBoxTraslacionZ.setValue(z)

      try:
        self.barraRotacionX.setValue(self.gradoX1)
        self.barraRotacionY.setValue(self.gradoY1)
        self.barraRotacionZ.setValue(self.gradoZ1No)

      except (AttributeError):
        self.barraRotacionX.setValue(0)
        self.barraRotacionY.setValue(0)
        self.barraRotacionZ.setValue(0)



  def onMoveTraslacionEjespinBox(self):
    print "Traslacion eje tornillo spinBox"

  def onMoveTraslacionEje(self):
      print "Traslacion eje tornillo slide"