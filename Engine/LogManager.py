import xml.etree.ElementTree as ET
import os

class LogManager:
    def __init__(self):
        _path = os.getcwd() + '\\logs.xml'
        if not os.path.exists(_path):
            self.Create()
        _path = os.getcwd() + '\\Logs\\'
        if not os.path.exists(_path):
            os.mkdir(_path)
        self.tree = ET.parse('logs.xml')
        self.root = self.tree.getroot()
    
    def Create(self):
        root = ET.Element('log')
        tree = ET.ElementTree(root)
        tree.write('logs.xml')
        
    def GetTaskElement(self, guid):
        task_list = self.root.findall('task')
        res_element = None
        for task in task_list:
            if task.attrib.get('guid') == guid:
                res_element = task
                break
        return res_element
    
    def LoadTasks(self):
        tasks = []
        for ele in self.root.findall('task'):
            task = MirrorTask.Deserialize(ele)
            if task is None:
                continue
            tasks.append(task)
        return tasks

    def Deserialize(self, xml):
        data = []
        for entry in xml.findall('./'):
            en_data = {}
            for child in entry.iter():
                tag = child.tag
                txt = child.text
                en_data[tag] = txt
            data.append(en_data)
        return data
        
    def LoadLogs(self, guid):
        entries = []
        for ele in self.root.findall('task'):
            if ele.attrib.get('guid') == guid:
                entries = self.Deserialize(ele)
                break
        return entries
        
    def AddLog(self, task, str_log, timestamp):
        xelement = self.GetTaskElement(task.Guid)
        if xelement is None:
            xelement = ET.SubElement(self.root, 'task')
            xelement.set('guid', task.Guid)
        xelement.set('lastSuccess', timestamp)
        
        entry = ET.SubElement(xelement, 'entry')
        ET.SubElement(entry, 'timeStamp').text = timestamp
        ET.SubElement(entry, 'type').text = 'information'
        ET.SubElement(entry, 'message').text = task.GetCopyPath()
        
        log_path = os.getcwd() + '\\Logs\\' + task.Guid
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        file_count = len(os.listdir(log_path))
        file_name = '%d.log'%(file_count + 1)
        f = open("%s\\%s"%(log_path, file_name), "w")
        f.write(str_log)
        f.close()
        ET.SubElement(entry, 'dataRef').text = file_name
        self.tree.write('logs.xml')
