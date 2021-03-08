import datetime
import uuid
import os
import subprocess
import re
import xml.etree.ElementTree as ET
from Engine.Settings import Settings


class MirrorTask:
    '''Class to implement basic rocketcopy task
    Attributes:
    ----------
    Guid : str
        guid to identify each task
    Source : str
        source dir copied from
    Target : str
        target dir copied to
    ExcludedFiles : list
        list of files to be excluded
    ExcludedFolders : list
        list of folders to be excluded
    ExcludedAttributes : str
        command arg to be used in excluded obj
    CustomRobocopySwitches : str
        custom switch operations
    UseCustomOptions : Bool
        use or not custom switches
    LastOperation : string
        last operation time stamp
    Scheduled : Bool
        Bool that this task is sceduled or not
    _parent : FrmMainWindow
        UI class to emit signals
    _direction : Bool
        true: backup false:restore
    Methods:
    ----------
    setParent(parent):
        sets the UI instance as the parent
    Deserialize(xml):
        parse the xml element
    Serialize(xml)
        updates the xml node with task attributes
    makeLog(str_msg):
        prints the log on main window
    GetExcludeOptions(add_quite=False)
        make the excludeoptions as a string
    buildSwitches()
        make the list of switch
    GetCmd()
        returns the robocopy path
    GetCopyPath()
        returns the source and target depending on direction
    GetParams()
        get the params, src, dst of robocopy
    GetScheduleParams()
        get params to be registered in Task Schedule
    run():
        performs the robocopy by subprocess
    '''

    def __init__(self):
        self.Guid = str(uuid.uuid4())
        self.Source = ''
        self.Target = ''
        self.ExcludedFiles = []
        self.ExcludedFolders = []
        self.ExcludedAttributes = ""
        self.CustomRobocopySwitches = ''
        self.UseCustomOptions = False
        self.LastOperation = ''
        self.Scheduled = False
        self._parent = None
        self._direction = True

    def setParent(self, parent):
        '''
        '''
        self._parent = parent

    @staticmethod
    def Deserialize(xml):
        '''
        parse the xml element
        Returns:
        --------
        task : MirrorTask
            returns the parsed task
        '''
        if xml is None:
            return None
        task = MirrorTask()
        try:
            # updates Guid from xml guid attrib
            task.Guid = xml.attrib.get('guid')
            # iterates sub nodes
            for child in xml.iter():
                tag = child.tag
                txt = child.text
                if txt is None:
                    txt = ''
                # loads Source
                if tag == 'source':
                    task.Source = txt
                # loads Target
                elif tag == 'target':
                    task.Target = txt
                # loads Exclusions
                elif tag == 'exclusions':
                    for ch_ele in child.iter():
                        if ch_ele.tag == 'file':
                            task.ExcludedFiles.append(ch_ele.text)
                        elif ch_ele.tag == "folder":
                            task.ExcludedFolders.append(ch_ele.text)
                elif tag == "excludedAttributes":
                    task.ExcludedAttributes = txt
                elif tag == 'useCustomOptions':
                    task.UseCustomOptions = True if txt == 'True' else False
                elif tag == "customRobocopySwitches":
                    task.CustomRobocopySwitches = re.sub(' +', ' ', txt)
                elif tag == "lastOperation":
                    task.LastOperation = txt
                elif tag == 'scheduled':
                    task.Scheduled = True if txt == 'True' else False
        except Exception as e:
            print(f'MirrorTask Deserialize Err:{e}')
        return task

    def Serialize(self, xml):
        '''
        updates the xml node with task attributes
        '''
        try:
            # updates guid
            xml.set('guid', self.Guid)
            # updates Source
            ET.SubElement(xml, 'source').text = self.Source
            # updates ExcludedFiles
            if len(self.ExcludedFiles) > 0:
                node = ET.SubElement(xml, 'exclusions')
                for text in self.ExcludedFiles:
                    ET.SubElement(node, 'file').text = text
            # updates ExcludedFolders
            if len(self.ExcludedFolders) > 0:
                tmp = xml.findall("exclusions")
                if len(tmp) == 0:
                    node = ET.SubElement(xml, "exclusions")
                else:
                    node = tmp[0]
                for text in self.ExcludedFolders:
                    if len(text) > 0:
                        ET.SubElement(node, 'folder').text = text
            ET.SubElement(xml, 'excludedAttributes').text = self.ExcludedAttributes             # noqa
            ET.SubElement(xml, 'target').text = self.Target

            ET.SubElement(xml, 'customRobocopySwitches').text = self.CustomRobocopySwitches     # noqa
            ET.SubElement(xml, 'lastOperation').text = self.LastOperation
            ET.SubElement(xml, 'scheduled').text = str(self.Scheduled)
            ET.SubElement(xml, 'useCustomOptions').text = str(self.UseCustomOptions)            # noqa
        except Exception as e:
            print(f'MirrorTask/Serialize Err:{e}')

    def makeLog(self, str_msg):
        '''
        emits the log signal
        '''
        try:
            _date = datetime.datetime.now().strftime(
                Settings.MainWin_Log_DateFormt)
            _log = f'{_date}: {str_msg}\n\n'
            self._parent.log.emit(_log)
        except Exception as e:
            print(f'MirrorTask/makeLog Err:{e}')

    def GetExcludeOptions(self, add_quote=False):
        '''
        make the excludeoptions as a string
        Parameters:
        -------------
        add_quote : Bool
            determines if '\"' is added to wrap paths
        Returns:
        -------------
        params: list
            list of params for Excluding
        '''
        params = []
        try:
            # loads ExcludedAttributes params
            if len(self.ExcludedAttributes) > 0:
                params.append("/xa:")
                params.append(self.ExcludedAttributes)
            # loads ExcludedFiles params
            if len(self.ExcludedFiles) > 0:
                params.append('/xf')
                for f in self.ExcludedFiles:
                    # for wildcard
                    if f[0] != '\\':
                        params.append(f)
                        continue
                    # add '\' if add_quote is True
                    if add_quote:
                        t = '\"' + self.Source + f + '\"'
                    else:
                        t = self.Source + f
                    params.append(t)
            # loads ExcludedFolders params
            if len(self.ExcludedFolders) > 0:
                params.append("/xd")
                for dir in self.ExcludedFolders:
                    # for wildcard
                    if dir[0] != '\\':
                        params.append(dir)
                        continue
                    # add '\' if add_quote is True
                    if add_quote:
                        t = '\"' + self.Source + dir + '\"'
                    else:
                        t = self.Source+dir
                    params.append(t)
        except Exception as e:
            print(f'GetExcludeOptions Err:{e}')
        # use ';' as a splitter
        return ';'.join(params)

    def buildSwitches(self):
        '''
        make the list of switch
        '''
        stringBuilder = []
        try:
            # Loads CustomRobocopySwitches params
            text = self.CustomRobocopySwitches
            for t in text.split(' '):
                stringBuilder.append(t)
            # Loads GetExcludeOptions params
            text = self.GetExcludeOptions()
            if len(text) > 0:
                for t in text.split(';'):
                    stringBuilder.append(t)
        except Exception as e:
            print(f'BuildSwitches Err:{e}')
        return stringBuilder

    def GetCmd(self):
        '''
        returns the robocopy path
        '''
        return f'{os.getcwd()}\\{Settings.RoboCopy_Tool_Path}'

    def GetCopyPath(self):
        '''
        returns the source and target depending on direction
        '''
        if self._direction:
            return f'{self.Source} to {self.Target}'
        else:
            return f'{self.Target} to {self.Source}'

    def GetParams(self):
        '''
        get the params, src, dst of robocopy
        '''
        src = self.Source if self._direction else self.Target
        dst = self.Target if self._direction else self.Source
        params = self.buildSwitches()
        # build cmd params
        cmd = [self.GetCmd(), src, dst]
        # add switch options
        for p in params:
            cmd.append(p)
        return cmd, src, dst

    def GetScheduleParams(self):
        '''
        get params to be registered in Task Schedule
        '''
        params = []
        try:
            # exec file
            params.append(self.GetCmd())
            # src
            params.append(f'\"{self.Source}\"')
            # dst
            params.append(f'\"{self.Target}\"')
            # exclude params
            for p in self.GetExcludeOptions(True).split(';'):
                params.append(p)
            # default switches
            for p in Settings.RobocopySwitches.split(' '):
                if p not in params:
                    params.append(p)
            # custom switches
            for p in self.CustomRobocopySwitches.split(' '):
                params.append(p)
        except Exception as e:
            print(f'GetScheduleParams Err:{e}')
        return params

    def run(self):
        '''
        performs the robocopy by subprocess
        '''
        # load cmd params, src, dst
        cmd, src, dst = self.GetParams()
        # prepare subprocess call
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        # gets the output of the process
        stdout = proc.communicate()[0].decode('utf-8')
        # put the log
        self.makeLog(f'[{src} copied to [{dst}]')
        # send the process result
        self._parent.updateList.emit(stdout)
