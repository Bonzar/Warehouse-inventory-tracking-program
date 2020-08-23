from WarehouseCode import *
from json import load

print("""
    Welcome to the office equipment accounting program.
    ------------------------------------------------------
    We have 4 type's of equipment:
        -Printer(PR)
        -Scanner(SC)
        -PrinterScanner(PS)
        -Xerox(XE)
    You can add and del certain types of office equipment
    with a specific firm model and properties different
    for each type of equipment.
    ------------------------------------------------------
    Specification for models:
        First 2 symbols - abbreviation of Name office equipment
        For Scanner - after the abbreviation should be number - version of scanner
        For Printer - in the end of model should be a letter (b/c) that mean type of painting (Black&White / RGB)
        For PrinterScanner both of the top.""")

while True:
    command = input('\n''Enter a command: ').title()
    if command == 'Help':
        print('Available command:\n'
              '-Help (list of available commands)\n'
              '-Add (add equipment to warehouse)\n'
              '-Del (del equipment from warehouse)\n'
              '-List (display the contents of the warehouse)\n'
              '-Default (reset the contents of the warehouse)')
    elif command == 'Add':
        equipment = input(
            'Choice equipment:\n'
            '-Printer(PR)\n'
            '-Scanner(SC)\n'
            '-PrinterScanner(PS)\n'
            '-Xerox(XE)\n:'
        ).title()
        if equipment == 'Back':
            continue
        firm = input('Firm: ')
        model = input('Model: ')
        cost = int(input('Cost: '))
        if equipment == 'Printer' or equipment == 'Pr':
            p = Printer(model, firm, cost)
            Printer.add_printer(p)
        elif equipment == 'Scanner' or equipment == 'Sc':
            s = Scanner(model, firm, cost)
            Scanner.add_scanner(s)
        elif equipment == 'Printerscanner' or equipment == 'Ps':
            ps = PrinterScanner(model, firm, cost)
            PrinterScanner.add_printer_scanner(ps)
        elif equipment == 'Xerox' or equipment == 'Xe':
            x = Xerox(model, firm, cost)
            Xerox.add_xerox(x)
    elif command == 'Del':
        equipment = input(
            'Choice equipment:\n'
            '-Printer(PR)\n'
            '-Scanner(SC)\n'
            '-PrinterScanner(PS)\n'
            '-Xerox(XE)\n:'
        ).title()
        if equipment == 'Back':
            continue
        if equipment == 'Printer' or equipment == 'Pr':
            print('Models on warehouse:')
            if len(Warehouse.list_equipment['Printer']):
                for i in range(len(Warehouse.list_equipment['Printer'])):
                    print(Warehouse.list_equipment["Printer"][i]["model"])
            else:
                print('Nothing to delete!')
                continue
            model = input('Enter model: ')
            p = Printer(model)
            Printer.del_printer(p)
        elif equipment == 'Scanner' or equipment == 'Sc':
            print('Models on warehouse:')
            if len(Warehouse.list_equipment['Scanner']):
                for i in range(len(Warehouse.list_equipment['Scanner'])):
                    print(Warehouse.list_equipment["Scanner"][i]["model"])
            else:
                print('Nothing to delete!')
                continue
            model = input('Enter model: ')
            s = Scanner(model)
            Scanner.del_scanner(s)
        elif equipment == 'Printerscanner' or equipment == 'Ps':
            print('Models on warehouse:')
            if len(Warehouse.list_equipment['PrinterScanner']):
                for i in range(len(Warehouse.list_equipment['PrinterScanner'])):
                    print(Warehouse.list_equipment["PrinterScanner"][i]["model"])
            else:
                print('Nothing to delete!')
                continue
            model = input('Enter model: ')
            p = PrinterScanner(model)
            PrinterScanner.del_printer_scanner(p)
        elif equipment == 'Xerox' or equipment == 'Xe':
            print('Models on warehouse:')
            if len(Warehouse.list_equipment['Xerox']):
                for i in range(len(Warehouse.list_equipment['Xerox'])):
                    print(Warehouse.list_equipment["Xerox"][i]["model"])
            else:
                print('Nothing to delete!')
                continue
            model = input('Enter model: ')
            x = Xerox(model)
            Xerox.del_xerox(x)
    elif command == 'Default':
        Warehouse.default()
    elif command == 'Exit':
        raise SystemExit
    elif command == 'List':
        with open('WarehouseList.json', 'r', encoding='utf-8') as List:
            print(List.read())
