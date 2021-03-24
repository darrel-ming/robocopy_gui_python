""" Settings

This script lists values used in the tool.

"""

import re


class Settings:
    """
    A class used to store common values used in the tool
    ...
    Attributes:
    -----------
    RobocopySwitches : str
        a string represents to be used as a default robocopy switches
    Schedule_Folder : str
        the name of folder to contain task on 'Task Scheduler'
    RoboPath : str
        the path of robocopy execution file
    Product_Label : str
        product label
    Product_Version : str
        product version
    Product_AboutLink : str
        about url to be shown on MainWindow/statusbar
    Table_ColumnNames : list(str)
        TableView column labesl
    Schedule_String/UnScheduled_String : str
        Scheduls string on the table view
    Log_DateFormat : str
        DateFormat on log view
    Task_Remove_Msg : str
        Message when the task is removed
    Task_Remove_ErrMsg : str
        Error Message when the task is removed
    Task_Save_ErrMsg : str
        Error Message when the task is saved
    Methods:
    -----------
    """
    RobocopySwitches = "/z /e /fft /r:12 /w:5 /tbd /np /s"
    Schedule_Folder = 'RoboCopy'
    RoboPath = "\\Tools\\Robocopy.exe"

    Product_Label = "RocketCopy"
    Product_Version = 1.0
    Product_AboutLink = 'Help: <a href=\"https://www.lundgrensimon.com/rocketcopy/\">lundgrensimon.com/rocketcopy</a>'  # noqa

    Table_ColumnNames = [
        'Source',
        'Destination',
        'Scheduled',
        'Last Operation']
    Schedule_String = "Yes"
    UnScheduled_String = "No"

    Log_DateFormat = '%Y-%m-%d %H:%M:%S'

    Task_Remove_Msg = 'Are you sure you want to remove the selected task?'
    Task_Remove_ErrMsg = 'The mirror task could not be deleted.'
    Task_Save_ErrMsg = 'The mirror task could not be saved.'

    LOGS_DIR = 'Logs'
    LOGS_XML = 'logs.xml'
    LOGXML_ROOT = 'log'
    LOGXML_NODE = 'task'

    MainWin_Log_DateFormt = '%d.%m.%Y %H:%M'
    RoboCopy_Exe = 'robocopy.exe'
    RoboCopy_Tool_Path = f'Tools\\{RoboCopy_Exe}'

    Schedule_Action_ID = 'RocketCopy'

    TASK_XML = 'tasks.xml'
    TASKXML_ROOT = 'tasks'
    TASKXML_NODE = 'task'

    EDIT_DLG_Invalid_Src_Caption = 'Invalid source folder'
    EDIT_DLG_Invalid_Src_TEXT = 'The source folder does not exist.'
    EDIT_DLG_Invalid_Tar_Caption = 'Invalid target folder'
    EDIT_DLG_Invalid_Tar_TEXT = 'The target folder does not exist.'
    EDIT_DLG_Invalid_Tar_TEXT2 = 'The target folder must not be in the source folder.'
    
    EXCLUDE_DLG_INVALID_File_Caption = 'Invalid file'
    EXCLUDE_DLG_INVALID_File_TEXT = 'The selected file is not contained in the source folder.'
    EXCLUDE_DLG_INVALID_Wild_Caption = 'Invalid name'
    EXCLUDE_DLG_INVALID_Wild_TEXT = 'Willcard name is invalid!'
    EXCLUDE_DLG_INVALID_SubDir_Caption = 'Invalid subfolder'
    EXCLUDE_DLG_INVALID_SubDir_TEXT = 'The selected folder is not contained in the source folder.'
    
    HIST_DLG_ERR_Caption = 'Error'
    HIST_DLG_ERR_TEXT = 'Log file does not exist!'
    HIST_TABLE_COLUMNS = ['Timestamp', 'Task']
    
    SCHEDULE_TYPES = ['One-Shot-Run', 'Daily', 'Weekly', 'Monthly']

    def __init__(self):
        """
        Parameters
        ----------
        """
        self.RobocopySwitches = re.sub(' +', ' ', self.RobocopySwitches)
