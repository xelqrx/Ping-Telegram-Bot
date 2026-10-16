import subprocess

def ping_site(site, time_between):
    result = subprocess.run(["ping", site, "-c", "4", "-i", time_between], capture_output=True, text=True)
    return result.returncode