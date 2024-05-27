"""
Tests For The Grayscale Image Conversion Script

This script tests the functions made for the grayscale algorithm with
series of different scenarios.
"""

from grayscaling import grayscaling, isGrayscale, resizeImage, MAX_WIDTH, MAX_HEIGHT
import cv2 as cv
import os

# Folder path for the sample images
sampleFolderRoute = "test-samples/"

count = 0

# Test 1 - Valid jpg file format
filename = "mushoku-tensei.jpg"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is not None:
    grayscaleImage = grayscaling(img)
    grayscalePath = os.path.join(sampleFolderRoute, "mushoku-tensei-grayscale.jpg")
    cv.imwrite(grayscalePath, grayscaleImage)
    print("Test 1 passed")
    count += 1
else:
    print("Test 1 not passed")

# Test 2 - Valid jpeg file format
filename = "sunset-background.jpeg"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is not None:
    grayscaleImage = grayscaling(img)
    grayscalePath = os.path.join(sampleFolderRoute, "sunset-background-grayscale.jpeg")
    cv.imwrite(grayscalePath, grayscaleImage)
    print("Test 2 passed")
    count += 1
else:
    print("Test 2 not passed")

# Test 3 - Valid png file format
filename = "Sekiro.png"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is not None:
    grayscaleImage = grayscaling(img)
    grayscalePath = os.path.join(sampleFolderRoute, "Sekiro-grayscale.png")
    cv.imwrite(grayscalePath, grayscaleImage)
    print("Test 3 passed")
    count += 1
else:
    print("Test 3 not passed")

# Test 4 - Invalid file format (avif)
filename = "galactic-night.avif"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is None:
    print("Test 4 passed")
    count += 1
else:
    print("Test 4 not passed")

# Test 5 - Incredibly large image
filename = "SAO.jpg"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is not None:
    maxWidth = MAX_WIDTH
    maxHeight = MAX_HEIGHT
    grayscaleImage = resizeImage(grayscaling(img), maxWidth, maxHeight)
    grayscalePath = os.path.join(sampleFolderRoute, "SAO-grayscale.jpg")
    cv.imwrite(grayscalePath, grayscaleImage)
    print("Test 5 passed")
    count += 1
else:
    print("Test 5 not passed")

# Test 6 - Image already grayscaled
filename = "Sekiro-grayscale.png"
img = cv.imread(cv.samples.findFile(sampleFolderRoute + filename))
if img is not None and isGrayscale(img):
    print("Test 6 passed")
    count += 1
else:
    print("Test 6 not passed")

print("Passed", count, "of 6 tests")