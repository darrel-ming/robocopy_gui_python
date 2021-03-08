import xml.etree.ElementTree as ET
import os
from Engine.MirrorTask import MirrorTask
from Engine.ScheduledTasksManager import ScheduledTasksManager
from Engine.Settings import Settings


class TaskManager:
    '''
    Class to manage Mirror Tasks
    Attributes:
    -----------
    xml_file : str
        path that save/loads to xml file
    tree : ElementTree
        xml tree
    root : Element
        root node of tree
    Methods:
    ------------
    Create():
        create empty xml for tasks, and save it
    LoadTasks():
        parse the xml and makes the list of tasks
    GetTaskElement():
        get the task by guid
    SaveTask():
        updates the task to xml
    Save():
        save the tree to xml
    DeleteTask():
        delete the task from xml tree, and saves
    '''
    xml_file = Settings.TASK_XML

    def __init__(self):
        '''
        if xml file does not exit, create empty xml and save it
        '''
        try:
            # check if xml file exist
            if not os.path.exists(self.xml_file):
                # create new one
                self.Create()
            # parse xml file
            self.tree = ET.parse(self.xml_file)
            # get root node
            self.root = self.tree.getroot()
        except Exception as e:
            print(f'TaskManager init err:{e}')

    def Create(self):
        '''
        create empty xml for tasks, and save it
        '''
        try:
            root = ET.Element(Settings.TASKXML_ROOT)
            tree = ET.ElementTree(root)
            tree.write(self.xml_file)
        except Exception as e:
            print(f'TaskManager create err:{e}')

    def LoadTasks(self):
        '''
        parse the xml and makes the list of tasks
        '''
        tasks = []
        try:
            # makes the list from xml
            for ele in self.root.findall(Settings.TASKXML_NODE):
                task = MirrorTask.Deserialize(ele)
                if task is None:
                    continue
                tasks.append(task)
        except Exception as e:
            print(f'TaskManager/LoadTasks err:{e}')
        return tasks

    def GetTaskElement(self, guid):
        '''
        get the task by guid
        Parameters:
        -----------
        guid : string
            guid identifier to get task
        '''
        res_element = None
        try:
            task_list = self.root.findall(Settings.TASKXML_NODE)
            for task in task_list:
                if task.attrib.get('guid') == guid:
                    res_element = task
                    break
        except Exception as e:
            print(f'TaskManager/GetTask err:{e}')
        return res_element

    def SaveTask(self, task):
        '''
        saves the task list to xml
        Parameters:
        -------------
        task: MirrorTask
            task to be saved
        '''
        if task is None:
            return
        try:
            # get the element by task guid
            xelement = self.GetTaskElement(task.Guid)
            # if element is None, creates new one
            if xelement is not None:
                xelement.clear()
            else:
                # makes the node
                xelement = ET.SubElement(self.root, Settings.TASKXML_NODE)
            # make sub nodes
            task.Serialize(xelement)
            # save to file
            self.Save()
        except Exception as e:
            print(f'TaskManager/SaveTask err:{e}')

    def Save(self):
        # saves xml tree to file
        self.tree.write(self.xml_file)

    def DeleteTask(self, task):
        '''
        delete the task from xml tree, and saves
        '''
        if task is None:
            return
        try:
            _manager = ScheduledTasksManager()
            _manager.DeleteTask(task)
            xelement = self.GetTaskElement(task.Guid)
            if xelement is None:
                return
            self.root.remove(xelement)
            self.Save()
        except Exception as e:
            print(f'DeleteTask err:{e}')
