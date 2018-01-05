import sys
sys.path.append('../')
from EEGClass import EEGData
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout,QVBoxLayout,QHBoxLayout,QDialog,QCheckBox,QFileDialog,QFrame,QLabel,QWidget,QPushButton,QSplitter,QMainWindow, QTextEdit,QAction, qApp, QApplication
from PyQt5.QtGui import QIcon,QDrag
from PyQt5.QtCore import Qt,QMimeData


BUTTON_CHOOSED = 'NONE'
eeg_global = EEGData()

#functions

class DragButton(QPushButton):

    def __init__(self, title, parent):
        self.title = title
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return
        BUTTON_CHOOSED = self.title
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        #print(e.pos(),"====",self.rect().topLeft().y())

        dropAction1 = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('leftpress',self.title)
        if e.button() == Qt.RightButton:
            BUTTON_CHOOSED = self.title
            print('rightpress',BUTTON_CHOOSED)

class preprocessWidget(QDialog):
    def __init__(self,parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.ICAState = 1
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        ICA = QCheckBox('ICA',self)
        ICA.toggle()
        ICA.stateChanged.connect(self.ICAStateChange)

        self.AlphaState = 1
        Alpha = QCheckBox('Alpha',self)
        Alpha.toggle()
        Alpha.stateChanged.connect(self.AlphaStateChange)

        self.BetaState = 1
        Beta = QCheckBox('Beta',self)
        Beta.toggle()
        Beta.stateChanged.connect(self.BetaStateChange)

        self.GammaState = 1
        Gamma = QCheckBox('Gamma',self)
        Gamma.toggle()
        Gamma.stateChanged.connect(self.GammaStateChange)

        runb = QPushButton('RUN',self)
        runb.clicked.connect(self.run)
        hbox.addWidget(ICA)
        hbox.addWidget(Alpha)
        hbox.addWidget(Beta)
        hbox.addWidget(Gamma)
        vbox.addLayout(hbox)
        vbox.addWidget(runb)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PreprocessCheckBox')
        self.show()
        # Alpha = QCheckbox('Alpha',self)
        # Beta = QCheckbox('Beta',self)
    def ICAStateChange(self):
        self.ICAState = ~self.ICAState
    def AlphaStateChange(self):
        self.AlphaState = ~self.AlphaState
    def BetaStateChange(self):
        self.BetaState = ~self.BetaState
    def GammaStateChange(self):
        self.GammaState = ~self.GammaState

    def run(self):
        print(self.ICAState)
        if self.ICAState == 1:
            eeg_global.preprocess(ICA=True)
        if self.AlphaState == 1:
            eeg_global.preprocess(Alpha=True)
        if self.BetaState == 1:
            eeg_global.preprocess(Beta=True)
        if self.GammaState == 1:
            eeg_global.preprocess(Gamma=True)
        self.done(1)

class visualboardWidget(QDialog):
    def __init__(self,parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.visualRawState = 1
        visualRaw = QCheckBox('visualRaw',self)
        visualRaw.toggle()
        visualRaw.stateChanged.connect(self.visualRawStateChange)

        self.visualSensorState = 1
        visualSensor = QCheckBox('visualSensor',self)
        visualSensor.toggle()
        visualSensor.stateChanged.connect(self.visualSensorStateChange)

        self.visualICAState = 1
        visualICA = QCheckBox('visualICA',self)
        visualICA.toggle()
        visualICA.stateChanged.connect(self.visualICAStateChange)

        self.visualAlphaState = 1
        visualAlpha = QCheckBox('visualAlpha',self)
        visualAlpha.toggle()
        visualAlpha.stateChanged.connect(self.visualAlphaStateChange)

        self.visualBetaState = 1
        visualBeta = QCheckBox('visualBeta',self)
        visualBeta.toggle()
        visualBeta.stateChanged.connect(self.visualBetaStateChange)

        self.visualGammaState = 1
        visualGamma = QCheckBox('visualGamma',self)
        visualGamma.toggle()
        visualGamma.stateChanged.connect(self.visualGammaStateChange)

        PLOTB = QPushButton('PLOT',self)
        PLOTB.clicked.connect(self.PLOT)

        grid.addWidget(visualRaw,1,1)
        grid.addWidget(visualSensor,1,2)
        grid.addWidget(visualAlpha,2,1)
        grid.addWidget(visualBeta,2,2)
        grid.addWidget(visualGamma,2,3)
        grid.addWidget(visualICA,2,4)
        grid.addWidget(PLOTB,3,4)

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('VisualBoard')
        self.show()

    def visualRawStateChange(self):
        self.visualRawState = ~self.visualRawState
    def visualSensorStateChange(self):
        self.visualSensorState = ~self.visualSensorState
    def visualICAStateChange(self):
        self.visualICAState = ~self.visualICAState
    def visualAlphaStateChange(self):
        self.visualAlphaState = ~self.visualAlphaState
    def visualBetaStateChange(self):
        self.visualBetaState = ~self.visualBetaState
    def visualGammaStateChange(self):
        self.visualGammaState = ~self.visualGammaState

    def PLOT(self):
        print('PLOT wait to fill')

        if self.visualRawState == 1:
            eeg_global.visualBoard(Raw=True)
        if self.visualSensorState == 1:
            eeg_global.visualBoard(Sensor=True)
        if self.visualICAState == 1:
            eeg_global.visualBoard(ICA=True)
        if self.visualAlphaState == 1:
            eeg_global.visualBoard(Alpha=True)
        if self.visualBetaState == 1:
            eeg_global.visualBoard(Beta=True)
        if self.visualGammaState == 1:
            eeg_global.visualBoard(Gamma=True)



class GraphicInterface(QFrame):

    def __init__(self):
        QWidget.__init__(self)

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.button_io = DragButton("Import", self)
        self.button_io.clicked.connect(self.io_showDialog)
        self.button_loc = DragButton("LoadSensorLoc",self)
        self.button_loc.clicked.connect(self.loc_showDialog)
        self.button_preprocess = DragButton("Preprocess",self)
        self.button_preprocess.clicked.connect(self.preprocess)
        self.button_featureextract = DragButton("FeatureExtract",self)
        self.button_visualboard = DragButton("VisualBoard",self)
        self.button_visualboard.clicked.connect(self.VisualBoard_showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(self.button_loc)
        vbox.addWidget(self.button_io)
        vbox.addWidget(self.button_preprocess)
        vbox.addWidget(self.button_featureextract)
        vbox.addWidget(self.button_visualboard)

        self.setLayout(vbox)

        #self.button_io.connect()

        self.setWindowTitle('Graphic Interface')

    def io_showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'open data','/home')
        f = fname[0]

        vhdrpath = f
        temppath = f.split('.')[0]
        print(temppath)
        eegpath = temppath + '.eeg'
        vmrkpath = temppath + '.vmrk'
        eeg_global.readBP(eegpath,vhdrpath,vmrkpath)
        print('import eegdata successfully')
        # self.setGeometry(300, 300, 280, 150)
    def loc_showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'load sensor location','/home/EEGDataProcess/src')
        f = fname[0]
        locpath = f
        print(locpath)
        eeg_global.readLoc(locpath)

    def VisualBoard_showDialog(self):
        v = visualboardWidget(self)
        v.show()
        print('visualBoard start')

    def preprocess(self):
        p = preprocessWidget(self)
        p.show()
        print('preprocessing')
    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):

        print(BUTTON_CHOOSED)
        position = e.pos()
        if BUTTON_CHOOSED == 'NONE':
            return
        if BUTTON_CHOOSED == 'Import':
            self.button_io.move(position)
        if BUTTON_CHOOSED == 'Preprocess':
            self.button_preprocess.move(position)
        if BUTTON_CHOOSED == 'FeatureExtract':
            self.button_featureextract.move(position)
        if BUTTON_CHOOSED == 'VisualBoard':
            self.button_visualboard.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

class MainWidget(QWidget):
    DATA_INFORMATION = "DataName:\nConfiguration:\nsample rates:\n\n\n\n\n\n\n"
    command_information = "None"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        splitter_left_right = QSplitter(Qt.Horizontal)
        self.label_data_information = QLabel(self.DATA_INFORMATION)
        self.label_command_information = QLabel(self.command_information)
        self.label_data_information.setFrameStyle(QFrame.Box|QFrame.Plain)
        self.label_command_information.setFrameStyle(QFrame.Box|QFrame.Plain)

        self.graphic_interface = GraphicInterface()
        self.graphic_interface.setFrameStyle(QFrame.Box|QFrame.Plain)

        splitter_left_right.addWidget(self.label_data_information)
        splitter_left_right.addWidget(self.graphic_interface)

        splitter_top_bottom = QSplitter(Qt.Vertical)
        splitter_top_bottom.addWidget(splitter_left_right)
        splitter_top_bottom.addWidget(self.label_command_information)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(splitter_top_bottom)

        self.setLayout(vbox)
        self.show()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.eeg = EEGData()
        print(self.eeg)
        self.initUI()

    def initUI(self):

        self.statusBar()

        self._actions_init()
        #menuBar
        self._menubar_inti_()


        main_widget = MainWidget()
        self.setCentralWidget(main_widget)
        # self.setGeometry(300, 300, 300, 200)
        # self.setWindowTitle('Menubar')
        # self.show()
        #toolbar
        #         exitAction = QAction(QIcon('/home/qch/Pictures/2.jpg'), 'Exit', self)
        #         exitAction.setShortcut('Ctrl+Q')
        #         exitAction.triggered.connect(qApp.quit)
        #
        #         self.toolbar = self.addToolBar('Exit')
        #         self.toolbar.addAction(exitAction)
        # #textedit  in central widget
        #         textEdit = QTextEdit()
        #         self.setCentralWidget(textEdit)

        self.setGeometry(300, 300, 500,500)
        self.setWindowTitle('main window')

        self.show()


    def _actions_init(self):
        #IO tool
        self.IO_Import_Data = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&IO_Import_Data', self)
        #self.IO_import_data.setShortcut('Ctrl+I')
        self.IO_Import_Data.setStatusTip('IO_Import_Data')
        self.IO_Import_Data.triggered.connect(qApp.quit)

        self.IO_Save_Data = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&IO_Save_Data', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.IO_Save_Data.setStatusTip('IO_save_data')
        self.IO_Save_Data.triggered.connect(qApp.quit)

        self.IO_Load_Location = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&IO_Load_Location', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.IO_Load_Location.setStatusTip('IO_Load_Location')
        self.IO_Load_Location.triggered.connect(qApp.quit)
        #Preprocess tool
        self.Preprocess_Filter = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&Preprocess_Filter', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.Preprocess_Filter.setStatusTip('Preprocess_Filter')
        self.Preprocess_Filter.triggered.connect(qApp.quit)

        self.Preprocess_ICA = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&Preprocess_ICA', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.Preprocess_ICA.setStatusTip('Preprocess_ICA')
        self.Preprocess_ICA.triggered.connect(qApp.quit)

        #FeatureExtract tool
        self.FeatureExtract_Time = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&FeatureExtract_Time', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.FeatureExtract_Time.setStatusTip('FeatureExtract_Time')
        self.FeatureExtract_Time.triggered.connect(qApp.quit)

        self.FeatureExtract_Frequency = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&FeatureExtract_Frequency', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.FeatureExtract_Frequency.setStatusTip('FeatureExtract_Frequency')
        self.FeatureExtract_Frequency.triggered.connect(qApp.quit)
        #VisualBoard
        self.VisualBoard_Raw = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&VisualBoard_Raw', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.VisualBoard_Raw.setStatusTip('VisualBoard_Raw')
        self.VisualBoard_Raw.triggered.connect(qApp.quit)

        self.VisualBoard_Sensor = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&VisualBoard_Sensor', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.VisualBoard_Sensor.setStatusTip('VisualBoard_Sensor')
        self.VisualBoard_Sensor.triggered.connect(qApp.quit)

        self.VisualBoard_Analysis = QAction(QIcon('/home/qch/Pictures/2.jpg'), '&VisualBoard_Analysis', self)
        #self.IO_save_data.setShortcut('Ctrl+S')
        self.VisualBoard_Analysis.setStatusTip('VisualBoard_Analysis')
        self.VisualBoard_Analysis.triggered.connect(qApp.quit)


    def _menubar_inti_(self):

        self.menubar = self.menuBar()

        menubar = self.menubar.addMenu('&IOOperation')
        menubar.addAction(self.IO_Import_Data)
        menubar.addAction(self.IO_Save_Data)
        menubar.addAction(self.IO_Load_Location)

        menubar = self.menubar.addMenu('&Preprocess')
        menubar.addAction(self.Preprocess_Filter)
        menubar.addAction(self.Preprocess_ICA)

        menubar = self.menubar.addMenu('&FeatureExtract')
        menubar.addAction(self.FeatureExtract_Time)
        menubar.addAction(self.FeatureExtract_Frequency)

        menubar = self.menubar.addMenu('&VisualBoard')
        menubar.addAction(self.VisualBoard_Raw)
        menubar.addAction(self.VisualBoard_Sensor)
        menubar.addAction(self.VisualBoard_Analysis)
            #
    # def _layout_inti_(self):
    #     splitter_left_right = QSplitter(Qt.Horizontal)
    #     self.label_data_information = QLabel(self.DATA_INFORMATION)
    #     self.label_command_information = QLabel(self.command_information)
    #     self.label_data_information.setFrameStyle(QFrame.Box|QFrame.Plain)
    #     self.label_command_information.setFrameStyle(QFrame.Box|QFrame.Plain)
    #
    #     self.graphic_interface = GraphicInterface()
    #
    #     splitter_left_right.addWidget(self.label_data_information)
    #     splitter_left_right.addWidget(self.graphic_interface)
    #
    #     splitter_top_bottom = QSplitter(Qt.Vertical)
    #     splitter_top_bottom.addWidget(splitter_left_right)
    #     splitter_left_right.addWidget(self.label_command_information)
    #     vbox = QtWidgets.QVBoxLayout()
    #     vbox.addWidget(splitter_top_bottom)
    #
    #     self.setLayout(vbox)





if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
