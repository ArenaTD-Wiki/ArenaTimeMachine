import time
import subprocess
from keep_alive import keep_alive
keep_alive()


while True: 
  command = ["waybackpack", "https://arenatd.fandom.com", "-d", "/home/runner/ArenaTimeMachine/Archives", "--follow-redirects", "--no-clobber"]
  subprocess.run(command, check=True)
  time.sleep(4000)