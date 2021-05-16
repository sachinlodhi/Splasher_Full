import PySimpleGUI as psg
import backend
import threading
import sys
import subprocess
import base64
import webbrowser

psg.theme("Black")


def gui():
    resolution_list = [
        "800x600",
        "1024x768",
        "1280x960",
        "1280x1024",
        "1600x1200",
        "1280x720",
        "1280x800",
        "1440x900",
        "1680x1050",
        "1920x1080",
        "1920x1200",
        "3840x2160",
    ]
    # Reading ICON
    with open(r"splash.png", "rb") as image_file:
            ICON = base64.b64encode(image_file.read())

    layout = [[psg.Image(data= ICON)],
              [psg.Text("Choose the Source of The Wallpaper", font='Lucida', justification='left')],

              [psg.Combo(["Random", "Collection"], default_value="Random", key='source', readonly=True,
                         enable_events=True)],

              [psg.Text('Tags', justification='left', key='title_Tags', visible=False)],
              [psg.InputText(justification='left', key='tags', visible=False, default_text="california,usa")],
              [psg.Text('Collection ID', justification='left', key='title_CID', visible=False)],
              [psg.InputText(justification='left', default_text='200798', key='collectionID', visible=False)],

              [psg.Text('Time(seconds)', justification='left'), ],
              [psg.InputText(justification='left', key='time', visible=True, default_text='60')],

              [psg.Text("Resolution", font='Lucida', justification='left')],
              [psg.Combo(list(resolution_list), default_value=resolution_list[9], key='resolution', readonly=True)],
              [psg.Text("Verbosity", key="verbosity"),
               psg.Radio("ON", "verbosity", key='verbose_ON', enable_events=True, default=False),
               psg.Radio("OFF", "verbosity", key="verbose_OFF", enable_events=True, default=True)],

              [psg.Output(size=(110, 10), background_color='black', text_color='white', key='Status_Box', visible=False)],
              # [psg.T('Prompt>'), psg.Input(key='-IN-', do_not_clear=False)],

              [psg.Button('Run'), psg.Button("Cancel"), psg.Button("Support Me!!!", key='donate',font=("Helvetica", 12, "italic"))],


              ]

    window = psg.Window('Splasher',  resizable=True, icon = ICON ).Layout(layout)
    # window.set_icon("splash.png")

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == 'Cancel':
            break
        if event == "Run":
            threading.Thread(target=backend.begin, args=(values,), daemon=True).start()
            # runCommand(cmd=values['-IN-'], window=window)
        if event == 'Donate' or event == 'donate':
            webbrowser.open_new('https://paypal.me/SachinLodhi ')

        if values["source"] == 'Random':
            window.Element('title_Tags').Update(visible=True)
            window.Element('tags').Update(visible=True)

            window.Element('title_CID').Update(visible=False)
            window.Element('collectionID').Update(visible=False)
        if values["source"] == 'Collection':
            window.Element('title_CID').Update(visible=True)
            window.Element('collectionID').Update(visible=True)

            window.Element('title_Tags').Update(visible=False)
            window.Element('tags').Update(visible=False)

        if values["verbose_ON"] == True:

            window.Element("Status_Box").Update(visible=True)

        if values["verbose_OFF"] == True:

            window.Element("Status_Box").Update(visible=False)

        # print(f"R1 : {values['verbose_ON']}, R2 : {values['verbose_OFF']}")

        verbosity = values['verbose_ON']


def runCommand(cmd, timeout=None, window=None):
    nop = None
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.refresh() if window else nop  # yes, a 1-line if, so shoot me

    retval = p.wait(timeout)
    return (retval, output)


