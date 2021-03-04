import xml.etree.ElementTree as ET
import os
from Engine.MirrorTask import MirrorTask
class TaskManager:
    def __init__(self):
        if os.ex
        self.tree = ET.parse('tasks.xml')
        self.root = self.tree.getroot()

    def LoadTasks(self):
        tasks = []
        for ele in self.root.findall('task'):
            task = MirrorTask.Deserialize(ele)
            if task is None:
                continue
            tasks.append(task)
        return tasks

    def GetTaskElement(self, guid):
        task_list = self.root.findall('task')
        res_element = None
        for task in task_list:
            if task.attrib.get('guid') == guid:
                res_element = task
                break
        return res_element

    def SaveTask(self, task):
        if task == None:
            return
        xelement = self.GetTaskElement(task.Guid)
        if xelement is not None:
            xelement.clear()
        else:
            xelement = ET.SubElement(self.root, 'task')

        task.Serialize(xelement)
        self.Save()
        
    def Save(self):
        self.tree.write('tasks.xml')
        
    def DeleteTask(self, task):
        if task is None:
            return
        try:
            # remove task from scheduled manager
            pass
        except Exception as e:
            pass
        xelement = self.GetTaskElement(task.Guid)
        if xelement is None:
            return
        self.root.remove(xelement)
        self.Save()