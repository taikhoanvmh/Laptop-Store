from xml.etree import  ElementTree as ET
from hashlib import sha1
import random
import json

path = './database/bills.xml'

class Bill():
    def __init__(self, id: str, day: str, month: str, info: dict):
        self._id = id
        self._day = day
        self._month = month
        self._info = info

    @property
    def id(self):
        return self._id
    @property
    def day(self):
        return  self._day
    @property
    def month(self):
        return self._month
    @property
    def info(self):
        return self._info

    #---------------------------------

    @staticmethod
    def getIDBill(info: dict):
        #gen a random num
        num = random.randint(0, 10000)

        info['rand'] = num
        encoded = json.dumps(info, sort_keys=True).encode()
        id = sha1(encoded).hexdigest()
        return id

    @staticmethod
    def addNewBill(order: dict):

        root = ET.parse(path).getroot()

        newBill = order.copy()
        mont = newBill['month']
        # Create new bill
        try:
            id = Bill.getIDBill(order)
            idBill = {'id': id,
                      'month': mont}
            newinfo = ET.SubElement(root, "Bill", idBill)
            detail = ET.SubElement(newinfo, "detail", newBill)

            #write to xml file
            tree = ET.ElementTree(root)
            tree.write(path)
            return True
        except:
            return False

    @staticmethod
    def deleteBill(id: str):
        # Find id if it exists, then remove
        root = ET.parse(path).getroot()
        for profile in root.findall('Bill'):
            if id == profile.attrib.get('id'):
                root.remove(profile)
                ET.ElementTree(root).write(path)
                return True
        return False


    @staticmethod
    def getBillByMonth(month: str):
        bills = []
        root = ET.parse(path).getroot()
        for profile in root.findall('Bill'):
            # Get info
            if month == profile.attrib.get('month'):
                try:
                    #----------------------
                    id = profile.attrib.get('id')
                    day = profile[0].attrib.get('day')
                    info = profile[0].attrib
                    bills.append(Bill(id, month,day,info))
                    print(day)
                except:
                    continue
        return bills
















