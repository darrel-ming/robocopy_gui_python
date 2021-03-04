import datetime, math
import win32com.client
from Engine.Settings import Settings

class ScheduledTasksManager:
    def __init__(self):
        self.scheduler = win32com.client.Dispatch("Schedule.Service")
        self.scheduler.Connect()
        root = self.scheduler.GetFolder('\\')
        self.root = None
        folder_name = '\\%s'%Settings.Schedule_Folder
        try:
            self.root = self.scheduler.GetFolder(folder_name)
        except Exception as e:
            print(e)
        if self.root is None:
            root.CreateFolder(folder_name)
            self.root = self.scheduler.GetFolder(folder_name)

        
    def Get(self, task):
        if task is None:
            return None
        aa = None
        try:
            aa = self.root.GetTask(task.Guid)
        except Exception as e:
            print(e)
        return aa # self.scheduler.GetTask('Test Task') # self.GetName(task)
        
    def GetName(self, task):
        return 'RoboMirror ({0})'.format(task.Guid)
    
    def DeleteTask(self, task):
        self.root.DeleteTask(
            task.Guid,  # Task name
            0)
        
    def Apply(self, task, index, start_time):
        if not task.Scheduled:
            self.DeleteTask(task)
            return
        task_def = self.scheduler.NewTask(0)

        # Create trigger
        TASK_TRIGGER_TIME = 1
        # Daily Trigger
        if index == 0:
            TASK_TRIGGER_TIME = 2
        elif index == 1:
            TASK_TRIGGER_TIME = 3
        elif index == 2:
            TASK_TRIGGER_TIME = 4
            
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()
        daysofweek = [2, 4, 8, 16, 32, 64, 1]
        if index == 0:
            trigger.DaysInterval = 1
            trigger.Id = "DailyTriggerID"
        elif index == 1:
            trigger.DaysOfWeek = daysofweek[start_time.weekday()]
            trigger.WeeksInterval = 1
            trigger.Id = "WeeklyTriggerID"
        elif index == 2:
            trigger.DaysOfMonth = math.pow(2, start_time.day -1)

            trigger.Id = "MonthlyTriggerID"
        trigger.Enabled = task.Scheduled

        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = 'RoboCopy'
        action.Path = task.GetCmd()
        cmd, _, _ = task.GetParams()
        action.Arguments = ' '.join(cmd[1:])

        # Set parameters
        task_def.RegistrationInfo.Description = '%s %s'%(task.Source, task.Target)
        task_def.Settings.Enabled = task.Scheduled
        task_def.Settings.StopIfGoingOnBatteries = False

        # Register task
        # If task already exists, it will be updated
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0

        self.root.RegisterTaskDefinition(
            task.Guid,  # Task name
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE)