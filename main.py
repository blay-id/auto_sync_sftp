
import os, json,time
from sync_SFTP import SFTPAutoSync


host = "host"
user_name = "username"
password = "password"

#change filters for not syncronize
filters = ['__pycache__','kk', 'node_modules', '.','.git','tmp']

#set path (not use /root/)
remote_path = "jspy"

main_path = os.path.join("../backup_sftp", remote_path)
if not os.path.exists(main_path):os.makedirs(main_path)

sftp = SFTPAutoSync(host, user_name, password, filters)
print("[ FTP SYNC RUNNING... ]")
print("[ SYNCRONIZE FROM : {}/{}/{} ]".format(host, user_name,remote_path))
print("[ TO : {}]".format(main_path))


while True:
    try:
        
        print("...........................")
        sftp.normalize()         #refresh data
        sftp.sync(remote_path, main_path) #detect from sftp
        sftp.ftp_find_del(main_path)      #detect file deleted from sftp
        sftp.sync_d(remote_path, main_path) #detect localpath

    except Exception as e:
        print(e)
