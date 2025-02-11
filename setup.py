from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox

import sys

class SetUP(QWidget):

  def __init__(self):
    
    super(SetUP, self).__init__()
    uic.loadUi("SetUP_widget.ui", self)

    self.setGeometry(750, 300, 650, 410)  # sets window position (750, 300) and its size w=600, h= 450
    self.setFixedSize(650, 410)  # fixes the window proportions so size cant be changed

    self.monthselect = self.findChild(QComboBox, 'Month_picker')
    self.YearSelect = self.findChild(QComboBox,'Year_Picker')
    self.AntiSocial = self.findChild(QCheckBox, 'AntiSoc_Check')
    self.BikeTheft = self.findChild(QCheckBox, 'BikeTheft_Check')
    self.Drugs = self.findChild(QCheckBox, 'Drugs_Check')
    self.ShopLift = self.findChild(QCheckBox, 'Shopflift_Check')
    self.Robbery = self.findChild(QCheckBox, 'Robbery_Check')
    self.PublicOrder = self.findChild(QCheckBox, 'PubOrder_Check') 
    self.CrimDmgArson = self.findChild(QCheckBox, 'CrimDmgArs_Check')
    self.VehicleCrim = self.findChild(QCheckBox, 'Vehicle Check')
    self.Vio_SexualOffs = self.findChild(QCheckBox, 'Vio_SexOff_Check')
    self.PersonTheft = self.findChild(QCheckBox, 'PersonTheft_Check')
    self.Weapons = self.findChild(QCheckBox, 'WeaponPossess_Check')
    self.Burglary = self.findChild(QCheckBox, 'Burglary_Check')
    self.SelectAll = self.findChild(QCheckBox, 'SelectAL_Check')
    self.Save_btn = self.findChild(QPushButton, 'Save_Button')
    self.Safe = False # setting changes as unsaved, here as its connected to Save_btn
    self.Cont_btn = self.findChild(QPushButton, 'Continue_Button')
    self.Canc_btn = self.findChild(QPushButton, 'Cancel_Button')

    self.crimelist = []
    self.crimeSelected = 0
    self.month = {
      0:'January',
      1:'February',
      2:'March',
      3:'April',
      4:'May',
      5:'June',
      6:'July',
      7:'August',
      8:'September',
      9:'October',
      10:'November',
      11:'December'
    }
    self.year = {
      0:2024,
      1:2023,
      2:2022,
      3:2021,
      4:2020
    }

    #setting event handlers
    self.monthselect.currentIndexChanged.connect(self.monthchange)
    self.YearSelect.currentIndexChanged.connect(self.YearChange)
    self.SelectAll.clicked.connect(self.Select_All)
    self.Robbery.stateChanged.connect(self.Robber_Select)
    self.CrimDmgArson.stateChanged.connect(self.CrimDmgArson_Select)
    self.Weapons.stateChanged.connect(self.Weapons_Select)
    self.Vio_SexualOffs.stateChanged.connect(self.VioSexOffs_Select)
    self.Burglary.stateChanged.connect(self.Burglary_Select)
    self.PublicOrder.stateChanged.connect(self.PublicOrder_Select)
    self.VehicleCrim.stateChanged.connect(self.VehicleCrim_Select)
    self.Drugs.stateChanged.connect(self.Drug_Select)
    self.PersonTheft.stateChanged.connect(self.PersonTheft_Select)
    self.ShopLift.stateChanged.connect(self.ShopLift_Select)
    self.BikeTheft.stateChanged.connect(self.Bike_Select)
    self.AntiSocial.stateChanged.connect(self.AntiSo_Select)
    self.Save_btn.clicked.connect(self.Saved)
    self.Cont_btn.clicked.connect(self.Cont)
    self.Canc_btn.clicked.connect(self.Cancel)
    


    self.show()
  #enddef


  def monthchange(self):
    self.m_index = self.monthselect.currentIndex()
    self.month_Chosen = self.month[self.m_index]
    print(self.month_Chosen)
  #enddef

  def YearChange(self):
    self.y_index = self.YearSelect.currentIndex()
    self.year_Chosen = self.year[self.y_index]
  #enddef

  def NumCrimes_Selected(self, crime):
    

    if crime == True:

      self.crimeSelected += 1
      print(self.crimeSelected)

      if self.crimeSelected == 9:
        self.SelectAll.setChecked(True)

      #endif

    else:
      self.crimeSelected -= 1
      self.SelectAll.setChecked(False)
      print(self.crimeSelected)

    #endif
  #enddef

  def Select_All(self):

    state = self.SelectAll.checkState()

    if state == 2:
      self.Robbery.setChecked(True)
      self.Arson.setChecked(True)
      self.Crim_Dmg.setChecked(True)
      self.Violence.setChecked(True)
      self.Burglary.setChecked(True)
      self.FraudForge.setChecked(True)
      self.SexualOffs.setChecked(True)
      self.Drugs.setChecked(True)
      self.TheftHandle.setChecked(True)

    else:
      self.Robbery.setChecked(False)
      self.Arson.setChecked(False)
      self.Crim_Dmg.setChecked(False)
      self.Violence.setChecked(False)
      self.Burglary.setChecked(False)
      self.FraudForge.setChecked(False)
      self.SexualOffs.setChecked(False)
      self.Drugs.setChecked(False)
      self.TheftHandle.setChecked(False)

    #endif
  #enddef

  def Robber_Select(self):

    state = self.Robbery.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Robbery')
      print(self.crimelist)
      self.NumCrimes_Selected(True)
    
    else:

      #self.SelectAll.setChecked(False)
      self.crimelist.remove('Robbery')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #endef

  def CrimDmgArson_Select(self):

    state = self.CrimDmgArson.checkState()
    self.Safe = False

    if state == 2 :
      
      self.crimelist.append('Criminal Damage and Arson')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Criminal Damage and Arson')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def Weapons_Select(self):

    state = self.Weapons.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Possession of Weapons')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      print(self.crimelist)
      self.crimelist.remove('Possession of Weapons')
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def VioSexOffs_Select(self):

    state = self.Vio_SexualOffs.checkState()
    self.Safe = False

    if state == 2:
      
      self.crimelist.append('Violence and Sexual Offences')
      print(self.crimelist)
      self.NumCrimes_Selected(True)
    
    else:

      print(self.crimelist)
      self.NumCrimes_Selected(False)
      self.crimelist.remove('Violence')

    #endif
  #enddef

  def Burglary_Select(self):

    state = self.Burglary.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Burglary')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      print(self.crimelist)
      self.NumCrimes_Selected(False)
      self.crimelist.remove('Burglary')

    #endif
  #enddef

  def FandF_Select(self):
    self.Safe =False
    state = self.FraudForge.checkState()

    if state == 2:

      self.crimelist.append('Fraud and Forgary')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Fraud and Forgary')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def SexualOffs_Select(self):
    self.Safe =False
    state = self.SexualOffs.checkState()

    if state == 2:

      self.crimelist.append('Sexual Offences')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Sexual Offences')
      self.NumCrimes_Selected(False)
      print(self.crimelist)

    #endif
  #enddef

  def Drug_Select(self):
    self.Safe =False
    state = self.Drugs.checkState()

    if state == 2:

      self.crimelist.append('Drugs')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Drugs')
      print(self.crimelist)

    #endif
  #enddef

  def TheftHandle_Select(self):
    self.Safe =False
    state = self.TheftHandle.checkState()

    if state == 2:

      self.crimelist.append('Theft and Handling')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Theft and Handling')
      print(self.crimelist)

    #endif
  #enddef

  def Saved(self):
    #add if statements for Month and Year for if they arent changed assume normal

    self.Safe = True  #  sets safe as True, essentially 'Saving' changes
    print('Saved:')
    print(self.crimelist)
    print(self.month_Chosen)
    print(self.year_Chosen)
  #endef

  def Cont(self):

      #  Checking Cont Method can access same variables as Save Mathod

    if self.Safe == True:
      self.close()

    else:

      msgbox = QMessageBox.warning(
        self,
        'HOLD ON',
        'Changes Are Not Saved! \nAre you sure you want to continue',
        QMessageBox.Yes | QMessageBox.No)

      if msgbox == QMessageBox.Yes:
        self.close()
      #endif
    #endif
  #enddef

  def Cancel(self):

    self.close()  #  closes the window
  #enddef




#1.  add function that adds a checked item to a list
#2.  add function that removes unchecked items from the list
#3.  add function that adds the month to a list
#4.  add function that adds the year to a list
#5. (3 and 4 probably dont need to be lists just variables)
#6.  add function that collects the chosen crimes and date when the Save Buttion is clicked 
  

app = QApplication(sys.argv)

window = SetUP()
window.show()
app.exec_()