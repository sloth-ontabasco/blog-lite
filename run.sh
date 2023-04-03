#!/bin/bash
gnome-terminal -- python3 BE/main &
cd frontend
gnome-terminal -- npm run serve &