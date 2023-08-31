from enum import Enum

class BugType(Enum):
    FEATURE = 'feature'
    BUG = 'bug'

class BugStatus(Enum):
    NEW = 'new'
    STARTED = 'started'
    COMPLETED = 'completed'
    RESOLVED = 'resolved'
    
    
