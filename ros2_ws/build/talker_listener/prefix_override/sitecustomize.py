import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/maaz/Stash-Colonel/ros2_ws/install/talker_listener'
