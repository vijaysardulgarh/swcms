#!/bin/bash



# Add all changes to the staging area
git add .

# Commit changes with a commit message
git commit -m "SIMS Update"

# Push changes to the remote repository (assuming the remote name is origin and the branch is main)
git push origin main
