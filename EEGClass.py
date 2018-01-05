from eeg_read_save.eeg_read import readBP,readLoc
from eeg_preprocess.eegFilter import Filtereeg
from eeg_visual_board.eeg_visual import *
import os

class EEGData(object):
    dirpath = "/home/qch/EEGDataProcess/src/examples/"
    eeg_name = "happy"

    eegpath = dirpath + eeg_name + ".eeg"
    vhdrpath = dirpath + eeg_name +".vhdr"
    vmrkpath = dirpath + eeg_name + ".vmrk"

    locpath = "/home/qch/EEGDataProcess/src/python1128/Standard-10-20-Cap81.ced"

    eeg_raw = []
    eeg_ICA =[]

    eeg_bands_alpha = []
    eeg_bands_beta = []
    eeg_bands_gamma = []

    eeg_features_timedomain = []
    eeg_features_frequencydomain = []

    configuration = {}
    mark = {}
    def __init__(self):
        self.eeg_raw, self.configuration, self.mark = readBP(
                                   self.eegpath, self.vhdrpath, self.vmrkpath)
        print(self.eeg_raw.shape,self.configuration, self.mark)
        # eeg_visual_raw(self.eeg_raw)
    def readBP(self,eegpath,vhdrpath,vmrkpath):
        self.eeg_raw, self.configuration, self.mark = readBP(
                                   eegpath, vhdrpath, vmrkpath)
        
    def readLoc(self, locpath):
        self.sensorLoc, self.sensorName = readLoc(locpath)
        # print(self.sensorLoc,self.sensorName,self.sensorLoc.shape)

    def preprocess(self,ICA=False, Alpha=False, Beta=False, Gamma=False):

        if ICA==True:
            print("EEGClass: wait to realize ICA")
        if Alpha==True:
            self.eeg_bands_alpha = Filtereeg(eegdata=self.eeg_raw,methodID="BUTTER",
                            fs=self.configuration['Frequency'],downfz=8,upfz=13)
            print(self.eeg_bands_alpha.shape,self.configuration['Frequency'])
            print("EEGClass: Alpha extracted")
        if Beta==True:
            self.eeg_bands_beta = Filtereeg(eegdata=self.eeg_raw,methodID="BUTTER",
                            fs=self.configuration['Frequency'],downfz=16,upfz=31)
            print(self.eeg_bands_beta.shape)
            print("EEGClass: Beta extracted")
        if Gamma==True:
            self.eeg_bands_gamma = Filtereeg(eegdata=self.eeg_raw,methodID="BUTTER",
                            fs=self.configuration['Frequency'],downfz=32,upfz=100)
            print(self.eeg_bands_gamma.shape)
            print("EEGClass: Gamma extracted")
    def visualBoard(self, Raw=False, Sensor=False, ICA=False, Alpha=False, Beta=False
                    , Gamma=False):
        if Raw==True:
            Visualeeg32_subplot(self.eeg_raw,'Raw')
            Visualeeg32_one(self.eeg_raw[0:32,:],'Raw')
            print("EEGClass: ploting rawdata")
        if Sensor==True:
            Visualeeg_sensor2D(self.sensorName,self.sensorLoc)
            Visualeeg_sensor3D(self.sensorName,self.sensorLoc)
            print("EEGClass: wait to realize")
        if ICA==True:
            print("EEGClass: wait to realize")
        if Alpha==True:
            Visualeeg32_one(self.eeg_bands_alpha,'Alpha')
            print(self.eeg_bands_alpha.shape)
            print("EEGClass: ploting alpha")
        if Beta==True:
            Visualeeg32_one(self.eeg_bands_beta,'Beta')
            print("EEGClass: ploting beta")
        if Gamma==True:
            Visualeeg32_one(self.eeg_bands_gamma,'Gamma')
            print("EEGClass: ploting gamma")

# print(os.getcwd())
# e = EEGData()
