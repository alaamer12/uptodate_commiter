"""
Example of windows service
"""

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'MyService'
    _svc_display_name_ = 'My Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.is_running = True

    def SvcDoRun(self):
        while self.is_running:
            hostname = socket.gethostname()
            servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                                  servicemanager.PYS_SERVICE_STARTED,
                                  (self._svc_name_, ''))
            time.sleep(10)
            servicemanager.LogInfoMsg(f"Running on {hostname}")

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyService)
