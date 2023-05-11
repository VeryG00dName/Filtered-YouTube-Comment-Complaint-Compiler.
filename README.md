# YouTube Common Complaints Analyzer

This repository contains a Python script that analyzes YouTube comments for a specific video and generates a list of common complaints along with their frequency. The script utilizes the YouTube Data API and the OpenAI ChatCompletion model to retrieve comments, filter relevant ones, and extract common complaints.

## Features

- Retrieve comments for a specified YouTube video using the YouTube Data API.
- Filter relevant comments based on predefined keywords.
- Extract common complaints from the relevant comments using the OpenAI ChatCompletion model.
- Print the list of common complaints along with their frequency.

## Examples of output.
1. Complaint about missing the old days of gameplay (mentioned twice)
2. Complaint about current state of gameplay and nerfs (mentioned four times)
3. Complaint about specific killer's strength or weakness (mentioned six times for Trapper, Pig, Wraith, Nurse, Freddy, and Doctor)
4. Complaint about the survivor's tactics and behavior (mentioned twice)
5. Complaint about the developer's decision and action (mentioned three times)
6. Unfair gameplay elements such as insta-mori without hooking, insta-heal mid chase, and BNP's that instantly complete a gen
7. Decisive Strike being too powerful with no prerequisite
8. Certain killers being too weak or strong, such as Pig being unplayable on certain maps and Myers needing more power
9. BHVR's inconsistency in balancing killers on release vs fixing/nerfing later
10. The removal of pallet vacuum, which some players believe was a better state for survivors and allowed for more precise loops.

## Purpose
This is a very rough proof of concept for demonstration purposes.
