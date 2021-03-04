import datetime, uuid, os
import xml.etree.ElementTree as ET
import time, subprocess
from threading import Thread
from Engine.Settings import Settings

class MirrorTask:
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
        self._parent = parent
        
    @staticmethod
    def Deserialize(xml):
        if xml is None:
            return None
        task = MirrorTask()
        task.Guid = xml.attrib.get('guid')
        for child in xml.iter():
            tag = child.tag
            txt = child.text
            if txt is None:
                txt = ''
            if tag == 'source':
                task.Source = txt
            elif tag == 'target':
                task.Target = txt
            
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
                task.CustomRobocopySwitches = txt
            elif tag == "lastOperation":
                task.LastOperation = txt
            elif tag == 'scheduled':
                task.Scheduled = True if txt == 'True' else False
        return task
        
    def Serialize(self, xml):
        xml.set('guid', self.Guid)
        ET.SubElement(xml, 'source').text = self.Source
        if len(self.ExcludedFiles) > 0:
            node = ET.SubElement(xml, 'exclusions')
            for text in self.ExcludedFiles:
                ET.SubElement(node, 'file').text = text
        if len(self.ExcludedFolders) > 0:
            tmp = xml.findall("exclusions")
            if len(tmp) == 0:
                node = ET.SubElement(xml, "exclusions")
            else:
                node = tmp[0]
            for text in self.ExcludedFolders:
                if len(text) > 0:
                    ET.SubElement(node, 'folder').text = text
        ET.SubElement(xml, 'excludedAttributes').text = self.ExcludedAttributes
        ET.SubElement(xml, 'target').text = self.Target
        
        ET.SubElement(xml, 'customRobocopySwitches').text = self.CustomRobocopySwitches
        ET.SubElement(xml, 'lastOperation').text = self.LastOperation
        ET.SubElement(xml, 'scheduled').text = str(self.Scheduled)
        ET.SubElement(xml, 'useCustomOptions').text = str(self.UseCustomOptions)


    def output_reader(self, proc, outq):
        for line in iter(proc.stdout.readline, b''):
            outq.put(line.decode('utf-8'))
        
    def makeLog(self, str_msg):
        _date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
        _log = '{0}: {1}\n\n'.format(_date, str_msg)
        self._parent.log.emit(_log)
        
    def GetExcludeOptions(self):
        params = []

        if len(self.ExcludedAttributes) > 0:
            params.append("/xa:")
            params.append(self.ExcludedAttributes)
            
        if len(self.ExcludedFiles) > 0:
            params.append('/xf')
            for f in self.ExcludedFiles:
                if f[0] != '\\':
                    params.append(f)
                    continue
                t = self.Source + f
                t = t.replace('/', '\\')
                params.append(t)
                
        if len(self.ExcludedFolders) > 0:
            params.append("/xd")
            for dir in self.ExcludedFolders:
                if dir[0] != '\\':
                    params.append(dir)
                    continue
                t = self.Source+dir
                t = t.replace('/', '\\')
                params.append(t)
            
        return ' '.join(params)
    
    def buildSwitches(self, src):
        text = self.CustomRobocopySwitches.replace('  ', ' ')
        stringBuilder = []
        for t in text.split(' '):
            stringBuilder.append(t)
            
        text = self.GetExcludeOptions()
        if len(text) > 0:
            for t in text.split(' '):
                stringBuilder.append(t)
            
        return stringBuilder
        
    def GetCmd(self):
        return os.getcwd() + '\\Tools\\robocopy.exe'
    
    def GetCopyPath(self):
        if self._direction:
            return '%s to %s' % (self.Source, self.Target)
        else:
            return '%s to %s' % (self.Target, self.Source)
    def GetParams(self):
        robocopy_file = self.GetCmd()
        src = self.Source if self._direction else self.Target
        dst = self.Target if self._direction else self.Source
        params = self.buildSwitches(src)
        src = src.replace('/', '\\')
        dst = dst.replace('/', '\\')
        cmd = [self.GetCmd(),
                src,
                dst]
        for p in params:
            cmd.append(p)
        return cmd, src, dst
    
    def run(self):
        cmd, src, dst = self.GetParams()
        '''proc = subprocess.Popen(cmd)
        
        # proc.stdout.close()
        # proc.wait()
        # self.makeLog('[%s->%s] Starting.....' % (src, dst))
        while True:
            # output = proc.stdout.readline()
            if proc.poll() is not None:
                break
            # if output:
                # print(output)
                # if self._parent is not None:
                    # try:
                        # str_msg = output.decode('utf-8')
                        # self._parent.log.emit(str_msg)
                    # except Exception as e:
                        # pass
        '''
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        stdout = proc.communicate()[0].decode('utf-8')
        self.makeLog("[%s] copied to [%s]" % (src, dst))
        self._parent.updateList.emit(stdout)


