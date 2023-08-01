# bulkrenamer

## What is this?
This is a small personal script to rename my film photo scan files into a format I like. 

## HowTo
For me personally, I presort the pictures after scanning into '01.jpg', '02.jpg' etc. in the order they were taken.

Call this script with 3 arguments:
1. Path to the folder where your photos are located
2. Name of the filmstock
3. Number of the filmstock

Example:

`python3 bulkrenamer.py /home/user/Pictures/to_sort/ TMax400 01`

This will result in the output files looking like "2023-08-01-TMax400-01-01.jpg"
