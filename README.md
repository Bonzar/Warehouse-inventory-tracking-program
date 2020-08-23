# Warehouse-inventory-tracking-program
Model for keeping records of office equipment inventory in warehause.

## Description
This project I did as a course in the course of training.
The model is a command-line program in which you can add and del certain types of office equipment
with a specific firm model and properties different for each type of equipment.

### Types of equipment:
  - Printer (PR)
  - Scanner (SC)
  - PrinterScanner (PS)
  - Xerox (XE)

### Specification for adding models:
  - *First 2 symbols* - abbreviation of Name office equipment
  - *For Scanner* - after the abbreviation should be number - version of scanner
  - *For Printer* - in the end of model should be a letter (b/c) that mean type of painting (Black&White / RGB)
  - *For PrinterScanner* - both of the top.
  
  Example for a scanner printer: **PS2_2Hfb3C**, where "2" (after the abbreviation) indicates the scanner version, and "C" at the end indicates the RGB printer

## Avaible commands:
  - `add` - adding a new model of equipment or adding the number of existing ones.
  - `del` - deleting a certain number of models from the warehouse
  - `list` - view all equipment records in the warehouse in JSON format
  - `help` - list of available commands with a description
  - `exit` - exit the program
  - `default` - clearing the **ENTIRE** warehouse of **ALL** records

## Program start:
1. Log in to the command prompt.
2. Select the python interpreter (the program is written in python 3.8) and run the file using it 'WarehousePlay.py':

- `$ python3 WarehousePlay.py`

## File's
- *WarehousePlay.py* - for to start the program (script for managing all program components).
- *WarehouseList.json* - contains all records of equipment in the warehouse.
- *WarehouseCode.py* - all program components (functions, classes, etc.)
