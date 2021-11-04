from xml.etree import  ElementTree as ET
from hashlib import sha1

path = './database/laptop.xml'

class Brand():
    def __init__(self, name: str, laps: list):
        self._name = name
        self._laptops = laps

    @property
    def name(self):
        return self._name

    @property
    def laptops(self):
        return self._laptops

    @staticmethod
    def getIDLap(nameBrand, nameLap):
        data = nameBrand + nameLap
        id = sha1(data.encode()).hexdigest()
        return id

    @staticmethod
    def addBrand(name: str):
        root = ET.parse(path).getroot()
        # Check name brand
        for child in root:
            if name == child.tag:
                return False

        # Add new brand
        newBrand = ET.SubElement(root, name)
        ET.ElementTree(root).write(path)
        return True

    @staticmethod
    def deleteBrand(name: str):
        root = ET.parse(path).getroot()
        # Check name brand
        for child in root:
            if name == child.tag:
                root.remove(child)
                ET.ElementTree(root).write(path)
                return True
        return False

    @staticmethod
    def fixName(oldName : str, newName: str):
        root = ET.parse(path).getroot()
        # Check name brand
        for child in root:
            if oldName == child.tag:
                child.tag = newName
                ET.ElementTree(root).write(path)
                return True
        return False

    @staticmethod
    def getAllInfo():
        info = []
        root = ET.parse(path).getroot()
        for child in root:
            info.append(child.tag)
        return info

    @staticmethod
    def addNewLap(brand: str, namelap: str):
        root = ET.parse(path).getroot()
        for profile in root.findall(brand):
            newL = ET.SubElement(profile, namelap)
            newL.text = Brand.getIDLap(brand, namelap)
            ET.ElementTree(root).write(path)
            return True
        return False

    @staticmethod
    def delLap(brand: str, namelap: str):
        # Find id if it exists, then remove
        root = ET.parse(path).getroot()
        for profile in root.findall(brand):
            a = profile.find(namelap)
            profile.remove(a)
            ET.ElementTree(root).write(path)
            return True
        return False

    @staticmethod
    def getAllLap(brand: str):
        laps = []
        root = ET.parse(path).getroot()
        for bra in root.findall(brand):
            for lap in bra:
                laps.append(lap.tag)
        return laps















