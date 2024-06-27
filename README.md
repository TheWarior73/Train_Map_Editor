# Train Map Editor
A custom map editor for train networks !

# Table of content :

- [How to use](#how-to-use)
- [Purpose](#purpose)
- [Planned Features](#planned-features)
- [Todo](#todo)
- [Software Licence](#licence)


# How to use

Run the app.py script\
(should have all the other scripts in the directory too for now)

> [!IMPORTANT]
> This software uses PyQt6, a python library.\
> In this software, PyQt6 is in `Version: 6.6.1`\
> The python Interpreter is in `-v 3.9.12`, if you are using another version the software may not work as intended.

> [!WARNING] 
> Authors of the software canot be blamed if the software is not running as expected. Especially if the above versions are not met


# Purpose
I am developing and supporting this editor to enable myself and other users to create and edit train network maps.

It will be similar to the `Tenessine Metro MapMaker` (which inspired me for this project), but with more freedom because I felt too restricted when using it.
I want more flexibility with where I can display my station names, types, fonts sizes, legend display etc.

# Planned Features
I am planning on adding the following features to the train map editor:
- Loading/Saving network map 
- Being able to edit the map
- Being able to create a map
- Being able to change map style easily (TBD if set styles or if custom)
- Let the user be as free as possible with their map
- Add some tools to help building the map
- A proper GUI and toolbars etc.

# Todo
> [!NOTE]
> List may (and will) be subject to changes

- [ ] Backend
  - [x] Load/Save system
  - [x] Network 
  - [x] Network Editing (methods)
  - [ ] Network Editing (when given data, edit it)

- [ ] GUI
  - [ ] Map editing
  - [ ] Map creation
  - [ ] Building tools
  - [ ] Map styling
- [ ] Bug hunting

- [x] Redirect Help (F1) to actual GitHub repo

- [ ] Add light/Dark mode for the app `var.setProprety("class", " ")`

# Licence
> For the full version, visit the [LICENCE](LICENSE) file

MIT License

Copyright (c) 2024 Th3_Warior
