import math
import win32com.client
from Engine.Settings import Settings


class ScheduledTasksManager:
    ''' Class to manage Task Scheduler
    Attributes:
    -----------
    Methods:
    -----------
    Get(task):
        get the task by guid
    DeleteTask(task):
        removes the task
    Apply(task, index, start_time)
        set the schedule options to the task
    '''

    def __init__(self):
        '''
        Initializes the ScheduleTaskManager
        '''
        self.scheduler = win32com.client.Dispatch("Schedule.Service")
        self.scheduler.Connect()
        # get the root folder
        root = self.scheduler.GetFolder('\\')
        self.root = None
        folder_name = f'\\{Settings.Schedule_Folder}'
        try:
            self.root = self.scheduler.GetFolder(folder_name)
        except Exception as e:
            print(f'No {folder_name} folder:{e}')
        # if no exists, creates new one
        if self.root is None:
            # creates root folder
            root.CreateFolder(folder_name)
            # get thre root folder
            self.root = self.scheduler.GetFolder(folder_name)

    def Get(self, task):
        '''
        get the TaskScheduler task
        Parameters:
        -----------
        task: MirrorTask
        Returns:
        -----------
        sc_task : SchedulerTask
            the task registed in system TaskScheduler
        '''
        if task is None:
            return None
        sc_task = None
        try:
            sc_task = self.root.GetTask(task.Guid)
        except Exception as e:
            print(f'Cant get the task! {e}')
        return sc_task

    def DeleteTask(self, task):
        '''
        removes the task
        Parameters:
        -----------
        task: MirrorTask
        '''
        try:
            self.root.DeleteTask(task.Guid, 0)
        except Exception as e:
            print(f'Cant remove task:{e}')

    def Apply(self, task, index, start_time):
        '''
        Register/Unregister task to system Task Scheduler
        Parameters:
        -----------
        task : MirrorTask
            input task to be processed
        index: int
            schedule type as following
            0: On-Shoot-Time trigger
            1: Daily trigger
            2: Weekly trigger
            3: Monthly trigger
        '''
        try:
            # if 'Scheduled' value is not, removes the task
            if not task.Scheduled:
                self.DeleteTask(task)
                return
            # register new task
            task_def = self.scheduler.NewTask(0)
            # Create trigger
            TASK_TRIGGER_TIME = 1
            # on-shoot-time
            if index == 0:
                TASK_TRIGGER_TIME = 1
            # daily trigger
            elif index == 1:
                TASK_TRIGGER_TIME = 2
            # weekly trigger
            elif index == 2:
                TASK_TRIGGER_TIME = 3
            # monthly trigger
            elif index == 3:
                TASK_TRIGGER_TIME = 4
            # create a trigger
            trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
            # set the time to start
            trigger.StartBoundary = start_time.isoformat()
            # params for daily trigger
            daysofweek = [2, 4, 8, 16, 32, 64, 1]
            # set options for each trigger
            if index == 0:
                trigger.Id = "TimeTriggerId"
            elif index == 1:
                trigger.DaysInterval = 1
                trigger.Id = "DailyTriggerID"
            elif index == 2:
                trigger.DaysOfWeek = daysofweek[start_time.weekday()]
                trigger.WeeksInterval = 1
                trigger.Id = "WeeklyTriggerID"
            elif index == 3:
                trigger.DaysOfMonth = math.pow(2, start_time.day-1)
                trigger.Id = "MonthlyTriggerID"
            # enables the task
            trigger.Enabled = task.Scheduled
            # Create action
            TASK_ACTION_EXEC = 0
            action = task_def.Actions.Create(TASK_ACTION_EXEC)
            action.ID = Settings.Schedule_Action_ID
            action.Path = task.GetCmd()
            # get the arguments for robocopy
            cmd = task.GetScheduleParams()
            # set the arguments to action
            action.Arguments = ' '.join(cmd[1:])

            # Set parameters
            task_def.RegistrationInfo.Description = f'{task.Source} {task.Target}'  # noqa
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
        except Exception as e:
            print(f'Setting Schedule Err:{e}')
