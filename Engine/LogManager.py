import xml.etree.ElementTree as ET
import os
import shutil
from Engine.Settings import Settings
from Engine.MirrorTask import MirrorTask


class LogManager:
    '''Class to manage logs for task

        LogManager creates 'Logs' folder and also
    creates each folder with the GUID of the task.
    Attributes:
    -------------
    Methods:
    -------------
    Create():
        crates empty xml for log manager
    GetTaskElement(guid):
        Retrieves the task from GUID string
    Deserialize(xml):
        parse the xml element
    LoadLogs(guid):
        Reads the log content of the task
    AddLog(task, str_log, timestamp)
        Adds new log the task history
    DeleteTask(task)
        Removes the task
    '''

    xml_file = Settings.LOGS_XML

    def __init__(self):
        '''
        check if Logs dir is exist and if not,
        creates a new one.
        '''
        try:
            # get the log xml path
            _path = f'{os.getcwd()}\\{self.xml_file}'
            # check if it exist
            if not os.path.exists(_path):
                # if not, create
                self.Create()
            # create a folder for tasks
            _path = f'{os.getcwd()}\\{Settings.LOGS_DIR}\\'
            # check if dir is exist, otherwise creates one
            if not os.path.exists(_path):
                os.mkdir(_path)
            # parse the xml
            self.tree = ET.parse(self.xml_file)
            # get the root element
            self.root = self.tree.getroot()
        except Exception as e:
            print(f"LogManager Error:{e}")

    def Create(self):
        '''
            Creates empty xml tree and saves
        '''
        try:
            root = ET.Element(Settings.LOGXML_ROOT)
            tree = ET.ElementTree(root)
            tree.write(self.xml_file)
        except Exception as e:
            print(f"Create Log XML file err:{e}")

    def GetTaskElement(self, guid):
        '''
        Retrieves the task from GUID string
        Parameters:
        -----------
        guid : str
            GUID assigned to the task
        Returns:
        -----------
            res_element : Element found by guid
        '''
        # prepare the result element
        res_element = None
        try:
            # make the list of task
            task_list = self.root.findall(Settings.LOGXML_NODE)
            # iterates the task list
            for task in task_list:
                # compare GUID
                if task.attrib.get('guid') == guid:
                    res_element = task
                    break
        except Exception as e:
            print(f"LogManager/GetTaskElement Err:{e}")
        return res_element

    def LoadTasks(self):
        '''
        Loads task from XML and returns as a list
        Returns:
            the list of task
        '''
        # empty the return list
        tasks = []
        try:
            # iterates 'task' tag
            for ele in self.root.findall(Settings.LOGXML_NODE):
                task = MirrorTask.Deserialize(ele)
                if task is None:
                    continue
                tasks.append(task)
        except Exception as e:
            print(f"LogManager/LoadTask Err:{e}")
        return tasks

    def Deserialize(self, xml):
        '''
        parse the xml element
        Parameters:
        -----------
        xml: Element
            input element to be parsed
        Returns:
        ----------
        data: list
            the list of task attributes
        '''
        data = []
        try:
            # iterates all
            for entry in xml.findall('./'):
                # prepare dict()
                en_data = {}
                for child in entry.iter():
                    # key
                    tag = child.tag
                    # value
                    txt = child.text
                    en_data[tag] = txt
                data.append(en_data)
        except Exception as e:
            print(f'LogManager/Deserialize Err:{e}')
        return data

    def LoadLogs(self, guid):
        '''
        Reads the log content of the task
        Parameters:
        -----------
        guid : str
            guid of the task to be loaded
        Returns:
        ----------
        entries: list
            list of the tasks that match the guid
        '''
        entries = []
        try:
            for ele in self.root.findall(Settings.LOGXML_NODE):
                if ele.attrib.get('guid') == guid:
                    entries = self.Deserialize(ele)
                    break
        except Exception as e:
            print(f'LogManager/LoadLogs{e}')
        return entries

    def AddLog(self, task, str_log, timestamp):
        '''
        Adds new log the task history and saves
        Parameters:
        -----------
        task: MirrorTask
            task that log must be added
        str_log: str
            sting contents to be added
        timestamp: DateTime stamp
            timestamp when the log is created
        '''
        try:
            if task is None:
                return
            # retrieves the task by guid
            xelement = self.GetTaskElement(task.Guid)
            # if not exist, create new one
            if xelement is None:
                xelement = ET.SubElement(self.root, Settings.LOGXML_NODE)
                xelement.set('guid', task.Guid)
            # updates the timestamp
            xelement.set('lastSuccess', timestamp)

            # creates sub attributes
            entry = ET.SubElement(xelement, 'entry')
            ET.SubElement(entry, 'timeStamp').text = timestamp
            ET.SubElement(entry, 'type').text = 'information'
            ET.SubElement(entry, 'message').text = task.GetCopyPath()

            log_path = f'{os.getcwd()}\\{Settings.LOGS_DIR}\\{task.Guid}'
            # check if log dir exist, and if not, creates new one.
            if not os.path.exists(log_path):
                os.mkdir(log_path)
            # get the total contents in the dir
            file_count = len(os.listdir(log_path))
            # get the new log file name
            file_name = f'{file_count + 1}.log'
            # saves the str_log to the file
            f = open(f'{log_path}\\{file_name}', 'w')
            f.write(str_log)
            f.close()
            # updates the log file path
            ET.SubElement(entry, 'dataRef').text = file_name
            # save sthe xml file
            self.tree.write(self.xml_file)
        except Exception as e:
            print(f'LogManager/AddLog Err:{e}')

    def DeleteTask(self, task):
        '''
        Removes the task
        '''
        try:
            if task is None:
                return
            # removes the directory for the task
            log_path = f'{os.getcwd()}\\{Settings.LOGS_DIR}\\{task.Guid}'
            if os.path.exists(log_path):
                shutil.rmtree(log_path)
            # get the task by guid
            xelement = self.GetTaskElement(task.Guid)
            if xelement is None:
                return
            # removes from root node.
            self.root.remove(xelement)
            # saves the xml
            self.tree.write(self.xml_file)
        except Exception as e:
            print(f'LogManager/DeleteTask Err:{e}')
