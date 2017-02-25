#!/bin/bash

articles=$(ls | head -n 100)
zip -xi corpus-reuters $articles
#for article in $(ls | head -n 100); do

