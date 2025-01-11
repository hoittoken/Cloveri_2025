import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from orm import SyncOrm

SyncOrm.create_tables()
SyncOrm.insert_interns()
SyncOrm.insert_grades()
SyncOrm.insert_tools()

SyncOrm.select_interns()
#SyncOrm.update_interns()