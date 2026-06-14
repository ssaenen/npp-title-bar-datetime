# Notepad++ Title Bar Date & Time

A small [PythonScript](https://github.com/bruderstein/PythonScript) plugin for [Notepad++](https://notepad-plus-plus.org/) that updates the window title to show the **current file name** and **last modified date/time**.

**Example title:** `document.txt - 2026-06-14 15:30:45 - Notepad++`

Unsaved or new files display `Unsaved` instead of a timestamp.

## Features

- Shows the active file name in the Notepad++ title bar
- Displays the file's last modified date and time (updates when you switch tabs or save)
- Unicode-safe — works with non-ASCII file names and paths
- Registers only once per session to avoid duplicate callbacks

## Requirements

- [Notepad++](https://notepad-plus-plus.org/downloads/) (Windows)
- [PythonScript plugin](https://github.com/bruderstein/PythonScript) for Notepad++

## Installation

### 1. Install the PythonScript plugin

If you do not already have PythonScript installed:

1. Open Notepad++
2. Go to **Plugins → Plugins Admin**
3. Search for **PythonScript**
4. Select it and click **Install**
5. Restart Notepad++ when prompted

### 2. Add the script

**Option A — Create via the menu (recommended for first-time setup)**

1. Go to **Plugins → Python Script → New Script**
2. Name the script `title_date_time` (or any name you prefer)
3. Paste the contents of [`title_date_time.py`](title_date_time.py) into the new script
4. Save the script

**Option B — Copy the file directly**

Copy `title_date_time.py` into your PythonScript scripts folder:

```
%APPDATA%\Notepad++\plugins\config\PythonScript\scripts\
```

On most systems this resolves to:

```
C:\Users\<YourUsername>\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts\
```

### 3. Run the script

1. Go to **Plugins → Python Script → Scripts → title_date_time**
2. Run the script once
3. Open the console via **Plugins → Python Script → Show Console** if needed
4. You should see: `Title bar update script is now active (Unicode safe)!`

The title bar updates automatically when you switch between open files or save a file.

## Automatic loading (optional)

To enable the script every time Notepad++ starts, use one of these methods:

### Method 1 — Add to `startup.py`

1. Go to **Plugins → Python Script → Open Scripts Folder**
2. Open or create `startup.py`
3. Add this line:

```python
exec(open(os.path.join(os.path.dirname(__file__), 'title_date_time.py')).read())
```

Make sure `import os` is available at the top of `startup.py` if it is not already.

### Method 2 — Place in the scripts directory

Keep `title_date_time.py` in the PythonScript scripts folder and run it from `startup.py` as shown above.

> **Important:** The script is designed to run **once per Notepad++ session**. Running it multiple times in the same session is safe (it will print "already running"), but you should avoid registering duplicate callbacks by only including it once in your startup configuration.

## How it works

The script registers a callback on two Notepad++ events:

- `BUFFERACTIVATED` — when you switch to a different open file
- `FILESAVED` — when the current file is saved

On each event, it reads the current file path, looks up the last modified timestamp from the filesystem, and updates the Notepad++ window title using the Windows Unicode API (`SetWindowTextW`).

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No confirmation message | Open **Plugins → Python Script → Show Console** |
| Title does not update | Run the script once from the Scripts menu |
| "Already running" message | Normal — the script is already active in this session |
| Wrong or missing timestamp | Save the file at least once; unsaved buffers show "Unsaved" |

## License

Free to use and modify. No warranty provided.
