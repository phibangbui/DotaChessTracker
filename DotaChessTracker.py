from pip._vendor.distlib.compat import raw_input

#SPECIES
BEAST = "Beast (2, 4 6)"
DEMON = "Demon"
DRAGON = "Dragon (3)"
DWARF = "Dwarf"
ELEMENT = "Element (2)"
ELF = "Elf (3, 6)"
GOBLIN = "Goblin (3, 6)"
HUMAN = "Human (2, 4, 6)"
NAGA = "Naga (2, 4)"
OGRE = "Ogre"
ORC = "Orc (2, 4)"
TROLL = "Troll (2, 4)"
UNDEAD = "Undead (2, 4)"

#CLASS
ASSASSIN = "Assassin (3, 6)"
DEMON_HUNTER = "Demon Hunter"
DRUID = "Druid (2, 4)"
HUNTER = "Hunter (3, 6)"
KNIGHT = "Knight (2, 4, 6)"
MAGE = "Mage (3, 6)"
MECH = "Mech (2, 4)"
SHAMAN = "Shaman (2)"
WARLOCK = "Warlock (3, 6)"
WARRIOR = "Warrior (3, 6, 9)"

species_list = [BEAST, DEMON, DRAGON, DWARF, ELEMENT, ELF, DRAGON, GOBLIN, HUMAN, BEAST, DRAGON, NAGA, OGRE, ORC, TROLL, UNDEAD]
class_list = [ASSASSIN, DEMON_HUNTER, DRUID, HUNTER, KNIGHT, MAGE, MECH, SHAMAN, WARLOCK, WARRIOR]

chessPieceList = []
my_pieces = []

class ChessPiece(object):
    def __init__(self, name, pieceSpecies, pieceClass):
        self.name = name
        self.pieceSpecies = pieceSpecies
        self.pieceClass = pieceClass

def initializeChessPieces():
    chessPieceList.append(ChessPiece("Enchantress", BEAST, DRUID))
    chessPieceList.append(ChessPiece("Tusk", BEAST, WARRIOR))
    chessPieceList.append(ChessPiece("Venomancer", BEAST, WARLOCK))
    chessPieceList.append(ChessPiece("Sand King", BEAST, ASSASSIN))
    chessPieceList.append(ChessPiece("Lone Druid", BEAST, DRUID))
    chessPieceList.append(ChessPiece("Pain Queen", DEMON, ASSASSIN))
    chessPieceList.append(ChessPiece("Chaos Knight", DEMON, KNIGHT))
    chessPieceList.append(ChessPiece("Terrorblade", DEMON, DEMON_HUNTER))
    chessPieceList.append(ChessPiece("Shadow Fiend", DEMON, WARLOCK))
    chessPieceList.append(ChessPiece("Doom", DEMON, WARRIOR))
    chessPieceList.append(ChessPiece("Viper", DRAGON, ASSASSIN))
    chessPieceList.append(ChessPiece("Sniper", DWARF, HUNTER))
    chessPieceList.append(ChessPiece("Gyrocopter", DWARF, MECH))
    chessPieceList.append(ChessPiece("Morphling", ELEMENT, ASSASSIN))
    chessPieceList.append(ChessPiece("Razor", ELEMENT, MAGE))
    chessPieceList.append(ChessPiece("Enigma", ELEMENT, WARLOCK))
    chessPieceList.append(ChessPiece("Tiny", ELEMENT, WARRIOR))
    chessPieceList.append(ChessPiece("Phantom Assassin", ELF, ASSASSIN))
    chessPieceList.append(ChessPiece("Templar Assassin", ELF, ASSASSIN))
    chessPieceList.append(ChessPiece("Anti Mage", ELF, DEMON_HUNTER))
    chessPieceList.append(ChessPiece("Treant Protector", ELF, DRUID))
    chessPieceList.append(ChessPiece("Furion", ELF, DRUID))
    chessPieceList.append(ChessPiece("Wind Ranger", ELF, HUNTER))
    chessPieceList.append(ChessPiece("Luna", ELF, KNIGHT))
    chessPieceList.append(ChessPiece("Puck", ELF, MAGE))
    chessPieceList.append(ChessPiece("Puck", DRAGON, MAGE))
    chessPieceList.append(ChessPiece("Bounty Hunter", GOBLIN, ASSASSIN))
    chessPieceList.append(ChessPiece("Clockwerk", GOBLIN, MECH))
    chessPieceList.append(ChessPiece("Tinker", GOBLIN, MECH))
    chessPieceList.append(ChessPiece("Timbersaw", GOBLIN, MECH))
    chessPieceList.append(ChessPiece("Techies", GOBLIN, MECH))
    chessPieceList.append(ChessPiece("Alchemist", GOBLIN, WARLOCK))
    chessPieceList.append(ChessPiece("Omni Knight", HUMAN, KNIGHT))
    chessPieceList.append(ChessPiece("Crystal Maiden", HUMAN, MAGE))
    chessPieceList.append(ChessPiece("Lina", HUMAN, MAGE))
    chessPieceList.append(ChessPiece("Light Keeper", HUMAN, MAGE))
    chessPieceList.append(ChessPiece("Kunkka", HUMAN, WARRIOR))
    chessPieceList.append(ChessPiece("Lycan", HUMAN, WARRIOR))
    chessPieceList.append(ChessPiece("Lycan", BEAST, WARRIOR))
    chessPieceList.append(ChessPiece("Dragon Knight", HUMAN, KNIGHT))
    chessPieceList.append(ChessPiece("Dragon Knight", DRAGON, KNIGHT))
    chessPieceList.append(ChessPiece("Slark", NAGA, ASSASSIN))
    chessPieceList.append(ChessPiece("Medusa", NAGA, HUNTER))
    chessPieceList.append(ChessPiece("Tide Hunter", NAGA, HUNTER))
    chessPieceList.append(ChessPiece("Slardar", NAGA, WARRIOR))
    chessPieceList.append(ChessPiece("Ogre Magi", OGRE, MAGE))
    chessPieceList.append(ChessPiece("Beast Master", ORC, HUNTER))
    chessPieceList.append(ChessPiece("Disruptor", ORC, SHAMAN))
    chessPieceList.append(ChessPiece("Axe", ORC, WARRIOR))
    chessPieceList.append(ChessPiece("Juggernaut", ORC, WARRIOR))
    chessPieceList.append(ChessPiece("Bat Rider", TROLL, KNIGHT))
    chessPieceList.append(ChessPiece("Shadow Shaman", TROLL, SHAMAN))
    chessPieceList.append(ChessPiece("Witch Doctor", TROLL, WARLOCK))
    chessPieceList.append(ChessPiece("Troll", TROLL, WARRIOR))
    chessPieceList.append(ChessPiece("Drow Ranger", UNDEAD, HUNTER))
    chessPieceList.append(ChessPiece("Abaddon", UNDEAD, KNIGHT))
    chessPieceList.append(ChessPiece("Lich", UNDEAD, MAGE))
    chessPieceList.append(ChessPiece("Necrophos", UNDEAD, WARLOCK))

def isSpecies(chessPiece, findSpecies):
    if (chessPiece.pieceSpecies == findSpecies):
        return True
    else:
        return False

def isClass(chessPiece, findClass):
    if (chessPiece.pieceClass == findClass):
        return True
    else:
        return False

def start_point():

    print ("\n ====== START SCREEN ====== \n")

    start_point_selection = raw_input("[1] : Add a Unit \n" +
                           "[2] : Remove a Unit \n" +
                           "[3] : Check Units \n")
    start_point_choice = {'1' : addPiece, '2' : removePiece, '3' : checkPieces}
    start_point_choice[start_point_selection]()

def addPiece():

    print ("\n ====== PIECE ADDITION SCREEN ====== \n")

    categorySelection = raw_input("[1] : Species \n" +
                            "[2] : Classes \n" +
                            "[3] : Go Back \n")
    categorySelectionChoice = {'1' : chooseSpecies, '2' : chooseClasses, '3' : start_point}
    categorySelectionChoice[categorySelection]()

def removePiece():

    print ("\n ====== PIECE REMOVAL SCREEN ====== \n")

    if not my_pieces:
        print("You don't have any pieces\n")
        start_point()

    selection_string = ""
    for index in range(len(my_pieces)):
            selection_string += ("[" + str(index) + "] : " + my_pieces[index].name + "\n")
    speciesSelection = raw_input(selection_string)
    
    removed_piece = my_pieces[int(speciesSelection)]
    my_pieces.remove(removed_piece)

    start_point()
    

def chooseSpecies():

    print ("\n ====== SPECIES SELECTION SCREEN ====== \n")

    selection_string = ""
    for index in range(len(species_list)):
            selection_string += ("[" + str(index) + "] : " + species_list[index] + "\n")
    speciesSelection = raw_input(selection_string)
    
    mySpecies = species_list[int(speciesSelection)]
    mySpeciesList = list(filter(lambda x: isSpecies(x, mySpecies), chessPieceList))
    
    chess_piece_selection_string = ""
    for speciesIndex in range(len(mySpeciesList)):
            chess_piece_selection_string += ("[" + str(speciesIndex) + "] : " + mySpeciesList[speciesIndex].name + '\n')

    print ("\n ====== PIECE SELECTION SCREEN ====== \n")

    chessPieceSelection = raw_input(chess_piece_selection_string)

    my_pieces.append(mySpeciesList[int(chessPieceSelection)])
    start_point()

def chooseClasses():

    print ("\n ====== CLASS SELECTION SCREEN ====== \n")

    selection_string = ""
    for index in range(len(class_list)):
            selection_string += ("[" + str(index) + "] : " + class_list[index] + "\n")
    classSelection = raw_input(selection_string)
    
    myClass = class_list[int(classSelection)]
    myClassList = list(filter(lambda x: isClass(x, myClass), chessPieceList))
    
    chess_piece_selection_string = ""
    for pieceIndex in range(len(myClassList)):
            chess_piece_selection_string += ("[" + str(pieceIndex) + "] : " + myClassList[pieceIndex].name + '\n')

    print ("\n ====== PIECE SELECTION SCREEN ====== \n")

    chessPieceSelection = raw_input(chess_piece_selection_string)

    my_pieces.append(myClassList[int(chessPieceSelection)])
    start_point()

def checkPieces():

    print ("\n ====== PIECE CHECK SCREEN ====== \n")

    dedupedList = []
    dedupedClassList = []
    dedupedSpeciesList = []
    for piece in my_pieces:
        if piece not in dedupedList:
            dedupedList.append(piece) 

    for dedupedPiece in dedupedList:
        if (not (dedupedPiece.pieceClass in dict(dedupedClassList))):
            pieceClassList = list(filter(lambda x: isClass(x, dedupedPiece.pieceClass), dedupedList))
            dedupedClassList.append((dedupedPiece.pieceClass, pieceClassList))

        if (not (dedupedPiece.pieceSpecies in dict(dedupedSpeciesList))):
            pieceSpeciesList = list(filter(lambda x: isSpecies(x, dedupedPiece.pieceSpecies), dedupedList))
            dedupedSpeciesList.append((dedupedPiece.pieceSpecies, pieceSpeciesList))

    print ("======= CLASSES HERE =======")
    for classList in dedupedClassList:
        print (classList[0] + " : " + str(len(classList[1])))

    print ("======= SPECIES HERE =======")
    for speciesList in dedupedSpeciesList:
        print (speciesList[0] + " : " + str(len(speciesList[1])))

    print ("======= ALL PIECES HERE =======")
    for my_piece in my_pieces:
        print ("Name: " + my_piece.name)
    start_point()


initializeChessPieces()
start_point()
