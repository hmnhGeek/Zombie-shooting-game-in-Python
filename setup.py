import cx_Freeze

executables = [cx_Freeze.Executable('Shoot Me!!.py', shortcutName = 'Shoot the Zombie!!', shortcutDir = 'DesktopFolder', icon = 'z.ico')]

cx_Freeze.setup(
    name='Shoot the Zombie!!',
    options={"build_exe": {"packages":["pygame", "random", "Tkinter", "os", "pickle", "tkMessageBox", "PIL", "uuid"], "include_files":["zombie.png", "stz.png", "z.ico", "aboutGame.txt", "MACFILE.dat", "help.txt", "zombieSound.mp3"]}},

    description="Shooting Game",
    executables = executables
    )
