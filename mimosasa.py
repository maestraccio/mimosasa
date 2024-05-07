#!/usr/bin/python3
import pathlib, os, ast, calendar, textwrap, random, shutil
from time import sleep
from datetime import datetime, date, timedelta
os.chdir(os.path.dirname(os.path.realpath(__file__)))
versie = "0.0.27"
versiedatum = "20240507"
nu = datetime.now()
nustr = datetime.strftime(nu,"%Y%m%d")
w = 80
K = ""
fornum = "{0:>8.2f}".format
forni = fornum
forno = fornum
forl2 = "{:<2}".format
forc3 = "{:^3}".format
forl3 = "{:<3}".format
forr3 = "{:>3}".format
forl4 = "{:<4}".format
forr4 = "{:>4}".format
forc5 = "{:^5}".format
forr5 = "{:>5}".format
forr6 = "{:>6}".format
forc7 = "{:^7}".format
forl8 = "{:<8}".format
forc8 = "{:^8}".format
forc9 = "{:^9}".format
forr8 = "{:>8}".format
forc10 = "{:^10}".format
forc11 = "{:^11}".format
forl11 = "{:<11}".format
forl12 = "{:<12}".format
forr14 = "{:>14}".format
forc15 = "{:^15}".format
forl15 = "{:<15}".format
forr15 = "{:>15}".format
forc17 = "{:^17}".format
forc20 = "{:^20}".format
forl20 = "{:<20}".format
forr20 = "{:>20}".format
forc21 = "{:^21}".format
forl25 = "{:<25}".format
forr25 = "{:>25}".format
forl29 = "{:<29}".format
forr30 = "{:>30}".format
forc33 = "{:^33}".format
forc34 = "{:^34}".format
forl34 = "{:<34}".format
forl35 = "{:<35}".format
forr35 = "{:>35}".format
forc78 = "{:^78}".format
forcw = ("{:^%s}" % w).format
forlw = ("{:<%s}" % w).format
forrw = ("{:>%s}" % w).format
lijst = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
huishoudelijkelijst = ["A","B","C","D","E","F","O"]
zakelijkelijst = ["0","1","2","3","4","5","6","7","8","9"]
afsluitlijst = ["Q","X",":Q"]
taallijst = [
    "NL",
    "EN",
    "IT"
    ]
taaldict = {
    taallijst[0]: "Nederlands",
    taallijst[1]: "English",
    taallijst[2]: "Italiano"
    }
jalijst = [">","]",")","}"]
neelijst = ["<","[","(","{"]
inputindent = "  : "
endederror = afsluitlijst[0]
standaardstartdatum = 11111111
standaardeinddatum = 99991231
standaardbodembedrag = -9999999.99
standaardtopbedrag = 9999999.99
budgetnul = 0.0001
oepsEN = "Oops, something went wrong"
oepsIT = "Ups, qualcosa è andato storto"
oeps = "Oeps, daar ging wat mis"
woordcategorieEN = "Category"
woordcategorieIT = "Categoria"
woordcategorie = "Categorie"
woordtransactieEN = "Transaction"
woordtransactieIT = "Transazione"
woordtransactie = "Transactie"
geenspaarpottenEN = "There are no savings pots (yet)"
geenspaarpottenIT = "Non ci sono (ancora) salvadanai"
geenspaarpotten = "Er zijn (nog) geen spaarpotten"

lijn = "|"+78*"-"+"|"
toplijn = "+"+78*"-"+"+"
tweehalvelijnen = "|"+38*"-"+"||"+38*"-"+"|"
tweehalvetoplijnen = "+"+38*"-"+"++"+38*"-"+"+"
scheidtransactielijn = "-"*23+"+"+"-"*23
opmaakdatumlijst = [
        "YYYYMMDD",
        "DDMMYYYY",
        "YY-MM-DD",
        "DD-MM-YY",
        "DD/MM/YY",
        "DD-mmmYY",
        "DDmmm\'YY"
        ]
elementenEN = [
        "Date",
        "Amount",
        "Counterparty",
        "Reference"
        ]
elementenIT = [
        "Data",
        "Importo",
        "Controparte",
        "Riferimento"
        ]
elementen = [
        "Datum",       # 0
        "Bedrag",      # 1
        "Wederpartij", # 2
        "Onderwerp"    # 3
        ]
nieuwheaderlijstEN = [
        "Account name",
        "Account holder",
        "Active account",
        "Language",
        "Currency",
        "Opening balance",
        "Show total balance on start screen",
        "Marking Lower >< Higher",
        "Show zero lines at totals",
        "Date format",
        "Color scheme",
        "Level of menu expansion",
        "Print monthly overview to file",
        "Export everything to CSV file",
        "Tip of the day"
        ]
nieuwheaderlijstIT = [
        "Nome del conto",
        "Titolare del conto",
        "Conto attivo",
        "Lingua",
        "Valuta",
        "Saldo iniziale",
        "Mostra saldo totale nella schermata iniziale",
        "Indicazione Inferiore >< Superiore",
        "Righe vuote nei totali",
        "Formato data",
        "Schema di colori",
        "Livello di espansione del menu",
        "Stampa riepilogo mensile su file",
        "Esporta tutto in file CSV",
        "Consiglio del giorno"
        ]
nieuwheaderlijst = [
        "Rekeningnaam",                      # 0
        "Rekeninghouder",                    # 1
        "Actieve rekening",                  # 2
        "Taal",                              # 3
        "Valuta",                            # 4
        "Startsaldo",                        # 5
        "Toon totaalsaldo op startscherm",   # 6
        "Markering Lager >< Hoger",          # 7
        "Nulregels bij totalen",             # 8
        "Datumformaat",                      # 9
        "Kleurenschema",                     # 10
        "Niveau van uitvouwen menu",         # 11
        "Print maandoverzicht naar bestand", # 12
        "Exporteer alles naar csv-bestand",  # 13
        "Tip van de dag"                     # 14
        ]

lijnlijstEN = [
        "ID",
        "Name",
        "Target",
        "Credit",
        "Spent",
        "Rest"
        ]
lijnlijstIT = [
        "ID",
        "Nome",
        "Obiettivo",
        "Credito",
        "Pagato",
        "Rimanente"
        ]
lijnlijst = [
        "ID",       # 0
        "Naam",     # 1
        "Doel",     # 2
        "Tegoed",   # 3
        "Betaald",  # 4
        "Rest"      # 5
        ]
nieuwheader = {
        nieuwheaderlijst[0]:"",
        nieuwheaderlijst[1]:"",
        nieuwheaderlijst[2]:">",
        nieuwheaderlijst[3]:"NL",
        nieuwheaderlijst[4]:"€",
        nieuwheaderlijst[5]:0.0,
        nieuwheaderlijst[6]:"<",
        nieuwheaderlijst[7]:[-100.00,100.00],
        nieuwheaderlijst[8]:"<",
        nieuwheaderlijst[9]:"YY-MM-DD",
        nieuwheaderlijst[10]:"Categorie",
        nieuwheaderlijst[11]:2,
        nieuwheaderlijst[12]:"<",
        nieuwheaderlijst[13]:"<",
        nieuwheaderlijst[14]:">"
        }
nieuwalternatievenamendictEN = {
        "0":"fixd ass/equity",
        "1":"cash (equiv.)",
        "2":"intermediary",
        "3":"inventory",
        "4":"expenses",
        "5":"cost centers",
        "6":"manufact.acc.",
        "7":"cost of goods",
        "8":"sales",
        "9":"private",
        "A":"income & buffer",
        "B":"fixed costs",
        "C":"groceries",
        "D":"travel & stay",
        "E":"medical",
        "F":"loans",
        "G":"",
        "H":"",
        "I":"",
        "J":"",
        "K":"",
        "L":"",
        "M":"",
        "N":"",
        "O":"other"
        }
nieuwalternatievenamendictIT = {
        "0":"attiv. fisse",
        "1":"dispon. liquide",
        "2":"conti intermedi",
        "3":"magazzino",
        "4":"costi",
        "5":"centri di costo",
        "6":"contiproduzione",
        "7":"costi vendute",
        "8":"ricavi",
        "9":"privato",
        "A":"reddito&buffer",
        "B":"costi fissi",
        "C":"spese",
        "D":"viaggioalloggio",
        "E":"medico",
        "F":"prestiti",
        "G":"",
        "H":"",
        "I":"",
        "J":"",
        "K":"",
        "L":"",
        "M":"",
        "N":"",
        "O":"altro"
        }
nieuwalternatievenamendict = {
        "0":"vaste act/pass.",
        "1":"vlotte act/pass",
        "2":"tussenrekening",
        "3":"voorraden",
        "4":"gemaakte kosten",
        "5":"kostenplaatsen",
        "6":"fabricagerek.",
        "7":"inkoopwaarde",
        "8":"omzet",
        "9":"privé",
        "A":"inkomen&buffer",
        "B":"vaste lasten",
        "C":"boodschappen",
        "D":"reis & verblijf",
        "E":"medisch",
        "F":"leningen",
        "G":"",
        "H":"",
        "I":"",
        "J":"",
        "K":"",
        "L":"",
        "M":"",
        "N":"",
        "O":"overig"
        }
menuEN = {
    "0": "Account management and help",
        "0,0": "Help",
        "0,1": "Manage account settings",
            "0,1,0": " Reset account settings",
            "0,1,1": " "+nieuwheaderlijstEN[0],
            "0,1,2": " "+nieuwheaderlijstEN[1], 
            "0,1,3": " "+nieuwheaderlijstEN[2],
            "0,1,4": " "+nieuwheaderlijstEN[3],
            "0,1,5": " "+nieuwheaderlijstEN[4],
            "0,1,6": " "+nieuwheaderlijstEN[5],
            "0,1,7": " "+nieuwheaderlijstEN[6],
            "0,1,8": " "+nieuwheaderlijstEN[7],
            "0,1,9": " "+nieuwheaderlijstEN[8],
            "0,1,10": " "+nieuwheaderlijstEN[9],
            "0,1,11": " "+nieuwheaderlijstEN[10],
            "0,1,12": " "+nieuwheaderlijstEN[11],
            "0,1,13": " "+nieuwheaderlijstEN[12],
            "0,1,14": " "+nieuwheaderlijstEN[13],
            "0,1,15": " "+nieuwheaderlijstEN[14],
        "0,2": "%s management" % woordcategorieEN,
            "0,2,1": " Add new %s" % woordcategorieEN.lower(),
            "0,2,2": " Modify %s name" % woordcategorieEN.lower(),
            "0,2,3": " Modify monthly budget",
            "0,2,4": " Delete %s" % woordcategorieEN.lower(),
            "0,2,5": " Household <> Business account / Reset",
            "0,2,6": " Reset standard category names",
        "0,3": "Add new account",
        "0,4": "Delete account",
        "0,5": "Transfer settings to another account",
    "1": " > Show < ",
        "1,0": "Collect and sort transactions",
            "1,0,1": " Sort by %s 1231 > 0101" % elementenEN[0].upper(),
            "1,0,2": " Sort by %s 0101 < 1231" % elementenEN[0].upper(),
            "1,0,3": " Sort by %s + > -" % elementenEN[1].upper(),
            "1,0,4": " Sort by %s - < +" % elementenEN[1].upper(),
            "1,0,5": " Sort by %s Z > A" % elementenEN[2].upper(),
            "1,0,6": " Sort by %s A < Z" % elementenEN[2].upper(),
            "1,0,7": " Sort by %s Z > A" % elementenEN[3].upper(),
            "1,0,8": " Sort by %s A < Z" % elementenEN[3].upper(),
        "1,1": "Collect transactions and display table",
        "1,2": "Show monthly total",
        "1,3": "View %ss in collection" % woordtransactieEN.lower(),
    "2": "Add %s" % woordtransactieEN.lower(),
        "2,1": "Add a new transaction to the account",
        "2,2": "Copy an existing transaction to today",
    "3": "Modify %s" % woordtransactieEN.lower(),
        "3,1": "Modify %s %s" % (woordtransactieEN.lower(),elementenEN[0]),
        "3,2": "Modify %s %s" % (woordtransactieEN.lower(),elementenEN[1]),
        "3,3": "Modify %s %s" % (woordtransactieEN.lower(),elementenEN[2]),
        "3,4": "Modify %s %s" % (woordtransactieEN.lower(),elementenEN[3]),
        "3,5": "Modify %s %s" % (woordtransactieEN.lower(),woordcategorieEN),
    "4": "Delete %s" % woordtransactieEN.lower(),
    "5": "Savings pots",
        "5,1": "View savings pots",
        "5,2": "Add new savings pot",
        "5,3": "Modify savings pot",
            "5,3,1": " Change savings pot #name",
            "5,3,2": " Change savings pot target value",
            "5,3,3": " Change savings pot credit",
            "5,3,4": " Change savings pot paid",
        "5,4": "Delete savings pot",
    "<": "Back",
    "Q": "Quit"
        }
menuIT = {
    "0": "Gestione account e aiuto",
        "0,0": "Aiuto",
        "0,1": "Gestire impostazioni account",
            "0,1,0": " Ripristina impostazioni",
            "0,1,1": " "+ nieuwheaderlijstIT[0],
            "0,1,2": " "+nieuwheaderlijstIT[1],
            "0,1,3": " "+nieuwheaderlijstIT[2],
            "0,1,4": " "+nieuwheaderlijstIT[3],
            "0,1,5": " "+nieuwheaderlijstIT[4],
            "0,1,6": " "+nieuwheaderlijstIT[5],
            "0,1,7": " "+nieuwheaderlijstIT[6],
            "0,1,8": " "+nieuwheaderlijstIT[7],
            "0,1,9": " "+nieuwheaderlijstIT[8],
            "0,1,10": " "+nieuwheaderlijstIT[9],
            "0,1,11": " "+nieuwheaderlijstIT[10],
            "0,1,12": " "+nieuwheaderlijstIT[11],
            "0,1,13": " "+nieuwheaderlijstIT[12],
            "0,1,14": " "+nieuwheaderlijstIT[13],
            "0,1,15": " "+nieuwheaderlijstIT[14],
        "0,2": "Gestione %s" % woordcategorieIT.lower(),
            "0,2,1": " Aggiundere nuova %s" % woordcategorieIT.lower(),
            "0,2,2": " Modificare nome %s" % woordcategorieIT.lower(),
            "0,2,3": " Modificare budget mensile",
            "0,2,4": " Eliminare %s" % woordcategorieIT.lower(),
            "0,2,5": " Conto domestico <> aziendale / Ripristina",
            "0,2,6": " Ripristina i nomi delle categorie standard",
        "0,3": "Aggiungere nuovo account",
        "0,4": "Eliminare account",
        "0,5": "Trasferire le impostazioni a un altro account",
    "1": " > Visualizzare < ",
        "1,0": "Collezionare e ordinare transazioni",
            "1,0,1": " Ordina per %s 1231 > 0101" % elementenIT[0].upper(),
            "1,0,2": " Ordina per %s 0101 < 1231" % elementenIT[0].upper(),
            "1,0,3": " Ordina per %s + > -" % elementenIT[1].upper(),
            "1,0,4": " Ordina per %s - < +" % elementenIT[1].upper(),
            "1,0,5": " Ordina per %s Z > A" % elementenIT[2].upper(),
            "1,0,6": " Ordina per %s A < Z" % elementenIT[2].upper(),
            "1,0,7": " Ordina per %s Z > A" % elementenIT[3].upper(),
            "1,0,8": " Ordina per %s A < Z" % elementenIT[3].upper(),
        "1,1": "Collezionare transazioni e visualizzare la tabella",
        "1,2": "Visualizzare totale mensile",
        "1,3": "Visualizzare transazioni in collezione",
    "2": "Aggiungere %s" % woordtransactieIT.lower(),
        "2,1": "Aggiungere una nuova transazione al conto",
        "2,2": "Copiare una transazione esistente su oggi",
    "3": "Modificare %s" % woordtransactieIT.lower(),
        "3,1": "Modificare %s %s" % (woordtransactieIT.lower(),elementenIT[0]),
        "3,2": "Modificare %s %s" % (woordtransactieIT.lower(),elementenIT[1]),
        "3,3": "Modificare %s %s" % (woordtransactieIT.lower(),elementenIT[2]),
        "3,4": "Modificare %s %s" % (woordtransactieIT.lower(),elementenIT[3]),
        "3,5": "Modificare %s %s" % (woordtransactieIT.lower(),woordcategorieIT),
    "4": "Eliminare %s" % woordtransactieIT.lower(),
    "5": "Contenitori di risparmio",
        "5,1": "Visualizzare contenitori di risparmio",
        "5,2": "Aggiungere nuovo contenitore di risparmio",
        "5,3": "Modificare contenitore di risparmio",
            "5,3,1": " Cambia salvadanaio #nome",
            "5,3,2": " Cambia salvadanaio obiettivo",
            "5,3,3": " Cambia salvadanaio credito",
            "5,3,4": " Cambia salvadanaio pagato",
        "5,4": "Eliminare contenitore di risparmio",
    "<": "Tornare",
    "Q": "Uscire"
        }
menu = {
    "0": "Rekeningbeheer en help",
        "0,0": "Help",
        "0,1": "Rekeninginstellingenbeheer",
            "0,1,0": " Reset rekeninginstellingen",
            "0,1,1": " "+nieuwheaderlijst[0],
            "0,1,2": " "+nieuwheaderlijst[1],
            "0,1,3": " "+nieuwheaderlijst[2],
            "0,1,4": " "+nieuwheaderlijst[3],
            "0,1,5": " "+nieuwheaderlijst[4],
            "0,1,6": " "+nieuwheaderlijst[5],
            "0,1,7": " "+nieuwheaderlijst[6],
            "0,1,8": " "+nieuwheaderlijst[7],
            "0,1,9": " "+nieuwheaderlijst[8],
            "0,1,10": " "+nieuwheaderlijst[9],
            "0,1,11": " "+nieuwheaderlijst[10],
            "0,1,12": " "+nieuwheaderlijst[11],
            "0,1,13": " "+nieuwheaderlijst[12],
            "0,1,14": " "+nieuwheaderlijst[13],
            "0,1,15": " "+nieuwheaderlijst[14],
        "0,2": "%sbeheer" % woordcategorie,
            "0,2,1": " Voeg nieuwe %s toe" % woordcategorie.lower(),
            "0,2,2": " %snaam wijzigen" % woordcategorie,
            "0,2,3": " Maandbudget wijzigen",
            "0,2,4": " %s verwijderen" % woordcategorie,
            "0,2,5": " Huishoudelijke <> Zakelijke rekening / Reset",
            "0,2,6": " Reset standaard categorienamen",
        "0,3": "Nieuwe rekening toevoegen",
        "0,4": "Rekening verwijderen",
        "0,5": "Instellingen overzetten naar andere rekening",
    "1": " > Weergeven < ",
        "1,0": "Verzamel en sorteer transacties",
            "1,0,1": " Sorteer op %s 1231 > 0101" % elementen[0],
            "1,0,2": " Sorteer op %s 0101 < 1231" % elementen[0],
            "1,0,3": " Sorteer op %s + > -" % elementen[1],
            "1,0,4": " Sorteer op %s - < +" % elementen[1],
            "1,0,5": " Sorteer op %s Z > A" % elementen[2],
            "1,0,6": " Sorteer op %s A < Z" % elementen[2],
            "1,0,7": " Sorteer op %s Z > A" % elementen[3],
            "1,0,8": " Sorteer op %s A < Z" % elementen[3],
        "1,1": "Verzamel transacties en toon tabel",
        "1,2": "Maandtotaal weergeven",
        "1,3": "Bekijk %ss in collectie" % woordtransactie.lower(),
    "2": "%s toevoegen" % woordtransactie,
        "2,1": "Voeg een nieuwe transactie aan de rekening toe",
        "2,2": "Kopieer een bestaande transactie naar vandaag",
    "3": "%s wijzigen" % woordtransactie,
        "3,1": "Wijzig %s%s" % (woordtransactie.lower(),elementen[0]),
        "3,2": "Wijzig %s%s" % (woordtransactie.lower(),elementen[1]),
        "3,3": "Wijzig %s%s" % (woordtransactie.lower(),elementen[2]),
        "3,4": "Wijzig %s%s" % (woordtransactie.lower(),elementen[3]),
        "3,5": "Wijzig %s%s" % (woordtransactie.lower(),woordcategorie),
    "4": "%s verwijderen" % woordtransactie,
    "5": "Spaarpotten",
        "5,1": "Bekijk spaarpotten",
        "5,2": "Voeg nieuwe spaarpot toe",
        "5,3": "Wijzig spaarpot",
            "5,3,1": " Wijzig spaarpot #naam",
            "5,3,2": " Wijzig spaarpot doelwaarde",
            "5,3,3": " Wijzig spaarpot tegoed",
            "5,3,4": " Wijzig spaarpot betaald",
        "5,4": "Verwijder spaarpot",
    "<": "Terug",
    "Q": "Afsluiten"
        }
helpmenuEN = {
    "0": textwrap.wrap("Version: %s, Date: %s \\\\ \"mimosasa\" is an app in which you can manage your expenses and savings in various bank accounts. It is written in Python by Maestraccio and is available for free download and use. \"mimosasa\" stands for \"Money In, Money Out: Spendings And Savings Aid\" and is the successor of \"mimo\". You can call up the relevant help article for many functions with \"H\". Choose \"<\" (or any other \"opening bracket\" like \"(\" or \"[\") to return to the main menu, or \"Q\" to exit the program entirely." % (versie,versiedatum),w),
        "0,0": textwrap.wrap("For each account, an \"account folder\" is created in the \"app folder\" where the various category files and a settings file are placed. The \"mimosasa\" app uses \"ID's\" to identify individual transactions. These transactions can then be displayed, modified, deleted, and so on. You can provide these \"ID's\" in CSV format (comma- or space-separated, for example \"A0,B1\") when requested. The account balance is divided into a \"buffer\" determined by the budgeting of the categories, \"credit\" allocated to the savings pots, and the remaining discretionary balance.",w),
        "0,1": textwrap.wrap("Here the account environment settings can be adjusted. Personalize the display to your own taste, and visually distinguish multiple accounts you manage to prevent mistakes. Set what you do and do not want to show, and whether you want to save overviews to your computer. Always enter amounts using a period \".\" as the decimal separator.",w),
            "0,1,0": textwrap.wrap("Reset the account settings to the default settings. This will place a new settings file in both the \"account folder\" and the \"app folder\".",w),
            "0,1,1": textwrap.wrap("Enter the name of the account here. This way, you can differentiate between multiple accounts you manage in the same app without having to memorize the long account numbers.",w),
            "0,1,2": textwrap.wrap("Enter the name of the account holder here.",w),
            "0,1,3": textwrap.wrap("Here you can only adjust the status of OTHER accounts. It is not possible to deactivate the - obviously active - account currently in use. Choose another account and indicate whether it is an \"active\" or an \"inactive\" account. Inactive accounts are, for example, archived or prepared accounts that are not shown in the overviews.",w),
            "0,1,4": textwrap.wrap("You can adjust the language of the app here. The transactions themselves are not translated, and personalized category names are not either, but all menus and commands are. At the moment, you can choose between \"NL\" (Dutch, default), \"EN\" (English), and \"IT\" (Italian).",w),
            "0,1,5": textwrap.wrap("You can assign the currency symbol here. You can choose any character, but make sure it is exactly one position wide on the screen.",w),
            "0,1,6": textwrap.wrap("Enter the initial balance of the account here from the moment before the first transaction took place. The app is essentially designed to open a new \"account\" in the app each year - although it is possible to continue through multiple years.",w),
            "0,1,7": textwrap.wrap("It is now possible to hide the account balance on the start screen - the default setting is now: \"%s : No\". If the setting is \"Yes\", the sum of multiple accounts - with matching currencies - is also displayed." % (nieuwheaderlijstEN[6]),w),
            "0,1,8": textwrap.wrap("In transactions, the currency symbol is emphasized below and above a threshold that you can determine yourself. By default, these thresholds are set to \"less than -100.00\" and \"greater than 100.00\". These amounts are also used as default values.",w),
            "0,1,9": textwrap.wrap("In the monthly overview, transactions are displayed per category. You can choose to show or hide unused categories in this overview.",w),
            "0,1,10": textwrap.wrap("The default date formatting is \"YYYYMMDD\" but not everyone finds that clear. Therefore, multiple display options have been added to make the date readable for you as well.",w),
            "0,1,11": textwrap.wrap("There are multiple color schemes available. Apart from being more pleasant to look at, this can be very useful if you work with multiple accounts and want to make a clear visual distinction.",w),
            "0,1,12": textwrap.wrap("You can choose the level at which the menu is displayed to you. The higher the value, the more menu options are expanded.",w),
            "0,1,13": textwrap.wrap("The displayed monthly totals can also be saved as a plain text file. To avoid having to choose every time, you can set this as the default here or turn it off. You will find these files in the \"account folder\" with the \"year+month\" (\"YYYYMM\") for the transactions, and as \"year+month+a\" (\"YYYYMMa\") for the budget analysis, without a file extension. These files are created if they do not exist yet, and otherwise overwritten each time. If necessary, you can manually add the file extension \".txt\", but then it will not be updated.",w),
            "0,1,14": textwrap.wrap("You can choose to save a csv file with all transactions from that account each time you close the app. You will find this csv file in the \"account folder\" as \"export.csv\". This file is created if it does not exist yet, and otherwise overwritten with fresh data.",w),
            "0,1,15": textwrap.wrap("At the start of the app, a random help article can be shown as the \"Tip of the day\". This can be useful, especially in the beginning, to familiarize yourself with the functionalities. This can be turned on or off here.",w),
        "0,2": textwrap.wrap("Here you can adjust the names of different categories, allocate budgets, and more. Categories where money comes in (monthly) are assigned a negative budget, which is used as a buffer at the beginning of a new month. In the monthly analysis, the balance booked on those categories is ignored until the buffer is reached.",w),
            "0,2,1": textwrap.wrap("Add a new category. Business accounts contain standard ledgers \"%s\" through \"%s\", household accounts the categories \"%s\" through \"%s\" and \"%s\", but all intermediate letters can be used, and all those letters and numbers can also be exchanged between business and household accounts." % (zakelijkelijst[0],zakelijkelijst[-1],huishoudelijkelijst[0],huishoudelijkelijst[5],huishoudelijkelijst[-1]),w),
            "0,2,2": textwrap.wrap("Initially, standard names are assigned to the categories, but you can adjust them here as desired. The default categories for business accounts are: 0: %s, 1: %s, 2: %s, 3: %s, 4: %s, 5: %s, 6: %s, 7: %s, 8: %s, 9: %s, and for household accounts (standard): A: %s, B: %s, C: %s, D: %s, E: %s, F: %s, O: %s. All these standard category names are automatically translated from Dutch (the default language) to other languages when you switch languages, but not if you have adjusted a category name yourself." % (nieuwalternatievenamendictEN[zakelijkelijst[0]],nieuwalternatievenamendictEN[zakelijkelijst[1]],nieuwalternatievenamendictEN[zakelijkelijst[2]],nieuwalternatievenamendictEN[zakelijkelijst[3]],nieuwalternatievenamendictEN[zakelijkelijst[4]],nieuwalternatievenamendictEN[zakelijkelijst[5]],nieuwalternatievenamendictEN[zakelijkelijst[6]],nieuwalternatievenamendictEN[zakelijkelijst[7]],nieuwalternatievenamendictEN[zakelijkelijst[8]],nieuwalternatievenamendictEN[zakelijkelijst[9]],nieuwalternatievenamendictEN[huishoudelijkelijst[0]],nieuwalternatievenamendictEN[huishoudelijkelijst[1]],nieuwalternatievenamendictEN[huishoudelijkelijst[2]],nieuwalternatievenamendictEN[huishoudelijkelijst[3]],nieuwalternatievenamendictEN[huishoudelijkelijst[4]],nieuwalternatievenamendictEN[huishoudelijkelijst[5]],nieuwalternatievenamendictEN[huishoudelijkelijst[6]]),w),
            "0,2,3": textwrap.wrap("Each expenditure category contains a positive disposable budget, and the categories where the money comes in a negative one (which is used as a buffer). Ensure that the overall balance is always exactly zero (\"0.0\").",w),
            "0,2,4": textwrap.wrap("Keep in mind that by removing a category, you will also delete all transactions assigned to this category! Make sure the category is empty (use function \"3,5\" if necessary) before using this function. In many cases, this is not necessary; you can optionally hide unused categories with option \"0,1,9\".",w),
            "0,2,5": textwrap.wrap("You can delete all transactions by resetting the categories, replacing household categories (%s to %s) with business ones (%s to %s), or vice versa." % (huishoudelijkelijst[0],huishoudelijkelijst[-1],zakelijkelijst[0],zakelijkelijst[-1]),w),
            "0,2,6": textwrap.wrap("You can reset any personalized category names back to the standard category names here.",w),
        "0,3": textwrap.wrap("In \"mimosasa\" you can manage multiple accounts. Add a new account here.",w),
        "0,4": textwrap.wrap("You can delete accounts completely. Note: this is irreversible: once it's gone, it's gone!",w),
        "0,5": textwrap.wrap("You can transfer the account settings from one account to another. This is particularly useful when creating a \"new account\" for a new year and wanting to retain the old settings.",w),
    "1": textwrap.wrap("View individual transactions in detail, create filtered overviews, analyze your income and expenses. To start, the daily balance is displayed, along with the monthly score per category.",w),
        "1,0": textwrap.wrap("Gather multiple transactions per \"ID\" or delete the previously created collection without showing the transactions. The selected transactions can then be sorted in ascending or descending order on each element. By default, no sorting is applied; the transactions are initially invoked in the order in which the \"ID's\" are specified. For efficient use, it is advised to keep the list short and clear.",w),
            "1,0,1": textwrap.wrap("The collection is sorted by %s, with the latest transaction at the front." % elementenEN[0].lower(),w),
            "1,0,2": textwrap.wrap("The collection is sorted by %s, with the first transaction at the front." % elementenEN[0].lower(),w),
            "1,0,3": textwrap.wrap("The collection is sorted by %s, with the transaction with the highest amount at the front." % elementenEN[1].lower(),w),
            "1,0,4": textwrap.wrap("The collection is sorted by %s, with the transaction with the lowest amount at the front." % elementenEN[1].lower(),w),
            "1,0,5": textwrap.wrap("The collection is sorted alphabetically from Z to A based on %s." % elementenEN[2].lower(),w),
            "1,0,6": textwrap.wrap("The collection is sorted alphabetically from A to Z based on %s." % elementenEN[2].lower(),w),
            "1,0,7": textwrap.wrap("The collection is sorted alphabetically from Z to A based on %s." % elementenEN[3].lower(),w),
            "1,0,8": textwrap.wrap("The collection is sorted alphabetically from A to Z based on %s." % elementenEN[3].lower(),w),
        "1,1": textwrap.wrap("Select transactions based on various criteria (%s, %s, %s, %s and %s) and generate a clear table. You can use \"keyboard shortcuts\", or specify each element individually. The possible \"keyboard shortcuts\" are displayed; it is possible to add a number to \"M\" (month) or \"W\" (week): \"0\" includes today. All selected transactions are also collected in the collection, which is always displayed above the selection menu. If the selection covers one day, the daily total for that day is shown." % (elementenEN[0].lower(),elementenEN[1].lower(),elementenEN[2].lower(),elementenEN[3].lower(),woordcategorieEN.lower()),w),
        "1,2": textwrap.wrap("Show the budget analysis of one month. By default, the current month is displayed. You will see the progress of each category compared to the assigned budget, and the monthly performance.",w),
        "1,3": textwrap.wrap("Show the details of individual transactions in the collection. The number of characters in \"%s\" and \"%s\" is unlimited but is truncated in the table. All additional information is expanded here." % (elementenEN[2].lower(),elementenEN[3].lower()),w),
    "2": textwrap.wrap("You can add new transactions to your account, and assign each one to a category. You can enter a new transaction per element or consecutively on one line in CSV style, or you can make a copy of a previous transaction and later adjust the details using the options under \"3\". New transactions are immediately added to the collection, so you can view or modify them right away.",w),
        "2,1": textwrap.wrap("Add a new transaction to your account here. You can enter the elements step by step, or - for the more experienced user - consecutively on one line in CSV style: \"%s,%s,%s,%s,%s\". Therefore, you cannot use a comma (\",\") in any element. Always use a period (\".\") as the decimal separator. If the CSV input contains invalid data, the step-by-step input takes over." % (elementenEN[0].lower(),elementenEN[1].lower(),elementenEN[2].lower(),elementenEN[3].lower(),woordcategorieEN.lower()),w),
        "2,2": textwrap.wrap("Make a copy of a previously entered transaction here and automatically replace the original date with today's date. You can use any transaction as a template to later adjust details with the options in menu \"3\". If a collection already exists, those transactions are offered one by one; otherwise, you will be asked to provide an \"ID\" - or more precisely: a list of \"ID's\" in the form of a CSV list. This is the recommended method for adding recurring transactions. Note: if you make an identical copy of a transaction earlier today, it will not be automatically added to the collection.",w),
    "3": textwrap.wrap("All elements of an existing transaction can be adjusted here. If a collection already exists, those transactions are offered one by one; otherwise, you will be asked to provide an \"ID\" - or more precisely: a list of \"ID's\" in the form of a CSV list.",w),
        "3,1": textwrap.wrap("Adjust the %s of the transaction. Enter the new date as \"YYYYMMDD\". The default date, for example if an invalid or incomplete date is entered, is today's date. Set the date format displayed in the table (\"1,1\") or the transaction display (\"1,3\") at \"0,1,10\"." % elementenEN[0],w),
        "3,2": textwrap.wrap("Adjust the %s of the transaction. Enter the amount without currency and with a period (\".\") as decimal separator. Set the currency symbol at \"0,1,5\"." % elementenEN[1],w),
        "3,3": textwrap.wrap("Adjust the %s of the transaction. This can be a debtor or a creditor, a customer or a supplier (store). The number of characters to use is free, but will be truncated in the table display (\"1,1\"). It is therefore wise to always start with a recognizable fragment, especially with longer descriptions." % elementenEN[2],w),
        "3,4": textwrap.wrap("Adjust the %s of the transaction. Here you provide a description of the content of this transaction, such as a billed service or a number of items purchased. You can also include payment references or invoice numbers here. The number of characters to use is free, but will be truncated in the table display (\"1,1\"). It is therefore wise to always start with a recognizable fragment, especially with longer descriptions." % elementenEN[3],w),
        "3,5": textwrap.wrap("Place a transaction in another category. Each transaction is assigned to a category to which a budget is allocated. These budgets are distributed in \"0,2,3\" and the progress can be seen per month in \"1,2\".",w),
    "4": textwrap.wrap("",w),
    "5": textwrap.wrap("The function %s is not ready yet." % menuEN["5"],w),
        "5,1": textwrap.wrap("The function %s is not ready yet." % menuEN["5,1"],w),
        "5,2": textwrap.wrap("The function %s is not ready yet." % menuEN["5,2"],w),
        "5,3": textwrap.wrap("The function %s is not ready yet." % menuEN["5,3"],w),
            "5,3,1": textwrap.wrap("The function %s is not ready yet." % menuEN["5,3,1"],w),
            "5,3,2": textwrap.wrap("The function %s is not ready yet." % menuEN["5,3,2"],w),
            "5,3,3": textwrap.wrap("The function %s is not ready yet." % menuEN["5,3,3"],w),
            "5,3,4": textwrap.wrap("The function %s is not ready yet." % menuEN["5,3,4"],w),
        "5,4": textwrap.wrap("The function %s is not ready yet." % menuEN["5,4"],w),
    "<": textwrap.wrap("Back to main menu",w), # Wordt nooit aangesproken
    "Q": textwrap.wrap("Quit app",w) # Wordt nooit aangesproken
        }
helpmenuIT = {
    "0": textwrap.wrap("Versione: %s, Data: %s \\\\ \"mimosasa\" è un'applicazione in cui è possibile gestire le spese e i salvadanai in vari conti bancari. È scritta in Python da Maestraccio ed è gratuita da scaricare e utilizzare. \"mimosasa\" sta per \"Money In, Money Out: Spendings And Savings Aid\" ed è il successore di \"mimo\". È possibile richiamare l'articolo di aiuto relativo a molte funzioni con \"H\". Scegli \"<\" (O qualsiasi altra \"parentesi aperta\" come \"(\" o \"[\") per tornare al menu principale, o \"Q\" per uscire completamente dal programma." % (versie,versiedatum),w),
        "0,0": textwrap.wrap("Per ogni conto viene creata una \"cartella conto\" nella \"cartella dell'app\" in cui vengono inseriti i vari file di categoria e un file con gli impostazioni del conto. L'app \"mimosasa\" utilizza gli \"ID\" per identificare le singole transazioni. Queste transazioni possono poi essere visualizzate, modificate, eliminate, ecc. È possibile fornire questi \"ID\" in formato CSV (separato da virgole o spazi, ad esempio \"A0, B1\") quando richiesto. Il saldo del conto viene suddiviso in un \"buffer\" determinato dalla pianificazione del bilancio delle categorie, \"credito\" assegnato ai salvadanai e il saldo residuo disponibile per la spesa libera.",w),
        "0,1": textwrap.wrap("In questa sezione è possibile modificare le impostazioni dell'ambiente conto. Personalizza la visualizzazione secondo i tuoi gusti e distingui visivamente più conti gestiti da te per evitare errori. Imposta cosa desideri visualizzare e come, e se desideri salvare riepiloghi sul tuo computer. Inserisci sempre gli importi con un punto \".\" come separatore decimale.",w),
            "0,1,0": textwrap.wrap("Ripristina le impostazioni del conto ai valori predefiniti. Verrà creato un nuovo file di impostazioni sia nella \"cartella conto\" che nella \"cartella dell'app\".",w),
            "0,1,1": textwrap.wrap("Inserisci qui il nome del conto. In questo modo puoi distinguere tra più conti gestiti nella stessa app senza dover imparare a memoria i lunghi numeri di conto.",w),
            "0,1,2": textwrap.wrap("Inserisci qui il nome del titolare del conto.",w),
            "0,1,3": textwrap.wrap("Qui puoi solo modificare lo stato di ALTRE conti. Non è possibile disattivare il conto attualmente in uso, che è ovviamente attivo. Seleziona un altro conto e specifica se si tratta di un conto \"attivo\" o \"non attivo\". I conti non attivi sono ad esempio conti archiviati o preparati che non vengono visualizzati negli elenchi.",w),
            "0,1,4": textwrap.wrap("Qui puoi modificare la lingua dell'app. Le transazioni stesse non vengono tradotte, così come i nomi personalizzati delle categorie, ma tutti i menu e i comandi sì. Al momento puoi scegliere tra \"NL\" (olandese, predefinito), \"EN\" (inglese) e \"IT\" (italiano).",w),
            "0,1,5": textwrap.wrap("Qui puoi assegnare il simbolo di valuta. Puoi scegliere qualsiasi carattere, ma assicurati che abbia una larghezza di esattamente una posizione nella visualizzazione dello schermo.",w),
            "0,1,6": textwrap.wrap("Inserisci qui il saldo iniziale sul conto dal momento prima che si verificasse la prima transazione. L'app è fondamentalmente progettata per aprire un nuovo \"conto\" ogni anno nell'app, anche se è possibile continuare per diversi anni.",w),
            "0,1,7": textwrap.wrap("È ora possibile nascondere il saldo del conto nella schermata iniziale: l'impostazione predefinita ora è: \"%s: No\". Se l'impostazione è \"Sì\", viene visualizzata anche la somma di più conti - con valute corrispondenti." % nieuwheaderlijstIT[6],w),
            "0,1,8": textwrap.wrap("Nelle transazioni, il simbolo della valuta viene enfatizzato ulteriormente sopra e sotto una soglia da voi stessi determinata. Di default, queste soglie sono impostate su \"inferiore a -100,00\" e \"superiore a 100,00\". Queste cifre vengono anche utilizzate come cifre standard.",w),
            "0,1,9": textwrap.wrap("Nella panoramica mensile vengono visualizzate le transazioni per categoria. È possibile scegliere di mostrare o nascondere le categorie non utilizzate in questa panoramica.",w),
            "0,1,10": textwrap.wrap("La visualizzazione predefinita della data è \"AAAAMMGG\" ma non tutti la trovano chiara. Sono state quindi aggiunte diverse opzioni di visualizzazione per rendere la data più facilmente leggibile anche per voi.",w),
            "0,1,11": textwrap.wrap("Sono disponibili diversi schemi di colori. Oltre a rendere più piacevole la vista, questo può essere molto utile se lavori su più conti e desideri fare una chiara distinzione visiva.",w),
            "0,1,12": textwrap.wrap("È possibile scegliere il livello in cui viene visualizzato il menu a tendina. Più alta è la valore, più opzioni di menu vengono espandete.",w),
            "0,1,13": textwrap.wrap("I totali mensili mostrati possono essere salvati anche come file di testo semplice. Per evitare di dover scegliere ogni volta, è possibile impostarlo o disattivarlo qui per impostazione predefinita. Troverete questi nella \"cartella del conto\" con l'anno e il mese (\"AAAAMM\") per le transazioni, e come \"anno+mese+a\" (\"AAAAMMa\") per l'analisi del budget, senza estensione del file. Questi file vengono creati se non esistono ancora, altrimenti vengono sovrascritti continuamente. Se necessario, è possibile aggiungere manualmente l'estensione del file \".txt\", ma in tal caso non verrà aggiornato.",w),
            "0,1,14": textwrap.wrap("È possibile scegliere di salvare sempre un file csv con tutte le transazioni di quel conto quando si chiude l'applicazione. Troverete questo file csv nella \"cartella del conto\" come \"export.csv\". Questo viene creato se non esiste ancora, altrimenti sovrascritto con nuovi dati.",w),
            "0,1,15": textwrap.wrap("All'avvio dell'app, può essere visualizzato un articolo casuale di aiuto come \"Suggerimento del giorno\". Questo può essere utile soprattutto all'inizio per familiarizzare con le funzionalità. È possibile attivarlo o disattivarlo qui.",w),
        "0,2": textwrap.wrap("Qui è possibile modificare il nome delle varie categorie, distribuire i budget, eccetera. Le categorie su cui entra denaro (mensilmente) ricevono un budget negativo, che viene utilizzato come buffer all'inizio di un nuovo mese. Nell'analisi mensile il saldo registrato su tali categorie viene ignorato fino a quando il buffer non è raggiunto.",w),
            "0,2,1": textwrap.wrap("Aggiungi una nuova categoria. I conti aziendali contengono di default i conti \"%s\" a \"%s\", i conti domestici le categorie \"%s\" a \"%s\" e \"%s\", ma tutte le lettere intermedie possono essere utilizzate, e tutte quelle lettere e numeri possono anche essere scambiati tra conti aziendali e domestici." % (zakelijkelijst[0],zakelijkelijst[-1],huishoudelijkelijst[0],huishoudelijkelijst[5],huishoudelijkelijst[-1]),w),
            "0,2,2": textwrap.wrap("Di base vengono assegnati nomi standard alle categorie, ma qui puoi modificarli a tuo piacimento. Le categorie standard per i conti aziendali sono: 0: %s, 1: %s, 2: %s, 3: %s, 4: %s, 5: %s, 6: %s, 7: %s, 8: %s, 9: %s, e per i conti domestici (standard): A: %s, B: %s, C: %s, D: %s, E: %s, F: %s, O: %s. Tutti questi nomi (standard olandesi) vengono tradotti quando si cambia lingua, ma non se hai personalizzato il nome di una categoria." % (nieuwalternatievenamendictIT[zakelijkelijst[0]],nieuwalternatievenamendictIT[zakelijkelijst[1]],nieuwalternatievenamendictIT[zakelijkelijst[2]],nieuwalternatievenamendictIT[zakelijkelijst[3]],nieuwalternatievenamendictIT[zakelijkelijst[4]],nieuwalternatievenamendictIT[zakelijkelijst[5]],nieuwalternatievenamendictIT[zakelijkelijst[6]],nieuwalternatievenamendictIT[zakelijkelijst[7]],nieuwalternatievenamendictIT[zakelijkelijst[8]],nieuwalternatievenamendictIT[zakelijkelijst[9]],nieuwalternatievenamendictIT[huishoudelijkelijst[0]],nieuwalternatievenamendictIT[huishoudelijkelijst[1]],nieuwalternatievenamendictIT[huishoudelijkelijst[2]],nieuwalternatievenamendictIT[huishoudelijkelijst[3]],nieuwalternatievenamendictIT[huishoudelijkelijst[4]],nieuwalternatievenamendictIT[huishoudelijkelijst[5]],nieuwalternatievenamendictIT[huishoudelijkelijst[6]]),w),
            "0,2,3": textwrap.wrap("Ogni categoria di spesa contiene un budget spendibile positivo, mentre le categorie in cui entra denaro hanno un budget negativo (utilizzato come buffer). Assicurati che il saldo complessivo sia sempre esattamente zero (\"0.0\").",w),
            "0,2,4": textwrap.wrap("Ricordati che eliminando una categoria elimini anche tutte le transazioni al suo interno! Assicurati che la categoria sia vuota (utilizza la funzione \"3,5\" se necessario) prima di utilizzare questa funzione. Spesso questo non è necessario; eventualmente puoi nascondere le categorie non utilizzate con l'opzione \"0,1,9\".",w),
            "0,2,5": textwrap.wrap("È possibile cancellare tutte le transazioni reimpostando le categorie, sostituendo le categorie domestiche (da %s a %s) con quelle aziendali (da %s a %s), o viceversa. In questo modo, anche i nomi delle categorie personalizzati vengono sostituiti con quelli standard." % (huishoudelijkelijst[0],huishoudelijkelijst[-1],zakelijkelijst[0],zakelijkelijst[-1]),w),
            "0,2,6": textwrap.wrap("Qui è possibile ripristinare i nomi delle categorie eventualmente personalizzati ai nomi delle categorie predefiniti.",w),
        "0,3": textwrap.wrap("In \"mimosasa\" è possibile gestire più account. Aggiungi qui un nuovo account.",w),
        "0,4": textwrap.wrap("È possibile eliminare completamente gli account. Attenzione: questo è irreversibile: via è via!",w),
        "0,5": textwrap.wrap("È possibile trasferire le impostazioni dell'account da un account all'altro. Questo è particolarmente utile quando si crea un \"nuovo account\" per un nuovo anno e si desidera mantenere le vecchie impostazioni.",w),
    "1": textwrap.wrap("Visualizza le singole transazioni in dettaglio, crea riepiloghi filtrati, analizza i tuoi guadagni e le tue spese. Per iniziare verrà mostrato il saldo giornaliero e il punteggio mensile per categoria.",w),
        "1,0": textwrap.wrap("Raccogli più transazioni per \"ID\" o cancella la raccolta creata in precedenza, senza mostrare le transazioni. Le transazioni selezionate possono poi essere ordinate in ordine crescente o decrescente su ciascun elemento. Per impostazione predefinita, non viene applicato alcun ordinamento; le transazioni vengono inizialmente richiamate nell'ordine in cui vengono specificati gli \"ID\". Per un uso efficiente, si consiglia di mantenere l'elenco breve e ordinato.",w),
            "1,0,1": textwrap.wrap("La collezione viene ordinata per %s, con l'ultima transazione in testa." % elementenIT[0].lower(),w),
            "1,0,2": textwrap.wrap("La collezione viene ordinata per %s, con la prima transazione in testa." % elementenIT[0].lower(),w),
            "1,0,3": textwrap.wrap("La collezione viene ordinata per %s, con la transazione di importo più alto in testa." % elementenIT[1].lower(),w),
            "1,0,4": textwrap.wrap("La collezione viene ordinata per %s, con la transazione di importo più basso in testa." % elementenIT[1].lower(),w),
            "1,0,5": textwrap.wrap("La collezione viene ordinata in ordine alfabetico da Z ad A per %s." % elementenIT[2].lower(),w),
            "1,0,6": textwrap.wrap("La collezione viene ordinata in ordine alfabetico da A ad Z per %s." % elementenIT[2].lower(),w),
            "1,0,7": textwrap.wrap("La collezione viene ordinata in ordine alfabetico da Z ad A per %s." % elementenIT[3].lower(),w),
            "1,0,8": textwrap.wrap("La collezione viene ordinata in ordine alfabetico da A ad Z per %s." % elementenIT[3].lower(),w),
        "1,1": textwrap.wrap("Seleziona transazioni basate su diversi criteri (%s, %s, %s, %s e %s) e genera una tabella ben organizzata. Puoi utilizzare \"scorciatoie da tastiera\", oppure specificare singolarmente tutti gli elementi. Le possibili \"scorciatoie da tastiera\" vengono mostrate; è possibile aggiungere un numero a \"M\" (mese) o \"W\" (settimana): \"0\" include oggi. Tutte le transazioni selezionate vengono anche raccolte nella collezione, che viene mostrata sempre sopra il menu a discesa. Se la selezione comprende un solo giorno, verrà mostrato il totale di quel giorno." % (elementenIT[0].lower(),elementenIT[1].lower(),elementenIT[2].lower(),elementenIT[3].lower(),woordcategorieIT.lower()),w),
        "1,2": textwrap.wrap("Mostra l'analisi del bilancio di un mese. Di default viene mostrato il mese corrente. Vedrai il progresso di ogni categoria rispetto al budget assegnato e le prestazioni mensili.",w),
        "1,3": textwrap.wrap("Mostra i dettagli delle singole transazioni nella collezione. Il numero di caratteri consentito in \"%s\" e \"%s\" è illimitato, ma nella tabella (\"1,1\") verranno tagliati e mostrati solo parzialmente. Tutte le informazioni in quei caratteri extra verranno comunque espansi qui." % (elementenIT[2].lower(),elementenIT[3].lower()),w),
    "2": textwrap.wrap("È possibile aggiungere nuove transazioni al proprio conto, assegnandole ciascuna a una categoria. Una nuova transazione può essere inserita per elemento o in successione su una singola riga in stile CSV, oppure è possibile creare una copia di una transazione precedente e modificare i dettagli successivamente con le opzioni sotto \"3\". Le nuove transazioni vengono aggiunte direttamente alla collezione, in modo da poterle visualizzare o modificare immediatamente.",w),
        "2,1": textwrap.wrap("Aggiungi qui una nuova transazione al tuo conto. Puoi inserire gli elementi passo dopo passo, o - per l'utente più esperto - uno di seguito all'altro su una riga in stile CSV: \"%s,%s,%s,%s,%s\". Pertanto, non è possibile utilizzare una virgola (\",\") in nessun elemento. Usa sempre un punto (\".\") come separatore decimale. Se l'input CSV contiene dati non validi, il metodo passo dopo passo prenderà il sopravvento." % (elementenIT[0].lower(),elementenIT[1].lower(),elementenIT[2].lower(),elementenIT[3].lower(),woordcategorieIT.lower()),w),
        "2,2": textwrap.wrap("Fai qui una copia di una transazione inserita in precedenza e sostituisci automaticamente la data originale con quella di oggi. Puoi usare ogni transazione come modello per modificarla in dettaglio più tardi con le opzioni nel menu \"3\". Se esiste già una collezione, tali transazioni verranno offerte una per una, altrimenti ti verrà chiesto di specificare un \"ID\" - o meglio: un elenco di \"ID\" nel formato di un elenco CSV. Questo è il metodo consigliato per aggiungere transazioni ricorrenti. Nota: se fai una copia identica di una transazione già oggi, questa non verrà aggiunta automaticamente alla collezione.",w),
    "3": textwrap.wrap("Tutti gli elementi di una transazione esistente possono essere modificati qui. Se esiste già una collezione, tali transazioni verranno offerte una per una, altrimenti ti verrà chiesto di specificare un \"ID\" - o meglio: una lista di \"ID\" sotto forma di lista CSV.",w),
        "3,1": textwrap.wrap("Modifica la data della transazione. Inserisci la nuova data come \"AAAAMMGG\". La data predefinita, ad esempio se viene inserita una data non valida o incompleta, è la data odierna. Puoi impostare il formato della data nella tabella (\"1,1\") o nella visualizzazione della transazione (\"1,3\") con \"0,1,10\".",w),
        "3,2": textwrap.wrap("Modifica l'importo della transazione. Inserisci l'importo senza valuta e utilizza un punto (\".\") come separatore decimale. Puoi impostare la valuta con \"0,1,5\".",w),
        "3,3": textwrap.wrap("Modifica la controparte della transazione. Può essere un debitore o un creditore, un cliente o un fornitore (negozio). Il numero di caratteri da utilizzare è libero, ma verrà abbreviato nella visualizzazione tabellare (\"1,1\"). È quindi consigliabile iniziare sempre con un frammento riconoscibile, specialmente per descrizioni più lunghe.",w),
        "3,4": textwrap.wrap("Modifica l'oggetto della transazione. Qui fornisci una descrizione del contenuto di questa transazione, come ad esempio un servizio fatturato o un insieme di articoli acquistati. Puoi includere anche informazioni di pagamento o numeri di fattura. Il numero di caratteri da utilizzare è libero, ma verrà abbreviato nella visualizzazione tabellare (\"1,1\"). È quindi consigliabile iniziare sempre con un frammento riconoscibile, specialmente per descrizioni più lunghe.",w),
        "3,5": textwrap.wrap("Sposta una transazione in un'altra categoria. Ogni transazione viene assegnata a una categoria a cui è associato un budget. Questi budget sono distribuiti in \"0,2,3\" e il progresso è visibile mensilmente in \"1,2\".",w),
    "4": textwrap.wrap("Qui puoi eliminare definitivamente singole transazioni. Se esiste già una collezione, queste transazioni vengono offerte una per volta; in caso contrario, ti verrà chiesto di specificare un \"ID\" - o meglio: una lista di \"ID\" sotto forma di un elenco CSV.",w),
    "5": textwrap.wrap("La funzione %s non è ancora completa." % menu["5"],w),
        "5,1": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,1"],w),
        "5,2": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,2"],w),
        "5,3": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,3"],w),
            "5,3,1": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,3,1"],w),
            "5,3,2": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,3,2"],w),
            "5,3,3": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,3,3"],w),
            "5,3,4": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,3,4"],w),
        "5,4": textwrap.wrap("La funzione %s non è ancora completa." % menu["5,4"],w),
    "<": textwrap.wrap("Ritorna al menu principale",w),
    "Q": textwrap.wrap("Esci dali'app",w)
        }
helpmenu = {
    "0": textwrap.wrap("Versie: %s, Datum: %s \\\\ \"mimosasa\" is een app waarin u in verschillende bankrekeningen uw uitgaven en spaarpotten kunt beheren. Het is geschreven in Python door Maestraccio en is gratis te downloaden en gebruiken. \"mimosasa\" staat voor \"Money In, Money Out: Spendings And Savings Aid\" en is de opvolger van \"mimo\". U kunt bij veel functies het betreffende helpartikel aanroepen met \"H\". Kies \"<\" (of ieder ander \"haakje-openen\" zoals \"(\" of \"[\") om terug te keren naar het hoofdmenu, of \"Q\" om het programma helemaal te verlaten." % (versie,versiedatum),w),
        "0,0": textwrap.wrap("Voor iedere rekening wordt in de \"appmap\" een \"rekeningmap\" aangemaakt waarin de verschillende categoriebestanden worden geplaatst. De app \"mimosasa\" gebruikt \"ID's\" om individuele transacties te identificeren. Deze transacties kunnen vervolgens worden weergegeven, gewijzigd, verwijderd, enzovoorts. U kunt deze \"ID's\" in CSV-formaat (komma- of spatiegescheiden, bijvoorbeeld \"A0,B1\") opgeven wanneer daarom gevraagd wordt. Het rekeningsaldo wordt verdeeld in een \"buffer\" die wordt bepaald door de budgettering van de categorieën, \"tegoed\" dat is toegewezen aan de spaarpotten, en het resterende vrij besteedbare saldo.",w),
        "0,1": textwrap.wrap("Hier kunnen de rekeningomgevingsinstellingen worden aangepast. Personaliseer de weergave naar eigen smaak, en onderscheid visueel meerdere door u beheerde rekeningen om vergissingen te voorkomen. Stel in wat u wel en hoe of niet wil tonen, en of u overzichten naar uw computer wilt opslaan. Geef bedragen altijd in met een punt \".\" als decimaalscheidingsteken.",w),
            "0,1,0": textwrap.wrap("Zet de rekeninginstellingen terug naar de standaardinstellingen. Hierbij wordt zowel een nieuw instellingenbestand in de \"rekeningmap\" als in de \"appmap\" geplaatst.",w),
            "0,1,1": textwrap.wrap("Voer hier de naam van de rekening in. U kunt zo onderscheid maken tussen meerdere rekeningen die u in dezelfde app beheert, zonder de lange rekeningnummers uit het hoofd te hoeven leren.",w),
            "0,1,2": textwrap.wrap("Voer hier de naam van de rekeninghouder in.",w),
            "0,1,3": textwrap.wrap("Hier kunt u alleen de status van ANDERE rekeningen aanpassen. Het is niet mogelijk om de - vanzelfsprekend actieve - rekening die nu in gebruik is te deactiveren. Kies een andere rekening en geef aan of het een \"actieve\" of een \"niet-actieve\" rekening betreft. Niet-actieve rekeningen zijn bijvoorbeeld gearchiveerde of voorbereide rekeningen, die niet in de overzichten worden getoond.",w),
            "0,1,4": textwrap.wrap("Hier kunt u de taal van de app aanpassen. De transacties zelf worden niet vertaald, en gepersonaliseerde namen van categorieën ook niet, maar alle menu's en opdrachten wel. Op dit moment kunt u kiezen tussen \"NL\" (Nederlands, standaard), \"EN\" (Engels) en \"IT\" (Italiaans).",w),
            "0,1,5": textwrap.wrap("Hier kunt u het valutasymbool toewijzen. U kunt ieder karakter kiezen, maar zorg ervoor dat het in de weergave op het scherm precies één positie breed is.",w),
            "0,1,6": textwrap.wrap("Voer hier het startsaldo op de rekening in van het moment vóórdat de eerste transactie plaatsvond. De app is in principe geschreven om ieder jaar in de app een nieuwe \"rekening\" te openen - hoewel het mogelijk is om meerdere jaren dóór te schrijven.",w),
            "0,1,7": textwrap.wrap("Het is nu mogelijk om het rekeningsaldo op het startscherm te verbergen - de standaardinstelling is nu :\"%s : Nee\". Als de instelling \"Ja\" is wordt van meerdere rekeningen - bij overeenkomstige valuta - ook de optelling weergegeven." % (nieuwheaderlijst[6]),w),
            "0,1,8": textwrap.wrap("In de transacties wordt het valutateken extra geaccentueerd onder en boven een door u zelf te bepalen grens. Standaard staan deze op \"lager dan -100.00\" en \"hoger dan 100.00\". Deze bedragen worden ook als standaarbedragen gebruikt bij het aanmaken o.",w),
            "0,1,9": textwrap.wrap("In het maandoverzicht worden de transacties per categorie weergegeven. U kunt ervoor kiezen niet-gebruikte categorieën niet in dit overzicht te tonen of te verbergen.",w),
            "0,1,10": textwrap.wrap("De standaard-datumweergave is \"JJJJMMDD\" maar niet iedereen vindt dat duidelijk. Er zijn daarom meerdere weergave-opties toegevoegd om de datum ook voor u duidelijk leesbaar te maken.",w),
            "0,1,11": textwrap.wrap("Er zijn meerdere kleurenschema's beschikbaar. Behalve aangenamer om naar te kijken kan dit goed van pas komen als u in meerdere rekeningen werkt en duidelijk visueel onderscheid wilt maken.",w),
            "0,1,12": textwrap.wrap("U kunt het niveau kiezen waarin het keuzemenu aan u wordt getoond. Hoe hoger de waarde, hoe meer menu-opties er worden uitgevouwd.",w),
            "0,1,13": textwrap.wrap("De getoonde maandtotalen kunt u ook als platte-tekstbestand opslaan. Om niet iedere keer te hoeven kiezen kunt u dat hier standaard instellen of uitzetten. U vindt deze dan in de \"rekeningmap\" met het \"jaartal+maand\" (\"JJJJMM\") voor de transacties, en als \"jaartal+maand+a\" (\"JJJJMMa\") voor de budgetanalyse, zonder bestandsextensie. Deze bestanden worden aangemaakt als ze nog niet bestaan, en anders steeds overschreven. U kunt hier zelf, indien nodig, handmatig de bestandsextensie \".txt\" achter zetten, maar dan zal het niet worden ververst.",w),
            "0,1,14": textwrap.wrap("U kunt ervoor kiezen om bij het afsluiten van de app steeds een csv-bestand op te slaan met alle transacties van die rekening erin. U vindt dit csv-bestand dan in de \"rekeningmap\" als \"export.csv\". Dit wordt aangemaakt als het nog niet bestaat, en anders overschreven met verse data.",w),
            "0,1,15": textwrap.wrap("Bij aanvang van de app kan steeds een willekeurig helpartikel als \"Tip van de dag\" worden getoond. Dat kan zeker in het begin handig zijn om kennis te maken met de functionaliteiten. Dit kan hier worden aan- of uitgezet.",w),
        "0,2": textwrap.wrap("Hier kunt u de naam van de verschillende categorieën aanpassen, budgetten verdelen, enzovoorts. De categorieën waarop (maandelijks) geld binnenkomt krijgen een negatief budget, dat als buffer wordt gebruikt bij aanvang van een nieuwe maand. In de maandanalyse wordt het saldo dat op die categorieën wordt ingeboekt genegeerd totdat de buffer is bereikt.",w),
            "0,2,1": textwrap.wrap("Voeg een nieuwe categorie toe. Zakelijke rekeningen bevatten standaard de grootboeken \"%s\" t/m \"%s\", huishoudelijke rekeningen de categorieën \"%s\" t/m \"%s\" en \"%s\", maar alle tussenliggende letters kunnen worden gebruikt, en al die letters en cijfers kunnen ook tussen zakelijke en huishoudelijke rekeningen worden uitgewisseld." % (zakelijkelijst[0],zakelijkelijst[-1],huishoudelijkelijst[0],huishoudelijkelijst[5],huishoudelijkelijst[-1]),w),
            "0,2,2": textwrap.wrap("Aan de categorieën worden in beginsel standaardnamen toegekend, maar u kunt die hier zelf naar wens aanpassen. De standaardcategorieën zijn voor zakelijke rekeningen: 0: %s, 1: %s, 2: %s, 3: %s, 4: %s, 5: %s, 6: %s, 7: %s, 8: %s, 9: %s, en voor huishoudelijke rekeningen (standaard): A: %s, B: %s, C: %s, D: %s, E: %s, F: %s, O: %s. Al deze (standaard Nederlandse) namen worden vertaald als u van taal wisselt, maar niet als u zelf een categorienaam heeft aangepast." % (nieuwalternatievenamendict[zakelijkelijst[0]],nieuwalternatievenamendict[zakelijkelijst[1]],nieuwalternatievenamendict[zakelijkelijst[2]],nieuwalternatievenamendict[zakelijkelijst[3]],nieuwalternatievenamendict[zakelijkelijst[4]],nieuwalternatievenamendict[zakelijkelijst[5]],nieuwalternatievenamendict[zakelijkelijst[6]],nieuwalternatievenamendict[zakelijkelijst[7]],nieuwalternatievenamendict[zakelijkelijst[8]],nieuwalternatievenamendict[zakelijkelijst[9]],nieuwalternatievenamendict[huishoudelijkelijst[0]],nieuwalternatievenamendict[huishoudelijkelijst[1]],nieuwalternatievenamendict[huishoudelijkelijst[2]],nieuwalternatievenamendict[huishoudelijkelijst[3]],nieuwalternatievenamendict[huishoudelijkelijst[4]],nieuwalternatievenamendict[huishoudelijkelijst[5]],nieuwalternatievenamendict[huishoudelijkelijst[6]]),w),
            "0,2,3": textwrap.wrap("Iedere uitgavencategorie bevat een positief besteedbaar budget, en de categorieën waar het geld binnenkomt een negatief (dat wordt gebruikt als buffer). Zorg ervoor dat de gehele balans altijd precies nul (\"0.0\") is.",w),
            "0,2,4": textwrap.wrap("Denk eraan dat u met het verwijderen van een categorie ook alle transacties erin verwijdert! Verzeker u ervan dat de categorie leeg is (gebruik de functie \"3,5\" indien nodig) voordat u deze functie gebruikt. In veel gevallen hoeft dit niet; u kunt eventueel niet-gebruikte categorieën verbergen met optie \"0,1,9\".",w),
            "0,2,5": textwrap.wrap("U kunt alle transacties wissen door de categorieën te resetten, huishoudelijke categorieën (%s t/m %s) vervangen door zakelijke (%s t/m %s), of vice versa. Hierbij worden ook de eventueel gepersonaliseerde categorienamen vervangen door de standaardnamen." % (huishoudelijkelijst[0],huishoudelijkelijst[-1],zakelijkelijst[0],zakelijkelijst[-1]),w),
            "0,2,6": textwrap.wrap("U kunt hier de eventueel gepersonaliseerde categorienamen terugzetten naar de standaard categorienamen.",w),
    "1": textwrap.wrap("Toon individuele transacties in detail, maak gefilterde samenvattingen, analyseer je inkomsten en uitgaven. Als eerste wordt het dagsaldo en de maandelijkse score per categorie getoond.",w),
        "1,0": textwrap.wrap("Verzamel transacties per \"ID\" of verwijder de eerder gemaakte verzameling, zonder die transacties weer te geven. De geselecteerde transacties kunnen vervolgens op elk element in oplopende of aflopende volgorde worden gesorteerd. Standaard wordt er geen sortering toegepast; de transacties worden in eerste instantie opgeroepen in de volgorde waarin de \"ID's\" zijn gespecificeerd. Voor efficiënt gebruik wordt aanbevolen om de lijst kort en overzichtelijk te houden.",w),
            "1,0,1": textwrap.wrap("De collectie wordt gestorteerd op %s, met de laatste %s vooraan" % (elementen[0].lower(),elementen[0].lower()),w),
            "1,0,2": textwrap.wrap("De collectie wordt gestorteerd op %s, met de eerste %s vooraan" % (elementen[0].lower(),elementen[0].lower()),w),
            "1,0,3": textwrap.wrap("De collectie wordt gestorteerd op %s, met het hoogste %s vooraan" % (elementen[1].lower(),elementen[1].lower()),w),
            "1,0,4": textwrap.wrap("De collectie wordt gestorteerd op %s, met het laagste %s vooraan" % (elementen[1].lower(),elementen[1].lower()),w),
            "1,0,5": textwrap.wrap("De collectie wordt gestorteerd op %s, van Z naar A" % (elementen[2].lower()),w),
            "1,0,6": textwrap.wrap("De collectie wordt gestorteerd op %s, van A naar Z" % (elementen[2].lower()),w),
            "1,0,7": textwrap.wrap("De collectie wordt gestorteerd op %s, van Z naar A" % (elementen[3].lower()),w),
            "1,0,8": textwrap.wrap("De collectie wordt gestorteerd op %s, van A naar Z" % (elementen[3].lower()),w),
        "1,1": textwrap.wrap("Selecteer transacties op basis van verschillende criteria (%s, %s, %s, %s en %s) en genereer een overzichtelijke tabel. Er kan gebruik worden gemaakt van \"sneltoetsen\", of u kunt alle elementen afzonderlijk opgeven. De mogelijke \"sneltoetsen\" worden getoond; het is mogelijk \"M\" (maand) of \"W\" (week) te voorzien van een getal; \"0\" is inclusief vandaag. Alle geselecteerde transacties worden ook verzameld in de collectie, die steeds getoond wordt boven het keuzemenu. Omvat de selectie één dag, dan wordt het dagtotaal op die dag getoond." % (elementen[0].lower(),elementen[1].lower(),elementen[2].lower(),elementen[3].lower(),woordcategorie.lower()),w),
        "1,2": textwrap.wrap("Toon de budgetanalyse van één maand. Standaard wordt de huidige maand getoond. U ziet de voortgang van iedere categorie ten opzichte van het daaraan toegekende budget, en de maandprestatie.",w),
        "1,3": textwrap.wrap("Toon de details van individuele transacties in de collectie. Het toegestaan aantal karakters in \"%s\" en \"%s\" is onbeperkt, maar in de tabel (\"1,1\") worden die afgekapt en slechts ten dele getoond. Alle informatie in die extra karakters wordt hier wel uitgevouwen." % (elementen[2].lower(),elementen[3].lower()),w),
    "2": textwrap.wrap("U kunt nieuwe transacties aan uw rekening toevoegen, die elk aan een categorie worden toegekend. Een nieuwe transactie kunt u per element invoeren of achter elkaar op één regel in CSV-stijl, of u kunt een kopie maken van een eerdere transactie en de details later aanpassen met de opties onder \"3\". Nieuwe transacties worden direct aan de collectie toegevoegd, zodat u die meteen kunt inzien of aanpassen.",w),
        "2,1": textwrap.wrap("Voeg hier een nieuwe transactie aan uw rekening toe. U kunt de elementen stap-voor-stap ingeven, of - voor de meer ervaren gebruiker - achter elkaar op één lijn in CSV-stijl: \"%s,%s,%s,%s,%s\". U kunt daarom in geen enkel element een komma (\",\") gebruiken. Gebruik als decimaalscheidingsteken altijd een punt (\".\"). Mocht de CSV-ingave ongeldige data bevatten, dan neemt de stap-voor-stap-ingave het over." % (elementen[0].lower(),elementen[1].lower(),elementen[2].lower(),elementen[3].lower(),woordcategorie.lower()),w),
        "2,2": textwrap.wrap("Maak hier een kopie van een eerder ingevoerde transactie en vervang automatisch de oorspronkelijke datum met die van vandaag. U kunt iedere transactie als sjabloon gebruiken om later op details aan te passen met de opties in menu \"3\". Als er al een collectie bestaat worden die transacties één voor één aangeboden, anders wordt u gevraagd een \"ID\" - of beter: een lijst van \"ID's\" in de vorm van een CSV-lijst - op te geven. Dit is de aanbevolen methode voor het toevoegen van terugkerende transacties. Let op: als u een identieke kopie maakt van een transactie eerder vandaag, dan wordt die niet automatisch aan de collectie toegevoegd.",w),
    "3": textwrap.wrap("Alle elementen van een bestaande transactie kunnen hier worden aangepast. Als er al een collectie bestaat worden die transacties één voor één aangeboden, anders wordt u gevraagd een \"ID\" - of beter: een lijst van \"ID's\" in de vorm van een CSV-lijst - op te geven.",w),
        "3,1": textwrap.wrap("Pas de %s van de transactie aan. Voer de nieuwe datum in als \"JJJJMMDD\". De standaarddatum, bijvoorbeeld als er een ongeldige of onvolledige datum wordt ingevoerd, is de datum van vandaag. De datumopmaak in de tabel (\"1,1\") of de transactieweergave (\"1,3\") stelt u in bij \"0,1,10\"." % (elementen[0].lower()),w),
        "3,2": textwrap.wrap("Pas het %s van de transactie aan. Voer het bedrag in zonder valuta en met een punt (\".\") als decimaalscheidingsteken. De valuta stelt u in bij \"0,1,5\"." % (elementen[1].lower()),w),
        "3,3": textwrap.wrap("Pas de %s van de transactie aan. Dit kan een debiteur of een crediteur zijn, een klant of een leverancier (winkel). Het aantal karakers om te gebruiken is vrij, maar wordt in de tabelweergave (\"1,1\") wel afgekort. Het is daarom verstandig om zeker bij langere beschrijvingen altijd te beginnen met een herkenbaar fragment." % (elementen[2].lower()),w),
        "3,4": textwrap.wrap("Pas het %s van de transactie aan. Hierin geeft u een beschrijving van de inhoud van deze transactie op, zoals een dienst die is gefactureerd of een aantal artikelen dat werd aangeschaft. Ook betalingskenmerken of factuurnummers kunt u hier kwijt. Het aantal karakers om te gebruiken is vrij, maar wordt in de tabelweergave (\"1,1\") wel afgekort. Het is daarom verstandig om zeker bij langere beschrijvingen altijd te beginnen met een herkenbaar fragment." % (elementen[3].lower()),w),
        "3,5": textwrap.wrap("Plaats een transactie in een andere %s. Iedere transactie wordt toegekend aan een categorie waaraan een budget is toegekend. Deze budgetten worden verdeeld in \"0,2,3\" en de voortgang is per maand te zien in \"1,2\"." % (woordcategorie.lower()),w),
    "4": textwrap.wrap("Hier kunt u individuele transacties definitief verwijderen. Als er al een collectie bestaat worden die transacties één voor één aangeboden, anders wordt u gevraagd een \"ID\" - of beter: een lijst van \"ID's\" in de vorm van een CSV-lijst - op te geven.",w),
    "5": textwrap.wrap("De functie %s is nog niet af." % menu["5"],w),
        "5,1": textwrap.wrap("De functie %s is nog niet af." % menu["5,1"],w),
        "5,2": textwrap.wrap("De functie %s is nog niet af." % menu["5,2"],w),
        "5,3": textwrap.wrap("De functie %s is nog niet af." % menu["5,3"],w),
            "5,3,1": textwrap.wrap("De functie %s is nog niet af." % menu["5,3,1"],w),
            "5,3,2": textwrap.wrap("De functie %s is nog niet af." % menu["5,3,2"],w),
            "5,3,3": textwrap.wrap("De functie %s is nog niet af." % menu["5,3,3"],w),
            "5,3,4": textwrap.wrap("De functie %s is nog niet af." % menu["5,3,4"],w),
        "5,4": textwrap.wrap("De functie %s is nog niet af." % menu["5,4"],w),
    "<": textwrap.wrap("Terug naar hoofdmenu",w), # Wordt nooit aangesproken
    "Q": textwrap.wrap("Verlaat de app",w) # Wordt nooit aangesproken
        }
##### Alle mogelijke kleuren (kan van pas komen)
ResetAll                = "\033[0m"
Vet                     = "\033[1m"
Vaag                    = "\033[2m"
Omkeren                 = "\033[7m"
Zwart                   = "\033[30m"
Rood                    = "\033[31m"
Groen                   = "\033[32m"
Geel                    = "\033[33m"
Blauw                   = "\033[34m"
Magenta                 = "\033[35m"
Cyaan                   = "\033[36m"
LichtGrijs              = "\033[37m"
DonkerGrijs             = "\033[90m"
LichtRood               = "\033[91m"
LichtGroen              = "\033[92m"
LichtGeel               = "\033[93m"
LichtBlauw              = "\033[94m"
LichtMagenta            = "\033[95m"
LichtCyaan              = "\033[96m"
Wit                     = "\033[97m"
AchtergrondDefault      = "\033[49m"
AchtergrondZwart        = "\033[40m"
AchtergrondRood         = "\033[41m"
AchtergrondGroen        = "\033[42m"
AchtergrondGeel         = "\033[43m"
AchtergrondBlauw        = "\033[44m"
AchtergrondMagenta      = "\033[45m"
AchtergrondCyaan        = "\033[46m"
AchtergrondLichtGrijs   = "\033[47m"
AchtergrondDonkerGrijs  = "\033[100m"
AchtergrondLichtRood    = "\033[101m"
AchtergrondLichtGroen   = "\033[102m"
AchtergrondLichtGeel    = "\033[103m"
AchtergrondLichtBlauw   = "\033[104m"
AchtergrondLichtMagenta = "\033[105m"
AchtergrondLichtCyaan   = "\033[106m"
AchtergrondWit          = "\033[107m"
colgoed = LichtGroen
colslecht = LichtRood
colmatig = Magenta
colonbepaald = Blauw
colhuh = LichtBlauw
coltoe = Groen
coltoon = LichtGeel
colwijzig = LichtCyaan
colverwijder= Rood
coltekst = LichtMagenta

kleurenschemalijst = [
    "Categorie",
    "Alle",
    "Mono",
    "Regenboog"
    ]

def toonkleurenschemaopties():
    for i in range(len(kleurenschemalijst)):
        print(forr3(i)+" : "+vertaalv(kleurenschemalijst[i]))

def updatekleuren(rekening):
    header = haalheader(rekening)
    if header[nieuwheaderlijst[10]] == kleurenschemalijst[1]:
        kleuren = {
                "ResetAll":ResetAll,
                "Vaag":Vaag,
                "Omkeren":Omkeren,
                "Rood":Rood,
                "Groen":Groen,
                "Geel":Geel,
                "Blauw":Blauw,
                "Magenta":Magenta,
                "Cyaan":Cyaan,
                "LichtGrijs":LichtGrijs,
                "DonkerGrijs":DonkerGrijs,
                "LichtRood":LichtRood,
                "LichtGroen":LichtGroen,
                "LichtGeel":LichtGeel,
                "LichtBlauw":LichtBlauw,
                "LichtMagenta":LichtMagenta,
                "LichtCyaan":LichtCyaan,
                "Wit":Wit,
                "colgoed":LichtGroen,
                "colslecht":LichtRood,
                "colmatig":Magenta,
                "colonbepaald":Blauw,
                "colhuh":LichtBlauw,
                "coltoe":Groen,
                "coltoon":LichtGeel,
                "colwijzig":LichtCyaan,
                "colverwijder":Rood,
                "coltekst":LichtMagenta,
                "0":Wit,
                "1":LichtGeel,
                "2":LichtGroen,
                "3":LichtCyaan,
                "4":LichtRood,
                "5":Magenta,
                "6":Geel,
                "7":Cyaan,
                "8":Rood,
                "9":Groen,
                "Q":DonkerGrijs,
                "<":DonkerGrijs
                }
        catcol = {
                "0":Rood,
                "1":Groen,
                "2":Geel,
                "3":Blauw,
                "4":Magenta,
                "5":Cyaan,
                "6":LichtGrijs,
                "7":DonkerGrijs,
                "8":LichtRood,
                "9":LichtGroen,
                "A":Rood,
                "B":Groen,
                "C":Geel,
                "D":Blauw,
                "E":Magenta,
                "F":Cyaan,
                "G":LichtGrijs,
                "H":DonkerGrijs,
                "I":LichtRood,
                "J":LichtGroen,
                "K":LichtGeel,
                "L":LichtBlauw,
                "M":LichtMagenta,
                "N":LichtCyaan,
                "O":Wit
                }
    elif header[nieuwheaderlijst[10]] == kleurenschemalijst[2]:
        kleuren = {
                "ResetAll":"",
                "Vaag":"",
                "Omkeren":"",
                "Rood":"",
                "Groen":"",
                "Geel":"",
                "Blauw":"",
                "Magenta":"",
                "Cyaan":"",
                "LichtGrijs":"",
                "DonkerGrijs":"",
                "LichtRood":"",
                "LichtGroen":"",
                "LichtGeel":"",
                "LichtBlauw":"",
                "LichtMagenta":"",
                "LichtCyaan":"",
                "Wit":"",
                "colgoed":"",
                "colslecht":"",
                "colmatig":"",
                "colonbepaald":"",
                "colhuh":"",
                "coltoe":"",
                "coltoon":"",
                "colwijzig":"",
                "colverwijder":"",
                "coltekst":"",
                "0":"",
                "1":"",
                "2":"",
                "3":"",
                "4":"",
                "5":"",
                "6":"",
                "7":"",
                "8":"",
                "9":"",
                "Q":"",
                "<":""
                }
        catcol = {
                "0":"",
                "1":"",
                "2":"",
                "3":"",
                "4":"",
                "5":"",
                "6":"",
                "7":"",
                "8":"",
                "9":"",
                "A":"",
                "B":"",
                "C":"",
                "D":"",
                "E":"",
                "F":"",
                "G":"",
                "H":"",
                "I":"",
                "J":"",
                "K":"",
                "L":"",
                "M":"",
                "N":"",
                "O":""
                }
    elif header[nieuwheaderlijst[10]] == kleurenschemalijst[3]:
        kleuren = {
                "ResetAll":ResetAll,
                "Vaag":Vaag,
                "Omkeren":Omkeren,
                "Rood":Rood,
                "Groen":Groen,
                "Geel":Geel,
                "Blauw":Blauw,
                "Magenta":Magenta,
                "Cyaan":Cyaan,
                "LichtGrijs":LichtGrijs,
                "DonkerGrijs":DonkerGrijs,
                "LichtRood":LichtRood,
                "LichtGroen":LichtGroen,
                "LichtGeel":LichtGeel,
                "LichtBlauw":LichtBlauw,
                "LichtMagenta":LichtMagenta,
                "LichtCyaan":LichtCyaan,
                "Wit":Wit,
                "colgoed":Omkeren+LichtGroen,
                "colslecht":Omkeren+LichtRood,
                "colmatig":Omkeren+Magenta,
                "colonbepaald":Omkeren+Blauw,
                "colhuh":Omkeren+LichtBlauw,
                "coltoe":Groen,
                "coltoon":LichtGeel,
                "colwijzig":LichtCyaan,
                "colverwijder":Rood,
                "coltekst":LichtMagenta,
                "0":Wit,
                "1":LichtGeel,
                "2":LichtGroen,
                "3":LichtCyaan,
                "4":LichtRood,
                "5":Magenta,
                "6":Geel,
                "7":Cyaan,
                "8":Rood,
                "9":Groen,
                "Q":DonkerGrijs,
                "<":DonkerGrijs
                }
        catcol = {
                "0":AchtergrondRood+LichtGroen,
                "1":AchtergrondGeel+LichtBlauw,
                "2":AchtergrondLichtGeel+Blauw,
                "3":AchtergrondGroen+LichtRood,
                "4":AchtergrondBlauw+LichtGeel,
                "5":AchtergrondMagenta+LichtCyaan,
                "6":AchtergrondRood+LichtGroen,
                "7":AchtergrondGeel+LichtBlauw,
                "8":AchtergrondLichtGeel+Blauw,
                "9":AchtergrondGroen+LichtRood,
                "A":AchtergrondRood+LichtGroen,
                "B":AchtergrondGeel+LichtBlauw,
                "C":AchtergrondLichtGeel+Blauw,
                "D":AchtergrondGroen+LichtRood,
                "E":AchtergrondBlauw+LichtGeel,
                "F":AchtergrondMagenta+LichtCyaan,
                "G":AchtergrondRood+LichtGroen,
                "H":AchtergrondGeel+LichtBlauw,
                "I":AchtergrondLichtGeel+Blauw,
                "J":AchtergrondGroen+LichtRood,
                "K":AchtergrondBlauw+LichtGeel,
                "L":AchtergrondMagenta+LichtCyaan,
                "M":AchtergrondLichtGroen+Rood,
                "N":AchtergrondLichtRood+Groen,
                "O":AchtergrondWit+Zwart
                }
    else:
        kleuren = {
                "ResetAll":ResetAll,
                "Vaag":Vaag,
                "Omkeren":Omkeren,
                "Rood":ResetAll,
                "Groen":ResetAll,
                "Geel":ResetAll,
                "Blauw":ResetAll,
                "Magenta":ResetAll,
                "Cyaan":ResetAll,
                "LichtGrijs":ResetAll,
                "DonkerGrijs":ResetAll,
                "LichtRood":ResetAll,
                "LichtGroen":ResetAll,
                "LichtGeel":ResetAll,
                "LichtBlauw":ResetAll,
                "LichtMagenta":ResetAll,
                "LichtCyaan":ResetAll,
                "Wit":ResetAll,
                "colgoed":LichtGroen,
                "colslecht":LichtRood,
                "colmatig":ResetAll,
                "colonbepaald":ResetAll,
                "colhuh":ResetAll,
                "coltoe":ResetAll,
                "coltoon":ResetAll,
                "colwijzig":ResetAll,
                "colverwijder":ResetAll,
                "coltekst":ResetAll,
                "0":ResetAll,
                "1":ResetAll,
                "2":ResetAll,
                "3":ResetAll,
                "4":ResetAll,
                "5":ResetAll,
                "6":ResetAll,
                "7":ResetAll,
                "8":ResetAll,
                "9":ResetAll,
                "Q":ResetAll,
                "<":ResetAll
                }
        catcol = {
                "0":Rood,
                "1":Groen,
                "2":Geel,
                "3":Blauw,
                "4":Magenta,
                "5":Cyaan,
                "6":LichtGrijs,
                "7":DonkerGrijs,
                "8":LichtRood,
                "9":LichtGroen,
                "A":Rood,
                "B":Groen,
                "C":Geel,
                "D":Blauw,
                "E":Magenta,
                "F":Cyaan,
                "G":LichtGrijs,
                "H":DonkerGrijs,
                "I":LichtRood,
                "J":LichtGroen,
                "K":LichtGeel,
                "L":LichtBlauw,
                "M":LichtMagenta,
                "N":LichtCyaan,
                "O":Wit
                }
    return kleuren,catcol

def coljanee(rekening,header,item):
    kleuren,catcol = updatekleuren(rekening)
    if item == ">":
        coljn = kleuren["colgoed"]
    elif item == "<":
        coljn = kleuren["colslecht"]
    else:
        coljn = ""
    return coljn

#____     __   \/   ____     __  ____   __   __ 
# ||\    /|    ||    ||\    /|  /   \\ / '' 6_\\
# ||\\  /||  / ||\\  ||\\  /|| || \/ ||'-\\// ||
# || \\/ || || || || || \\/ || || || ||\\_/\\/|\
# ||  \  || || || || ||  \  || || || || __   __ 
#_/\_   _/\_|| \/ ||_/\_   _/\_ \ || / / '' 6_\\
# Money In   \\___/  Money Out    ||   '-\\// ||
#  spendings and savings aid      \/   \\_/\\/|\
logo =  """
%s                ____     __   \\/%s   ____     __  ____%s   __%s   __ 
%s                 ||\\    /|    ||%s    ||\\    /|  /   \\\\%s / ''%s 6_\\\\
%s                 ||\\\\  /||%s  /%s ||%s\\\\%s  ||\\\\  /|| ||%s \\/%s ||%s'-\\\\%s// ||
%s                 || \\\\/ ||%s ||%s ||%s ||%s || \\\\/ || ||%s ||%s ||%s\\\\_/%s\\\\/|\\
%s                 ||  \\  ||%s ||%s ||%s ||%s ||  \\  || ||%s ||%s ||%s __%s   __ 
%s                _/\\_   _/\\_%s||%s \\/%s ||%s_/\\_   _/\\_ \\%s ||%s /%s / ''%s 6_\\\\
%s                 Money In%s   \\\\___/%s  Money Out%s    ||%s   '-\\\\%s// ||
%s                  spendings%s and savings%s aid%s      \\/%s   \\\\_/%s\\\\/|\\%s
""" % (
          colgoed, colslecht, coltoon, Geel,
          colgoed, colslecht, coltoon, Geel,
          colgoed, colonbepaald, colgoed, colonbepaald, colslecht, colonbepaald, colslecht, coltoon, Geel,
          colgoed, colonbepaald, colgoed, colonbepaald, colslecht, colonbepaald, colslecht, coltoon, Geel,
          colgoed, colonbepaald, colgoed, colonbepaald, colslecht, colonbepaald, colslecht, Geel, coltoon,
          colgoed, colonbepaald, colgoed, colonbepaald, colslecht, colonbepaald, colslecht, Geel, coltoon,
          colgoed, colonbepaald, colslecht, colonbepaald, Geel, coltoon,
          coltoon, Geel, coltoon, colonbepaald, Geel, coltoon, ResetAll
          )

for i in logo:
    print(i,flush = True, end = "")
    sleep(0.00125)
print()

def printdatum(nustr):
    kleuren,catcol = updatekleuren(rekening)
    datum = opmaakdatum(nustr)
    print(kleuren["coltoon"]+forcw(("%s = " % nustr)+datum)+kleuren["ResetAll"])

def printdatumlinks(datum):
    kleuren,catcol = updatekleuren(rekening)
    dat = opmaakdatum(datum)
    print(col+("%s = " % datum)+dat+ResetAll)

def doei():
    try:
        with open("laatstgekozen","r") as l:
            rekening = l.read()
    except(Exception) as f:
        #print(f)
        exit()
    try:
        header = haalheader(rekening)
        Taal = header[nieuwheaderlijst[3]]
    except(Exception) as f:
        #print(f)
        exit()
    if header[nieuwheaderlijst[13]] == ">":
        exportcsv(rekening)
    if Taal == "EN":
        print(coltekst+forcw("Thank you for using mimosasa and have a nice day")+ResetAll)
    elif Taal == "IT":
        print(coltekst+forcw("Grazie per usare mimosasa e buona giornata")+ResetAll)
    else:
        print(coltekst+forcw("Bedankt voor het gebruiken van mimosasa en nog een fijne dag")+ResetAll)
    print()
    exit()

def exportcsv(rekening):
    ok = {}
    ok = haaltransacties(rekening,ok)
    rekeningtotaal = rekeningsom(rekening)
    alternatievenamendict = haalalternatievenamen(rekening)
    with open(os.path.join(rekening,"export.csv"),"w") as e:
        print(rekening+","+str(rekeningtotaal)+",", file = e)
        cat = {}
        for i in ok:
            categorie = i[0]
            cat[categorie] = ""
        geprint = False
        for i in cat:
            categorie = haalcategorie(rekening,i)
            budget = str(categorie[0][1])
            if geprint == False:
                print(i+","+alternatievenamendict[i]+","+budget+",", file = e)
                geprint = True
            for j in ok:
                if i in j:
                    for k in ok[j]:
                        print(k, end = ",", file = e)
                    print("", file = e)
                geprint = False

def checkfloat(floattest):
    try:
        floa = float(floattest)
        return True
    except:
        return False

def checkint(inttest):
    try:
        integ = int(inttest)
        return True
    except:
        return False

def checkdatum(YYYYMMDD):
    try:
        datum = datetime.strftime(datetime.strptime(YYYYMMDD,"%Y%m%d"),"%Y%m%d")
        return True
    except:
        return False

def grootgetal(getal,forsom,K):
    if getal <= -10000000:
        getal = "-----"
        forsom = "{:>5}".format
        K = " ~K"
        return getal,forsom,K
    elif 10000000 <= getal:
        getal = "+++++"
        forsom = "{:>5}".format
        K = " ~K"
        return getal,forsom,K
    elif getal <= -100000 or 100000 <= getal:
        getal = int(getal/1000)
        forsom = "{:>5}".format
        K = " ~K"
        return getal,forsom,K
    else:
        getal = getal
        forsom = fornum
        K = ""
        return round(getal,2),forsom,K

def rekeningsom(rekening):
    header = haalheader(rekening)
    som = header[nieuwheaderlijst[5]]
    for i in lijst:
        try:
            categorie = haalcategorie(rekening,i)
            for j in categorie[1:]:
                som += j[1]
        except(Exception) as f:
            pass
            #print(f)
    return round(som,2)

def haalheader(rekening):
    if rekening.upper() in (neelijst+afsluitlijst):
        doei()
    with open(os.path.join(rekening,"header"),"r") as h:
        header = ast.literal_eval(h.read())
    return header

def rekeningenoverzicht():
    rekeningenlijst = []
    for i in os.listdir():
        if "#" in i:
            rekeningenlijst.append(i)
    rekeningenlijst = sorted(rekeningenlijst)
    return rekeningenlijst

def haallaatstgekozen():
    try:
        with open("laatstgekozen","r") as l:
            laatstgekozen = l.read()
    except(Exception) as f:
        #print(f)
        rekeningenlijst = rekeningenoverzicht()
        laatstgekozen = rekeningenlijst[0]
        with open("laatstgekozen","w") as l:
            print(laatstgekozen, file = l, end = "")
    return laatstgekozen

def toonrekeningsaldo(rekeningenlijst):
    laatstgekozen = haallaatstgekozen()
    maxreklen = len(max(rekeningenlijst, key = len))
    totaalalles = 0.0
    valutalijst = []
    for i in rekeningenlijst:
        IBAN = i[:i.index("#")]
        JAAR = forr4(i[i.index("#")+1:])
        if i == laatstgekozen:
            L = ">"
        else:
            L = " "
        kleuren,catcol = updatekleuren(i)
        header = haalheader(i)
        rekeningnaam = header[nieuwheaderlijst[0]]
        actieverekening = header[nieuwheaderlijst[2]]
        Taal = header[nieuwheaderlijst[3]]
        valuta = header[nieuwheaderlijst[4]]
        rekeningtotaal = header[nieuwheaderlijst[5]]
        toontotaal = header[nieuwheaderlijst[6]]
        if len(rekeningnaam) > 25:
            rn1 = rekeningnaam[:19]
            rn2 = "..."
            rn3 = rekeningnaam[-3:]
            rekeningnaam = rn1+rn2+rn3
        categorieenlijst = haalcategorieen(i)
        forsom = fornum
        if actieverekening.upper() in jalijst:
            if toontotaal in jalijst:
                for j in categorieenlijst:
                    with open(os.path.join(i,j),"r") as c:
                        categorie = ast.literal_eval(c.read())
                        for k in categorie[1:]:
                            rekeningtotaal += k[1]
                valutalijst.append(valuta)
                totaalalles += rekeningtotaal
                getal,forsom,K = grootgetal(rekeningtotaal,forsom,"")
                printstuffzw = L+forl3(rekeningenlijst.index(i)+1)+" "+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+valuta+forsom(getal)+K+forr25(rekeningnaam)
                lenprtstfzw = len(printstuffzw)
                print(int((w-lenprtstfzw)/2)*" "+kleuren["coltoe"]+L+forl3(rekeningenlijst.index(i)+1)+" "+catcol["5"]+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+kleuren["ResetAll"]+" "+grotegetalkleuren(i,header,rekeningtotaal)+valuta+forsom(getal)+K+kleuren["ResetAll"]+kleuren["coltekst"]+forr25(rekeningnaam)+kleuren["ResetAll"])
            else:
                printstuffzw = L+forl3(rekeningenlijst.index(i)+1)+" "+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+valuta+" "*8+forr25(rekeningnaam)
                lenprtstfzw = len(printstuffzw)
                print(int((w-lenprtstfzw)/2)*" "+kleuren["coltoe"]+L+forl3(rekeningenlijst.index(i)+1)+" "+catcol["5"]+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+kleuren["ResetAll"]+" "+grotegetalkleuren(i,header,rekeningtotaal)+kleuren["ResetAll"]+valuta+" "*8+kleuren["coltekst"]+forr25(rekeningnaam)+kleuren["ResetAll"])
    valutalijst = sorted(valutalijst)
    if len(valutalijst) > 0:
        if valutalijst[0] == valutalijst[-1]:
            totaalallesK,forsom,K = grootgetal(totaalalles,forsom,K)
            print(int((w-lenprtstfzw)/2)*" "+" "+forl3(" ")+" "+("{:^%s}" % maxreklen).format(" ")+" "+"_"+"_"*8)
            print(int((w-lenprtstfzw)/2)*" "+" "+forl3(" ")+" "+("{:^%s}" % maxreklen).format(" ")+" "+grotegetalkleuren("","",totaalalles)+valuta+forsom(totaalallesK)+K+ResetAll)

def toonrekeningenactief(rekeningenlijst):
    laatstgekozen = haallaatstgekozen()
    maxreklen = len(max(rekeningenlijst, key = len))
    totaalalles = 0.0
    valutalijst = []
    for i in rekeningenlijst:
        IBAN = i[:i.index("#")]
        JAAR = forr4(i[i.index("#")+1:])
        if i == laatstgekozen:
            L = ">"
        else:
            L = " "
        kleuren,catcol = updatekleuren(i)
        header = haalheader(i)
        rekeningnaam = header[nieuwheaderlijst[0]]
        actieverekening = header[nieuwheaderlijst[2]]
        Taal = header[nieuwheaderlijst[3]]
        valuta = header[nieuwheaderlijst[4]]
        rekeningtotaal = header[nieuwheaderlijst[5]]
        toontotaal = header[nieuwheaderlijst[6]]
        if Taal == "EN":
            if actieverekening.upper() in jalijst:
                actief = " %s Yes" % nieuwheaderlijstEN[2]
            else:
                actief = " %s: No" % nieuwheaderlijstEN[2]
        elif Taal == "IT":
            if actieverekening.upper() in jalijst:
                actief = " %s: Sì" % nieuwheaderlijstIT[2]
            else:
                actief = " %s: No" % nieuwheaderlijstIT[2]
        else:
            if actieverekening.upper() in jalijst:
                actief = " %s: Ja" % nieuwheaderlijst[2]
            else:
                actief = " %s: Nee" % nieuwheaderlijst[2]
        lenactief = len(actief)
        if len(rekeningnaam) > 25:
            rn1 = rekeningnaam[:19]
            rn2 = "..."
            rn3 = rekeningnaam[-3:]
            rekeningnaam = rn1+rn2+rn3
        categorieenlijst = haalcategorieen(i)
        forsom = fornum
        if toontotaal in jalijst:
            for j in categorieenlijst:
                with open(os.path.join(i,j),"r") as c:
                    categorie = ast.literal_eval(c.read())
                    for k in categorie[1:]:
                        rekeningtotaal += k[1]
            valutalijst.append(valuta)
            totaalalles += rekeningtotaal
            getal,forsom,K = grootgetal(rekeningtotaal,forsom,"")
            printstuffzw = L+forl3(rekeningenlijst.index(i)+1)+" "+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+valuta+forsom(getal)+K+forl25(actief)
            lenprtstfzw = len(printstuffzw)
            print(int((w-lenprtstfzw)/2)*" "+kleuren["coltoe"]+L+forl3(rekeningenlijst.index(i)+1)+" "+kleuren["coltoon"]+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+grotegetalkleuren(i,header,rekeningtotaal)+valuta+forsom(getal)+K+kleuren["ResetAll"]+kleuren["coltekst"]+forl25(actief)+kleuren["ResetAll"])
        else:
            printstuffzw = L+forl3(rekeningenlijst.index(i)+1)+" "+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+valuta+" "*8+forl25(actief)
            lenprtstfzw = len(printstuffzw)
            print(int((w-lenprtstfzw)/2)*" "+kleuren["coltoe"]+L+forl3(rekeningenlijst.index(i)+1)+" "+kleuren["coltoon"]+("{:>%s}" % maxreklen).format(IBAN+" "+JAAR)+" "+grotegetalkleuren(i,header,rekeningtotaal)+kleuren["ResetAll"]+valuta+" "*8+kleuren["coltekst"]+forl25(actief)+kleuren["ResetAll"])

def kiesrekening(rekeningenlijst):
    laatstgekozen = haallaatstgekozen()
    col = coltekst
    rekeningloop = True
    while rekeningloop == True:
        rekeningkeuze = input(inputindent+col)
        print(ResetAll, end = "")
        if rekeningkeuze.upper() in afsluitlijst:
            doei()
        try:
            keuze = int(rekeningkeuze)
            if 0 < keuze <= len(rekeningenlijst):
                rekening = rekeningenlijst[keuze-1]
                with open("laatstgekozen","w") as l:
                    print(rekening, file = l, end = "")
                return rekening
        except(Exception) as f:
            #print(f)
            if rekeningkeuze == "":
                rekening = haallaatstgekozen()
                return rekening

def kiesrekeningalleennummer(rekeningenlijst,rekening):
    laatstgekozen = haallaatstgekozen()
    col = coltekst
    rekeningkeuze = input(inputindent+col)
    print(ResetAll, end = "")
    if rekeningkeuze.upper() in afsluitlijst:
        doei()
    try:
        keuze = int(rekeningkeuze)
        if 0 < keuze <= len(rekeningenlijst):
            rekeningalleennummer = rekeningenlijst[keuze-1]
    except(Exception) as f:
        #print(f)
        rekeningalleennummer = rekening
    return rekeningalleennummer

def taalkeuze():
    col = coltekst
    for i in taaldict:
        if i == taallijst[0]:
            print(forr3(">0")+" : "+taaldict[i])
        else:
            print(forr3(taallijst.index(i))+" : "+taaldict[i])
    antwoord = input()
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return "<"
    test = checkint(antwoord)
    if test == True and int(antwoord) in range(len(taallijst)):
        if antwoord == "1":
            Taal = "EN"
        elif antwoord == "2":
            Taal = "IT"
        else:
            Taal = "NL"
    else:
        Taal = "NL"
    return Taal

def geefIBAN(Taal):
    if Taal == "EN":
        print("Enter your account number")
    elif Taal == "IT":
        print("Inserisci il numero del conto")
    else:
        print("Geef het rekeningnummer")
    IBAN = input(coltoe+inputindent).upper()
    print(ResetAll, end = "")
    if IBAN.upper() in afsluitlijst:
        doei()
    elif IBAN.upper() in neelijst:
        return "<"
    else:
        return IBAN

def geefJAAR(Taal):
    if Taal == "EN":
        print("Enter the year")
    elif Taal == "IT":
        print("Inserisci l'anno")
    else:
        print("Geef het jaar")
    JAAR = input(coltoe+inputindent).upper()
    print(ResetAll, end = "")
    if JAAR.upper() in afsluitlijst:
        doei()
    elif JAAR.upper() in neelijst:
        return "<"
    else:
        return JAAR

def maaknieuwerekening():
    try:
        kleuren,catcol = updatekleuren(rekening)
        col = kleuren["coltoe"]
    except(Exception) as f:
        #print(f)
        col = coltoe
    nieuweTaal = taalkeuze()
    if nieuweTaal.upper() in neelijst:
        return "<"
    if nieuweTaal == "EN":
        for i in helpmenuEN["0"]:
            print(i)
        for i in helpmenuEN["0,0"]:
            print(i)
    elif nieuweTaal == "IT":
        for i in helpmenuIT["0"]:
            print(i)
        for i in helpmenuIT["0,0"]:
            print(i)
    else:
        for i in helpmenu["0"]:
            print(i)
        for i in helpmenu["0,0"]:
            print(i)
    IBAN = geefIBAN(nieuweTaal)
    if IBAN in neelijst:
        return "<"
    JAAR = geefJAAR(nieuweTaal)
    if IBAN in neelijst:
        return "<"
    nieuwerekening = IBAN+"#"+JAAR
    os.mkdir(nieuwerekening)
    # print bestanden naar map: categorieen, header
    nieuwheader[nieuwheaderlijst[3]] = nieuweTaal
    with open(os.path.join(nieuwerekening,"header"),"w") as h:
        print(nieuwheader, file = h, end = "")
    with open("header","w") as hbu:
        print(nieuwheader, file = hbu, end = "")
    for i in huishoudelijkelijst:
        with open(os.path.join(nieuwerekening,i),"w") as c:
            print([[nieuwalternatievenamendict[i],budgetnul]], file = c, end = "")
    return nieuwerekening

def vertaalv(v):
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        v = v\
        .replace(woordcategorie,woordcategorieEN)\
        .replace(kleurenschemalijst[1],"All")\
        .replace(kleurenschemalijst[2],"Mono")\
        .replace(kleurenschemalijst[3],"Rainbow")\
        .replace(">","Yes")\
        .replace("<","No")
        for i in nieuwalternatievenamendict:
            if v == nieuwalternatievenamendict[i]:
                v = nieuwalternatievenamendictEN[i]
    elif Taal == "IT":
        v = v\
        .replace(woordcategorie,woordcategorieIT)\
        .replace(kleurenschemalijst[1],"Tutti")\
        .replace(kleurenschemalijst[2],"Mono")\
        .replace(kleurenschemalijst[3],"Arcobaleno")\
        .replace(">","Sì")\
        .replace("<","No")\
        .replace("DDMMYYYY","GGMMAAAA")\
        .replace("DD-MM-YY","GG-MM-AA")\
        .replace("YY-MM-DD","AA-MM-GG")\
        .replace("DD/MM/YY","GG/MM/AA")\
        .replace("DDmmm\'YY","GGmmm\'AA")\
        .replace("DD-mmmYY","GG-mmmAA")\
        .replace("YYYYMMDD","AAAAMMGG")
        for i in nieuwalternatievenamendict:
            if v == nieuwalternatievenamendict[i]:
                v = nieuwalternatievenamendictIT[i]
    else:
        v = v\
        .replace(">","Ja")\
        .replace("<","Nee")\
        .replace("DDMMYYYY","DDMMJJJJ")\
        .replace("YY-MM-DD","JJ-MM-DD")\
        .replace("DD-MM-YY","DD-MM-JJ")\
        .replace("DD/MM/YY","DD/MM/JJ")\
        .replace("DDmmm\'YY","DDmmm\'JJ")\
        .replace("DD-mmmYY","DD-mmmJJ")\
        .replace("YYYYMMDD","JJJJMMDD")
    return v

def printheaderall(rekening):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        menulinks = nieuwheaderlijstEN
    elif Taal == "IT":
        menulinks = nieuwheaderlijstIT
    else:
        menulinks = nieuwheaderlijst
    maxlen = len(max(menulinks, key = len))
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[0])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[0]][:w-maxlen-2]+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[1])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[1]][:w-maxlen-2]+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[2])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[2]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[3])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+taaldict[header[nieuwheaderlijst[3]]]+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[4])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[4]]+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[5])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[6])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[6]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[7])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[8])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[8]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[9])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[9]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[10])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[10]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[11])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+str(header[nieuwheaderlijst[11]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[12])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[12]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[13])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[13]])+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[14])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+vertaalv(header[nieuwheaderlijst[14]])+ResetAll)

def printheader(rekening):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        menulinks = nieuwheaderlijstEN
    elif Taal == "IT":
        menulinks = nieuwheaderlijstIT
    else:
        menulinks = nieuwheaderlijst
    maxlen = len(max(menulinks[:2], key = len))
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[0])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[0]][:w-maxlen-2]+ResetAll)
    print(kleuren["LichtRood"]+("{:<%d}" % maxlen).format(menulinks[1])+kleuren["Blauw"]+": "+kleuren["LichtGroen"]+header[nieuwheaderlijst[1]][:w-maxlen-2]+ResetAll)

def haalalternatievenamen(rekening):
    categorieenlijst = haalcategorieen(rekening)
    alternatievenamendict = {}
    for i in categorieenlijst:
        with open(os.path.join(rekening,i)) as c:
            catnaam = ast.literal_eval(c.read())[0][0]
            alternatievenamendict[i] = catnaam
    return alternatievenamendict

def tooncategorieen(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    valuta = header[nieuwheaderlijst[4]]
    alternatievenamendict = haalalternatievenamen(rekening)
    for i in alternatievenamendict:
        with open(os.path.join(rekening,i), "r") as c:
            som = 0
            cat = ast.literal_eval(c.read())
            budget = cat[0][1]
            for j in cat[1:]:
                if int(nustr[:6]+"01") <= int(j[0]) <= int(nustr[:]+"31"):
                    som += j[1]
        som,forsom,K = grootgetal(som,fornum,"")
        bud,forbud,Kb = grootgetal(budget,fornum,"")
        print(catcol[i]+forcw(forc3(i)+forc15(vertaalv(alternatievenamendict[i]))+forc3(valuta)+forsom(som)+K+"/"+forc3(valuta)+forbud(bud)+Kb)+ResetAll)

def kleinegetalkleuren(getal):
    header = haalheader(rekening)
    ondergrens = header[nieuwheaderlijst[7]][0]
    bovengrens = header[nieuwheaderlijst[7]][1]
    kleuren,catcol = updatekleuren(rekening)
    if getal > bovengrens:
        getalkleur = kleuren["Omkeren"]+kleuren["colgoed"]
    elif getal > 0:
        getalkleur = kleuren["colgoed"]
    elif getal == 0:
        getalkleur = kleuren["colmatig"]
    elif getal < ondergrens:
        getalkleur = kleuren["Omkeren"]+kleuren["colslecht"]
    else:
        getalkleur = kleuren["colslecht"]
    return getalkleur

def grotegetalkleuren(rekening,header,getal):
    try:
        kleuren,catcol = updatekleuren(rekening)
        if getal >= 0:
            getalkleur = kleuren["colgoed"]
        else:
            getalkleur = kleuren["colslecht"]
    except(Exception) as f:
        #print(f)
        if getal >= 0:
            getalkleur = colgoed
        else:
            getalkleur = colslecht
    return getalkleur

def eenrekeningtotaal(rekening):
    header = haalheader(rekening)
    rekeningnaam = header[nieuwheaderlijst[0]]
    rekeninghouder = header[nieuwheaderlijst[1]]
    kleuren,catcol = updatekleuren(rekening)
    valuta = header[nieuwheaderlijst[4]]
    getal = rekeningsom(rekening)
    getalkleur = kleinegetalkleuren(getal)
    getal,forsom,K = grootgetal(getal,fornum,"")
    IBAN = rekening[:rekening.index("#")]
    if len(IBAN) > 20:
        toonIBAN = IBAN[:15]+"..."+IBAN[-2:]
    else:
        toonIBAN = IBAN
    JAAR = forr4(rekening[rekening.index("#")+1:])
    printstuff = kleuren["LichtGeel"]+kleuren["Omkeren"]+forc20(toonIBAN)+ResetAll+" "+kleuren["Geel"]+forl4(JAAR[:4])+ResetAll+" "+kleuren["coltekst"]+kleuren["Omkeren"]+forc21(rekeningnaam[:21])+ResetAll+" "+kleuren["coltekst"]+forc21(rekeninghouder[:21])+ResetAll+" "+getalkleur+valuta+" "+forsom(getal)+K+ResetAll
    print(printstuff)
    vrijbesteedbaar(rekening,header)
    return getal,forsom,K

def programmastart():
    with open("header","w") as h:
        print(nieuwheader, file = h, end = "")
    try:
        rekeningenlijst = rekeningenoverzicht()
        rekeningentotaal = toonrekeningsaldo(rekeningenlijst)
        rekening = kiesrekening(rekeningenlijst)
        if rekening == endederror:
            rekening = int(endederror)
    except(Exception) as f:
        #print(f)
        rekening = maaknieuwerekening()
    return rekening

def haalcategorie(rekening,cat):
    categorieenlijst = haalcategorieen(rekening)
    if cat in categorieenlijst:
        with open(os.path.join(rekening,cat),"r") as c:
            categorie = ast.literal_eval(c.read())
        return categorie
    else:
        return "<"

def schrijfcategorie(rekening,cat,categorie):
    kat = [categorie[0]]
    kate = sorted(categorie[1:])
    for i in kate:
        kat.append(i)
    with open(os.path.join(rekening,cat),"w") as c:
        print(kat, file = c, end = "")

def haalcategorieen(rekening):
    categorieenlijst = []
    for i in os.listdir(rekening):
        if i in lijst:
            categorieenlijst.append(i)
    categorieenlijst = sorted(categorieenlijst)
    return categorieenlijst

def haaltransacties(rekening,ok):
    categorieenlijst = haalcategorieen(rekening)
    ok = {}
    for i in categorieenlijst:
        if i in os.listdir(rekening):
            categorie = haalcategorie(rekening,i)
            categorienaambudget = categorie[0]
            categorietrans = sorted(categorie[1:])
            cat = [categorienaambudget]
            jndex = 0
            for j in categorietrans:
                cat.append(j)
                oki = i+str(jndex)
                jndex += 1
                ok[oki] = j
    return ok

def geefeendatum(rekening,header,col,ok,datum):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        elcat = elementenEN
        elcat.append(woordcategorieEN)
        maxlen = len(max(elcat,key = len))
    elif Taal == "IT":
        elcat = elementenIT
        elcat.append(woordcategorieIT)
        maxlen = len(max(elcat,key = len))
    else:
        elcat = elementen
        elcat.append(woordcategorie)
        maxlen = len(max(elcat,key = len))
    datumkeuze = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(elcat[0].upper())+ResetAll+inputindent)
    if datumkeuze.upper() in afsluitlijst:
        doei()
    elif datumkeuze.upper() in neelijst:
        return "<"
    elif datumkeuze.upper() == "*":
        return "*"
    else:
        test = checkdatum(datumkeuze)
        if test == True:
            transactiedatum = int(datumkeuze)
        else:
            if datumkeuze == "-":
                transactiedatum = standaardstartdatum
            elif datumkeuze == "+":
                transactiedatum = standaardeinddatum
            elif datumkeuze == "":
                transactiedatum = int(nustr) 
            elif datumkeuze.upper() == "M" and datum == int(nustr):
                transactiedatum = int(str(nustr[:6])+"01")
            elif datumkeuze.upper() == "W" and datum == int(nustr):
                transactiedatum = int(datetime.strftime(datetime.strptime(str(datum),"%Y%m%d") - timedelta(weeks = 1),"%Y%m%d"))
            elif len(datumkeuze) > 1 and datumkeuze[0].upper() in ["M","W"]:
                test = checkint(datumkeuze[1:])
                if test == True:
                    if datumkeuze[0].upper() == "M":
                        maandverschil = int(datumkeuze[1:])
                        maand = int(nustr[4:6])
                        jaar = int(nustr[:4])
                        while maandverschil > 0:
                            maand -= 1
                            if maand == 0:
                                maand = 12
                                jaar -= 1
                            maandverschil -= 1
                        transactiedatum = int("{:0>4}".format(jaar)+"{:0>2}".format(maand)+"01")
                    else:
                        transactiedatum = int(datetime.strftime(datetime.strptime(str(datum),"%Y%m%d") - timedelta(weeks = int(datumkeuze[1:])+1),"%Y%m%d"))
            elif len(datumkeuze) > 1 and datumkeuze[0] in ["-","+"]:
                test = checkint(datumkeuze[1:])
                if test == True:
                    if datumkeuze[0] == "-":
                        transactiedatum = int(datetime.strftime(datetime.strptime(str(datum),"%Y%m%d") - timedelta(days = int(datumkeuze[1:])),"%Y%m%d"))
                    else:
                        transactiedatum = int(datetime.strftime(datetime.strptime(str(datum),"%Y%m%d") + timedelta(days = int(datumkeuze[1:])),"%Y%m%d"))
                else:
                   transactiedatum = datum
            else:
                test = checkint(datumkeuze)
                if test == True:
                    transactiedatum = int(datetime.strftime(datetime.strptime(str(datum),"%Y%m%d") - timedelta(days = int(datumkeuze)),"%Y%m%d"))
                else:
                    transactiedatum = datum 
        toondatum = opmaakdatum(transactiedatum)
        printdatumlinks(transactiedatum)
        return transactiedatum

def geefdatumbereik(rekening,header,col,ok,datum):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    datumlijst = []
    if Taal == "EN":
        print("Start")
    elif Taal == "IT":
        print("Inizio")
    else:
        print("Start")
    startdatum = geefeendatum(rekening,header,col,ok,datum)
    if startdatum == "<":
        return "<"
    elif startdatum == "*":
        return [standaardstartdatum,standaardeinddatum]
    if Taal == "EN":
        print("End")
    elif Taal == "IT":
        print("Fine")
    else:
        print("Eind")
    einddatum = geefeendatum(rekening,header,col,ok,startdatum)
    if einddatum == "<":
        return "<"
    elif startdatum == "*":
        return [standaardstartdatum,standaardeinddatum]
    if startdatum <= einddatum:
        datumlijst.append(startdatum)
        datumlijst.append(einddatum)
    else:
        datumlijst.append(einddatum)
        datumlijst.append(startdatum)
    return datumlijst

def geefeenbedrag(rekening,header,col,ok,bedrag):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    if bedrag == standaardbodembedrag:
        transactiebedrag = standaardtopbedrag
        return transactiebedrag
    elif bedrag == header[nieuwheaderlijst[7]][0]:
        transactiebedrag = header[nieuwheaderlijst[7]][1]
        return transactiebedrag
    else:
        if Taal == "EN":
            elcat = elementenEN
            elcat.append(woordcategorieEN)
            maxlen = len(max(elcat,key = len))
        elif Taal == "IT":
            elcat = elementenIT
            elcat.append(woordcategorieIT)
            maxlen = len(max(elcat,key = len))
        else:
            elcat = elementen
            elcat.append(woordcategorie)
            maxlen = len(max(elcat,key = len))
        bedragkeuze = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(elcat[1].upper())+ResetAll+inputindent)
        if bedragkeuze.upper() in afsluitlijst:
            doei()
        elif bedragkeuze.upper() in neelijst:
            return "<"
        elif bedragkeuze.upper() == "*":
            return "*"
        else:
            test = checkfloat(bedragkeuze)
            if test == True:
                transactiebedrag = float(bedragkeuze)
            else:
                if bedragkeuze in ["-","+"] and bedrag != 0.0:
                    transactiebedrag = bedrag * -1
                elif bedragkeuze == "-":
                    transactiebedrag = standaardbodembedrag
                elif bedragkeuze == "+":
                    transactiebedrag = standaardtopbedrag
                elif bedragkeuze == "*" and bedrag == 0.0:
                    transactiebedrag = standaardbodembedrag
                elif bedragkeuze == "" and bedrag != 0.0:
                    transactiebedrag = bedrag
                else:
                    transactiebedrag = header[nieuwheaderlijst[7]][0]
            K = ""
            toongetal,forsom,K = grootgetal(transactiebedrag,fornum,K)
            print(col+valuta+forsom(toongetal)+K+ResetAll)
            return transactiebedrag

def geefbedragbereik(rekening,header,col,ok,bedrag):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    bedraglijst = []
    if Taal == "EN":
        print("Bottom")
    elif Taal == "IT":
        print("Inferiore")
    else:
        print("Bodem")
    bodembedrag = geefeenbedrag(rekening,header,col,ok,bedrag)
    if bodembedrag == "<":
        return "<"
    elif bodembedrag == "*":
        return [standaardbodembedrag,standaardtopbedrag]
    if bodembedrag == header[nieuwheaderlijst[7]][0]:
        topbedrag = header[nieuwheaderlijst[7]][1]
        if Taal == "EN":
            print("Top")
        elif Taal == "IT":
            print("Superiore")
        else:
            print("Top")
        K = ""
        toongetal,forsom,K = grootgetal(topbedrag,fornum,K)
        print(col+valuta+forsom(toongetal)+K+ResetAll)
    else:
        if Taal == "EN":
            print("Top")
        elif Taal == "IT":
            print("Superiore")
        else:
            print("Top")
        topbedrag = geefeenbedrag(rekening,header,col,keuze1lijst,ok,bodembedrag)
    if topbedrag == "<":
        return "<"
    elif topbedrag == "*":
        return [standaardbodembedrag,standaardtopbedrag]
    if bodembedrag <= topbedrag:
        bedraglijst.append(bodembedrag)
        bedraglijst.append(topbedrag)
    else:
        bedraglijst.append(topbedrag)
        bedraglijst.append(bodembedrag)
    return bedraglijst

def geefwederpartij(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        elcat = elementenEN
        elcat.append(woordcategorieEN)
        maxlen = len(max(elcat,key = len))
    elif Taal == "IT":
        elcat = elementenIT
        elcat.append(woordcategorieIT)
        maxlen = len(max(elcat,key = len))
    else:
        elcat = elementen
        elcat.append(woordcategorie)
        maxlen = len(max(elcat,key = len))
    wederpartij = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(elcat[2].upper())+ResetAll+inputindent)
    if wederpartij.upper() in afsluitlijst:
        doei()
    elif wederpartij.upper() in neelijst:
        wederpartij = "<"
    elif wederpartij == "*":
        wederpartij = ""
    return wederpartij

def geefonderwerp(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        elcat = elementenEN
        elcat.append(woordcategorieEN)
        maxlen = len(max(elcat,key = len))
    elif Taal == "IT":
        elcat = elementenIT
        elcat.append(woordcategorieIT)
        maxlen = len(max(elcat,key = len))
    else:
        elcat = elementen
        elcat.append(woordcategorie)
        maxlen = len(max(elcat,key = len))
    onderwerp = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(elcat[3].upper())+ResetAll+inputindent)
    if onderwerp.upper() in afsluitlijst:
        doei()
    elif onderwerp.upper() in neelijst:
        onderwerp = "<"
    elif onderwerp == "*":
        onderwerp = ""
    return onderwerp

def geefcategorie(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    categoriekeuzelijst = []
    if Taal == "EN":
        elcat = elementenEN
        elcat.append(woordcategorieEN)
        maxlen = len(max(elcat,key = len))
    elif Taal == "IT":
        elcat = elementenIT
        elcat.append(woordcategorieIT)
        maxlen = len(max(elcat,key = len))
    else:
        elcat = elementen
        elcat.append(woordcategorie)
        maxlen = len(max(elcat,key = len))
    tooncategorieen(rekening,header)
    categoriekeuze = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(elcat[4].upper())+ResetAll+inputindent)
    if categoriekeuze.upper() in afsluitlijst:
        doei()
    elif categoriekeuze.upper() in neelijst:
        categoriekeuze = "<"
        return "<"
    elif categoriekeuze == "*":
        categoriekeuze = lijst
    else:
        for i in categoriekeuze:
            if i.upper() in lijst:
                categoriekeuzelijst.append(i.upper())
        if categoriekeuzelijst == []:
            categoriekeuzelijst = lijst
    return categoriekeuzelijst

def vertaalmnd(datum):
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        mnd = str(datum)[4:6]\
        .replace("01","Jan")\
        .replace("02","Feb")\
        .replace("03","Mar")\
        .replace("04","Apr")\
        .replace("05","May")\
        .replace("06","Jun")\
        .replace("07","Jul")\
        .replace("08","Aug")\
        .replace("09","Sep")\
        .replace("10","Oct")\
        .replace("11","Nov")\
        .replace("12","Dec")
    elif Taal == "IT":
        mnd = str(datum)[4:6]\
        .replace("01","gen")\
        .replace("02","feb")\
        .replace("03","mar")\
        .replace("04","apr")\
        .replace("05","mag")\
        .replace("06","giu")\
        .replace("07","lug")\
        .replace("08","ago")\
        .replace("09","set")\
        .replace("10","ott")\
        .replace("11","nov")\
        .replace("12","dic")
    else:
        mnd = str(datum)[4:6]\
        .replace("01","jan")\
        .replace("02","feb")\
        .replace("03","mrt")\
        .replace("04","apr")\
        .replace("05","mei")\
        .replace("06","jun")\
        .replace("07","jul")\
        .replace("08","aug")\
        .replace("09","sep")\
        .replace("10","okt")\
        .replace("11","nov")\
        .replace("12","dec")
    return mnd

def haalopmaakdatumdict(datum):
    mnd = vertaalmnd(datum)
    opmaakdatumdict = {
        opmaakdatumlijst[0]: str(datum),
        opmaakdatumlijst[1]: str(datum)[6:]+str(datum)[4:6]+str(datum)[:4],
        opmaakdatumlijst[2]: str(datum)[2:4]+"-"+str(datum)[4:6]+"-"+str(datum)[6:],
        opmaakdatumlijst[3]: str(datum)[6:]+"-"+str(datum)[4:6]+"-"+str(datum)[2:4],
        opmaakdatumlijst[4]: str(datum)[6:]+"/"+str(datum)[4:6]+"/"+str(datum)[2:4],
        opmaakdatumlijst[5]: str(datum)[6:]+"-"+mnd+str(datum)[2:4],
        opmaakdatumlijst[6]: str(datum)[6:]+mnd+"\'"+str(datum)[2:4]
    }
    return opmaakdatumdict

def toondatumopmaakopties(datum):
    header = haalheader(rekening)
    datumopmaak = header[nieuwheaderlijst[9]]
    opmaakdatumdict = haalopmaakdatumdict(datum)
    tel = 0
    for i in opmaakdatumdict:
        print(forr3(tel)+" : %s (%s)" % (i,opmaakdatumdict[i]))
        tel += 1

def opmaakdatum(datum):
    header = haalheader(rekening)
    datumopmaak = header[nieuwheaderlijst[9]]
    opmaakdatumdict = haalopmaakdatumdict(datum)
    try:
        for i in opmaakdatumdict:
            datum = opmaakdatumdict[datumopmaak]
    except(Exception) as f:
        #print(f)
        pass
    return datum

def geefsneltoets(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    noodok = {}
    dezeweekeerste = int(datetime.strftime(datetime.strptime(nustr,"%Y%m%d")-timedelta(weeks = 1),"%Y%m%d"))
    dezeweek = [dezeweekeerste,int(nustr)]
    dezemaandeerste = int(nustr[:6] + "01")
    dezemaandeind = calendar.monthrange(int(str(dezemaandeerste)[:4]),int(str(dezemaandeerste)[4:6]))[1]
    dezemaandlaatste = int(str(dezemaandeerste)[:6]+str(dezemaandeind))
    dezemaand = [dezemaandeerste,dezemaandlaatste]
    for i in ok:
        noodok[i] = ok[i]
    ok = haaltransacties(rekening,ok)
    if Taal == "EN":
        wraptekst = textwrap.wrap("Type shortkey or skip",w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Digita tasto rapido o salta",w)
    else:
        wraptekst = textwrap.wrap("Typ sneltoets of sla over",w)
    print(col+kleuren["Omkeren"], end = "")
    for i in wraptekst:
        print(i)
    print(ResetAll, end = "")
    if Taal == "EN":
        print("*, #, MI, MO, M{number}, WI, WO, W{number}, %s" % woordcategorieEN.lower())
    elif Taal == "IT":
        print("*, #, MI, MO, M{numero}, WI, WO, W{numero}, %s" % woordcategorieIT.lower())
    else:
        print("*, #, MI, MO, M{getal}, WI, WO, W{getal}, %s" % woordcategorie.lower())
    sneltoets = input(col+inputindent)
    print(ResetAll, end = "")
    if sneltoets.upper() in afsluitlijst:
        doei()
    elif sneltoets.upper() in neelijst:
        return "<",ok,[],[],"","",lijst
    elif sneltoets.upper() == "*":
        datumlijst = [standaardstartdatum,standaardeinddatum]
        bedraglijst = [standaardbodembedrag,standaardtopbedrag]
    elif sneltoets.upper() == "#":
        datumlijst = [standaardstartdatum,standaardeinddatum]
        bedraglijst = [standaardbodembedrag,standaardtopbedrag]
        wederpartij = ""
        onderwerp = "#"
        categoriekeuzelijst = lijst
        return sneltoets,ok,datumlijst,bedraglijst,wederpartij,onderwerp,categoriekeuzelijst
    elif sneltoets.upper() in lijst:
        startdatum = int(nustr[:6]+"01")
        maandeind = calendar.monthrange(int(str(startdatum)[:4]),int(str(startdatum)[4:6]))[1]
        einddatum = int(str(startdatum)[:6]+str(maandeind))
        datumlijst = [startdatum,einddatum]
        bedraglijst = [standaardbodembedrag,standaardtopbedrag]
        wederpartij = ""
        onderwerp = ""
        categoriekeuzelijst = [sneltoets.upper()]
        return sneltoets,ok,datumlijst,bedraglijst,wederpartij,onderwerp,categoriekeuzelijst
    elif len(sneltoets) > 1 and sneltoets[0].upper() in ["M","W"]:
        if sneltoets[0].upper() == "M":
            test = checkint(sneltoets[1:])
            if test == True:
                maandverschil = int(sneltoets[1:])
                maand = int(nustr[4:6])
                jaar = int(nustr[:4])
                while maandverschil > 0:
                    maand -= 1
                    if maand == 0:
                        maand = 12
                        jaar -= 1
                    maandverschil -= 1
                startdatum = int("{:0>4}".format(jaar)+"{:0>2}".format(maand)+"01")
                maandeind = calendar.monthrange(int(str(startdatum)[:4]),int(str(startdatum)[4:6]))[1]
                einddatum = int(str(startdatum)[:6]+str(maandeind))
                datumlijst = [startdatum,einddatum]
                bedraglijst = [standaardbodembedrag,standaardtopbedrag]
            elif sneltoets[1:].upper() == "I":
                datumlijst = dezemaand
                bedraglijst = [0.0,standaardtopbedrag]
            elif sneltoets[1:].upper() == "O":
                datumlijst = dezemaand
                bedraglijst = [standaardbodembedrag,0.0]
            else:
                datumlijst = dezemaand
                bedraglijst = [standaardbodembedrag,standaardtopbedrag]
        else:
            test = checkint(sneltoets[1:])
            if test == True:
                weekverschil = int(sneltoets[1:])+1
                startdatum = int(datetime.strftime(datetime.strptime(nustr,"%Y%m%d")-timedelta(weeks = weekverschil),"%Y%m%d"))
                einddatum = int(nustr)
                datumlijst = [startdatum,einddatum]
                bedraglijst = [standaardbodembedrag,standaardtopbedrag]
            elif sneltoets[1:].upper() == "I":
                datumlijst = dezeweek
                bedraglijst = [0.0,standaardtopbedrag]
            elif sneltoets[1:].upper() == "O":
                datumlijst = dezeweek
                bedraglijst = [standaardbodembedrag,0.0]
            else:
                datumlijst = dezeweek
                bedraglijst = [standaardbodembedrag,standaardtopbedrag]
    else:
        sneltoets = False
        datumlijst = [dezemaandeerste,int(nustr)]
        bedraglijst = [standaardbodembedrag,standaardtopbedrag]
    wederpartij = ""
    onderwerp = ""
    categoriekeuzelijst = lijst
    return sneltoets,ok,datumlijst,bedraglijst,wederpartij,onderwerp,categoriekeuzelijst

def printselectie(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    noodok = {}
    for i in ok:
        noodok[i] = ok[i]
    ok = haaltransacties(rekening,ok)
    printdatum(nustr)
    sneltoets,ok,datumlijst,bedraglijst,wederpartij,onderwerp,categoriekeuzelijst = geefsneltoets(rekening,header,col,ok)
    if sneltoets == False:
        datumlijst = geefdatumbereik(rekening,header,col,ok,int(nustr))
        if datumlijst == "<":
            ok = noodok
            return rekening,header,col,keuze1lijst,ok
        ok = filterdatumlijst(datumlijst,ok)
        bedraglijst = geefbedragbereik(rekening,header,col,ok,0.0)
        if bedraglijst == "<":
            ok = noodok
            return rekening,header,col,keuze1lijst,ok
        ok = filterbedraglijst(bedraglijst,ok)
        wederpartij = geefwederpartij(rekening,header,col,ok)
        if wederpartij == "<":
            ok = noodok
            return rekening,header,col,keuze1lijst,ok
        ok = filterwederpartij(wederpartij,ok)
        onderwerp = geefonderwerp(rekening,header,col,ok)
        if onderwerp == "<":
            ok = noodok
            return rekening,header,col,keuze1lijst,ok
        ok = filteronderwerp(onderwerp,ok)
        categoriekeuzelijst = geefcategorie(rekening,header,col,ok)
        if categoriekeuzelijst == "<":
            ok = noodok
            return rekening,header,col,keuze1lijst,ok
        ok = filtercategorie(categoriekeuzelijst,ok)
    elif sneltoets == "<":
        return rekening,header,col,keuze1lijst,{}
    else:
        ok = filterdatumlijst(datumlijst,ok)
        ok = filterbedraglijst(bedraglijst,ok)
        ok = filterwederpartij(wederpartij,ok)
        ok = filteronderwerp(onderwerp,ok)
        ok = filtercategorie(categoriekeuzelijst,ok)
    scheidingslijn = "+"+"-"*6+"+"+"-"*10+"+"+"-"*10+"+"+"-"*14+"+"+"-"*34+"+"
    forni = "{0:>.2f}".format
    forno = "{0:>.2f}".format
    if datumlijst[0] == standaardstartdatum:
        datumlijst[0] = "-*"
    if datumlijst[1] == standaardeinddatum:
        datumlijst[1] = "+*"
    if bedraglijst[0] == standaardbodembedrag:
        bedraglijst[0] = "-*"
        forno = "{:}".format
    if bedraglijst[1] == standaardtopbedrag:
        bedraglijst[1] = "+*"
        forni = "{:}".format
    strcategoriekeuzelijst = ""
    for i in categoriekeuzelijst:
        strcategoriekeuzelijst += i
    if wederpartij == "":
        wederpartij = "*"
    if onderwerp == "":
        onderwerp = "*"
    if categoriekeuzelijst == lijst:
        strcategoriekeuzelijst = "*"
    if Taal == "EN":
        kopregel = forc78((elementenEN[0][:3]+": "+str(datumlijst[0])+">=<"+str(datumlijst[1])+", "+elementenEN[1][:3]+": "+valuta+" "+forno(bedraglijst[0])+">=<"+valuta+" "+forni(bedraglijst[1])+", "+elementenEN[2][:3]+": "+wederpartij+", "+elementenEN[3][:3]+": "+onderwerp+", "+strcategoriekeuzelijst)[:78])
        elementenlijn = forr5("ID")+" :"+forc10(elementenEN[0])+" "+forc10(elementenEN[1])+forr15(elementenEN[2])+" "+forl34(elementenEN[3])
    elif Taal == "IT":
        kopregel = forc78((elementenIT[0][:3]+": "+str(datumlijst[0])+">=<"+str(datumlijst[1])+", "+elementenIT[1][:3]+": "+valuta+" "+forno(bedraglijst[0])+">=<"+valuta+" "+forni(bedraglijst[1])+", "+elementenIT[2][:3]+": "+wederpartij+", "+elementenIT[3][:3]+": "+onderwerp+", "+strcategoriekeuzelijst)[:78])
        elementenlijn = forr5("ID")+" :"+forc10(elementenIT[0])+" "+forc10(elementenIT[1])+forr15(elementenIT[2])+" "+forl34(elementenIT[3])
    else:
        kopregel = forc78((elementen[0][:3]+": "+str(datumlijst[0])+">=<"+str(datumlijst[1])+", "+elementen[1][:3]+": "+valuta+" "+forno(bedraglijst[0])+">=<"+valuta+" "+forni(bedraglijst[1])+", "+elementen[2][:3]+": "+wederpartij+", "+elementen[3][:3]+": "+onderwerp+", "+strcategoriekeuzelijst)[:78])
        elementenlijn = forr5("ID")+" :"+forc10(elementen[0])+" "+forc10(elementen[1])+forr15(elementen[2])+" "+forl34(elementen[3])
    if Taal == "EN":
        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menuEN["1,0,1"],
          menuEN["1,0,2"],
          menuEN["1,0,3"],
          menuEN["1,0,4"],
          menuEN["1,0,5"],
          menuEN["1,0,6"],
          menuEN["1,0,7"],
          menuEN["1,0,8"]
          )
    )
    elif Taal == "IT":
        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menuIT["1,0,1"],
          menuIT["1,0,2"],
          menuIT["1,0,3"],
          menuIT["1,0,4"],
          menuIT["1,0,5"],
          menuIT["1,0,6"],
          menuIT["1,0,7"],
          menuIT["1,0,8"]
          )
    )
    else:
        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menu["1,0,1"],
          menu["1,0,2"],
          menu["1,0,3"],
          menu["1,0,4"],
          menu["1,0,5"],
          menu["1,0,6"],
          menu["1,0,7"],
          menu["1,0,8"]
          )
    )
    sorteren = input(col+inputindent)
    print(ResetAll, end = "")
    if sorteren.upper() in afsluitlijst:
        doei()
    elif sorteren.upper() in neelijst:
        return rekening,header,col,keuze1lijst,ok
    elif sorteren == "1":
        ok = sortokdatumreverse(rekening,ok)
    elif sorteren == "2":
        ok = sortokdatum(rekening,ok)
    elif sorteren == "3":
        ok = sortokbedragreverse(rekening,ok)
    elif sorteren == "4":
        ok = sortokbedrag(rekening,ok)
    elif sorteren == "5":
        ok = sortokwederpartijreverse(rekening,ok)
    elif sorteren == "6":
        ok = sortokwederpartij(rekening,ok)
    elif sorteren == "7":
        ok = sortokonderwerpreverse(rekening,ok)
    elif sorteren == "8":
        ok = sortokonderwerp(rekening,ok)
    else:
        pass
    ########## print naar scherm start ##########
    print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"])
    print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], end = "")
    print(kopregel, end = "")
    print(kleuren["coltoon"]+"|"+kleuren["ResetAll"])
    print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"])
    print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], end = "")
    print(elementenlijn, end = "")
    print(kleuren["coltoon"]+"|"+kleuren["ResetAll"])
    print(kleuren["coltoon"]+scheidingslijn+kleuren["ResetAll"])
    for i in ok:
        K = ""
        forsom = fornum
        getal = ok[i][1]
        keen,forsom,K = grootgetal(getal,forsom,K)
        datum = ok[i][0]
        mnd = vertaalmnd(datum)
        datum = opmaakdatum(datum)
        #transactielijnzw = "|"+forr5(i)+" :"+forc10(datum)+" "+forl2(valuta)+forsom(keen)+K+" "+forr14(ok[i][2][:14])+" "+forl34(ok[i][3][:34])+"|" # Uncomment bij print naar file
        #print(transactielijnzw, file = m)                                                                                                             # Uncomment bij print naar file
        transactielijn = kleuren["coltoon"]+"|"+kleuren["ResetAll"]+catcol[i[0]]+forr5(i)+kleuren["ResetAll"]+" :"+forc10(datum)+" "+kleinegetalkleuren(getal)+forl2(valuta)+kleuren["ResetAll"]+forsom(keen)+K+" "+forr14(ok[i][2][:14])+" "+catcol[i[0]]+forl34(ok[i][3][:34])+kleuren["ResetAll"]+kleuren["coltoon"]+"|"+kleuren["ResetAll"] # COMMENT BIJ PRINT NAAR FILE OF WEGHALEN
        print(transactielijn) # COMMENT BIJ PRINT NAAR FILE OF WEGHALEN
    print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"])
    ########## print naar scherm stop ##########
    if header[nieuwheaderlijst[12]] == ">" and len(str(datumlijst[0])) == 8 and str(datumlijst[0])[:6] == str(datumlijst[1])[:6]:
        kleuren,catcol,getalkleur = printkleuren() ########## deze regel haalt de kleuren weg voor "print naar file". HERHAAL DEZE LIJN DIRECT BOVEN transactielijn = !!
        col = ""
        with open(os.path.join(rekening,str(datumlijst[0])[:6]),"w") as m:
            ########## print naar file start ########## bij aanpassingen, wijzig eerst "print naar scherm" en kopieer dat naar hieronder. Eindig iedere print() met ", file = m"
            print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"], file = m)
            print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], end = "", file = m)
            print(kopregel, end = "", file = m)
            print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], file = m)
            print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"], file = m)
            print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], end = "", file = m)
            print(elementenlijn, end = "", file = m)
            print(kleuren["coltoon"]+"|"+kleuren["ResetAll"], file = m)
            print(kleuren["coltoon"]+scheidingslijn+kleuren["ResetAll"], file = m)
            for i in ok:
                K = ""
                forsom = fornum
                getal = ok[i][1]
                keen,forsom,K = grootgetal(getal,forsom,K)
                datum = ok[i][0]
                mnd = vertaalmnd(datum)
                datum = opmaakdatum(datum)
                transactielijnzw = "|"+forr5(i)+" :"+forc10(datum)+" "+forl2(valuta)+forsom(keen)+K+" "+forr14(ok[i][2][:14])+" "+forl34(ok[i][3][:34])+"|" # Uncomment bij print naar file
                print(transactielijnzw, file = m)                                                                                                             # Uncomment bij print naar file
                #transactielijn = kleuren["coltoon"]+"|"+kleuren["ResetAll"]+catcol[i[0]]+forr5(i)+kleuren["ResetAll"]+" :"+forc10(datum)+" "+kleinegetalkleuren(getal)+forl2(valuta)+kleuren["ResetAll"]+forsom(keen)+K+" "+forr14(ok[i][2][:14])+" "+catcol[i[0]]+forl34(ok[i][3][:34])+kleuren["ResetAll"]+kleuren["coltoon"]+"|"+kleuren["ResetAll"] # COMMENT BIJ PRINT NAAR FILE OF WEGHALEN
                #print(transactielijn) # COMMENT BIJ PRINT NAAR FILE OF WEGHALEN
            print(kleuren["coltoon"]+toplijn+kleuren["ResetAll"], file = m)
            ########## print naar file stop ##########
    if datumlijst[0] == datumlijst[1]:
        dagtotaal(rekening,header,col,datumlijst[0])
    if len(categoriekeuzelijst) == 1:
        samenvattingcategorie(rekening,categoriekeuzelijst[0],datumlijst)
    return rekening,header,col,keuze1lijst,ok

def samenvattingcategorie(rekening,cat,datumlijst):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    categorie = haalcategorie(rekening,cat)
    if categorie == "<":
        return
    som = 0
    tel = 0
    dezecategoriedezemaand = []
    if datumlijst[0] == "-*":
        datumlijst[0] = standaardstartdatum
    if datumlijst[1] == "+*":
        datumlijst[1] = standaardeinddatum
    for i in categorie[1:]:
        if datumlijst[0] <= i[0] <= datumlijst[1]:
            dezecategoriedezemaand.append(i)
            som += i[1]
            tel += 1
    if Taal == "EN":
        woorden = ["Total","Budget","Percent","Average","Count"]
    elif Taal == "IT":
        woorden = ["Totale","Budget","Percentuale","Media","Numero"]
    else:
        woorden = ["Totaal","Budget","Procent","Gemiddeld","Aantal"]
    maxlen = len(max(woorden, key = len))
    budget = categorie[0][1]
    if tel != 0:
        gemiddeld = som/tel
    procent = som/categorie[0][1]*-100
    if procent > 100:
        procentkleur = kleuren["colslecht"]
    else:
        procentkleur = kleuren["colgoed"]
    print(" "*10+col+"+-"+kleuren["Omkeren"]+catcol[cat]+cat+kleuren["ResetAll"]+col+"-"*(maxlen-(len(cat)))+"+"+"-"*10+kleuren["ResetAll"])
    print(" "*10+col+"| "+kleuren["ResetAll"]+catcol[cat]+("{:^%d}" % (maxlen+11)).format(vertaalv(categorie[0][0]))+kleuren["ResetAll"])
    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(woorden[0])+kleuren["ResetAll"]+": "+grotegetalkleuren(rekening,header,som)+valuta+kleuren["ResetAll"]+fornum(som))
    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(woorden[1])+kleuren["ResetAll"]+": "+grotegetalkleuren(rekening,header,budget)+valuta+kleuren["ResetAll"]+fornum(budget))
    if budget != budgetnul:
        print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(woorden[2])+kleuren["ResetAll"]+": "+procentkleur+"%"+kleuren["ResetAll"]+fornum(procent))
    if tel != 0:
        print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(woorden[3])+kleuren["ResetAll"]+": "+kleinegetalkleuren(gemiddeld)+valuta+kleuren["ResetAll"]+fornum(gemiddeld))
    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(woorden[4])+kleuren["ResetAll"]+": "+forr6(tel))
    print(" "*10+col+"+-"+"-"*maxlen+"+"+"-"*10+kleuren["ResetAll"])


def dagtotaal(rekening,header,col,datum):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    categorieenlijst = haalcategorieen(rekening)
    som = header[nieuwheaderlijst[5]]
    for cat in categorieenlijst:
        categorie = haalcategorie(rekening,cat)   
        for trans in categorie[1:]:
            if trans[0] <= datum:
                som += trans[1]
    if Taal == "EN":
        print("%sDay total on %s:%s" % (col,opmaakdatum(datum),kleuren["ResetAll"]),kleuren["Omkeren"]+grotegetalkleuren(rekening,header,round(som,2))+valuta+fornum(round(som,2))+kleuren["ResetAll"])
    elif Taal == "IT":
        print("%sTotale giornaliero per %s:%s" % (col,opmaakdatum(datum),kleuren["ResetAll"]),kleuren["Omkeren"]+grotegetalkleuren(rekening,header,round(som,2))+valuta+fornum(round(som,2))+kleuren["ResetAll"])
    else:
        print("%sDagtotaal op %s:%s" % (col,opmaakdatum(datum),kleuren["ResetAll"]),kleuren["Omkeren"]+grotegetalkleuren(rekening,header,round(som,2))+valuta+fornum(round(som,2))+kleuren["ResetAll"])

def printkleuren():
    kleuren = {
            "ResetAll":"",
            "Omkeren":"",
            "Rood":"",
            "Groen":"",
            "Geel":"",
            "Blauw":"",
            "Magenta":"",
            "Cyaan":"",
            "LichtGrijs":"",
            "DonkerGrijs":"",
            "LichtRood":"",
            "LichtGroen":"",
            "LichtGeel":"",
            "LichtBlauw":"",
            "LichtMagenta":"",
            "LichtCyaan":"",
            "Wit":"",
            "colgoed":"",
            "colslecht":"",
            "colmatig":"",
            "colonbepaald":"",
            "colhuh":"",
            "coltoe":"",
            "coltoon":"",
            "colwijzig":"",
            "colverwijder":"",
            "coltekst":"",
            "0":"",
            "1":"",
            "2":"",
            "3":"",
            "4":"",
            "5":"",
            "6":"",
            "7":"",
            "8":"",
            "9":"",
            "Q":""
            }
    catcol = {
            "0":"",
            "1":"",
            "2":"",
            "3":"",
            "4":"",
            "5":"",
            "6":"",
            "7":"",
            "8":"",
            "9":"",
            "A":"",
            "B":"",
            "C":"",
            "D":"",
            "E":"",
            "F":"",
            "G":"",
            "H":"",
            "I":"",
            "J":"",
            "K":"",
            "L":"",
            "M":"",
            "N":"",
            "O":""
            }
    getalkleur = ""
    return kleuren,catcol,getalkleur

def maandanalyse(rekening,datumlijst):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    nul = header[nieuwheaderlijst[8]]
    if Taal == "EN":
        print("Give the number of months in the past")
    elif Taal == "IT":
        print("Inserisci il numero di mesi nel passato")
    else:
        print("Geef het aantal maanden in het verleden")
    print(col, end = "")
    datumkeuze = input(inputindent)
    print(ResetAll,end = "")
    try:
        maandverschil = int(datumkeuze)
        maand = int(nustr[4:6])
        jaar = int(nustr[:4])
        while maandverschil > 0:
            maand = int(maand)-1
            if maand == 0:
                maand = 12
                jaar = jaar-1
            maandverschil -= 1
        startdatum = int("{:0>4}".format(jaar)+"{:0>2}".format(maand)+"01")
        datumlijst[0] = str(startdatum)
    except(Exception) as f:
        #print(f)
        pass
    maandeind = str(calendar.monthrange(int(str(datumlijst[0])[:4]),int(str(datumlijst[0])[4:6]))[1])
    datumlijst[1] = datumlijst[0][:6]+maandeind
    print("%s%s >=< %s%s" % (col,datumlijst[0],datumlijst[1],kleuren["ResetAll"]))
    totaalsaldo,forsomtotaal,Kt = eenrekeningtotaal(rekening)
    somal = 0
    budgetnegatief = budgetnul*-1
    categorieenlijst = haalcategorieen(rekening)
    budgetcategorieenlijst = []
    budgetcategorieensom = budgetnul
    if Taal == "EN":
        Bud = "%s bud" % (valuta)
    elif Taal == "IT":
        Bud = "%s bud" % (valuta)
    else:
        Bud = "%s bud" % (valuta)
    if Taal == "EN":
        Tot = "%s tot" % (valuta)
    elif Taal == "IT":
        Tot = "%s tot" % (valuta)
    else:
        Tot = "%s tot" % (valuta)
    honderdprocent = 44
    if honderdprocent % 2 == 0:
        off = ""
    else:
        off = "-"
    analyselijn = col+"+"+"-"*3+forc9(Tot)+"<0%--"+"-"*int((honderdprocent-12)/2)+"-+"+"-"*int(((honderdprocent-12)/2))+off+"100%>"+forc9(Bud)+"-"*13+"+"+kleuren["ResetAll"]
    analyselijnzw = "+"+"-"*3+forc9(Tot)+"<0%--"+"-"*int((honderdprocent-12)/2)+"-+"+"-"*int(((honderdprocent-12)/2))+off+"100%>"+forc9(Bud)+"-"*13+"+"
    print(analyselijn)
    if header[nieuwheaderlijst[12]] == ">" and str(datumlijst[0])[:6] == str(datumlijst[1])[:6]:
        with open(os.path.join(rekening,str(datumlijst[0])[:6])+"a","w") as a:
            print(analyselijnzw, file = a)
    for i in categorieenlijst:
        forsom = fornum
        K = ""
        forbud = fornum
        Kb = ""
        categorie = haalcategorie(rekening,i)
        budget = categorie[0][1]
        if budget < 0:
            budgetnegatief += budget
            budgetcategorieenlijst.append(i)
            for j in categorie[1:]:
                budgetcategorieensom += j[1]
        elif budget == 0:
            budgetnegatief = budgetnul * -1
        if budgetnegatief == 0:
            budgetnegatief = budgetnul * -1
        aantal = 0
        som = 0
        categorieinhoudgeselecteerdemaand = []
        for d in categorie[1:]:
            if int(str(datumlijst[0])[:6]+"01") <= d[0] <= int(str(datumlijst[1])[:6]+maandeind):
                categorieinhoudgeselecteerdemaand.append(d)
        if len(categorieinhoudgeselecteerdemaand) > 0:
            for j in categorieinhoudgeselecteerdemaand:
                som += j[1]
                aantal += 1
        if i in budgetcategorieenlijst:
            if som*-1 < budget:
                somal += (som+budget)
        else:
            somal += som
        if aantal == 0:
            aantal = ""
        if budget < som*-1:
            getalkleur = kleuren["colslecht"]
        elif budget >= som*-1:
            getalkleur = kleuren["colgoed"]
        streepje = budget/honderdprocent*-1
        aantalstreepjes = int(round(som/streepje))
        if som * budget > 0:
            aantalstreepjes = aantalstreepjes * -1
            getalkleur = kleuren["colhuh"]
        budget,forbud,Kb = grootgetal(budget,forsom,K)
        aantalstreepjesbovenbudget = 0
        if aantalstreepjes > honderdprocent:
            aantalstreepjesbovenbudget = aantalstreepjes - honderdprocent
            aantalstreepjes = honderdprocent
        som,forsom,K = grootgetal(som,forsom,K)
        lenstraant = 0
        if aantalstreepjes == 0:
            lenstraant = len(str(aantal))
        maandlijndezecategorie = col+"|"+kleuren["ResetAll"]+\
                kleuren["Omkeren"]+catcol[i]+" "+i+kleuren["ResetAll"]+" "+\
                getalkleur+valuta+kleuren["ResetAll"]+forsom(som)+K+\
                getalkleur+"-"*(aantalstreepjes-len(str(aantal)))+catcol[i]+str(aantal)+kleuren["ResetAll"]+" "*(honderdprocent-aantalstreepjes-lenstraant)+\
                catcol[i]+valuta+forbud(budget)+Kb+kleuren["ResetAll"]+\
                getalkleur+forl11("-"*aantalstreepjesbovenbudget)[:11]+kleuren["ResetAll"]+\
                kleuren["Omkeren"]+catcol[i]+i+" "+kleuren["ResetAll"]+\
                col+"|"+kleuren["ResetAll"]
        maandlijndezecategoriezw = "|"+\
                " "+i+" "+\
                valuta+forsom(som)+K+\
                "-"*(aantalstreepjes-len(str(aantal)))+str(aantal)+" "*(honderdprocent-aantalstreepjes-lenstraant)+\
                valuta+forbud(budget)+Kb+\
                forl11("-"*aantalstreepjesbovenbudget)[:11]+\
                i+" "+\
                "|"
        if nul == "<" and len(categorieinhoudgeselecteerdemaand) == 0:
            maandlijndezecategorie = ""
            maandlijndezecategoriezw = ""
        if maandlijndezecategorie != "":
            print(maandlijndezecategorie)
        if header[nieuwheaderlijst[12]] == ">" and str(datumlijst[0])[:6] == str(datumlijst[1])[:6]:
            with open(os.path.join(rekening,str(datumlijst[0])[:6])+"a","a") as a:
                print(maandlijndezecategoriezw, file = a)
    print(analyselijn)
    if Taal == "EN":
        voortgang = ("Score %s" % (str(datumlijst[0])[4:6]))[:12]
    elif Taal == "IT":
        voortgang = ("Score %s" % (str(datumlijst[0])[4:6]))[:12]
    else:
        voortgang = ("Score %s" % (str(datumlijst[0])[4:6]))[:12]
    if budgetcategorieensom + budgetnegatief >= 0:
        binnen = "+"
        colbinnen = kleuren["Omkeren"]+kleuren["colgoed"]
    else:
        binnen = "-"
        colbinnen = kleuren["Omkeren"]+kleuren["colslecht"]
    score = somal/budgetnegatief
    somal,forsom,K = grootgetal(somal,forsom,K)
    aantalstreepjes = int(round(score * honderdprocent))
    if score < 0:
        aantalstreepjes *= -1
        getalkleur = kleuren["colhuh"]
    if aantalstreepjes > honderdprocent:
        getalkleur = kleuren["colslecht"]
    else:
        getalkleur = kleuren["colgoed"]
    if aantalstreepjes >= 56:
        aantalstreepjes = 56
    if aantalstreepjes == 0:
        aantalstreepjes = 1
    print(col+"|"+kleuren["ResetAll"]+getalkleur+forl12(voortgang)+kleuren["Omkeren"]+"#"*(aantalstreepjes-1)+"|"+valuta+forsom(somal)+K+kleuren["ResetAll"]+" "*(56-aantalstreepjes)+colbinnen+binnen+kleuren["ResetAll"]+col+"|"+kleuren["ResetAll"])
    print(analyselijn)
    if header[nieuwheaderlijst[12]] == ">" and str(datumlijst[0])[:6] == str(datumlijst[1])[:6]:
        with open(os.path.join(rekening,str(datumlijst[0])[:6])+"a","a") as a:
            print(analyselijnzw, file = a)
            print("|"+forl12(voortgang)+"#"*(aantalstreepjes-1)+"|"+valuta+forsom(somal)+K+" "*(56-aantalstreepjes)+binnen+"|", file = a)
            print(analyselijnzw, file = a)

def IDlijst2ok(IDlijst):
    ok = {}
    for i in IDlijst:
        try:
            oki = i[0]+str(int(i[1:]))
            cat = haalcategorie(rekening,i[0])
            ok[oki] = cat[int(i[1:])+1]
        except(Exception) as f:
            #print(f)
            pass
    return ok

def toontransactie(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    ok = ifok(rekening,header,col,ok)
    for ID in ok:
        if Taal == "EN":
            el = elementenEN
        elif Taal == "IT":
            el = elementenIT
        else:
            el = elementen
        maxlen = len(max(el, key = len))
        try:
            alternatievenamendict = haalalternatievenamen(rekening)
            alt = vertaalv(alternatievenamendict[ID[0]])
            datum = ok[ID][0]
            datum = opmaakdatum(datum)
            print(" "*10+col+"+-"+kleuren["Omkeren"]+catcol[ID[0]]+ID+kleuren["ResetAll"]+col+"-"*(maxlen-(len(ID)))+"+"+"-"*10+kleuren["ResetAll"])
            print(" "*10+col+"| "+kleuren["ResetAll"]+catcol[ID[0]]+("{:^%d}" % (maxlen+11)).format(alt)+kleuren["ResetAll"])
            print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(el[0])+kleuren["ResetAll"]+":  "+datum)
            print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(el[1])+kleuren["ResetAll"]+": "+kleinegetalkleuren(ok[ID][1])+valuta+kleuren["ResetAll"]+fornum(ok[ID][1]))
            wraptekstlijst2 = textwrap.wrap(ok[ID][2],w-maxlen-14)
            for i in wraptekstlijst2:
                if i == wraptekstlijst2[0]:
                    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(el[2])+kleuren["ResetAll"]+": "+str(i))
                else:
                    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(" ")+kleuren["ResetAll"]+": "+str(i))
            wraptekstlijst3 = textwrap.wrap(ok[ID][3],w-maxlen-14)
            for i in wraptekstlijst3:
                if i == wraptekstlijst3[0]:
                    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(el[3])+kleuren["ResetAll"]+": "+str(i))
                else:
                    print(" "*10+col+"| "+kleuren["ResetAll"]+kleuren["coltoon"]+("{:<%d}" % maxlen).format(" ")+kleuren["ResetAll"]+": "+str(i))
            print(" "*10+col+"+-"+"-"*maxlen+"+"+"-"*10+kleuren["ResetAll"])
        except(Exception) as f:
            #print(f)
            pass
    return ok

def geefIDlijst(rekening,header,col,ok):
    IDlijst = []
    for i in ok:
        IDlijst.append(i)
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    loop = True
    while loop == True:
        IDCSV = input(kleuren["Omkeren"]+col+"CSV"+kleuren["ResetAll"]+col+": ").upper()
        print(ResetAll, end = "")
        if IDCSV.upper() in afsluitlijst:
            doei()
        elif IDCSV.upper() in neelijst:
            return "<"
        elif IDCSV.upper() == "H":
            if Taal == "EN":
                wraptekst = textwrap.wrap("Specify one or more \"ID's\" as a comma- or space-separated CSV list. An \"ID\" always starts with the category, immediately followed by an integer. If the specified \"ID\" matches an existing transaction, it is added to the collection. Examples of potentially valid CSV lists are: \"B4,C2\", \"a0\", \"C2, a0 B4\", etc.",w)
            elif Taal == "IT":
                wraptekst = textwrap.wrap("Specificare uno o più \"ID\" come elenco CSV separato da virgole o spazi. Un \"ID\" inizia sempre con la categoria, seguita immediatamente da un numero intero. Se l' \"ID\" specificato corrisponde a una transazione esistente, viene aggiunta alla collezione. Esempi di elenchi CSV potenzialmente validi sono: \"B4,C2\", \"a0\", \"C2, a0 B4\", ecc.",w)
            else:
                wraptekst = textwrap.wrap("Geef één of meer \"ID's\" op als komma- of spatiegescheiden CSV-lijst. Een \"ID\" begint altijd met de categorie, onmiddellijk gevolgd door een geheel getal. Als de opgegeven \"ID\" overeenkomt met een bestaande transactie, dan wordt die aan de collectie toegevoegd. Voorbeelden van mogelijk geldige CSV-lijsten zijn: \"B4,C2\", \"a0\", \"C2, a0 B4\", enz.",w)
            for i in wraptekst:
                print(i)
            del IDCSV
        else:
            if IDCSV == "*":
                IDlijst = []
                categorieenlijst = haalcategorieen(rekening)
                for i in categorieenlijst:
                    categorie = haalcategorie(rekening,i)
                    categorietrans = categorie[1:]
                    tel = 0
                    for j in categorietrans:
                        IDlijst.append(i+str(tel))
                        tel += 1
            else:
                try:
                    IDlijst = IDCSV.replace(" ",",").split(",")
                    for i in sorted(IDlijst, reverse = True):
                        if len(i) < 2 or i[0] not in lijst:
                            IDlijst.remove(i)
                except(Exception) as f:
                    #print(f)
                    pass
        return IDlijst

def collectie(rekening,ok):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IDlijst = geefIDlijst(rekening,header,col,ok)
    try:
        if IDlijst.upper() in neelijst:
            return ok
    except(Exception) as f:
        #print(f)
        ok = IDlijst2ok(IDlijst)
        return ok

def filterdatumlijst(datumlijst,okal):
    ok = {}
    for i in okal:
        if datumlijst[0] == standaardstartdatum and datumlijst[1] == standaardeinddatum:
            ok[i] = okal[i]
        elif datumlijst[0] <= okal[i][0] <= datumlijst[1]:
            ok[i] = okal[i]
    return ok

def filterbedraglijst(bedraglijst,okal):
    ok = {}
    for i in okal:
        if bedraglijst[0] == standaardbodembedrag and bedraglijst[1] == standaardtopbedrag:
            ok[i] = okal[i]
        elif bedraglijst[0] <= okal[i][1] <= bedraglijst[1]:
            ok[i] = okal[i]
    return ok

def filterwederpartij(wederpartij,okal):
    ok = {}
    for i in okal:
        if wederpartij.lower() in okal[i][2].lower():
            ok[i] = okal[i]
    return ok

def filteronderwerp(onderwerp,okal):
    ok = {}
    for i in okal:
        if onderwerp.lower() in okal[i][3].lower():
            ok[i] = okal[i]
    return ok

def filtercategorie(categoriekeuzelijst,okal):
    ok = {}
    for i in okal:
        if i[0] in categoriekeuzelijst:
            ok[i] = okal[i]
    return ok

def alsspaarpot(rekening,header,spaarpotten,i,transactiebedrag):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    toonspaarpotten(rekening,header,spaarpotten)
    if Taal == "EN":
        wraptekst1 = textwrap.wrap("You can now set aside something for this savings pot: %s. Would you like to replenish this savings pot?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        wraptekst2 = textwrap.wrap("A savings pot %s is found. Do you want to settle this complete transaction with that savings pot?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        nietgenoeg1 = textwrap.wrap("You can't put aside more than %s" % valuta+fornum(transactiebedrag),w)
        nietgenoeg2 = textwrap.wrap("Insufficient credit. You cannot pay %s from a credit of %s" % (valuta+fornum(transactiebedrag*-1),valuta+fornum(spaarpotten[i][1])),w)
        handmatig = textwrap.wrap("Try to top up your credit first and then manually correct the paid amount in this savings pot",w)
    elif Taal == "IT":
        wraptekst1 = textwrap.wrap("Ora puoi mettere da parte qualcosa per questo salvadanaio: %s. Vuoi ricaricare questo salvadanaio?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        wraptekst2 = textwrap.wrap("È stato trovato un salvadanaio: %s. Vuoi compensare questa intera transazione con quel salvadanaio?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        nietgenoeg1 = textwrap.wrap("Non puoi mettere da parte più di %s" % valuta+fornum(transactiebedrag),w)
        nietgenoeg2 = textwrap.wrap("Credito insufficiente. Non puoi pagare %s da un credito di %s" % (valuta+fornum(transactiebedrag*-1),valuta+fornum(spaarpotten[i][1])),w)
        handmatig = textwrap.wrap("Prova a ricaricare prima il tuo credito e poi correggi manualmente l'importo pagato da questo salvadanaio",w)
    else:
        wraptekst1 = textwrap.wrap("U kunt nu iets opzij zetten voor deze spaarpot: %s. Wilt u deze spaarpot aanvullen?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        wraptekst2 = textwrap.wrap("Er is een spaarpot gevonden: %s. Wilt u deze gehele transactie verrekenen met die spaarpot?" % (kleuren["5"]+i+kleuren["ResetAll"]),w)
        nietgenoeg1 = textwrap.wrap("Je kunt niet méér apart zetten dan %s" % valuta+fornum(transactiebedrag),w)
        nietgenoeg2 = textwrap.wrap("Onvoldoende tegoed. Je kunt geen %s betalen uit een tegoed van %s" % (valuta+fornum(transactiebedrag*-1),valuta+fornum(spaarpotten[i][1])),w)
        handmatig = textwrap.wrap("Probeer eerst uw tegoed aan te vullen en corrigeer daarna het uit deze spaarpot betaalde bedrag handmatig",w)
    if transactiebedrag > 0 and spaarpotten[i][1] < spaarpotten[i][0]:
        for j in wraptekst1:
            print(j)
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            pass
        else:
            loop = True
            while loop == True:
                bedrag = geefeenbedrag(rekening,header,col,ok,transactiebedrag)
                if bedrag == "<":
                    bedrag = 0
                elif bedrag == "*":
                    bedrag = transactiebedrag
                if bedrag <= transactiebedrag:
                    spaarpotten[i][1] += bedrag
                    spaarpotten[i][1] = round(spaarpotten[i][1],2)
                    with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                        print(spaarpotten, file = s, end = "")
                    toonspaarpotten(rekening,header,spaarpotten)
                    transactiebedrag -= bedrag
                    loop = False
                else:
                    for j in nietgenoeg1:
                        print(kleuren["colslecht"]+j+kleuren["ResetAll"])
    else:
        for j in wraptekst2:
            print(j)
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            pass
        else:
            if transactiebedrag * -1 <= spaarpotten[i][1]:
                spaarpotten[i][1] += transactiebedrag
                spaarpotten[i][1] = round(spaarpotten[i][1],2)
                spaarpotten[i][2] += transactiebedrag
                spaarpotten[i][2] = round(spaarpotten[i][2],2)
                with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                    print(spaarpotten, file = s, end = "")
                toonspaarpotten(rekening,header,spaarpotten)
                transactiebedrag = 0
            else:
                for j in nietgenoeg2:
                    print(kleuren["colslecht"]+j+kleuren["ResetAll"])
                for j in handmatig:
                    print(j)
    return transactiebedrag

def nieuwnieuw(rekening,ok):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    categorieenlijst = haalcategorieen(rekening)
    printdatum(nustr)
    IDlijst = []
    for i in ok:
        IDlijst.append(i)
    bereik = False
    bedrag = 0.0
    loop = True
    while loop == True:
        nieuwetransactie = []
        nieuwetransactieinputlijst = input(kleuren["Omkeren"]+col+"CSV"+kleuren["ResetAll"]+col+": ").split(",")
        print(ResetAll, end = "")
        if nieuwetransactieinputlijst[0].upper() in afsluitlijst:
            doei()
        elif nieuwetransactieinputlijst[0].upper() in neelijst:
            break
        elif nieuwetransactieinputlijst[0].upper() == "H":
            if Taal == "EN":
                wraptekst1 = textwrap.wrap("Specify the elements in CSV style: \"%s,%s,%s,%s,%s\". If the CSV input contains invalid data, the step-by-step input takes over." % (elementenEN[0].lower(),elementenEN[1].lower(),elementenEN[2].lower(),elementenEN[3].lower(),woordcategorieEN.lower()),w)
                wraptekst2 = textwrap.wrap("",w)
            elif Taal == "IT":
                wraptekst1 = textwrap.wrap("Inserisci gli elementi in stile CSV: \"%s,%s,%s,%s,%s\". Se l'input CSV contiene dati non validi, verrà utilizzato l'input passo dopo passo." % (elementenIT[0].lower(),elementenIT[1].lower(),elementenIT[2].lower(),elementenIT[3].lower(),woordcategorieIT.lower()),w)
                wraptekst2 = textwrap.wrap("",w)
            else:
                wraptekst1 = textwrap.wrap("Geef de elementen op in CSV-stijl: \"%s,%s,%s,%s,%s\". Mocht de CSV-ingave ongeldige data bevatten, dan neemt de stap-voor-stap-ingave het over." % (elementen[0].lower(),elementen[1].lower(),elementen[2].lower(),elementen[3].lower(),woordcategorie.lower()),w)
                wraptekst2 = textwrap.wrap("Er is een spaarpot gevonden. Wil je deze transactie verrekenen met spaarpot %s?" % i,w)
            for i in wraptekst1:
                print(i)
        elif len(nieuwetransactieinputlijst) == 5:
            if checkdatum(nieuwetransactieinputlijst[0]) == True:
                transactiedatum = int(nieuwetransactieinputlijst[0])
            else:
                transactiedatum = int(nustr)
            if checkfloat(nieuwetransactieinputlijst[1]) == True:
                transactiebedrag = round(float(nieuwetransactieinputlijst[1]),2)
            else:
                transactiebedrag = 0.0
            wederpartij = nieuwetransactieinputlijst[2]
            onderwerp = nieuwetransactieinputlijst[3]
            if nieuwetransactieinputlijst[4].upper() in categorieenlijst:
                nieuwetransactiecategorie = nieuwetransactieinputlijst[4].upper()
            else:
                nieuwetransactiecategorie = "O"
        else:
            transactiedatum = geefeendatum(rekening,header,col,ok,int(nustr))
            if str(transactiedatum).upper() in neelijst:
                break
            transactiebedrag = geefeenbedrag(rekening,header,col,ok,0.0)
            if str(transactiebedrag).upper() in neelijst:
                break
            wederpartij = geefwederpartij(rekening,header,col,ok)
            if wederpartij.upper() in neelijst:
                break
            onderwerp = geefonderwerp(rekening,header,col,ok)
            if onderwerp.upper() in neelijst:
                break
            categoriekeuzelijst = geefcategorie(rekening,header,col,ok)
            if len(categoriekeuzelijst) > 0:
                if categoriekeuzelijst[0] in categorieenlijst:
                    nieuwetransactiecategorie = categoriekeuzelijst[0]
                else:
                    nieuwetransactiecategorie = "O"
            else:
                nieuwetransactiecategorie = "O"
        if nieuwetransactieinputlijst[0].upper() != "H":
            try:
                nieuwetransactie.append(transactiedatum)
                nieuwetransactie.append(transactiebedrag)
                nieuwetransactie.append(wederpartij)
                nieuwetransactie.append(onderwerp)
                categorie = haalcategorie(rekening,nieuwetransactiecategorie)
                categorie.append(nieuwetransactie)
                cattrans = sorted(categorie[1:])
                cat = [categorie[0]]
                for j in cattrans:
                    cat.append(j)
                schrijfcategorie(rekening,nieuwetransactiecategorie,cat)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
                spaarpotten = haalspaarpotten(rekening)
                for i in spaarpotten:
                    if i in onderwerp and transactiebedrag != 0:
                        transactiebedrag = alsspaarpot(rekening,header,spaarpotten,i,transactiebedrag)
                IDlijst.append(nieuwetransactiecategorie+str(categorie.index(nieuwetransactie)-1))
                ok = IDlijst2ok(IDlijst)
                toontransactie(rekening,header,col,ok)
            except(Exception) as f:
                print(f)
                if Taal == "EN":
                    print(kleuren["colslecht"],oepsEN,kleuren["ResetAll"])
                elif Taal == "IT":
                    print(kleuren["colslecht"],oepsIT,kleuren["ResetAll"])
                else:
                    print(kleuren["colslecht"],oeps,kleuren["ResetAll"])
                break
    return ok

def ifok(rekening,header,col,ok):
    if ok == {}:
        IDlijst = geefIDlijst(rekening,header,col,ok)
    else:
        IDlijst = []
        for i in ok:
            IDlijst.append(i)
    ok = IDlijst2ok(IDlijst)
    return ok

def nieuwkopie(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = {i[0]+str(categorie.index(oudetransactie)-1):oudetransactie}
        dezeok = toontransactie(rekening,header,col,dezeok)
        if Taal == "EN":
            print("%s %s:" % (col+menuEN["2,2"],opmaakdatum(nustr)+kleuren["ResetAll"]))
        elif Taal == "IT":
            print("%s %s:" % (col+menuIT["2,2"],opmaakdatum(nustr)+kleuren["ResetAll"]))
        else:
            print("%s %s:" % (col+menu["2,2"],opmaakdatum(nustr)+kleuren["ResetAll"]))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwetransactie = [int(nustr),oudetransactie[1],oudetransactie[2],oudetransactie[3]]
            categorie.append(nieuwetransactie)
            cat = [categorie[0]]
            cattrans = []
            for j in categorie[1:]:
                cattrans.append(j)
            catsort = sorted(cattrans)
            for j in catsort:
                cat.append(j)
            schrijfcategorie(rekening,i[0],cat)
            # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
            transactiebedrag = nieuwetransactie[1]
            onderwerp = nieuwetransactie[3]
            spaarpotten = haalspaarpotten(rekening)
            for i in spaarpotten:
                if i in onderwerp and transactiebedrag != 0:
                    transactiebedrag = alsspaarpot(rekening,header,spaarpotten,i,transactiebedrag)
        dezeok = {i[0]+str(catsort.index(nieuwetransactie)):nieuwetransactie}
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        dezeok = toontransactie(rekening,header,col,dezeok)
        translijst.append(nieuwetransactie)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def verwijderkeuze(rekening,header,col,keuze1lijst,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    okv = []
    for i in ok:
        try:
            oudetransactie = ok[i]
            with open(os.path.join(rekening,i[0]),"r") as c:
                oudecat = ast.literal_eval(c.read())
            echteindexmineen = i[0]+str(oudecat.index(oudetransactie)-1)
            oki = {}
            oki[echteindexmineen] = oudetransactie
            toontransactie(rekening,header,col,oki)
            if Taal == "EN":
                print(kleuren["Omkeren"]+col+menuEN["4"]+kleuren["ResetAll"]+" "+kleuren["Omkeren"]+catcol[i[0]]+echteindexmineen+kleuren["ResetAll"])
            elif Taal == "IT":
                print(kleuren["Omkeren"]+col+menuIT["4"]+kleuren["ResetAll"]+" "+kleuren["Omkeren"]+catcol[i[0]]+echteindexmineen+kleuren["ResetAll"])
            else:
                print(kleuren["Omkeren"]+col+menu["4"]+kleuren["ResetAll"]+" "+kleuren["Omkeren"]+catcol[i[0]]+echteindexmineen+kleuren["ResetAll"])
            jn = geefjaofnee(rekening,header)
            if jn.upper() in afsluitlijst:
                doei()
            elif jn == "" or jn.upper() in neelijst:
                pass
            else:
                okv.append(i)
                cat = haalcategorie(rekening,i[0])
                categorie = [cat[0]]
                for j in cat[1:]:
                    if j != oudetransactie:
                        categorie.append(j)
                schrijfcategorie(rekening,i[0],categorie)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        except(Exception) as f: # faalt als er identieke transacties worden verwijderd
            #print(f)
            pass
    ok = ifok(rekening,header,col,ok)
    return rekening,header,col,keuze1lijst,ok

def wijzigdatum(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = {i[0]+str(categorie.index(oudetransactie)-1):oudetransactie}
        dezeok = toontransactie(rekening,header,col,dezeok)
        if Taal == "EN":
            print("%s (YYYMMDD) %s:" % (col+menuEN["3,1"]+kleuren["ResetAll"],ok[i][0]))
        elif Taal == "IT":
            print("%s (AAAAMMGG) %s:" % (col+menuIT["3,1"]+kleuren["ResetAll"],ok[i][0]))
        else:
            print("%s (JJJJMMDD) %s:" % (col+menu["3,1"]+kleuren["ResetAll"],ok[i][0]))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwedatum = geefeendatum(rekening,header,col,ok,ok[i][0])
            if nieuwedatum == "<":
                pass
            else:
                nieuwetransactie = [nieuwedatum,oudetransactie[1],oudetransactie[2],oudetransactie[3]]
                categorie.remove(oudetransactie)
                categorie.append(nieuwetransactie)
                cat = [categorie[0]]
                cattrans = []
                for j in categorie[1:]:
                    cattrans.append(j)
                catsort = sorted(cattrans)
                for j in catsort:
                    cat.append(j)
                schrijfcategorie(rekening,i[0],cat)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        dezeok = {i[0]+str(catsort.index(nieuwetransactie)):nieuwetransactie}
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        dezeok = toontransactie(rekening,header,col,dezeok)
        translijst.remove(oudetransactie)
        translijst.append(nieuwetransactie)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def wijzigbedrag(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = {i[0]+str(categorie.index(oudetransactie)-1):oudetransactie}
        dezeok = toontransactie(rekening,header,col,dezeok)
        if Taal == "EN":
            print("%s %s %s:" % (col+menuEN["3,2"]+kleuren["ResetAll"],valuta,fornum(ok[i][1])))
        elif Taal == "IT":
            print("%s %s %s:" % (col+menuIT["3,2"]+kleuren["ResetAll"],valuta,fornum(ok[i][1])))
        else:
            print("%s %s %s:" % (col+menu["3,2"]+kleuren["ResetAll"],valuta,fornum(ok[i][1])))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwbedrag = geefeenbedrag(rekening,header,col,ok,ok[i][1])
            if nieuwbedrag == "<":
                pass
            else:
                nieuwetransactie = [oudetransactie[0],nieuwbedrag,oudetransactie[2],oudetransactie[3]]
                categorie.remove(oudetransactie)
                categorie.append(nieuwetransactie)
                cat = [categorie[0]]
                cattrans = []
                for j in categorie[1:]:
                    cattrans.append(j)
                catsort = sorted(cattrans)
                for j in catsort:
                    cat.append(j)
                schrijfcategorie(rekening,i[0],cat)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        dezeok = {i[0]+str(catsort.index(nieuwetransactie)):nieuwetransactie}
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        dezeok = toontransactie(rekening,header,col,dezeok)
        translijst.remove(oudetransactie)
        translijst.append(nieuwetransactie)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def wijzigwederpartij(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = {i[0]+str(categorie.index(oudetransactie)-1):oudetransactie}
        dezeok = toontransactie(rekening,header,col,dezeok)
        if Taal == "EN":
            print("%s %s:" % (col+menuEN["3,3"]+kleuren["ResetAll"],ok[i][2]))
        elif Taal == "IT":
            print("%s %s:" % (col+menuIT["3,3"]+kleuren["ResetAll"],ok[i][2]))
        else:
            print("%s %s:" % (col+menu["3,3"]+kleuren["ResetAll"],ok[i][2]))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwewederpartij = geefwederpartij(rekening,header,col,ok)
            if nieuwewederpartij == "<":
                pass
            else:
                nieuwetransactie = [oudetransactie[0],oudetransactie[1],nieuwewederpartij,oudetransactie[3]]
                categorie.remove(oudetransactie)
                categorie.append(nieuwetransactie)
                cat = [categorie[0]]
                cattrans = []
                for j in categorie[1:]:
                    cattrans.append(j)
                catsort = sorted(cattrans)
                for j in catsort:
                    cat.append(j)
                schrijfcategorie(rekening,i[0],cat)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        dezeok = {i[0]+str(catsort.index(nieuwetransactie)):nieuwetransactie}
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        dezeok = toontransactie(rekening,header,col,dezeok)
        translijst.remove(oudetransactie)
        translijst.append(nieuwetransactie)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def wijzigonderwerp(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = {i[0]+str(categorie.index(oudetransactie)-1):oudetransactie}
        dezeok = toontransactie(rekening,header,col,dezeok)
        if Taal == "EN":
            print("%s %s:" % (col+menuEN["3,4"]+kleuren["ResetAll"],ok[i][3]))
        elif Taal == "IT":
            print("%s %s:" % (col+menuIT["3,4"]+kleuren["ResetAll"],ok[i][3]))
        else:
            print("%s %s:" % (col+menu["3,4"]+kleuren["ResetAll"],ok[i][3]))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwonderwerp = geefonderwerp(rekening,header,col,ok)
            if nieuwonderwerp == "<":
                pass
            else:
                nieuwetransactie = [oudetransactie[0],oudetransactie[1],oudetransactie[2],nieuwonderwerp]
                categorie.remove(oudetransactie)
                categorie.append(nieuwetransactie)
                cat = [categorie[0]]
                cattrans = []
                for j in categorie[1:]:
                    cattrans.append(j)
                catsort = sorted(cattrans)
                for j in catsort:
                    cat.append(j)
                schrijfcategorie(rekening,i[0],cat)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        dezeok = {i[0]+str(catsort.index(nieuwetransactie)):nieuwetransactie}
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        dezeok = toontransactie(rekening,header,col,dezeok)
        translijst.remove(oudetransactie)
        translijst.append(nieuwetransactie)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def wijzigcategorie(rekening,header,col,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    ok = ifok(rekening,header,col,ok)
    translijst = []
    IDlijst = []
    for i in ok:
        oudetransactie = ok[i]
        translijst.append(oudetransactie)
        categorie = haalcategorie(rekening,i[0])
        catsort = categorie[1:]
        dezeok = toontransactie(rekening,header,col,{i[0]+str(categorie.index(oudetransactie)-1):oudetransactie})
        oudecategorie = i[0]
        if Taal == "EN":
            print("%s %s:" % (col+menuEN["3,5"]+kleuren["ResetAll"],catcol[i[0]]+i[0]+kleuren["ResetAll"]))
        elif Taal == "IT":
            print("%s %s:" % (col+menuIT["3,5"]+kleuren["ResetAll"],catcol[i[0]]+i[0]+kleuren["ResetAll"]))
        else:
            print("%s %s:" % (col+menu["3,5"]+kleuren["ResetAll"],catcol[i[0]]+i[0]+kleuren["ResetAll"]))
        jn = geefjaofnee(rekening,header)
        if jn.upper() in afsluitlijst:
            doei()
        elif jn.upper() in neelijst:
            nieuwetransactie = oudetransactie
        else:
            nieuwecategorie = geefcategorie(rekening,header,col,ok)[0]
            if nieuwecategorie[0] == "<":
                pass
            else:
                nieuwecat = haalcategorie(rekening,nieuwecategorie)
                nieuwecat.append(oudetransactie)
                schrijfcategorie(rekening,nieuwecategorie,nieuwecat)
                nieuwecat = haalcategorie(rekening,nieuwecategorie)
                oudecat = haalcategorie(rekening,oudecategorie)
                oudecat.remove(oudetransactie)
                schrijfcategorie(rekening,oudecategorie,oudecat)
                oudecat = haalcategorie(rekening,oudecategorie)
                # Hier iets met "Toverwoord voor Spaarpotten": als ok[i][3] een "Toverwoord" bevat, vraag of deze verrekend moet worden met spaarpot
        if Taal == "EN":
            print(kleuren["Omkeren"]+col+"NOW:"+kleuren["ResetAll"])
        elif Taal == "IT":
            print(kleuren["Omkeren"]+col+"ORA:"+kleuren["ResetAll"])
        else:
            print(kleuren["Omkeren"]+col+"NU:"+kleuren["ResetAll"])
        try:
            dezeok = toontransactie(rekening,header,col,{nieuwecategorie+str(nieuwecat.index(oudetransactie)-1):oudetransactie})
        except(Exception) as f:
            #print(f)
            if Taal == "EN":
                wraptekst = textwrap.wrap("You can change the %s of only one %s from the same %s" % (woordcategorieEN.lower(),woordtransactieEN.lower(),woordcategorieEN.lower()),w)
            elif Taal == "IT":
                wraptekst = textwrap.wrap("È possibile cambiare la %s da solo una %s nella stessa %s" % (woordcategorieIT.lower(),woordtransactieIT.lower(),woordcategorieIT.lower()),w)
            else:
                wraptekst = textwrap.wrap("Je kunt de %s veranderen van slechts één %s in dezelfde %s" % (woordcategorie.lower(),woordtransactie.lower(),woordcategorie.lower()),w)
            for i in wraptekst:
                print(i)
        print(col+scheidtransactielijn+kleuren["ResetAll"])
    for i in ok:
        for j in translijst:
            categorie = haalcategorie(rekening,i[0])
            if j in categorie:
                IDlijst.append(i[0]+str(categorie.index(j)-1))
    IDlijst = sorted(IDlijst)
    ok = IDlijst2ok(IDlijst)
    return ok

def budgetcorrectie(rekening):
    dirlist = os.listdir(rekening)
    for i in dirlist:
        if i in lijst:
            categorie = haalcategorie(rekening,i)
            try:
                if len(categorie) == 0:
                    categorie.append(['',budgetnul])
                elif categorie[0][1] == 0 or categorie[0][1] == 0.0:
                    categorie[0][1] = budgetnul
            except(Exception) as f:
                #print(f)
                categorie = [['',budgetnul]]
            with open(os.path.join(rekening,i),"w") as cat:
                print(categorie,file = cat)

def sortokdatumreverse(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][0],ok[i][1],ok[i][2],ok[i][3],i])
    revoki = sorted(oki, reverse = True)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[0],i[1],i[2],i[3]]
    return ok

def sortokdatum(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][0],ok[i][1],ok[i][2],ok[i][3],i])
    revoki = sorted(oki)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[0],i[1],i[2],i[3]]
    return ok

def sortokbedragreverse(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][1],ok[i][0],ok[i][2],ok[i][3],i])
    revoki = sorted(oki, reverse = True)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[1],i[0],i[2],i[3]]
    return ok

def sortokbedrag(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][1],ok[i][0],ok[i][2],ok[i][3],i])
    revoki = sorted(oki)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[1],i[0],i[2],i[3]]
    return ok

def sortokwederpartijreverse(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][2],ok[i][1],ok[i][0],ok[i][3],i])
    revoki = sorted(oki, reverse = True)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[2],i[1],i[0],i[3]]
    return ok

def sortokwederpartij(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][2],ok[i][1],ok[i][0],ok[i][3],i])
    revoki = sorted(oki)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[2],i[1],i[0],i[3]]
    return ok

def sortokonderwerpreverse(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][3],ok[i][1],ok[i][2],ok[i][0],i])
    revoki = sorted(oki, reverse = True)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[3],i[1],i[2],i[0]]
    return ok

def sortokonderwerp(rekening,ok):
    oki = []
    for i in ok:
        oki.append([ok[i][3],ok[i][1],ok[i][2],ok[i][0],i])
    revoki = sorted(oki)
    categorieen = haalcategorieen(rekening)
    ok = {}
    for i in revoki:
        ok[i[-1]] = [i[3],i[1],i[2],i[0]]
    return ok

def geefjaofnee(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    janeelijst = ["<",">"]
    for i in janeelijst:#coljanee(rekening,header,
        print(forr3(janeelijst.index(i))+" : "+coljanee(rekening,header,i)+vertaalv(i)+kleuren["ResetAll"])
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return "<"
    elif antwoord == "0":
        return janeelijst[0]
    elif antwoord == "1":
        return janeelijst[1]
    else:
        return "<"

def resetheader(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        zekervraag = textwrap.wrap("Are you sure you want to reset the account settings to the default? The transaction data and the opening balance are kept intact",w)
    elif Taal == "IT":
        zekervraag = textwrap.wrap("Sei sicuro di voler ripristinare le impostazioni dell'account ai valori predefiniti? I dati delle transazioni e il saldo iniziale rimarranno invariati",w)
    else:
        zekervraag = textwrap.wrap("Weet u zeker dat u de rekeninginstellingen wilt terugzetten naar de standaardinstellingen? Transactiedata en het startsaldo blijven ongewijzigd",w)
    for i in zekervraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        ditstartsaldo = header[nieuwheaderlijst[5]]
        verseheader = {}
        for i in nieuwheader:
            if i == nieuwheaderlijst[5]:
                verseheader[i] = ditstartsaldo
            else:
                verseheader[i] = nieuwheader[i]
        with open(os.path.join(rekening,"header"),"w") as h:
            print(verseheader, file = h, end = "")
        with open(os.path.join("header"),"w") as hbu:
            print(nieuwheader, file = hbu, end = "")
    header = haalheader(rekening)
    return header

def resetalt(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        zekervraag = textwrap.wrap("Are you sure you want to reset the category names to the default? The transaction data are kept intact",w)
    elif Taal == "IT":
        zekervraag = textwrap.wrap("Sei sicuro di voler ripristinare i nomi delle categorie ai valori predefiniti? I dati delle transazioni rimarranno invariati",w)
    else:
        zekervraag = textwrap.wrap("Weet u zeker dat u de categorienamen wilt terugzetten naar de standaardnamen? Transactiedata blijven ongewijzigd",w)
    for i in zekervraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        for i in nieuwalternatievenamendict:
            try:
                with open(os.path.join(rekening,i),"r") as c:
                    cat = ast.literal_eval(c.read())
                    cat[0][0] = nieuwalternatievenamendict[i]
                    schrijfcategorie(rekening,i,cat)
            except(Exception) as f:
                #print(f)
                pass
    return header

def wijzigrekeningnaam(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[0],header[nieuwheaderlijst[0]]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[0],header[nieuwheaderlijst[0]]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[0],header[nieuwheaderlijst[0]]),w)
    for i in vraag:
        print(i)
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        header[nieuwheaderlijst[0]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigrekeninghoudernaam(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[1],header[nieuwheaderlijst[1]]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[1],header[nieuwheaderlijst[1]]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[1],header[nieuwheaderlijst[1]]),w)
    for i in vraag:
        print(i)
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        header[nieuwheaderlijst[1]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigactief(rekening,header):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        wraptekst = textwrap.wrap("The state of the marked account, that is currently in use, cannot be changed in this session",w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Lo stato del conto contrassegnato, che ora è in uso, non può essere cambiato in questa sessione",w)
    else:
        wraptekst = textwrap.wrap("De status van de gemarkeerde rekening, die nu in gebruik is, kan tijdens deze sessie niet worden gewijzigd",w)
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        rekeningenlijst = rekeningenoverzicht()
        toonrekeningenactief(rekeningenlijst)
        wijzigactief = input(col+inputindent)
        print(ResetAll, end = "")
        if wijzigactief.upper() in afsluitlijst:
            doei()
        elif wijzigactief.upper() in neelijst:
            return header
        else:
            test = checkint(wijzigactief)
            if test == True:
                andererekening = rekeningenlijst[int(wijzigactief)-1]
                andereIBAN = andererekening[:andererekening.index("#")]
                andereJAAR = forr4(andererekening[andererekening.index("#")+1:])
                with open(os.path.join(andererekening,"header"),"r") as ah:
                    andereheader = ast.literal_eval(ah.read())
                if andererekening != rekening:
                    if Taal == "EN":
                        actief = "Active"
                        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (andereIBAN,andereJAAR,nieuwheaderlijstEN[2],coljanee(rekening,header,andereheader[nieuwheaderlijst[2]])+vertaalv(andereheader[nieuwheaderlijst[2]])+kleuren["ResetAll"]),w)
                    elif Taal == "IT":
                        actief = "Attivo"
                        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (andereIBAN,andereJAAR,nieuwheaderlijstIT[2],coljanee(rekening,header,andereheader[nieuwheaderlijst[2]])+vertaalv(andereheader[nieuwheaderlijst[2]])+kleuren["ResetAll"]),w)
                    else:
                        actief = "Actief"
                        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (andereIBAN,andereJAAR,nieuwheaderlijst[2],coljanee(rekening,header,andereheader[nieuwheaderlijst[2]])+vertaalv(andereheader[nieuwheaderlijst[2]])+kleuren["ResetAll"]),w)
                    print(forr3(rekeningenlijst.index(andererekening)+1)+" : "+forl20(andereIBAN[:20])+" "+forl4(andereJAAR[:4])+" : "+actief+" : "+coljanee(rekening,header,andereheader[nieuwheaderlijst[2]])+vertaalv(andereheader[nieuwheaderlijst[2]])+kleuren["ResetAll"])
                    for i in vraag:
                        print(i)
                    antwoord = geefjaofnee(rekening,header)
                    if antwoord.upper() in afsluitlijst:
                        doei()
                    else:
                        andereheader[nieuwheaderlijst[2]] = antwoord
                        with open(os.path.join(andererekening,"header"),"w") as h:
                            print(andereheader, file = h, end = "")
    return header

def wijzigtaal(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[3],taaldict[header[nieuwheaderlijst[3]]]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[3],taaldict[header[nieuwheaderlijst[3]]]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[3],taaldict[header[nieuwheaderlijst[3]]]),w)
    for i in vraag:
        print(i)
    for i in taaldict:
        if i == taallijst[0]:
            print(forr3(">0")+" : "+taaldict[i])
        else:
            print(forr3(taallijst.index(i))+" : "+taaldict[i])
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    test = checkint(antwoord)
    if test == True and int(antwoord) in range(len(taallijst)):
        if antwoord == "1":
            header[nieuwheaderlijst[3]] = "EN"
        elif antwoord == "2":
            header[nieuwheaderlijst[3]] = "IT"
        else:
            header[nieuwheaderlijst[3]] = "NL"
    else:
        header[nieuwheaderlijst[3]] = "NL"
    with open(os.path.join(rekening,"header"),"w") as h:
        print(header, file = h, end = "")
    return header

def wijzigvaluta(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[4],header[nieuwheaderlijst[4]]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[4],header[nieuwheaderlijst[4]]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[4],header[nieuwheaderlijst[4]]),w)
    for i in vraag:
        print(i)
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        header[nieuwheaderlijst[4]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigstartsaldo(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[5],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]])),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[5],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]])),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[5],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]])),w)
    for i in vraag:
        print(i)
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        test = checkfloat(antwoord)
        if test == True:
            header[nieuwheaderlijst[5]] = round(float(antwoord),2)
            with open(os.path.join(rekening,"header"),"w") as h:
                print(header, file = h, end = "")
    return header

def wijzigtoonsaldo(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[6],coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[6],coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[6],coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"]),w)
    for i in vraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    else:
        header[nieuwheaderlijst[6]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigmarkering(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[7],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1])),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[7],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1])),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[7],header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1])),w)
    for i in vraag:
        print(i)
    if Taal == "EN":
        print("Low marking")
    elif Taal == "IT":
        print("Indicazione inferiore")
    else:
        print("Laag markering")
    laag = input(col+inputindent)
    print(ResetAll, end = "")
    if laag.upper() in afsluitlijst:
        doei()
    elif laag.upper() in neelijst:
        return header
    else:
        test = checkfloat(laag)
        if test == True:
            laag = round(float(laag),2)
        else:
            laag = header[nieuwheaderlijst[7]][0]
    if Taal == "EN":
        print("High marking")
    elif Taal == "IT":
        print("Indicazione superiore")
    else:
        print("Hoog markering")
    hoog = input(col+inputindent)
    print(ResetAll, end = "")
    if hoog.upper() in afsluitlijst:
        doei()
    elif hoog.upper() in neelijst:
        return header
    else:
        test = checkfloat(hoog)
        if test == True:
            hoog = round(float(hoog),2)
        else:
            hoog = header[nieuwheaderlijst[7]][1]
    header[nieuwheaderlijst[7]] = [laag,hoog]
    with open(os.path.join(rekening,"header"),"w") as h:
        print(header, file = h, end = "")
    return header

def wijzignullijnen(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[8],coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[8],coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[8],coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"]),w)
    for i in vraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    else:
        header[nieuwheaderlijst[8]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigdatumopmaak(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    mnd = vertaalmnd(int(nustr))
    datum = opmaakdatum(int(nustr))
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s (%s) to:" % (IBAN,JAAR,nieuwheaderlijstEN[9],vertaalv(header[nieuwheaderlijst[9]]),datum),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s (%s) in:" % (IBAN,JAAR,nieuwheaderlijstIT[9],vertaalv(header[nieuwheaderlijst[9]]),datum),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s (%s) naar:" % (IBAN,JAAR,nieuwheaderlijst[9],vertaalv(header[nieuwheaderlijst[9]]),datum),w)
    for i in vraag:
        print(i)
    datum = toondatumopmaakopties(int(nustr))
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        test = checkint(antwoord)
        if test == True and int(antwoord) in range(len(opmaakdatumlijst)):
            header[nieuwheaderlijst[9]] = opmaakdatumlijst[int(antwoord)]
            with open(os.path.join(rekening,"header"),"w") as h:
                print(header, file = h, end = "")
    return header

def wijzigkleurenschema(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[10],vertaalv(header[nieuwheaderlijst[10]])),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[10],vertaalv(header[nieuwheaderlijst[10]])),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[10],vertaalv(header[nieuwheaderlijst[10]])),w)
    for i in vraag:
        print(i)
    kleurenschema = toonkleurenschemaopties()
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        test = checkint(antwoord)
        if test == True and int(antwoord) in range(len(kleurenschemalijst)):
            header[nieuwheaderlijst[10]] = kleurenschemalijst[int(antwoord)]
            with open(os.path.join(rekening,"header"),"w") as h:
                print(header, file = h, end = "")
    return header

def wijzigmenuniveau(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    maxlevel = []
    for i in menu:
        tel = 0
        for j in i:
            if j == ",":
                tel += 1
        maxlevel.append(tel)
    maxtel = max(maxlevel)
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[11],header[nieuwheaderlijst[11]]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[11],header[nieuwheaderlijst[11]]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[11],header[nieuwheaderlijst[11]]),w)
    for i in vraag:
        print(i)
    antwoord = input(col+inputindent)
    print(ResetAll, end = "")
    if antwoord.upper() in afsluitlijst:
        doei()
    elif antwoord.upper() in neelijst:
        return header
    else:
        test = checkint(antwoord)
        if test == True:
            if int(antwoord) < 1:
                antwoord = 1
            elif int(antwoord) > maxtel+1:
                antwoord = maxtel+1
            header[nieuwheaderlijst[11]] = int(antwoord)
            with open(os.path.join(rekening,"header"),"w") as h:
                print(header, file = h, end = "")
    return header

def wijziganalyse2txt(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[12],coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[12],coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[12],coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"]),w)
    for i in vraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    else:
        header[nieuwheaderlijst[12]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigexport2csv(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[13],coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[13],coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[13],coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"]),w)
    for i in vraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    else:
        header[nieuwheaderlijst[13]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def wijzigtipvandedag(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    IBAN = rekening[:rekening.index("#")]
    JAAR = forr4(rekening[rekening.index("#")+1:])
    if Taal == "EN":
        vraag = textwrap.wrap("Change %s %s %s from %s to:" % (IBAN,JAAR,nieuwheaderlijstEN[14],coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]])+kleuren["ResetAll"]),w)
    elif Taal == "IT":
        vraag = textwrap.wrap("Cambia %s %s %s da %s in:" % (IBAN,JAAR,nieuwheaderlijstIT[14],coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]])+kleuren["ResetAll"]),w)
    else:
        vraag = textwrap.wrap("Wijzig %s %s %s van %s naar:" % (IBAN,JAAR,nieuwheaderlijst[14],coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]])+kleuren["ResetAll"]),w)
    for i in vraag:
        print(i)
    antwoord = geefjaofnee(rekening,header)
    if antwoord.upper() in afsluitlijst:
        doei()
    else:
        header[nieuwheaderlijst[14]] = antwoord
        with open(os.path.join(rekening,"header"),"w") as h:
            print(header, file = h, end = "")
    return header

def tipvandedag(rekening,header,col):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    keuzelijst = []
    if Taal == "EN":
        print(col+kleuren["Vaag"]+kleuren["Omkeren"]+forcw(menuEN["0,1,15"])+kleuren["ResetAll"])
        for i in helpmenuEN:
            keuzelijst.append(helpmenuEN[i])
        keuze = random.choice(keuzelijst)
        index = list(helpmenuEN.keys())[list(helpmenuEN.values()).index(keuze)]
        keuzemenu = menuEN
    elif Taal == "IT":
        print(col+kleuren["Vaag"]+kleuren["Omkeren"]+forcw(menuIT["0,1,15"])+kleuren["ResetAll"])
        for i in helpmenuIT:
            keuzelijst.append(helpmenuIT[i])
        keuze = random.choice(keuzelijst)
        index = list(helpmenuIT.keys())[list(helpmenuIT.values()).index(keuze)]
        keuzemenu = menuIT
    else:
        print(col+kleuren["Vaag"]+kleuren["Omkeren"]+forcw(menu["0,1,15"])+kleuren["ResetAll"])
        for i in helpmenu:
            keuzelijst.append(helpmenu[i])
        keuze = random.choice(keuzelijst)
        index = list(helpmenu.keys())[list(helpmenu.values()).index(keuze)]
        keuzemenu = menu
    print(col+index+kleuren["ResetAll"]+" : "+keuzemenu[index])
    for i in keuze:
        print(col+kleuren["Vaag"]+i+kleuren["ResetAll"])

def dithelp(rekening,header,col,item):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        helpme = helpmenuEN
    elif Taal == "IT":
        helpme = helpmenuIT
    else:
        helpme = helpmenu
    for i in item:
        if i in helpme:
            for j in helpme[i]:
                print(j)
    return rekening,header,col

def presenteerhelp(rekening,header,col,keuze1lijst):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        keuzemenu = menuEN
        helpkeuzemenu = helpmenuEN
    elif Taal == "IT":
        keuzemenu = menuIT
        helpkeuzemenu = helpmenuIT
    else:
        keuzemenu = menu
        helpkeuzemenu = helpmenu
    keuzemaxi = []
    for i,j in keuzemenu.items():
        keuzemaxi.append(i)
    maxleni = len(max(keuzemaxi, key = len))
    keuzemaxj = []
    for i,j in keuzemenu.items():
        keuzemaxj.append(j)
    maxlenj = len(max(keuzemaxj, key = len))
    keuze1menulijst = []
    for i,j in keuzemenu.items():
        if len(i) == 1:
            print(kleuren["Omkeren"]+("{:^%s}" % (maxleni+2)).format(i)+": "+("{:^%s}" % maxlenj).format(j)+kleuren["ResetAll"])
        else:
            print(("{:^%s}" % (maxleni+2)).format(i)+": "+("{:<%s}" % maxlenj).format(j))
        keuze1menulijst.append(i)
    if Taal == "EN":
        wraptekst = textwrap.wrap("Enter the index of the item - for example, as \"1,2\" or \"1 2\" - and then press \"Enter\" for help with that item",w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Digita l'indice dell'elemento - ad esempio come \"1,2\" o \"1 2\" - e poi premi \"Invio\" per assistenza su quell'elemento",w)
    else:
        wraptekst = textwrap.wrap("Typ de index van het item - bijvoorbeeld als \"1,2\" of \"1 2\" - en dan \"Enter\" voor hulp bij dat item",w)
    for i in wraptekst:
        print(i)


def kieshelp(rekening,header,col,keuze1lijst):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        keuzemenu = menuEN
        helpkeuzemenu = helpmenuEN
    elif Taal == "IT":
        keuzemenu = menuIT
        helpkeuzemenu = helpmenuIT
    else:
        keuzemenu = menu
        helpkeuzemenu = helpmenu
    presenteerhelp(rekening,header,col,keuze1lijst)
    loop = True
    while loop == True:
        helpkeuze = input(inputindent+kleuren["Omkeren"]).replace(" ",",").replace("-",",").replace("/",",").replace(".",",").replace(">",",")
        print(ResetAll, end = "")
        if helpkeuze.upper() in afsluitlijst:
            doei()
        elif helpkeuze.upper() in neelijst:
            return "<"
        elif helpkeuze == "":
            presenteerhelp(rekening,header,col,keuze1lijst)
        elif helpkeuze not in keuzemenu:
            pass
        else:
            print(kleuren["Omkeren"]+keuzemenu[helpkeuze]+kleuren["ResetAll"])
            for i in helpkeuzemenu[helpkeuze]:
                print(i)
    return keuze1lijst

def toevoegencategorie(rekening,header,col):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        nieuwalternatievenamendictTaal = nieuwalternatievenamendictEN
        wraptekst = textwrap.wrap("Choose a new category. Named categories are standard categories (but can be renamed), highlighted options are already taken and no longer available",w)
    elif Taal == "IT":
        nieuwalternatievenamendictTaal = nieuwalternatievenamendictIT
        wraptekst = textwrap.wrap("Scegli una nuova categoria. Le categorie denominate sono categorie standard (ma possono essere rinominate), le opzioni evidenziate sono già occupate e non più disponibili",w)
    else:
        nieuwalternatievenamendictTaal = nieuwalternatievenamendict
        wraptekst = textwrap.wrap("Kies een nieuwe categorie. Benoemde categorieën zijn standaardcategorieën (maar kunnen worden hernoemd), gearceerde opties zijn al in gebruik en niet langer beschikbaar",w)
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        categorieenlijst = haalcategorieen(rekening)
        alternatievenamendict = haalalternatievenamen(rekening)
        lenlijst = []
        for i in alternatievenamendict:
            lenlijst.append(alternatievenamendict[i])
        for i in nieuwalternatievenamendictTaal:
            lenlijst.append(nieuwalternatievenamendictTaal[i])
        maxlen = len(max(lenlijst, key = len))
        for i in lijst:
            kleur = catcol[i]
            if i in categorieenlijst:
                kleur = kleuren["Omkeren"]+kleur
            if i in alternatievenamendict:
                print(kleur+forr3(i)+" "+("{:^%d}" % maxlen).format(vertaalv(alternatievenamendict[i]))+kleuren["ResetAll"])
            elif i in nieuwalternatievenamendict:
                print(kleur+forr3(i)+" "+("{:^%d}" % maxlen).format(vertaalv(nieuwalternatievenamendict[i]))+kleuren["ResetAll"])
            else: # alle categorieën staan in de dictionary, maar je weet maar nooit
                print(kleur+forr3(i)+kleuren["ResetAll"])
        antwoord = input(col+inputindent)
        print(ResetAll, end = "")
        if antwoord.upper() in afsluitlijst:
            doei()
        elif antwoord.upper() in neelijst:
            return
        elif antwoord.upper() in lijst and antwoord.upper() not in categorieenlijst:
            with open(os.path.join(rekening,antwoord.upper()),"w") as c:
                print([[nieuwalternatievenamendict[antwoord.upper()],budgetnul]], file = c, end = "")

def wijzigcategorienaam(rekening,header,col):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        wraptekst = textwrap.wrap("Rename a %s. The maximum length is 15 characters, exceeding characters are cut off. Dutch standard %s names are automatically translated" % (woordcategorieEN.lower(),woordcategorieEN.lower()),w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Rinomina una %s. La lunghezza massima è di 15 caratteri, caratteri in eccesso vengono tagliati. I nomi delle categorie standard Olandesi vengono tradotti automaticamente" % (woordcategorieIT.lower()),w)
    else:
        wraptekst = textwrap.wrap("Geef een %s een andere naam. De maximale lengte is 15 tekens, overtollige tekens worden afgekapt. Nederlandse standaard%snamen worden automatisch naar andere talen vertaald" % (woordcategorie.lower(),woordcategorie.lower()),w)
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        categorieenlijst = haalcategorieen(rekening)
        alternatievenamendict = haalalternatievenamen(rekening)
        lenlijst = []
        for i in alternatievenamendict:
            lenlijst.append(alternatievenamendict[i])
        maxlen = len(max(lenlijst, key = len))
        for i in categorieenlijst:
            kleur = catcol[i]
            print(kleur+forr3(i)+" "+("{:^%d}" % maxlen).format(vertaalv(alternatievenamendict[i]))+kleuren["ResetAll"])
        antwoord = input(col+inputindent)
        print(ResetAll, end = "")
        if antwoord.upper() in afsluitlijst:
            doei()
        elif antwoord.upper() in neelijst:
            return
        elif antwoord.upper() in categorieenlijst:
            if Taal == "EN":
                wraptekst = textwrap.wrap("Rename %s %s %s to" % (woordcategorieEN.lower(),catcol[antwoord.upper()]+antwoord.upper(),vertaalv(alternatievenamendict[antwoord.upper()])+kleuren["ResetAll"]),w)
            elif Taal == "IT":
                wraptekst = textwrap.wrap("Rinomina %s %s %s in" % (woordcategorieIT.lower(),catcol[antwoord.upper()]+antwoord.upper(),vertaalv(alternatievenamendict[antwoord.upper()])+kleuren["ResetAll"]),w)
            else:
                wraptekst = textwrap.wrap("Wijzig naam %s %s %s naar" % (woordcategorie.lower(),catcol[antwoord.upper()]+antwoord.upper(),alternatievenamendict[antwoord.upper()]+kleuren["ResetAll"]),w)
            for i in wraptekst:
                print(i)
            antwoord2 = input(col+inputindent)
            print(ResetAll, end = "")
            if antwoord2.upper() in afsluitlijst:
                doei()
            elif antwoord2.upper() in neelijst:
                return
            else:
                with open(os.path.join(rekening,antwoord.upper()),"r") as c:
                    cat = ast.literal_eval(c.read())
                    cat[0][0] = antwoord2[:15]
                with open(os.path.join(rekening,antwoord.upper()),"w") as c:
                    print(cat, file = c, end = "")

def wijzigbudget(rekening,header,col):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    if Taal == "EN":
        wraptekst = textwrap.wrap("Redistribute budgets. Categories expecting income receive a negative budget, all others a positive one. Ensure that the balance is always %s" % (grotegetalkleuren(rekening,header,budgetnul)+"%s %s" % (valuta,fornum(budgetnul))+kleuren["ResetAll"]),w)
        woordbalans = "Balance: "
        catwoord = woordcategorieEN
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Riassegna i budget. Le categorie che prevedono entrate riceveranno un budget negativo, tutte le altre un budget positivo. Assicurati che il bilancio sia sempre %s" % (grotegetalkleuren(rekening,header,budgetnul)+"%s %s" % (valuta,fornum(budgetnul))+kleuren["ResetAll"]),w)
        woordbalans = "Bilancio: "
        catwoord = woordcategorieIT
    else:
        wraptekst = textwrap.wrap("Herverdeel budgetten. Categorieën waarop inkomsten verwacht worden krijgen een negatief budget, alle andere een positief. Let erop dat de balans altijd %s is" % (grotegetalkleuren(rekening,header,budgetnul)+"%s %s" % (valuta,fornum(budgetnul))+kleuren["ResetAll"]),w)
        woordbalans = "Balans: "
        catwoord = woordcategorie
    for i in wraptekst:
        print(i)
    categorieenlijst = haalcategorieen(rekening)
    aantalcategorieen = len(categorieenlijst)
    alternatievenamendict = haalalternatievenamen(rekening)
    loop = True
    while loop == True:
        tooncategorieen(rekening,header)
        balans = budgetnul*aantalcategorieen*-1
        for i in categorieenlijst:
            balans += haalcategorie(rekening,i)[0][1]
        print(woordbalans+grotegetalkleuren(rekening,header,balans*-1)+valuta+fornum(balans*-1)+kleuren["ResetAll"])
        antwoord = input(col+catwoord+inputindent)
        print(ResetAll, end = "")
        if antwoord.upper() in afsluitlijst:
            doei()
        elif antwoord.upper() in neelijst:
            return
        elif antwoord.upper() in categorieenlijst:
            categorie = haalcategorie(rekening,antwoord.upper())
            oudbudget = round(categorie[0][1],2)
            if Taal == "EN":
                wraptekst = textwrap.wrap("The new budget for %s %s %s %s %s" % (woordcategorieEN.lower(),catcol[antwoord.upper()]+antwoord.upper(),vertaalv(alternatievenamendict[antwoord.upper()])+kleuren["ResetAll"],grotegetalkleuren(rekening,header,oudbudget)+valuta,fornum(oudbudget)+kleuren["ResetAll"]),w)
            elif Taal == "IT":
                wraptekst = textwrap.wrap("Il nuovo budget per %s %s %s %s %s" % (woordcategorieIT.lower(),catcol[antwoord.upper()]+antwoord.upper(),vertaalv(alternatievenamendict[antwoord.upper()])+kleuren["ResetAll"],grotegetalkleuren(rekening,header,oudbudget)+valuta,fornum(oudbudget)+kleuren["ResetAll"]),w)
            else:
                wraptekst = textwrap.wrap("Het nieuwe budget voor %s %s %s %s %s" % (woordcategorie.lower(),catcol[antwoord.upper()]+antwoord.upper(),vertaalv(alternatievenamendict[antwoord.upper()])+kleuren["ResetAll"],grotegetalkleuren(rekening,header,oudbudget)+valuta,fornum(oudbudget)+kleuren["ResetAll"]),w)
            for i in wraptekst:
                print(i)
            antwoord2 = input(col+inputindent)
            print(ResetAll, end = "")
            if antwoord2.upper() in afsluitlijst:
                doei()
            elif antwoord2.upper() in neelijst:
                return
            else:
                test = checkfloat(antwoord2)
                if test == True:
                    categorie[0][1] = float(antwoord2)
                    with open(os.path.join(rekening,antwoord.upper()), "w") as c:
                        print(categorie, file = c, end = "")
                    budgetcorrectie(rekening)

def verwijdercategorie(rekening,header,col):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        wraptekst = textwrap.wrap("Remove a %s. %sAll transactions in this %s will be cancelled%s" % (woordcategorieEN.lower(),kleuren["colslecht"],woordcategorieEN.lower(),kleuren["ResetAll"]),w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Elimina una %s. %sTutte le transazioni in questa %s verranno cancellate%s" % (woordcategorieIT.lower(),kleuren["colslecht"],woordcategorieIT.lower(),kleuren["ResetAll"]),w)
    else:
        wraptekst = textwrap.wrap("Verwijder een %s. %sAlle transacties in deze %s worden gewist%s" % (woordcategorie.lower(),kleuren["colslecht"],woordcategorie.lower(),kleuren["ResetAll"]),w)
    for i in wraptekst:
        print(i)
    categorieenlijst = haalcategorieen(rekening)
    alternatievenamendict = haalalternatievenamen(rekening)
    loop = True
    while loop == True:
        tooncategorieen(rekening,header)
        antwoord = input(col+inputindent)
        print(ResetAll, end = "")
        if antwoord.upper() in afsluitlijst:
            doei()
        elif antwoord.upper() in neelijst:
            return
        elif antwoord.upper() in categorieenlijst:
            if antwoord.upper() not in nieuwalternatievenamendict:
                del alternatievenamendict[antwoord.upper()]
            else:
                alternatievenamendict[antwoord.upper()] = nieuwalternatievenamendict[antwoord.upper()]
            os.remove(os.path.join(rekening,antwoord.upper()))

def resetcategorie(rekening,header,col):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        hzlijst = ["Household","Business"]
        wraptekst = textwrap.wrap("Reset the entire account. You can choose it to be \"%s\" or \"%s\". %sAll transactions will be cancelled%s" % (hzlijst[0],hzlijst[1],kleuren["colslecht"],kleuren["ResetAll"]),w)
    elif Taal == "IT":
        hzlijst = ["Domestico","Aziendale"]
        wraptekst = textwrap.wrap("Ripristina l'intero conto. Puoi scegliere se deve essere \"%s\" o \"%s\". %sTutte le transazioni verranno cancellate%s" % (hzlijst[0],hzlijst[1],kleuren["colslecht"],kleuren["ResetAll"]),w)
    else:
        hzlijst = ["Huishoudelijk","Zakelijk"]
        wraptekst = textwrap.wrap("Reset de volledige rekening. Je kunt kiezen voor \"%s\" of \"%s\". %sAlle transacties worden gewist%s" % (hzlijst[0],hzlijst[1],kleuren["colslecht"],kleuren["ResetAll"]),w)
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        categorieenlijst = haalcategorieen(rekening)
        alternatievenamendict = haalalternatievenamen(rekening)
        tooncategorieen(rekening,header)
        for i in hzlijst:
            print(forr3(hzlijst.index(i))+" : "+i)
        antwoord = input(col+inputindent)
        print(ResetAll, end = "")
        if antwoord.upper() in afsluitlijst:
            doei()
        elif antwoord.upper() in neelijst:
            return
        elif antwoord.upper() in ["0","1"]:
            for i in lijst:
                try:
                    os.remove(os.path.join(rekening,i))
                except(Exception) as f:
                    #print(f)
                    pass
            if antwoord.upper() == "0":
                for i in huishoudelijkelijst:
                    with open(os.path.join(rekening,i),"w") as c:
                        print([budgetnul], file = c, end = "")
            else:
                for i in zakelijkelijst:
                    with open(os.path.join(rekening,i),"w") as c:
                        print([budgetnul], file = c, end = "")

def verwijderrekening(rekening,header,col):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        wraptekst = textwrap.wrap("Delete an account. The marked account is currently in use and cannot be deteleted in this session. %sAll transactions will be cancelled!%s" % (kleuren["colslecht"],kleuren["ResetAll"]),w)
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Rimuovere un conto. Il conto contrassegnato è in uso e non può essere eliminato in questa sessione. %sTutte le transazioni verranno cancellate!%s" % (kleuren["colslecht"],kleuren["ResetAll"]),w)
    else:
        wraptekst = textwrap.wrap("Verwijder een rekening. De gemarkeerde rekening is nu in gebruik en kan tijdens deze sessie niet worden verwijderd. %sAlle transacties worden gewist!%s" % (kleuren["colslecht"],kleuren["ResetAll"]),w)
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        rekeningenlijst = rekeningenoverzicht()
        toonrekeningenactief(rekeningenlijst)
        weg = input(col+inputindent)
        print(ResetAll, end = "")
        if weg.upper() in afsluitlijst:
            doei()
        elif weg.upper() in neelijst:
            return
        else:
            test = checkint(weg)
            if test == True:
                try:
                    andererekening = rekeningenlijst[int(weg)-1]
                    if andererekening != rekening:
                        andereIBAN = andererekening[:andererekening.index("#")]
                        andereJAAR = forr4(andererekening[andererekening.index("#")+1:])
                        with open(os.path.join(andererekening,"header"),"r") as ah:
                            andereheader = ast.literal_eval(ah.read())
                        anderekleuren,anderecatcol = updatekleuren(andererekening)
                        if Taal == "EN":
                            vraag = textwrap.wrap("Remove %s %s:" % (anderekleuren["coltoe"]+andereIBAN,andereJAAR+anderekleuren["ResetAll"]),w)
                        elif Taal == "IT":
                            vraag = textwrap.wrap("Elimina %s %s:" % (anderekleuren["coltoe"]+andereIBAN,andereJAAR+anderekleuren["ResetAll"]),w)
                        else:
                            vraag = textwrap.wrap("Verwijder %s %s:" % (anderekleuren["coltoe"]+andereIBAN,andereJAAR+anderekleuren["ResetAll"]),w)
                        for i in vraag:
                            print(i)
                        antwoord = geefjaofnee(rekening,header)
                        if antwoord.upper() in afsluitlijst:
                            doei()
                        elif antwoord.upper() in neelijst:
                            return
                        elif antwoord.upper() == ">":
                            shutil.rmtree(andererekening)
                except(Exception) as f:
                    #print(f)
                    pass

def headeroverzetten(rekening,header,col):
    Taal = header[nieuwheaderlijst[3]]
    kleuren,catcol = updatekleuren(rekening)
    if Taal == "EN":
        wraptekst = textwrap.wrap("Transfer all account settings to another account, including the opening balance from this account",w)
        headerlijst = nieuwheaderlijstEN
    elif Taal == "IT":
        wraptekst = textwrap.wrap("Trasferire tutte le impostazioni del conto a un altro account, incluso il saldo iniziale di questo conto",w)
        headerlijst = nieuwheaderlijstIT
    else:
        wraptekst = textwrap.wrap("Alle rekeninginstellingen overzetten naar andere rekening, inclusief het startsaldo van deze rekening",w)
        headerlijst = nieuwheaderlijst
    maxlen = len(max(headerlijst, key = len))
    for i in wraptekst:
        print(i)
    loop = True
    while loop == True:
        rekeningenlijst = rekeningenoverzicht()
        toonrekeningenactief(rekeningenlijst)
        deze = input(col+inputindent)
        print(ResetAll, end = "")
        if deze.upper() in afsluitlijst:
            doei()
        elif deze.upper() in neelijst:
            return
        else:
            test = checkint(deze)
            if test == True:
                try:
                    andererekening = rekeningenlijst[int(deze)-1]
                    if andererekening != rekening:
                        with open(os.path.join(andererekening,"header"),"w") as ah:
                            print(header, file = ah, end = "")
                except(Exception) as f:
                    #print(f)
                    pass

def beheerkeuze(rekening,header,col,keuze1lijst,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    if len(keuze1lijst) > 4:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
        keuze5 = keuze1lijst[4]
    elif len(keuze1lijst) > 3:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
    elif len(keuze1lijst) > 2:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
    elif len(keuze1lijst) > 1:
        keuze2 = keuze1lijst[1]
    else:
        if Taal == "EN":
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menuEN["0,0"],
          menuEN["0,1"],
          menuEN["0,2"],
          menuEN["0,3"],
          menuEN["0,4"],
          menuEN["0,5"]
          )
      )
        elif Taal == "IT":
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menuIT["0,0"],
          menuIT["0,1"],
          menuIT["0,2"],
          menuIT["0,3"],
          menuIT["0,4"],
          menuIT["0,5"]
          )
      )
        else:
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menu["0,0"],
          menu["0,1"],
          menu["0,2"],
          menu["0,3"],
          menu["0,4"],
          menu["0,5"]
          )
      )
    loop2 = True
    while loop2 == True:
        try:
            keuze2
        except(Exception) as f:
            #print(f)
            keuze2 = input(col+inputindent)
            print(ResetAll, end = "")
        if keuze2.upper() in afsluitlijst:
            doei()
        elif keuze2.upper() in neelijst:
            return rekening,header,col,keuze1lijst,ok
        elif keuze2.upper() == "H":
            dithelp(rekening,header,col,keuze1lijst)
            del keuze2
        elif keuze2 == "0":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                keuze1lijst = kieshelp(rekening,header,Wit,["0"])
                if keuze1lijst.upper() in neelijst:
                    return rekening,header,col,keuze1lijst,ok
                del keuze2
        elif keuze2 == "2":
            loop3 = True
            while loop3 == True:
                try:
                    keuze3
                except(Exception) as f:
                    #print(f)
                    if Taal == "EN":
                        maxlen = len(max(nieuwheaderlijstEN, key = len))
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s""" % (
          menuEN["0,2,1"],
          menuEN["0,2,2"],
          menuEN["0,2,3"],
          menuEN["0,2,4"],
          menuEN["0,2,5"],
          menuEN["0,2,6"]
          )
    )
                    elif Taal == "IT":
                        maxlen = len(max(nieuwheaderlijstIT, key = len))
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s""" % (
          menuIT["0,2,1"],
          menuIT["0,2,2"],
          menuIT["0,2,3"],
          menuIT["0,2,4"],
          menuIT["0,2,5"],
          menuIT["0,2,6"]
          )
    )
                    else:
                        maxlen = len(max(nieuwheaderlijst, key = len))
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s""" % (
          menu["0,2,1"],
          menu["0,2,2"],
          menu["0,2,3"],
          menu["0,2,4"],
          menu["0,2,5"],
          menu["0,2,6"]
          )
    )
                    keuze3 = input(col+inputindent)
                    print(ResetAll, end = "")
                if keuze3.upper() in afsluitlijst:
                    doei()
                elif keuze3.upper() in neelijst:
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3.upper() == "H":
                    dithelp(rekening,header,col,[keuze1lijst[0]+","+keuze2])
                    del keuze3
                elif keuze3 == "1":
                    toevoegencategorie(rekening,header,col)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "2":
                    wijzigcategorienaam(rekening,header,col)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "3":
                    wijzigbudget(rekening,header,col)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "4":
                    verwijdercategorie(rekening,header,col)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "5":
                    resetcategorie(rekening,header,col)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "6":
                    header = resetalt(rekening,header)
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                else:
                    return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "3":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                maaknieuwerekening()
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "4":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                verwijderrekening(rekening,header,col)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "5":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                headeroverzetten(rekening,header,col)
                return rekening,header,col,keuze1lijst,ok
        else:
            keuze2 = "1"
            loop3 = True
            while loop3 == True:
                Taal = header[nieuwheaderlijst[3]]
                try:
                    keuze3
                except(Exception) as f:
                    #print(f)
                    if Taal == "EN":
                        maxlen = len(max(nieuwheaderlijstEN, key = len))+1
                        print("""  0 : %s
  1 : %s %s
  2 : %s %s
  3 : %s %s
  4 : %s %s
  5 : %s %s
  6 : %s %s
  7 : %s %s
  8 : %s %s
  9 : %s %s
 10 : %s %s
 11 : %s %s
 12 : %s %s
 13 : %s %s
 14 : %s %s
 15 : %s %s""" % (
          menuEN["0,1,0"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,1"]), header[nieuwheaderlijst[0]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menuEN["0,1,2"]), header[nieuwheaderlijst[1]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menuEN["0,1,3"]), coljanee(rekening,header,header[nieuwheaderlijst[2]])+vertaalv(header[nieuwheaderlijst[2]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,4"]), taaldict[header[nieuwheaderlijst[3]]],
          ("{:<%d}" % maxlen).format(menuEN["0,1,5"]), header[nieuwheaderlijst[4]],
          ("{:<%d}" % maxlen).format(menuEN["0,1,6"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]]),
          ("{:<%d}" % maxlen).format(menuEN["0,1,7"]), coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,8"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1]),
          ("{:<%d}" % maxlen).format(menuEN["0,1,9"]), coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,10"]), vertaalv(header[nieuwheaderlijst[9]]+" (%s)" % opmaakdatum(int(nustr))),
          ("{:<%d}" % maxlen).format(menuEN["0,1,11"]), vertaalv(header[nieuwheaderlijst[10]]),
          ("{:<%d}" % maxlen).format(menuEN["0,1,12"]), header[nieuwheaderlijst[11]],
          ("{:<%d}" % maxlen).format(menuEN["0,1,13"]), coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,14"]), coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuEN["0,1,15"]), coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]]+kleuren["ResetAll"])
          )
    )
                    elif Taal == "IT":
                        maxlen = len(max(nieuwheaderlijstIT, key = len))+1
                        print("""  0 : %s
  1 : %s %s
  2 : %s %s
  3 : %s %s
  4 : %s %s
  5 : %s %s
  6 : %s %s
  7 : %s %s
  8 : %s %s
  9 : %s %s
 10 : %s %s
 11 : %s %s
 12 : %s %s
 13 : %s %s
 14 : %s %s
 15 : %s %s""" % (
          menuIT["0,1,0"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,1"]), header[nieuwheaderlijst[0]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menuIT["0,1,2"]), header[nieuwheaderlijst[1]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menuIT["0,1,3"]), coljanee(rekening,header,header[nieuwheaderlijst[2]])+vertaalv(header[nieuwheaderlijst[2]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,4"]), taaldict[header[nieuwheaderlijst[3]]],
          ("{:<%d}" % maxlen).format(menuIT["0,1,5"]), header[nieuwheaderlijst[4]],
          ("{:<%d}" % maxlen).format(menuIT["0,1,6"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]]),
          ("{:<%d}" % maxlen).format(menuIT["0,1,7"]), coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,8"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1]),
          ("{:<%d}" % maxlen).format(menuIT["0,1,9"]), coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,10"]), vertaalv(header[nieuwheaderlijst[9]]+" (%s)" % opmaakdatum(int(nustr))),
          ("{:<%d}" % maxlen).format(menuIT["0,1,11"]), vertaalv(header[nieuwheaderlijst[10]]),
          ("{:<%d}" % maxlen).format(menuIT["0,1,12"]), header[nieuwheaderlijst[11]],
          ("{:<%d}" % maxlen).format(menuIT["0,1,13"]), coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,14"]), coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menuIT["0,1,15"]), coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]]+kleuren["ResetAll"])
          )
    )
                    else:
                        maxlen = len(max(nieuwheaderlijst, key = len))+1
                        print("""  0 : %s
  1 : %s %s
  2 : %s %s
  3 : %s %s
  4 : %s %s
  5 : %s %s
  6 : %s %s
  7 : %s %s
  8 : %s %s
  9 : %s %s
 10 : %s %s
 11 : %s %s
 12 : %s %s
 13 : %s %s
 14 : %s %s
 15 : %s %s""" % (
          menu["0,1,0"],
          ("{:<%d}" % maxlen).format(menu["0,1,1"]), header[nieuwheaderlijst[0]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menu["0,1,2"]), header[nieuwheaderlijst[1]][:w - maxlen -7],
          ("{:<%d}" % maxlen).format(menu["0,1,3"]), coljanee(rekening,header,header[nieuwheaderlijst[2]])+vertaalv(header[nieuwheaderlijst[2]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menu["0,1,4"]), taaldict[header[nieuwheaderlijst[3]]],
          ("{:<%d}" % maxlen).format(menu["0,1,5"]), header[nieuwheaderlijst[4]],
          ("{:<%d}" % maxlen).format(menu["0,1,6"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[5]]),
          ("{:<%d}" % maxlen).format(menu["0,1,7"]), coljanee(rekening,header,header[nieuwheaderlijst[6]])+vertaalv(header[nieuwheaderlijst[6]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menu["0,1,8"]), header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][0])+" >< "+header[nieuwheaderlijst[4]]+fornum(header[nieuwheaderlijst[7]][1]),
          ("{:<%d}" % maxlen).format(menu["0,1,9"]), coljanee(rekening,header,header[nieuwheaderlijst[8]])+vertaalv(header[nieuwheaderlijst[8]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menu["0,1,10"]), vertaalv(header[nieuwheaderlijst[9]]+" (%s)" % opmaakdatum(int(nustr))),
          ("{:<%d}" % maxlen).format(menu["0,1,11"]), vertaalv(header[nieuwheaderlijst[10]]),
          ("{:<%d}" % maxlen).format(menu["0,1,12"]), header[nieuwheaderlijst[11]],
          ("{:<%d}" % maxlen).format(menu["0,1,13"]), coljanee(rekening,header,header[nieuwheaderlijst[12]])+vertaalv(header[nieuwheaderlijst[12]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menu["0,1,14"]), coljanee(rekening,header,header[nieuwheaderlijst[13]])+vertaalv(header[nieuwheaderlijst[13]])+kleuren["ResetAll"],
          ("{:<%d}" % maxlen).format(menu["0,1,15"]), coljanee(rekening,header,header[nieuwheaderlijst[14]])+vertaalv(header[nieuwheaderlijst[14]]+kleuren["ResetAll"])
          )
    )
                    keuze3 = input(col+inputindent)
                    print(ResetAll, end = "")
                if keuze3.upper() in afsluitlijst:
                    doei()
                elif keuze3.upper() in neelijst:
                    del keuze3
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3.upper() == "H":
                    dithelp(rekening,header,col,[keuze1lijst[0]+","+keuze2])
                    del keuze3
                elif keuze3 == "0":
                    header = resetheader(rekening,header)
                    del keuze3
                elif keuze3 == "1":
                    header = wijzigrekeningnaam(rekening,header)
                    del keuze3
                elif keuze3 == "2":
                    header = wijzigrekeninghoudernaam(rekening,header)
                    del keuze3
                elif keuze3 == "3":
                    header = wijzigactief(rekening,header)
                    del keuze3
                elif keuze3 == "4":
                    header = wijzigtaal(rekening,header)
                    del keuze3
                elif keuze3 == "5":
                    header = wijzigvaluta(rekening,header)
                    del keuze3
                elif keuze3 == "6":
                    header = wijzigstartsaldo(rekening,header)
                    del keuze3
                elif keuze3 == "7":
                    header = wijzigtoonsaldo(rekening,header)
                    del keuze3
                elif keuze3 == "8":
                    header = wijzigmarkering(rekening,header)
                    del keuze3
                elif keuze3 == "9":
                    header = wijzignullijnen(rekening,header)
                    del keuze3
                elif keuze3 == "10":
                    header = wijzigdatumopmaak(rekening,header)
                    del keuze3
                elif keuze3 == "11":
                    header = wijzigkleurenschema(rekening,header)
                    del keuze3
                elif keuze3 == "12":
                    header = wijzigmenuniveau(rekening,header)
                    del keuze3
                elif keuze3 == "13":
                    header = wijziganalyse2txt(rekening,header)
                    del keuze3
                elif keuze3 == "14":
                    header = wijzigexport2csv(rekening,header)
                    del keuze3
                elif keuze3 == "15":
                    header = wijzigtipvandedag(rekening,header)
                    del keuze3
                else:
                    del keuze3
            return rekening,header,col,keuze1lijst,ok

def toonkeuze(rekening,header,col,keuze1lijst,ok):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    if len(keuze1lijst) > 4:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
        keuze5 = keuze1lijst[4]
    elif len(keuze1lijst) > 3:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
    elif len(keuze1lijst) > 2:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
    elif len(keuze1lijst) > 1:
        keuze2 = keuze1lijst[1]
    else:
        eenrekeningtotaal(rekening)
        tooncategorieen(rekening,header)
        if Taal == "EN":
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s""" % (
          menuEN["1,0"],
          menuEN["1,1"],
          menuEN["1,2"],
          menuEN["1,3"]
          )
      )
        elif Taal == "IT":
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s""" % (
          menuIT["1,0"],
          menuIT["1,1"],
          menuIT["1,2"],
          menuIT["1,3"]
          )
      )
        else:
            print(
                    """  0 : %s
 >1 : %s
  2 : %s
  3 : %s""" % (
          menu["1,0"],
          menu["1,1"],
          menu["1,2"],
          menu["1,3"]
          )
      )
    loop2 = True
    while loop2 == True:
        try:
            keuze2
        except(Exception) as f:
            #print(f)
            keuze2 = input(col+inputindent)
            print(ResetAll, end = "")
        if keuze2.upper() in afsluitlijst:
            doei()
        elif keuze2.upper() in neelijst:
            return rekening,header,col,keuze1lijst,ok
        elif keuze2.upper() == "H":
            dithelp(rekening,header,col,keuze1lijst)
            del keuze2
        elif keuze2 == "0":
            loop3 = True
            while loop3 == True:
                try:
                    keuze3
                except(Exception) as f:
                    #print(f)
                    if Taal == "EN":
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menuEN["1,0,1"],
          menuEN["1,0,2"],
          menuEN["1,0,3"],
          menuEN["1,0,4"],
          menuEN["1,0,5"],
          menuEN["1,0,6"],
          menuEN["1,0,7"],
          menuEN["1,0,8"]
          )
    )
                    elif Taal == "IT":
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menuIT["1,0,1"],
          menuIT["1,0,2"],
          menuIT["1,0,3"],
          menuIT["1,0,4"],
          menuIT["1,0,5"],
          menuIT["1,0,6"],
          menuIT["1,0,7"],
          menuIT["1,0,8"]
          )
    )
                    else:
                        print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s
  5 : %s
  6 : %s
  7 : %s
  8 : %s""" % (
          menu["1,0,1"],
          menu["1,0,2"],
          menu["1,0,3"],
          menu["1,0,4"],
          menu["1,0,5"],
          menu["1,0,6"],
          menu["1,0,7"],
          menu["1,0,8"]
          )
    )
                    keuze3 = input(col+inputindent)
                    print(ResetAll, end = "")
                if keuze3.upper() in afsluitlijst:
                    doei()
                elif keuze3.upper() in neelijst:
                    return rekening,header,col,keuze1lijst,ok
                elif keuze3 == "1":
                    ok = sortokdatumreverse(rekening,ok)
                elif keuze3 == "2":
                    ok = sortokdatum(rekening,ok)
                elif keuze3 == "3":
                    ok = sortokbedragreverse(rekening,ok)
                elif keuze3 == "4":
                    ok = sortokbedrag(rekening,ok)
                elif keuze3 == "5":
                    ok = sortokwederpartijreverse(rekening,ok)
                elif keuze3 == "6":
                    ok = sortokwederpartij(rekening,ok)
                elif keuze3 == "7":
                    ok = sortokonderwerpreverse(rekening,ok)
                elif keuze3 == "8":
                    ok = sortokonderwerp(rekening,ok)
                else:
                    ok = collectie(rekening,ok)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "2":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                datumlijst = [startdatum,einddatum]
                maandanalyse(rekening,datumlijst)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "3":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = toontransactie(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        else: # "1"
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                rekening,header,col,keuze1lijst,ok = printselectie(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok

def nieuwkeuze(keuze1lijst,rekening,ok):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if len(keuze1lijst) > 4:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
        keuze5 = keuze1lijst[4]
    elif len(keuze1lijst) > 3:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
    elif len(keuze1lijst) > 2:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
    elif len(keuze1lijst) > 1:
        keuze2 = keuze1lijst[1]
    else:
        if Taal == "EN":
            print(
                    """ >1 : %s
  2 : %s""" % (
          menuEN["2,1"],
          menuEN["2,2"],
          )
      )
        elif Taal == "IT":
            print(
                    """ >1 : %s
  2 : %s""" % (
          menuIT["2,1"],
          menuIT["2,2"],
          )
      )
        else:
            print(
                    """ >1 : %s
  2 : %s""" % (
          menu["2,1"],
          menu["2,2"],
          )
      )
    loop = True
    while loop == True:
        try:
            keuze2
        except(Exception) as f:
            #print(f)
            keuze2 = input(col+inputindent)
            print(ResetAll, end = "")
        if keuze2.upper() in afsluitlijst:
            doei()
        elif keuze2.upper() in neelijst:
            return rekening,header,col,keuze1lijst,ok
        elif keuze2.upper() == "H":
            dithelp(rekening,header,col,keuze1lijst)
            del keuze2
        elif keuze2 == "2":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = nieuwkopie(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        else: # "1"
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = nieuwnieuw(rekening,ok)
                return rekening,header,col,keuze1lijst,ok

def wijzigkeuze(keuze1lijst,rekening,ok):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if len(keuze1lijst) > 4:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
        keuze5 = keuze1lijst[4]
    elif len(keuze1lijst) > 3:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
    elif len(keuze1lijst) > 2:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
    elif len(keuze1lijst) > 1:
        keuze2 = keuze1lijst[1]
    else:
        if Taal == "EN":
            print(
                    """  1 : %s
 >2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menuEN["3,1"],
          menuEN["3,2"],
          menuEN["3,3"],
          menuEN["3,4"],
          menuEN["3,5"]
          )
      )
        elif Taal == "IT":
            print(
                    """  1 : %s
 >2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menuIT["3,1"],
          menuIT["3,2"],
          menuIT["3,3"],
          menuIT["3,4"],
          menuIT["3,5"]
          )
      )
        else:
            print(
                    """  1 : %s
 >2 : %s
  3 : %s
  4 : %s
  5 : %s""" % (
          menu["3,1"],
          menu["3,2"],
          menu["3,3"],
          menu["3,4"],
          menu["3,5"]
          )
      )
    loop = True
    while loop == True:
        try:
            keuze2
        except(Exception) as f:
            #print(f)
            keuze2 = input(col+inputindent)
            print(ResetAll, end = "")
        if keuze2.upper() in afsluitlijst:
            doei()
        elif keuze2.upper() in neelijst:
            return rekening,header,col,keuze1lijst,ok
        elif keuze2.upper() == "H":
            dithelp(rekening,header,col,keuze1lijst)
            del keuze2
        elif keuze2 == "1":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = wijzigdatum(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "3":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = wijzigwederpartij(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "4":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = wijzigonderwerp(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        elif keuze2 == "5":
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = wijzigcategorie(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok
        else: # "2"
            try:
                keuze3
            except(Exception) as f:
                #print(f)
                ok = wijzigbedrag(rekening,header,col,ok)
                return rekening,header,col,keuze1lijst,ok

def haalspaarpotten(rekening):
    try:
        with open(os.path.join(rekening,"spaarpotten"),"r") as s:
            spaarpotten = ast.literal_eval(s.read())
        for i in spaarpotten:
            if spaarpotten[i][0]+spaarpotten[i][2] < spaarpotten[i][1]:
                spaarpotten[i][1] = spaarpotten[i][0]+spaarpotten[i][2]
                with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                    print(spaarpotten, file = s, end = "")
    except(Exception) as f:
        #print(f)
        spaarpotten = {}
    return spaarpotten

def inspaarpotten(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottegoed = 0
    if len(spaarpotten) > 0:
        for i in spaarpotten:
            spaarpottegoed += spaarpotten[i][1]
        tegoed,forsom,K = grootgetal(spaarpottegoed,fornum,"")
        if Taal == "EN":
            totaalinspaarpotten = "There is %s put aside in %s%s savings pots%s" % (grotegetalkleuren(rekening,header,spaarpottegoed)+valuta+forsom(tegoed)+K+kleuren["ResetAll"],kleuren["5"],len(spaarpotten),kleuren["ResetAll"])
        elif Taal == "IT":
            totaalinspaarpotten = "Messo da parte %s in %s%s salvadanai%s" % (grotegetalkleuren(rekening,header,spaarpottegoed)+valuta+forsom(tegoed)+K+kleuren["ResetAll"],kleuren["5"],len(spaarpotten),kleuren["ResetAll"])
        else:
            totaalinspaarpotten = "Er is %s opzij gezet in %s%s spaarpotten%s" % (grotegetalkleuren(rekening,header,spaarpottegoed)+valuta+forsom(tegoed)+K+kleuren["ResetAll"],kleuren["5"],len(spaarpotten),kleuren["ResetAll"])
        print(totaalinspaarpotten)
    return spaarpottegoed
        
def vrijbesteedbaar(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottegoed = inspaarpotten(rekening,header)
    rekeningtotaal = rekeningsom(rekening)
    categorieen = haalcategorieen(rekening)
    negatiefbudget = 0 
    for i in categorieen:
        categorie = haalcategorie(rekening,i)
        if categorie[0][1] < 0:
            negatiefbudget += categorie[0][1]
    besteedbaar = rekeningtotaal - spaarpottegoed + negatiefbudget
    vrij,forsom,K = grootgetal(besteedbaar,fornum,"")
    if Taal == "EN":
        vrijtegoed = "There is %s discretionary" % (grotegetalkleuren(rekening,header,besteedbaar)+valuta+forsom(vrij)+K+kleuren["ResetAll"])
    elif Taal == "IT":
        vrijtegoed = "È disponibile %s da spendere liberamente" % (grotegetalkleuren(rekening,header,besteedbaar)+valuta+forsom(vrij)+K+kleuren["ResetAll"])
    else:
        vrijtegoed = "Er is %s vrij te besteden" % (grotegetalkleuren(rekening,header,besteedbaar)+valuta+forsom(vrij)+K+kleuren["ResetAll"])
    print(vrijtegoed)
    return besteedbaar

def toonspaarpotten(rekening,header):
    vrijbesteedbaar(rekening,header)
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    if Taal == "EN":
        geenspaarpot = geenspaarpottenEN
        lijnst = lijnlijstEN
    elif Taal == "IT":
        geenspaarpot = geenspaarpottenIT
        lijnst = lijnlijstIT
    else:
        geenspaarpot = geenspaarpotten
        lijnst = lijnlijst
    if len(spaarpotten) == 0:
        print(geenspaarpot)
    spaarpottentoplijn = col+"+"+"-"*3+"+"+"-"*17+"+"+"-"*11+"+"+"-"*11+"+"+"-"*11+"+"+"-"*11+"+"+kleuren["ResetAll"]
    lijnlijstlijn = col+"|"+kleuren["ResetAll"]\
    +forc3(lijnst[0])+" "\
    +forc17(lijnst[1])+" "\
    +forc11(lijnst[2])+" "\
    +forc11(lijnst[3])+" "\
    +forc11(lijnst[4])+" "\
    +forc11(lijnst[5])+col\
    +"|"+kleuren["ResetAll"]
    print(spaarpottentoplijn)
    print(lijnlijstlijn)
    print(spaarpottentoplijn)
    tel = 1
    for i in spaarpotten:
        tegaan = (spaarpotten[i][0] + spaarpotten[i][2]) * -1
        print(col+"|"+kleuren["ResetAll"]\
            +forc3(tel)+": "\
            +kleuren["5"]+forl15(i[:15])+" : "\
            +kleuren["Vaag"]+valuta+grootgetal(spaarpotten[i][0],fornum,"")[1](grootgetal(spaarpotten[i][0],fornum,"")[0])+grootgetal(spaarpotten[i][0],fornum,"")[2]+kleuren["ResetAll"]+" : "\
            +grotegetalkleuren(rekening,header,spaarpotten[i][1])+valuta+grootgetal(spaarpotten[i][1],fornum,"")[1](grootgetal(spaarpotten[i][1],fornum,"")[0])+grootgetal(spaarpotten[i][1],fornum,"")[2]+kleuren["ResetAll"]+" : "\
            +grotegetalkleuren(rekening,header,spaarpotten[i][2])+valuta+grootgetal(spaarpotten[i][2],fornum,"")[1](grootgetal(spaarpotten[i][2],fornum,"")[0])+grootgetal(spaarpotten[i][2],fornum,"")[2]+kleuren["ResetAll"]+" : "\
            +grotegetalkleuren(rekening,header,tegaan)+valuta+grootgetal(tegaan,fornum,"")[1](grootgetal(tegaan,fornum,"")[0])+grootgetal(tegaan,fornum,"")[2]+kleuren["ResetAll"]\
            +col+" |"+kleuren["ResetAll"]
        )
        tel += 1
    print(spaarpottentoplijn)

def tooneenspaarpot(rekening,header,spaarpotten,spaarpot):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    if Taal == "EN":
        lijnst = lijnlijstEN
    elif Taal == "IT":
        lijnst = lijnlijstIT
    else:
        lijnst = lijnlijst
    lijnst.append(spaarpot)
    maxlen = len(max(lijnst, key = len))
    for i in spaarpotten:
        if i == spaarpot:
            tegaan = (spaarpotten[i][0] + spaarpotten[i][2]) * -1
            try:
                print(" "*10+col+"+-"+kleuren["Omkeren"]+spaarpot+kleuren["ResetAll"]+col+"-"*(maxlen-(len(spaarpot)))+"+"+"-"*10+kleuren["ResetAll"])
                print(" "*10+col+"| "+kleuren["ResetAll"]+("{:<%d}" % maxlen).format(lijnst[2])+":  "+col+kleuren["Vaag"]+valuta+grootgetal(spaarpotten[i][0],fornum,"")[1](grootgetal(spaarpotten[i][0],fornum,"")[0])+grootgetal(spaarpotten[i][0],fornum,"")[2]+kleuren["ResetAll"])
                print(" "*10+col+"| "+kleuren["ResetAll"]+("{:<%d}" % maxlen).format(lijnst[3])+":  "+grotegetalkleuren(rekening,header,spaarpotten[i][1])+valuta+grootgetal(spaarpotten[i][1],fornum,"")[1](grootgetal(spaarpotten[i][1],fornum,"")[0])+grootgetal(spaarpotten[i][1],fornum,"")[2]+kleuren["ResetAll"])
                print(" "*10+col+"| "+kleuren["ResetAll"]+("{:<%d}" % maxlen).format(lijnst[4])+":  "+grotegetalkleuren(rekening,header,spaarpotten[i][2])+valuta+grootgetal(spaarpotten[i][2],fornum,"")[1](grootgetal(spaarpotten[i][2],fornum,"")[0])+grootgetal(spaarpotten[i][2],fornum,"")[2]+kleuren["ResetAll"])
                print(" "*10+col+"+-"+"-"*maxlen+"+"+"-"*10+kleuren["ResetAll"])
            except(Exception) as f:
                #print(f)
                pass

def nieuwespaarpot(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header,spaarpotten)
        if Taal == "EN":
            print(menuEN["5,2"])
            vragenlijst = ["Name","Target value"]
            bestaatal = "This savings pot exists already"
        elif Taal == "IT":
            print(menuIT["5,2"])
            vragenlijst = ["Nome","Valore obiettivo"]
            bestaatal = "Questo salvadanaio esiste già"
        else:
            print(menu["5,2"])
            vragenlijst = ["Naam","Doelwaarde"]
            bestaatal = "Deze spaarpot bestaat al"
        maxlen = len(max(vragenlijst, key = len))
        loop = True
        while loop == True:
            naam = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(vragenlijst[0])+kleuren["ResetAll"]+inputindent)
            if naam.upper() in afsluitlijst:
                doei()
            elif naam.upper() in neelijst:
                return "<"
            elif len(naam) > 0:
                if naam[0] != "#":
                    naam = "#"+naam
            if naam in spaarpotten:
                print(kleuren["colslecht"]+bestaatal+kleuren["ResetAll"])
            elif naam == "":
                pass
            else:    
                print(col+naam+kleuren["ResetAll"])
                doel = input(kleuren["Omkeren"]+col+("{:^%d}" % maxlen).format(vragenlijst[1])+kleuren["ResetAll"]+inputindent)
                if doel.upper() in afsluitlijst:
                    doei()
                elif doel.upper() in neelijst:
                    return "<"
                test = checkfloat(doel)
                if test == True:
                    print(col+valuta+fornum(float(doel))+kleuren["ResetAll"])
                    spaarpotten[naam] = [float(doel),0,0]
                    toonspaarpotten(rekening,header,spaarpotten)
                    with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                        print(spaarpotten, file = s, end = "")
                else:
                    print(kleuren["colslecht"]+oeps+kleuren["ResetAll"])
                
    else:
        return "<"

def kiesspaarpot(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header,spaarpotten)
        if Taal == "EN":
            wraptekst = textwrap.wrap("Choose a savings pot",w)
        elif Taal == "IT":
            wraptekst = textwrap.wrap("Scegliere un salvadanaio",w)
        else:
            wraptekst = textwrap.wrap("Kies een spaarpot",w)
        for i in wraptekst:
            print(i)
        loop = True
        while loop == True:
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        spaarpot = spaarpottenlijst[int(spaarpotkeuze)-1]
                        return spaarpot
    else:
        return "<"

def verwijderspaarpot(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header,spaarpotten)
        if Taal == "EN":
            wraptekst1 = textwrap.wrap(kleuren["colslecht"]+menuEN["5,4"]+kleuren["ResetAll"],w)
            wraptekst2 = textwrap.wrap("Choose a savings pot",w)
        elif Taal == "IT":
            wraptekst1 = textwrap.wrap(kleuren["colslecht"]+menuIT["5,4"]+kleuren["ResetAll"],w)
            wraptekst2 = textwrap.wrap("Scegli un salvadanaio",w)
        else:
            wraptekst1 = textwrap.wrap(kleuren["colslecht"]+menu["5,4"]+kleuren["ResetAll"],w)
            wraptekst2 = textwrap.wrap("Kies een spaarpot",w)
        loop = True
        while loop == True:
            for i in wraptekst1:
                print(i)
            for i in wraptekst2:
                print(i)
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        tooneenspaarpot(rekening,header,spaarpotten,spaarpottenlijst[int(spaarpotkeuze)-1])
                        jn = geefjaofnee(rekening,header)
                        if jn.upper() in afsluitlijst:
                            doei()
                        elif jn.upper() in neelijst:
                            return "<"
                        else:
                            del spaarpotten[spaarpottenlijst[int(spaarpotkeuze)-1]]
                            toonspaarpotten(rekening,header,spaarpotten)
                            with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                                print(spaarpotten, file = s, end = "")
                            spaarpotten = haalspaarpotten(rekening)
                            spaarpottenlijst = []
                            for i in spaarpotten:
                                spaarpottenlijst.append(i)
    else:
        return "<"

def wijzigspaarpotnaam(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if Taal == "EN":
        wraptekst1 = textwrap.wrap(col+menuEN["5,3,1"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Choose a savings pot",w)
        geenspaarpot = geenspaarpottenEN
    elif Taal == "IT":
        wraptekst1 = textwrap.wrap(col+menuIT["5,3,1"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Scegli un salvadanaio",w)
        geenspaarpot = geenspaarpottenIT
    else:
        wraptekst1 = textwrap.wrap(col+menu["5,3,1"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Kies een spaarpot",w)
        geenspaarpot = geenspaarpotten
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header)
        loop = True
        while loop == True:
            for i in wraptekst1:
                print(i)
            for i in wraptekst2:
                print(i)
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            elif spaarpotkeuze.upper() == "H":
                if Taal == "EN":
                    for i in helpmenuEN["5,3,1"]:
                        print(i)
                if Taal == "IT":
                    for i in helpmenuIT["5,3,1"]:
                        print(i)
                else:
                    for i in helpmenu["5,3,1"]:
                        print(i)
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        tooneenspaarpot(rekening,header,spaarpotten,spaarpottenlijst[int(spaarpotkeuze)-1])
                        if Taal == "EN":
                            wraptekst3 = textwrap.wrap("Rename %ssavings pot %s%s to" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                            bestaatal = "This savings pot exists already"
                        elif Taal == "IT":
                            wraptekst3 = textwrap.wrap("Rinomina %ssalvadanaio %s%s in" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                            bestaatal = "Questo salvadanaio esiste già"
                        else:
                            wraptekst3 = textwrap.wrap("De nieuwe naam voor %sspaarpot %s%s is" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                            bestaatal = "Deze spaarpot bestaat al"
                        for i in wraptekst3:
                            print(i)
                        nieuwenaam = input(col+inputindent)
                        print(ResetAll, end = "")
                        if nieuwenaam.upper() in afsluitlijst:
                            doei()
                        elif nieuwenaam.upper() in neelijst:
                            return "<"
                        elif len(nieuwenaam) > 0:
                            if nieuwenaam[0] != "#":
                                nieuwenaam = "#"+nieuwenaam
                        else:
                            nieuwenaam = "#"+spaarpotkeuze
                        if nieuwenaam in spaarpotten:
                            print(kleuren["colslecht"]+bestaatal+kleuren["ResetAll"])
                        else:
                            spaarpotten = {nieuwenaam if k == spaarpottenlijst[int(spaarpotkeuze)-1] else k:v for k,v in spaarpotten.items()}
                            with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                                print(spaarpotten, file = s, end = "")
                            spaarpotten = haalspaarpotten(rekening)
                            spaarpottenlijst = []
                            for i in spaarpotten:
                                spaarpottenlijst.append(i)
                            toonspaarpotten(rekening,header)
    else:
        print(geenspaarpot)
        return "<"

def wijzigspaarpotdoelsaldo(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if Taal == "EN":
        wraptekst1 = textwrap.wrap(col+menuEN["5,3,2"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Choose a savings pot",w)
        geenspaarpot = geenspaarpottenEN
    elif Taal == "IT":
        wraptekst1 = textwrap.wrap(col+menuIT["5,3,2"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Scegli un salvadanaio",w)
        geenspaarpot = geenspaarpottenIT
    else:
        wraptekst1 = textwrap.wrap(col+menu["5,3,2"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Kies een spaarpot",w)
        geenspaarpot = geenspaarpotten
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header)
        loop = True
        while loop == True:
            for i in wraptekst1:
                print(i)
            for i in wraptekst2:
                print(i)
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            elif spaarpotkeuze.upper() == "H":
                if Taal == "EN":
                    for i in helpmenuEN["5,3,2"]:
                        print(i)
                if Taal == "IT":
                    for i in helpmenuIT["5,3,2"]:
                        print(i)
                else:
                    for i in helpmenu["5,3,2"]:
                        print(i)
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        tooneenspaarpot(rekening,header,spaarpotten,spaarpottenlijst[int(spaarpotkeuze)-1])
                        if Taal == "EN":
                            wraptekst3 = textwrap.wrap("Set %ssavings pot %s%s target value at" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        elif Taal == "IT":
                            wraptekst3 = textwrap.wrap("Il nuovo saldo obiettivo per %ssalvadanaio %s%s è" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        else:
                            wraptekst3 = textwrap.wrap("Het nieuwe doelsaldo voor %sspaarpot %s%s is" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        for i in wraptekst3:
                            print(i)
                        nieuwsaldo = input(col+inputindent)
                        print(ResetAll, end = "")
                        if nieuwsaldo.upper() in afsluitlijst:
                            doei()
                        elif nieuwsaldo.upper() in neelijst:
                            return "<"
                        test = checkfloat(nieuwsaldo)
                        if test == True:
                            spaarpotten[spaarpottenlijst[int(spaarpotkeuze)-1]][0] = float(nieuwsaldo)
                            with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                                print(spaarpotten, file = s, end = "")
                            spaarpotten = haalspaarpotten(rekening)
                            spaarpottenlijst = []
                            for i in spaarpotten:
                                spaarpottenlijst.append(i)
                            toonspaarpotten(rekening,header)
    else:
        print(geenspaarpot)
        return "<"

def wijzigspaarpottegoed(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if Taal == "EN":
        wraptekst1 = textwrap.wrap(col+menuEN["5,3,3"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Choose a savings pot",w)
        geenspaarpot = geenspaarpottenEN
    elif Taal == "IT":
        wraptekst1 = textwrap.wrap(col+menuIT["5,3,3"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Scegli un salvadanaio",w)
        geenspaarpot = geenspaarpottenIT
    else:
        wraptekst1 = textwrap.wrap(col+menu["5,3,3"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Kies een spaarpot",w)
        geenspaarpot = geenspaarpotten
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header)
        loop = True
        while loop == True:
            for i in wraptekst1:
                print(i)
            for i in wraptekst2:
                print(i)
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            elif spaarpotkeuze.upper() == "H":
                if Taal == "EN":
                    for i in helpmenuEN["5,3,3"]:
                        print(i)
                if Taal == "IT":
                    for i in helpmenuIT["5,3,3"]:
                        print(i)
                else:
                    for i in helpmenu["5,3,3"]:
                        print(i)
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        tooneenspaarpot(rekening,header,spaarpotten,spaarpottenlijst[int(spaarpotkeuze)-1])
                        if Taal == "EN":
                            wraptekst3 = textwrap.wrap("Set %ssavings pot %s%s credit at" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        elif Taal == "IT":
                            wraptekst3 = textwrap.wrap("Il nuovo credito in %ssalvadanaio %s%s è" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        else:
                            wraptekst3 = textwrap.wrap("Het nieuwe tegoed in %sspaarpot %s%s is" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        for i in wraptekst3:
                            print(i)
                        nieuwtegoed = input(col+inputindent)
                        print(ResetAll, end = "")
                        if nieuwtegoed.upper() in afsluitlijst:
                            doei()
                        elif nieuwtegoed.upper() in neelijst:
                            return "<"
                        test = checkfloat(nieuwtegoed)
                        if test == True:
                            spaarpotten[spaarpottenlijst[int(spaarpotkeuze)-1]][1] = float(nieuwtegoed)
                            with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                                print(spaarpotten, file = s, end = "")
                            spaarpotten = haalspaarpotten(rekening)
                            spaarpottenlijst = []
                            for i in spaarpotten:
                                spaarpottenlijst.append(i)
                            toonspaarpotten(rekening,header)
    else:
        print(geenspaarpot)
        return "<"

def wijzigspaarpotbetaald(rekening,header):
    kleuren,catcol = updatekleuren(rekening)
    Taal = header[nieuwheaderlijst[3]]
    valuta = header[nieuwheaderlijst[4]]
    spaarpotten = haalspaarpotten(rekening)
    spaarpottenlijst = []
    for i in spaarpotten:
        spaarpottenlijst.append(i)
    if Taal == "EN":
        wraptekst1 = textwrap.wrap(col+menuEN["5,3,4"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Choose a savings pot",w)
        geenspaarpot = geenspaarpottenEN
    elif Taal == "IT":
        wraptekst1 = textwrap.wrap(col+menuIT["5,3,4"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Scegli un salvadanaio",w)
        geenspaarpot = geenspaarpottenIT
    else:
        wraptekst1 = textwrap.wrap(col+menu["5,3,4"]+kleuren["ResetAll"],w)
        wraptekst2 = textwrap.wrap("Kies een spaarpot",w)
        geenspaarpot = geenspaarpotten
    if len(spaarpotten) > 0:
        toonspaarpotten(rekening,header)
        loop = True
        while loop == True:
            for i in wraptekst1:
                print(i)
            for i in wraptekst2:
                print(i)
            spaarpotkeuze = input(col+inputindent)
            print(ResetAll, end = "")
            if spaarpotkeuze.upper() in afsluitlijst:
                doei()
            elif spaarpotkeuze.upper() in neelijst:
                return "<"
            elif spaarpotkeuze.upper() == "H":
                if Taal == "EN":
                    for i in helpmenuEN["5,3,4"]:
                        print(i)
                if Taal == "IT":
                    for i in helpmenuIT["5,3,4"]:
                        print(i)
                else:
                    for i in helpmenu["5,3,4"]:
                        print(i)
            else:
                test = checkint(spaarpotkeuze)
                if test == True:
                    if int(spaarpotkeuze)-1 in range(len(spaarpotten)):
                        tooneenspaarpot(rekening,header,spaarpotten,spaarpottenlijst[int(spaarpotkeuze)-1])
                        if Taal == "EN":
                            wraptekst3 = textwrap.wrap("From this %ssavings pot %s%s is paid" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        elif Taal == "IT":
                            wraptekst3 = textwrap.wrap("Da questo %ssalvadanaio %s%s è pagato" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        else:
                            wraptekst3 = textwrap.wrap("Uit deze %sspaarpot %s%s is betaald" % (col,spaarpottenlijst[int(spaarpotkeuze)-1],kleuren["ResetAll"]),w)
                        for i in wraptekst3:
                            print(i)
                        nieuwbetaald = input(col+inputindent)
                        print(ResetAll, end = "")
                        if nieuwbetaald.upper() in afsluitlijst:
                            doei()
                        elif nieuwbetaald.upper() in neelijst:
                            return "<"
                        test = checkfloat(nieuwbetaald)
                        if test == True:
                            spaarpotten[spaarpottenlijst[int(spaarpotkeuze)-1]][1] = float(nieuwbetaald)
                            with open(os.path.join(rekening,"spaarpotten"),"w") as s:
                                print(spaarpotten, file = s, end = "")
                            spaarpotten = haalspaarpotten(rekening)
                            spaarpottenlijst = []
                            for i in spaarpotten:
                                spaarpottenlijst.append(i)
                            toonspaarpotten(rekening,header)
    else:
        print(geenspaarpot)
        return "<"

def spaarpotkeuze(keuze1lijst,rekening,ok):
    #spaarpotten = haalspaarpotten(rekening)
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    if Taal == "EN":
        geenspaarpot = geenspaarpottenEN
    elif Taal == "IT":
        geenspaarpot = geenspaarpottenIT
    else:
        geenspaarpot = geenspaarpotten
    if len(keuze1lijst) > 4:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
        keuze5 = keuze1lijst[4]
    elif len(keuze1lijst) > 3:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
        keuze4 = keuze1lijst[3]
    elif len(keuze1lijst) > 2:
        keuze2 = keuze1lijst[1]
        keuze3 = keuze1lijst[2]
    elif len(keuze1lijst) > 1:
        keuze2 = keuze1lijst[1]
    loop2 = True
    while loop2 == True:
        try:
            keuze2
        except(Exception) as f:
            #print(f)
            if Taal == "EN":
                print(
          """ >1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menuEN["5,1"],
          menuEN["5,2"],
          menuEN["5,3"],
          menuEN["5,4"]
          )
      )
            elif Taal == "IT":
                print(
          """ >1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menuIT["5,1"],
          menuIT["5,2"],
          menuIT["5,3"],
          menuIT["5,4"]
          )
      )
            else:
                print(
          """ >1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menu["5,1"],
          menu["5,2"],
          menu["5,3"],
          menu["5,4"]
          )
      )
            keuze2 = input(col+inputindent)
            print(ResetAll, end = "")
        if keuze2.upper() in afsluitlijst:
            doei()
        elif keuze2.upper() in neelijst:
            return rekening,header,col,keuze1lijst,ok
        elif keuze2.upper() == "H":
            dithelp(rekening,header,col,keuze1lijst)
            del keuze2
        elif keuze2 == "2":
            spaarpot = nieuwespaarpot(rekening,header)
            del keuze2
        elif keuze2 == "3":
            spaarpotten = haalspaarpotten(rekening)
            if len(spaarpotten) > 0:
                loop3 = True
                while loop3 == True:
                    try:
                        keuze3
                    except(Exception) as f:
                        #print(f)
                        if Taal == "EN":
                            print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menuEN["5,3,1"],
          menuEN["5,3,2"],
          menuEN["5,3,3"],
          menuEN["5,3,4"]
              )
          )
                        elif Taal == "IT":
                            print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menuIT["5,3,1"],
          menuIT["5,3,2"],
          menuIT["5,3,3"],
          menuIT["5,3,4"]
              )
          )
                        else:
                            print("""  1 : %s
  2 : %s
  3 : %s
  4 : %s""" % (
          menu["5,3,1"],
          menu["5,3,2"],
          menu["5,3,3"],
          menu["5,3,4"]
              )
          )
                        keuze3 = input(col+inputindent)
                        print(ResetAll, end = "")
                    if keuze3.upper() in afsluitlijst:
                        doei()
                    elif keuze3.upper() in neelijst:
                        return rekening,header,col,keuze1lijst,ok
                    elif keuze3 == "1":
                        wijzigspaarpotnaam(rekening,header)
                        del keuze3
                    elif keuze3 == "2":
                        wijzigspaarpotdoelsaldo(rekening,header)
                        del keuze3
                    elif keuze3 == "3":
                        wijzigspaarpottegoed(rekening,header)
                        del keuze3
                    elif keuze3 == "4":
                        wijzigspaarpotbetaald(rekening,header)
                        del keuze3
                    else:
                        del keuze3
            else:
                print(geenspaarpot)
                del keuze2
        elif keuze2 == "4":
            spaarpotten = haalspaarpotten(rekening)
            if len(spaarpotten) > 0:
                spaarpot = verwijderspaarpot(rekening,header)
                del keuze2
            else:
                print(geenspaarpot)
                del keuze2
        else:
            keuze2 = "1"
            toonspaarpotten(rekening,header)
            del keuze2

def keuze1menu(rekening):
    kleuren,catcol = updatekleuren(rekening)
    header = haalheader(rekening)
    Taal = header[nieuwheaderlijst[3]]
    niveau = header[nieuwheaderlijst[11]]
    if niveau < 1:
        niveau = 1
    if Taal == "EN":
        keuzemenu = menuEN
    elif Taal == "IT":
        keuzemenu = menuIT
    else:
        keuzemenu = menu
    keuzemaxi = []
    keuzemaxj = []
    for i,j in keuzemenu.items():
        aantalkommasini = i.count(",")
        if aantalkommasini < niveau:
            keuzemaxi.append(i)
            keuzemaxj.append(j)
    maxleni = len(max(keuzemaxi, key = len))
    maxlenj = len(max(keuzemaxj, key = len))
    okstring = ""
    if len(ok) > 0:
        for i in ok:
            okstring += i+" "
        if len(okstring.strip()) <= maxleni+maxlenj+5:
            for i in okstring.strip().split(" "):
                print(catcol[i[0]], end = "")
                print(i, end = "")
                print(ResetAll+" ", end = "")
            print()
        else:
            okstring = okstring.strip()[:maxleni+maxlenj+2]
            for i in okstring.strip().split(" "):
                print(catcol[i[0]], end = "")
                print(i, end = "")
                print(ResetAll+" ", end = "")
            print(">")
    keuze1menulijst = []
    for i,j in keuzemenu.items():
        aantalkommasini = i.count(",")
        if aantalkommasini < niveau:
            if i.count(",") == 0:
                print(kleuren["Omkeren"]+kleuren[i[0]]+("{:^%s}" % (maxleni)).format(i)+": "+("{:^%s}" % maxlenj).format(j)+kleuren["ResetAll"])
            elif i.count(",") == 1:
                print(kleuren[i[0]]+("{:^%s}" % (maxleni)).format(i)+": "+("{:<%s}" % maxlenj).format(j)+kleuren["ResetAll"])
            else:
                print(kleuren["Vaag"]+kleuren[i[0]]+("{:^%s}" % (maxleni)).format(i)+": "+("{:<%s}" % maxlenj).format(j)+kleuren["ResetAll"])
            keuze1menulijst.append(i)
    keuze1 = input(inputindent).replace(" ",",").replace("-",",").replace("/",",").replace(".",",")
    keuze1lijst = keuze1.split(",")
    if keuze1.upper() in afsluitlijst:
        doei()
    elif keuze1.upper() in neelijst:
        return rekening,header,"",keuze1lijst,ok
    elif keuze1lijst[0].upper() == "H":
        keuze1lijst[0] = kieshelp(rekening,header,Wit,["0"])
        return rekening,header,"",keuze1lijst,ok
    elif keuze1 not in keuzemenu:
        keuze1lijst = ["1"]
    col = kleuren[keuze1lijst[0]]
    print(col+keuzemenu[keuze1lijst[0]]+kleuren["ResetAll"])
    return rekening,header,col,keuze1lijst,ok

rekening = programmastart()
printdatum(nustr)
header = haalheader(rekening)
budgetcorrectie(rekening)
eenrekeningtotaal(rekening)
tooncategorieen(rekening,header)
startdatum = nustr[:6]+"01"
maandeind = calendar.monthrange(int(str(startdatum)[:4]),int(str(startdatum)[4:6]))[1]
einddatum = str(startdatum)[:6]+str(maandeind)
ok = {}
if header[nieuwheaderlijst[14]] == ">":
    col = ""
    tipvandedag(rekening,header,col)
loop = True
while loop == True:
    rekening,header,col,keuze1lijst,ok = keuze1menu(rekening)
    if keuze1lijst[0] == "0":
        rekening,header,col,keuze1lijst,ok = beheerkeuze(rekening,header,col,keuze1lijst,ok)
    if keuze1lijst[0] == "1":
        rekening,header,col,keuze1lijst,ok = toonkeuze(rekening,header,col,keuze1lijst,ok)
    if keuze1lijst[0] == "2":
        rekening,header,col,keuze1lijst,ok = nieuwkeuze(keuze1lijst,rekening,ok)
    if keuze1lijst[0] == "3":
        rekening,header,col,keuze1lijst,ok = wijzigkeuze(keuze1lijst,rekening,ok)
    if keuze1lijst[0] == "4":
        rekening,header,col,keuze1lijst,ok = verwijderkeuze(rekening,header,col,keuze1lijst,ok)
    if keuze1lijst[0] == "5":
        rekening,header,col,keuze1lijst,ok = spaarpotkeuze(keuze1lijst,rekening,ok)
