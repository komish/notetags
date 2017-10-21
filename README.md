# Notetags

A Python3 utility for utilizing tags on plain-text note files. Simple add tags to your plain-text files using a modifier you configure. From there, use this utility to list and search through them effectively.

# Getting Started

Download this application from Github

```
git clone https://github.com/komish/notetags \
  && cd notetags
```

Install the application using `pip3`

```
pip3 install --upgrade .
```

or Install using `setup.py`

```
python3 setup.py install
```

# Generating Configuration File

This utility uses a simple configuration file - `~/.notetags/config.ini`. Generate a base configuration file:

```
$ nt genconfig
Generating configuration...
Creating Directory /home/Username/.notetags if not exists: OK!
Creating configuration file at /home/Username/.notetags/config.ini: OK!
```

# Configuration Reference

Config file is in `ini` format. Section headers are provided:

## [DEFAULT]

|Directive|Information|Example|Required|Default Value|
|:---:|:---:|:---:|:---:|:---:|
|note_path|directory where notes are stored|`/home/Username/Notes`|Yes|None|
|accepted_extensions|colon-separated list of extensions for files to search|`.md:.txt`|No|`.md`|
|modifier|modifier that identifies a 'tag'|`@@`|No|`@@`

# How to use

Given the default modifier and file extension to use, you might list files with tags specifying the `modifier`:

```
$ nt list
Listing all tags:
   1 golang                           2 programming                      1 python
```

To search for files with an existing tag:

```
$ nt search programming
Searching for tag containing: "programming"
/home/Username/notebook/golang-basic-syntax.md                            TAGS:  golang programming
/home/Username/notebook/argparse-behavioral-notes.md                      TAGS:  python programming
```

You may want to search for a tag without knowing the full tag, using a substring match:

```
$ nt search py
Searching for tag containing: "py"
/home/Username/notebook/argparse-behavioral-notes.md                      TAGS:  python programming
```

Tags might be newline separated, or on the same line, or even inline with notes:

```
$ tail -1 /home/Username/notebook/argparse-behavioral-notes.md
@@python @@programming

$ tail -2 /home/Username/notebook/golang-basic-syntax.md
@@golang
@@programming
```
