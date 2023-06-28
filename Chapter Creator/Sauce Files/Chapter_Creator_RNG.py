import random
import os
import PySimpleGUI as Sg

Homeworld_Modifier = None
Founding = None
Progenitor_Chapter = None
Missing_Zygote_Base = None
Missing_Zygote_1 = None
Missing_Zygote_2 = None
Missing_Zygote_3 = None
Missing_Zygote_4 = None
Missing_Zygote_5 = None
Missing_Zygote_6 = None
Missing_Zygote_7 = None
Missing_Zygote_8 = None
Existing_Mutations_Base = None
Existing_Mutations_1 = None
Existing_Mutations_2 = None
Existing_Mutations_3 = None
Existing_Mutations_4 = None
Existing_Mutations_5 = None
Existing_Mutations_6 = None
Existing_Mutations_7 = None
Existing_Mutations_8 = None
Existing_Non_Codex_Element = None
Existing_Codex_Element = None
Unit_Restrictions = None
Chapter_Quirk_Base = None
Chapter_Quirk_1 = None
Chapter_Quirk_2 = None
Chapter_Quirk_3 = None
Primaris_Reinforcements = None
Homeworld = None
Existing_Non_Progenitor_Element = None
Legendary_Figure = None
Combat_Doctrine = None
chapter_name = None


def function_chapter_creation_table():
    # The following code is apparently necessary for these variables to be called properly later

    global Homeworld_Modifier
    global Founding
    global Progenitor_Chapter
    global Missing_Zygote_Base
    global Missing_Zygote_1
    global Missing_Zygote_2
    global Missing_Zygote_3
    global Missing_Zygote_4
    global Missing_Zygote_5
    global Missing_Zygote_6
    global Missing_Zygote_7
    global Missing_Zygote_8
    global Existing_Mutations_Base
    global Existing_Mutations_1
    global Existing_Mutations_2
    global Existing_Mutations_3
    global Existing_Mutations_4
    global Existing_Mutations_5
    global Existing_Mutations_6
    global Existing_Mutations_7
    global Existing_Mutations_8
    global Existing_Non_Codex_Element
    global Existing_Codex_Element
    global Unit_Restrictions
    global Chapter_Quirk_Base
    global Chapter_Quirk_1
    global Chapter_Quirk_2
    global Chapter_Quirk_3
    global Primaris_Reinforcements
    global Homeworld
    global Existing_Non_Progenitor_Element
    global Legendary_Figure
    global Combat_Doctrine

    # The following code defines the manner in which the Chapter's Homeworld is ruled

    def function_homeworld_rule():
        f.writelines("\n")
        f.writelines("\n    Rule of Homeworld")
        num_homeworld_rule = random.randint(1, 10)
        print("Homeworld Rule Roll:")
        print(num_homeworld_rule)
        if num_homeworld_rule <= 1:
            f.writelines("\nDirect: this Chapter rules the world themselves, and are personally involved in local"
                         " affairs.")
        elif num_homeworld_rule <= 4:
            f.writelines("\nStewardship: this Chapter rules the world via some manner of proxy, such as a local human "
                         "governor or equivalent.")
        elif num_homeworld_rule <= 10:
            f.writelines("\nDistant: this Chapter rules the world in name only, and are marginally involved in local"
                         " affairs at most.")

    # The following code defines to what degree the Chapter is royally fucked

    def function_doomed():
        global Existing_Mutations_Base
        global Existing_Mutations_1
        global Existing_Mutations_2
        global Existing_Mutations_3
        global Existing_Mutations_4
        global Existing_Mutations_5
        global Existing_Mutations_6
        global Existing_Mutations_7
        global Existing_Mutations_8
        num_doomed = random.randint(1, 3)
        print("DOOMED Roll:")
        print(num_doomed)
        if num_doomed <= 1 and "DOOMED" not in (Existing_Mutations_Base, Existing_Mutations_1, Existing_Mutations_2,
                                                Existing_Mutations_3, Existing_Mutations_4, Existing_Mutations_5,
                                                Existing_Mutations_6, Existing_Mutations_7, Existing_Mutations_8):
            f.writelines("\nDOOMED: this Chapter can only produce a single Progenoid Gland: the one in the neck."
                         " It takes 5 years to mature; if an Astartes dies prior to then, the gene-seed is lost.")
            Existing_Mutations_Base = "DOOMED"
        elif num_doomed <= 2 and "DOOMED" not in (Existing_Mutations_Base, Existing_Mutations_1, Existing_Mutations_2,
                                                  Existing_Mutations_3, Existing_Mutations_4, Existing_Mutations_5,
                                                  Existing_Mutations_6, Existing_Mutations_7, Existing_Mutations_8):
            f.writelines("\nDOOMED: this Chapter can only produce a single Progenoid Gland: the one in the chest."
                         " It takes 10 years to mature; if an Astartes dies prior to then, the gene-seed is lost.")
            Existing_Mutations_Base = "DOOMED"
        elif num_doomed <= 3 and "DOOMED" not in (Existing_Mutations_Base, Existing_Mutations_1, Existing_Mutations_2,
                                                  Existing_Mutations_3, Existing_Mutations_4, Existing_Mutations_5,
                                                  Existing_Mutations_6, Existing_Mutations_7, Existing_Mutations_8):
            f.writelines("\nDOOMED: this Chapter has lost the ability to create new Progenoid Glands. Unless this is"
                         " somehow fixed, they are doomed to suffer a slow death by attrition.")
            Existing_Mutations_Base = "DOOMED"

    # The following code defines the Chapter's special equipment if Organisation is Divergent or Unique

    def function_non_codex_element():
        global Existing_Non_Codex_Element
        global Unit_Restrictions
        num_non_codex_element = random.randint(1, 251)
        print("Non-Codex Element Roll:")
        print(num_non_codex_element)
        if num_non_codex_element <= 10 and Existing_Non_Codex_Element != "Favored Weapon":
            f.writelines("\nFavored Weapon: contrary to Codex standards, this Chapter has a strong preference for a"
                         " particular type of weapon, whether due to culture, circumstance or some other factor. They"
                         " will use this whenever feasible. Perhaps, if they're dedicated enough, even when"
                         " conventionally thought unfeasible or impractical.")
            Existing_Non_Codex_Element = "Favored Weapon"
        elif num_non_codex_element <= 20 and Existing_Non_Codex_Element != "Unique Markings":
            f.writelines("\nUnique Markings: contrary to Codex standards, this Chapter uses its own particular means"
                         " of marking various units and identifying certain ranks.")
            Existing_Non_Codex_Element = "Unique Markings"
        elif num_non_codex_element <= 30 and Existing_Non_Codex_Element != "Modified Packs":
            f.writelines("\nModified Jump Packs: contrary to Codex standards, this Chapter has made extensive"
                         " modifications to their jump packs, either in form, function, or both.")
            Existing_Non_Codex_Element = "Modified Packs"
        elif num_non_codex_element <= 40 and Existing_Non_Codex_Element != "Beast Companions":
            f.writelines("\nBestial Companion: contrary to Codex standards, this Chapter maintains a population of"
                         " animals that are important to either their culture, battlefield tactics and strategies, or"
                         " both.")
            Existing_Non_Codex_Element = "Beast Companions"
        elif num_non_codex_element <= 50 and Existing_Non_Codex_Element != "Rare Weapons":
            f.writelines("\nRare Weaponry: contrary to Codex standards, this Chapter, for one reason or another, has"
                         " access to, and fields, an abnormally large number of weapons otherwise considered rare,"
                         " exotic, or both.")
            Existing_Non_Codex_Element = "Rare Weapons"
        elif num_non_codex_element <= 60 and Existing_Non_Codex_Element != "Blessed Gear":
            f.writelines("\nBlessed Wargear: contrary to Codex standards, this Chapter requires its arms and armor to"
                         " be individually consecrated by a Chaplain (or equivalent) before going to war.")
            Existing_Non_Codex_Element = "Blessed Gear"
        elif num_non_codex_element <= 70 and Existing_Non_Codex_Element != "Special Mounts":
            f.writelines("\nSpecial Mounts: contrary to Codex standards, this Chapter makes use of either modified"
                         " bikes, genetically engineered animals, or something else entirely to carry them into"
                         " battle.")
            Existing_Non_Codex_Element = "Special Mounts"
        elif num_non_codex_element <= 80 and Existing_Non_Codex_Element != "Modified Vehicles":
            f.writelines("\nModified Vehicles: contrary to Codex standards, this Chapter has made extensive"
                         " modifications to their vehicles, either in form, function, or both.")
            Existing_Non_Codex_Element = "Modified Vehicles"
        elif num_non_codex_element <= 90 and Existing_Non_Codex_Element != "Special Style":
            f.writelines("\nPreferred Fighting Style: contrary to Codex standards, this Chapter has adopted methods of"
                         " waging war, whether individually or as a unit, that are considered unusual or unorthodox by"
                         " Astartes standards.")
            Existing_Non_Codex_Element = "Special Style"
        elif num_non_codex_element <= 100 and Existing_Non_Codex_Element != "Modified Weapons":
            f.writelines("\nModified Weaponry: contrary to Codex standards, this Chapter has made extensive"
                         " modifications to their weaponry, either in form, function, or both.")
            Existing_Non_Codex_Element = "Modified Weapons"
        elif num_non_codex_element <= 110 and Existing_Non_Codex_Element != "Modified Armor":
            f.writelines("\nModified Armor: contrary to Codex standards, this Chapter has made extensive modifications"
                         " to their armor, either in form, function, or both.")
            Existing_Non_Codex_Element = "Modified Armor"
        elif num_non_codex_element <= 120 and Existing_Non_Codex_Element != "Unique Rank Combo":
            f.writelines("\nUnique Rank Combinations: contrary to Codex standards, this Chapter has folded two (or,"
                         " very rarely, more) ranks into one, such as combining the roles of Apothecary and Librarian,"
                         " or Chaplain and Techmarine.")
            Existing_Non_Codex_Element = "Unique Rank Combo"
        elif num_non_codex_element <= 130 and Existing_Non_Codex_Element != "AlteredTerminatorRules" and \
                Unit_Restrictions != "Terminator":
            f.writelines("\nAltered Terminator Rules: contrary to Codex standards, this Chapter does not reserve its"
                         " terminator armor for 1st Company Veterans, instead issuing it by some other criteria. For"
                         " example, it might instead be reserved solely for Apothecaries.")
            Existing_Non_Codex_Element = "AlteredTerminatorRules"
        elif num_non_codex_element <= 140 and Existing_Non_Codex_Element != "AlteredScoutOrg":
            f.writelines("\nUnorthodox Neophytes: contrary to Codex standards, this Chapter does not field its"
                         " Neophytes as Scouts. New recruits might instead fill some other role, and might not even be"
                         " organised into their own separate Company.")
            Existing_Non_Codex_Element = "AlteredScoutOrg"
        elif num_non_codex_element <= 150 and Existing_Non_Codex_Element != "UnorthodoxMasterSelection" and \
                Unit_Restrictions != "Master":
            f.writelines("\nUnorthodox Chapter Master Selection: contrary to Codex standards, this Chapter does not"
                         " select its Chapter Master from amongst its Captains, instead preferring some other selection"
                         " criteria. For example, Chapter Masters may be drawn from the Chapter's Champions.")
            Existing_Non_Codex_Element = "UnorthodoxMasterSelection"
        elif num_non_codex_element <= 160 and Existing_Non_Codex_Element != "UnorthodoxCaptainSelection" and \
                Unit_Restrictions != "Captain":
            f.writelines("\nUnorthodox Captain Selection: contrary to Codex standards, this Chapter does not select its"
                         " Captains from amongst its 1st Company Veterans, instead preferring some other selection"
                         " criteria. For example, Captains may be drawn from the Chapter's Sergeants.")
            Existing_Non_Codex_Element = "UnorthodoxCaptainSelection"
        elif num_non_codex_element <= 170 and Existing_Non_Codex_Element != "UnorthodoxSergeantSelection" and \
                Unit_Restrictions != "Sergeant":
            f.writelines("\nUnorthodox Sergeant Selection: contrary to Codex standards, this Chapter does not select"
                         " its Sergeants from amongst its Veterans, instead preferring some other selection criteria."
                         " For example, Sergeants may be selected based on their mortal family's social standing, such"
                         " as being nobility or part of a martial caste.")
            Existing_Non_Codex_Element = "UnorthodoxSergeantSelection"
        elif num_non_codex_element <= 180 and Existing_Non_Codex_Element != "UnorthodoxChaplainSelection" and \
                Unit_Restrictions != "Chaplain":
            f.writelines("\nUnorthodox Chaplain Selection: contrary to Codex standards, this Chapter has its own "
                         "selection criteria for its spiritual caretakers. For example, they may be selected based on "
                         "religious aspects of their homeworld's culture.")
            Existing_Non_Codex_Element = "UnorthodoxChaplainSelection"
        elif num_non_codex_element <= 190 and Existing_Non_Codex_Element != "UnorthodoxApothecarySelection" and \
                Unit_Restrictions != "Apothecary":
            f.writelines("\nUnorthodox Apothecary Selection: contrary to Codex standards, this Chapter has its own "
                         "selection criteria for its medics. For example, they may be drawn entirely from the Chapter's"
                         " Sergeants.")
            Existing_Non_Codex_Element = "UnorthodoxApothecarySelection"
        elif num_non_codex_element <= 200 and Existing_Non_Codex_Element != "UnorthodoxTechmarineSelection" and \
                Unit_Restrictions != "Techmarine":
            f.writelines("\nUnorthodox Techmarine Selection: contrary to Codex standards, this Chapter has its own"
                         " selection criteria for its machine specialists. For example, they may be selected based on"
                         " some technological superstition, such as a cogitator's random number generator selecting"
                         " which Astartes to train as Techmarines.")
            Existing_Non_Codex_Element = "UnorthodoxTechmarineSelection"
        elif num_non_codex_element <= 210 and Existing_Non_Codex_Element != "UnorthodoxDevastatorSelection" and \
                Unit_Restrictions != "Devastator":
            f.writelines("\nUnorthodox Devastator Selection: contrary to Codex standards, this Chapter does not select"
                         " its Devastators from its recruits, instead preferring some other selection criteria. For"
                         " example, Devastators may instead be selected based on existing marksmanship skills, rather"
                         " than to build them.")
            Existing_Non_Codex_Element = "UnorthodoxDevastatorSelection"
        elif num_non_codex_element <= 220 and Existing_Non_Codex_Element != "UnorthodoxAssaultSelection" and \
                Unit_Restrictions != "Assault":
            f.writelines("\nUnorthodox Assault Marine Selection: contrary to Codex standards, this Chapter does not"
                         " select its Assault Marines from its Devastators, instead preferring some other selection"
                         " criteria. For example, Assault Marines may instead be selected based on temperament.")
            Existing_Non_Codex_Element = "UnorthodoxAssaultSelection"
        elif num_non_codex_element <= 230 and Existing_Non_Codex_Element != "UnorthodoxDreadnoughtSelection" and \
                Unit_Restrictions != "Dreadnought":
            f.writelines("\nUnorthodox Dreadnought Selection: contrary to Codex standards, this Chapter does not inter"
                         " its most gravely wounded in Dreadnoughts, instead preferring some other criteria. For"
                         " example, Dreadnoughts may instead be entirely comprised of volunteers. The Chapter will"
                         " still need some other way to deal with its most gravely wounded Astartes.")
            Existing_Non_Codex_Element = "UnorthodoxDreadnoughtSelection"
        elif num_non_codex_element <= 240 and Existing_Non_Codex_Element != "Unique Battle Language":
            f.writelines("\nUnique Battle Language: contrary to Codex standards, this Chapter maintains its own"
                         " Battle-Sign language, distinct enough from standard Astartes Battle-Sign that they are not"
                         " mutually understood.")
            Existing_Non_Codex_Element = "Unique Battle Language"
        elif num_non_codex_element <= 250 and Existing_Non_Codex_Element != "Unique Company Structure":
            f.writelines("\nUnique Company Structure: contrary to Codex standards, this Chapter does not have a Veteran"
                         " Company, 4 Battle Companies, 4 Reserve Companies and a Scout Company, instead preferring"
                         " some other organisation of Astartes into Companies or equivalent groupings. For example,"
                         " they might evenly spread their marines across a number of identical Companies, or use an"
                         " entirely different internal structure instead.")
        elif num_non_codex_element <= 251 and Existing_Non_Codex_Element != "Truly Unusual":
            f.writelines("\nChoose something truly unusual.")
            Existing_Non_Codex_Element = "Truly Unusual"

    # The following code defines the Chapter's Codex elements

    def function_codex_element():
        global Existing_Codex_Element
        num_codex_element = random.randint(1, 10)
        print("Codex Element Roll:")
        print(num_codex_element)
        if num_codex_element <= 1 and Existing_Codex_Element != "Narrow":
            f.writelines("\nNarrow Interpretation: this Chapter has a very narrow perception of the Codex, more-so than"
                         " originally intended when it was penned.")
            Existing_Codex_Element = "Narrow"
        elif num_codex_element <= 2 and Existing_Codex_Element != "Strict":
            f.writelines("\nStrict Interpretation: this Chapter is very strict in its enforcement of the Codex, with"
                         " severe punishments for deviating from its teachings.")
            Existing_Codex_Element = "Strict"
        elif num_codex_element <= 3 and Existing_Codex_Element != "Creative":
            f.writelines("\nCreative Interpretation: this Chapter is not alone in viewing the Codex as open to"
                         " interpretation, but it tends to have some rather peculiar ones as compared to its peers.")
            Existing_Codex_Element = "Creative"
        elif num_codex_element <= 4 and Existing_Codex_Element != "Flexible":
            f.writelines("\nFlexible Interpretation: this Chapter considers the Codex to be an invaluable set of"
                         " guidelines, but also acknowledges that it may not have all the answers to every conceivable"
                         " scenario.")
            Existing_Codex_Element = "Flexible"
        elif num_codex_element <= 5 and Existing_Codex_Element != "Plain":
            f.writelines("\nPlain Interpretation: this Chapter has no unusual interpretations of the Codex whatsoever."
                         " For all intents and purpose, it's an ordinary baseline Codex-compliant Chapter.")
            Existing_Codex_Element = "Plain"
        elif num_codex_element <= 6 and Existing_Codex_Element != "True":
            f.writelines("\nTrue Interpretation: this Chapter considers itself to be the only one to truly embrace the"
                         " Codex.")
            Existing_Codex_Element = "True"
        elif num_codex_element <= 7 and Existing_Codex_Element != "Loophole":
            f.writelines("\nLoophole Interpretation: this Chapter is famous, or infamous, for exploiting loopholes in"
                         " the Codex to suit their own needs. Examples include crusading Chapters being exempt from the"
                         " usual limit of 1000 fighting men, and there being no limits on vehicle numbers.")
            Existing_Codex_Element = "Loophole"
        elif num_codex_element <= 8 and Existing_Codex_Element != "Proselytic":
            f.writelines("\nProselytic Interpretation: this Chapter actively seeks to convince non-compliant Chapters"
                         " of the Codex's superiority.")
            Existing_Codex_Element = "Proselytic"
        elif num_codex_element <= 9 and Existing_Codex_Element != "Particular":
            f.writelines("\nParticular Interpretation: this Chapter tends to hold certain parts of the Codex in higher"
                         " regard than others. Its Astartes may all be of the same mind in this, or they might have"
                         " internal disagreements on the matter.")
            Existing_Codex_Element = "Particular"
        elif num_codex_element <= 10 and Existing_Codex_Element != "Lip":
            f.writelines("\nLip-Service: this Chapter is outwardly Codex-compliant, but secretly has little love for"
                         " it.")
            Existing_Codex_Element = "Lip"

    # The following code defines the Chapter's non-Progenitor elements

    def function_non_progenitor_element():
        global Existing_Non_Progenitor_Element
        global Progenitor_Chapter
        if Progenitor_Chapter == "Dark Angels":
            num_non_progenitor_element = random.randint(1, 11)
            print("Non-Progenitor Element Roll:")
            print(num_non_progenitor_element)
            if num_non_progenitor_element <= 2 and Existing_Non_Progenitor_Element != "Forgiven":
                f.writelines("\nForgiven: for one reason or another, this Chapter has lost much interest in hunting the"
                             " Fallen Angels. They most likely haven't abandoned it entirely, but may be one of the"
                             " very few who have.")
                Existing_Non_Progenitor_Element = "Forgiven"
            elif num_non_progenitor_element <= 4 and Existing_Non_Progenitor_Element != "No Deathwing":
                f.writelines("\nNo Deathwing: for one reason or another, this Chapter no longer fields Deathwing"
                             " Astartes. They may instead have reverted to Codex-compliant Terminators, have no"
                             " terminator armor at all, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Deathwing"
            elif num_non_progenitor_element <= 6 and Existing_Non_Progenitor_Element != "No Ravenwing":
                f.writelines("\nNo Ravenwing: for one reason or another, this Chapter no longer fields Ravenwing"
                             " Astartes. They may instead have reverted to Codex-compliant Bike Squads, have no bikes"
                             " at all, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Ravenwing"
            elif num_non_progenitor_element <= 8 and Existing_Non_Progenitor_Element != "Different Company":
                f.writelines("\nDifferent Company Structure: for one reason or another, this Chapter eschews the"
                             " Company structure laid out by its progenitor. They may instead have reverted to the"
                             " Codex-compliant structure, or something else entirely.")
                Existing_Non_Progenitor_Element = "Different Company"
            elif num_non_progenitor_element <= 10 and Existing_Non_Progenitor_Element != "Compliant":
                f.writelines("\nCodex-Compliant: for one reason or another, this Chapter has decided to eschew the ways"
                             " of its progenitor, instead embracing the Codex Astartes, although not necessarily in its"
                             " entirety.")
                Existing_Non_Progenitor_Element = "Compliant"
            elif num_non_progenitor_element <= 11 and Existing_Non_Progenitor_Element != "Unusual":
                f.writelines("\nChoose something truly unusual.")
                Existing_Non_Progenitor_Element = "Unusual"
        if Progenitor_Chapter == "Blood Angels":
            num_non_progenitor_element = random.randint(1, 11)
            print("Non-Progenitor Element Roll:")
            print(num_non_progenitor_element)
            if num_non_progenitor_element <= 2 and Existing_Non_Progenitor_Element != "No Sanguinary":
                f.writelines("\nNo Sanguinary Guard: for one reason or another, this Chapter no longer fields"
                             " Sanguinary Guards. They may instead have reverted to Codex-compliant Honor Guards, have"
                             " lost the means to produce their unique equipment, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Sanguinary"
            elif num_non_progenitor_element <= 4 and Existing_Non_Progenitor_Element != "No Angel Equipment":
                f.writelines("\nNo Blood Angel-Specific Equipment: for one reason or another, this Chapter no longer"
                             " fields units normally restricted to the Blood Angels and their successors, such as the"
                             " Baal-Pattern Predator. They have instead have reverted to using Codex-compliant"
                             " equipment, have lost the means to produce it, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Angel Equipment"
            elif num_non_progenitor_element <= 6 and Existing_Non_Progenitor_Element != "Thirst Solution":
                f.writelines("\nUnusual Red Thirst 'Solution': this Chapter has found some unique means by which they"
                             " believe they can reduce the frequency and/or effects of the Red Thirst. Whether or not"
                             " it actually works, they nonetheless use it, and may view it as their sole hope for"
                             " salvation from The Flaw. Or, alternately, they might just euthanize any Astartes who"
                             " falls under its influence.")
                Existing_Non_Progenitor_Element = "Thirst Solution"
            elif num_non_progenitor_element <= 8 and Existing_Non_Progenitor_Element != "Rage Solution":
                f.writelines("\nUnusual Black Rage 'Solution': this Chapter has found some unique means by which they"
                             " believe they can reduce the frequency and/or effects of the Black Rage. Whether or not"
                             " it actually works, they nonetheless use it, and may view it as their sole hope for"
                             " salvation from The Flaw. Or, alternately, they might just euthanize any Astartes who"
                             " falls under its influence.")
                Existing_Non_Progenitor_Element = "Rage Solution"
            elif num_non_progenitor_element <= 10 and Existing_Non_Progenitor_Element != "Compliant":
                f.writelines("\nCodex-Compliant: for one reason or another, this Chapter has decided to eschew the ways"
                             " of its progenitor, instead embracing the Codex Astartes, although not necessarily in its"
                             " entirety.")
                Existing_Non_Progenitor_Element = "Compliant"
            elif num_non_progenitor_element <= 11 and Existing_Non_Progenitor_Element != "Unusual":
                f.writelines("\nChoose something truly unusual.")
                Existing_Non_Progenitor_Element = "Unusual"
        if Progenitor_Chapter == "Iron Hands":
            num_non_progenitor_element = random.randint(1, 11)
            print("Non-Progenitor Element Roll:")
            print(num_non_progenitor_element)
            if num_non_progenitor_element <= 2 and Existing_Non_Progenitor_Element != "Non-Clan":
                f.writelines("\nNon-Clan System: for one reason or another, this Chapter eschews the Clan system of its"
                             " progenitor. They may instead have reverted to a Codex-compliant system, or something"
                             " else entirely.")
                Existing_Non_Progenitor_Element = "Non-Clan"
            elif num_non_progenitor_element <= 4 and Existing_Non_Progenitor_Element != "No Cybernetics":
                f.writelines("\nNo Cybernetics: for one reason or another, this Chapter no longer shares its"
                             " progenitor's obsession with cybernetic enhancements. Their obsession may have changed,"
                             " or is simply gone.")
                Existing_Non_Progenitor_Element = "No Cybernetics"
            elif num_non_progenitor_element <= 6 and Existing_Non_Progenitor_Element != "Chapter Master":
                f.writelines("\nChapter Master: for one reason or another, this Chapter has decided to reinstate the"
                             " office of Chapter Master, although not necessarily under that name.")
                Existing_Non_Progenitor_Element = "Chapter Master"
            elif num_non_progenitor_element <= 8 and Existing_Non_Progenitor_Element != "Non-Sergeant Terminators":
                f.writelines("\nNon-Sergeant Terminators: for one reason or another, this Chapter no longer reserves"
                             " its terminator armor for Sergeants.")
                Existing_Non_Progenitor_Element = "Non-Sergeant Terminators"
            elif num_non_progenitor_element <= 10 and Existing_Non_Progenitor_Element != "Compliant":
                f.writelines("\nCodex-Compliant: for one reason or another, this Chapter has decided to eschew the ways"
                             " of its progenitor, instead embracing the Codex Astartes, although not necessarily in its"
                             " entirety.")
                Existing_Non_Progenitor_Element = "No Compliant"
            elif num_non_progenitor_element <= 11 and Existing_Non_Progenitor_Element != "Unusual":
                f.writelines("\nChoose something truly unusual.")
                Existing_Non_Progenitor_Element = "No Unusual"
        if Progenitor_Chapter == "Space Wolves":
            num_non_progenitor_element = random.randint(1, 11)
            print("Non-Progenitor Element Roll:")
            print(num_non_progenitor_element)
            if num_non_progenitor_element <= 2 and Existing_Non_Progenitor_Element != "No Claws":
                f.writelines("\nNo Blood Claws: for one reason or another, this Chapter no longer uses Blood Claws, at"
                             " least not to break in Neophytes. They may instead have reverted to a Codex-compliant"
                             " Neophyte role, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Claws"
            elif num_non_progenitor_element <= 4 and Existing_Non_Progenitor_Element != "No Wolf":
                f.writelines("\nNo Wolf Priests: for one reason or another, this Chapter no longer uses Wolf Priests."
                             " They may have returned to using Apothecaries and Chaplains in separate roles, ceased"
                             " using one of the two altogether, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Wolf"
            elif num_non_progenitor_element <= 6 and Existing_Non_Progenitor_Element != "No Rune":
                f.writelines("\nNo Rune Priests: for one reason or another, this Chapter no longer uses Rune Priests."
                             " They may have done away with their progenitor's disdain for psykers, hate psykers even"
                             " more and recognised that Rune Priests are actually psykers, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Rune"
            elif num_non_progenitor_element <= 8 and Existing_Non_Progenitor_Element != "Non-Pack":
                f.writelines("\nNon-Pack Organisation: for one reason or another, this Chapter eschews the Pack system"
                             " of its progenitor. They may instead have reverted to a Codex-compliant system, or"
                             " something else entirely.")
                Existing_Non_Progenitor_Element = "Non-Pack"
            elif num_non_progenitor_element <= 10 and Existing_Non_Progenitor_Element != "Compliant":
                f.writelines("\nCodex-Compliant: for one reason or another, this Chapter has decided to eschew the ways"
                             " of its progenitor, instead embracing the Codex Astartes, although not necessarily in its"
                             " entirety.")
                Existing_Non_Progenitor_Element = "Compliant"
            elif num_non_progenitor_element <= 11 and Existing_Non_Progenitor_Element != "Unusual":
                f.writelines("\nChoose something truly unusual.")
                Existing_Non_Progenitor_Element = "Unusual"
        if Progenitor_Chapter == "Salamanders":
            num_non_progenitor_element = random.randint(1, 11)
            print("Non-Progenitor Element Roll:")
            print(num_non_progenitor_element)
            if num_non_progenitor_element <= 2 and Existing_Non_Progenitor_Element != "Non-Great Company":
                f.writelines("\nNon-Great Company Organisation: for one reason or another, this Chapter has decided to"
                             " do away with the Great Companies of its progenitor. They may instead have reverted to a"
                             " Codex-compliant system, or something else entirely.")
                Existing_Non_Progenitor_Element = "Non-Great Company"
            elif num_non_progenitor_element <= 4 and Existing_Non_Progenitor_Element != "Different 1st":
                f.writelines("\nDifferent 1st Company Leadership: for one reason or another, this Chapter's 1st Company"
                             " is not lead by the Chapter Master, as is the case with the Salamanders. They may instead"
                             " have reverted to using a 1st Company Captain as dictated by the Codex Astartes, or"
                             " something else entirely.")
                Existing_Non_Progenitor_Element = "Different 1st"
            elif num_non_progenitor_element <= 6 and Existing_Non_Progenitor_Element != "No Fire":
                f.writelines("\nNo Fire Preference: for one reason or another, this Chapter does not share its"
                             " progenitor's preference for fire- and heat-based weaponry. They may even distance"
                             " themselves from such weapons, have some other peculiar preference, or something else"
                             " entirely.")
                Existing_Non_Progenitor_Element = "No Fire"
            elif num_non_progenitor_element <= 8 and Existing_Non_Progenitor_Element != "No Promethean":
                f.writelines("\nNo Promethean Cult: for one reason or another, this Chapter has rejected the Promethean"
                             " Cult of its progenitor. They may have adopted some other variant of the Imperial Cult,"
                             " returned to more mundane beliefs, or something else entirely.")
                Existing_Non_Progenitor_Element = "No Promethean"
            elif num_non_progenitor_element <= 10 and Existing_Non_Progenitor_Element != "Compliant":
                f.writelines("\nCodex-Compliant: for one reason or another, this Chapter has decided to eschew the ways"
                             " of its progenitor, instead embracing the Codex Astartes, although not necessarily in its"
                             " entirety.")
                Existing_Non_Progenitor_Element = "Compliant"
            elif num_non_progenitor_element <= 11 and Existing_Non_Progenitor_Element != "Unusual":
                f.writelines("\nChoose something truly unusual.")
                Existing_Non_Progenitor_Element = "Unusual"

    # The following code defines the Chapter's unit restrictions

    def function_unit_restrictions():
        global Unit_Restrictions
        f.writelines("\n")
        f.writelines("\n    Unit Restrictions")
        num_unit_restrictions = random.randint(1, 100)
        print("Unit Restrictions Roll:")
        print(num_unit_restrictions)
        if num_unit_restrictions <= 15:
            f.writelines("\nThis Chapter has no Apothecaries; someone else takes on the crucial responsibility of"
                         " collecting progenoids from their fallen brothers.")
            Unit_Restrictions = "Apothecary"
        elif num_unit_restrictions <= 30:
            f.writelines("\nThis Chapter has no Assault Squads; jump packs can still be issued, if the Chapter has"
                         " access to them at all.")
            Unit_Restrictions = "Assault"
        elif num_unit_restrictions <= 45:
            f.writelines("\nThis Chapter has no Devastator Squads; heavy weapons can still be issued, if the Chapter"
                         " has access to them at all.")
            Unit_Restrictions = "Devastator"
        elif num_unit_restrictions <= 60:
            f.writelines("\nThis Chapter has no Techmarines; someone else takes on the vital task of repairing and"
                         " maintaining the Chapter's weapons and machines.")
            Unit_Restrictions = "Techmarine"
        elif num_unit_restrictions <= 75:
            f.writelines("\nThis Chapter has no Librarians; someone else accepts the mission of keeping the Chapter's"
                         " lore, recording its history and maintaining its library.")
            Unit_Restrictions = "Librarian"
        elif num_unit_restrictions <= 90:
            f.writelines("\nThis Chapter has no Chaplains; someone else shoulders the burden of looking after the"
                         " Chapter's relics and their brothers' spiritual well-being.")
            Unit_Restrictions = "Chaplain"
        elif num_unit_restrictions <= 105:
            f.writelines("\nThis Chapter has no Terminators; for whatever reason, they have no terminator armor"
                         " available.")
            Unit_Restrictions = "Terminator"
        elif num_unit_restrictions <= 98:
            f.writelines("\nThis Chapter has no Chapter Master; some other office or council needs to perform the tasks"
                         " otherwise carried out by the Chapter Master.")
            Unit_Restrictions = "Master"
        elif num_unit_restrictions <= 99:
            f.writelines("\nThis Chapter has no Dreadnoughts; something else needs to be done with the severely"
                         " wounded.")
            Unit_Restrictions = "Dreadnought"
        elif num_unit_restrictions <= 100:
            f.writelines("\nChoose something truly unusual.")

    # The following code defines modifiers for the Chapter's Homeworld

    def function_homeworld_modifier():
        global Homeworld_Modifier
        num_homeworld_modifier = random.randint(1, 100)
        print("Homeworld Modifier Roll:")
        print(num_homeworld_modifier)
        if num_homeworld_modifier <= 25:
            f.writelines("\nTemperate ")
            Homeworld_Modifier = "Temperate"
        elif num_homeworld_modifier <= 50:
            f.writelines("\nArid ")
            Homeworld_Modifier = "Arid"
        elif num_homeworld_modifier <= 60:
            f.writelines("\nFrozen ")
            Homeworld_Modifier = "Frozen"
        elif num_homeworld_modifier <= 65:
            f.writelines("\nOceanic ")
            Homeworld_Modifier = "Oceanic"
        elif num_homeworld_modifier <= 75:
            f.writelines("\nFeral ")
            Homeworld_Modifier = "Feral"
        elif num_homeworld_modifier <= 80:
            f.writelines("\nMountainous ")
            Homeworld_Modifier = "Mountainous"
        elif num_homeworld_modifier <= 85:
            f.writelines("\nPenal ")
            Homeworld_Modifier = "Penal"
        elif num_homeworld_modifier <= 90:
            f.writelines("\nSubterranean ")
            Homeworld_Modifier = "Subterranean"
        elif num_homeworld_modifier <= 99:
            f.writelines("\nForbidden ")
            Homeworld_Modifier = "Forbidden"
        elif num_homeworld_modifier == 100:
            f.writelines("\nSunless ")
            Homeworld_Modifier = "Sunless"

    # The following code defines a function that writes out extra text for homeworlds depending on its modifier.

    def function_homeworld_modifier_text():
        global Homeworld_Modifier
        if Homeworld_Modifier == "Temperate":
            f.writelines(" The world possesses a mild climate, agreeable to most humans.")
        if Homeworld_Modifier == "Arid":
            f.writelines(" The world possesses a very dry climate, and may feature extensive deserts.")
        if Homeworld_Modifier == "Frozen":
            f.writelines(" The world possesses an extremely cold climate, hazardous to most humans.")
        if Homeworld_Modifier == "Oceanic":
            f.writelines(" The world possesses vast oceans, covering 85% to 95% of the surface.")
        if Homeworld_Modifier == "Feral":
            f.writelines(" The world has regressed to a state of primitive tribalism, regardless of its previous"
                         " technological level and remaining infrastructure.")
        if Homeworld_Modifier == "Mountainous":
            f.writelines(" The world possesses vast mountain ranges visible from space, covering at least 70% of"
                         " the surface.")
        if Homeworld_Modifier == "Penal":
            f.writelines(" The world is almost entirely populated by criminals, sent here for isolation, labor or"
                         " both.")
        if Homeworld_Modifier == "Subterranean":
            f.writelines(" The world's surface is not at all conducive to settlement or construction. Consequently, its"
                         " population and infrastructure are almost entirely underground.")
        if Homeworld_Modifier == "Forbidden":
            f.writelines(" The world has been quarantined for one reason or another, and is now off-limits to all but"
                         " the Chapter and the highest Imperial authorities.")
        if Homeworld_Modifier == "Sunless":
            f.writelines(" The world has no sun. Any civilisation clinging to life in this desolate place does so"
                         " tentatively at best.")

    # The following code defines the Chapter's single lost Zygote

    def function_lost_zygote():
        global Missing_Zygote_Base
        global Missing_Zygote_1
        global Missing_Zygote_2
        global Missing_Zygote_3
        global Missing_Zygote_4
        global Missing_Zygote_5
        global Missing_Zygote_6
        global Missing_Zygote_7
        global Missing_Zygote_8
        global Existing_Mutations_Base
        global Existing_Mutations_1
        global Existing_Mutations_2
        global Existing_Mutations_3
        global Existing_Mutations_4
        global Existing_Mutations_5
        global Existing_Mutations_6
        global Existing_Mutations_7
        global Existing_Mutations_8
        f.writelines("\nLost zygote:")
        num_one_lost_zygote = random.randint(1, 100)
        print("Lost Zygote Roll:")
        print(num_one_lost_zygote)
        if num_one_lost_zygote <= 8 and "Catalepsean Node" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                   Missing_Zygote_2, Missing_Zygote_3, Missing_Zygote_4,
                                                                   Missing_Zygote_5, Missing_Zygote_6, Missing_Zygote_7,
                                                                   Missing_Zygote_8, Existing_Mutations_Base,
                                                                   Existing_Mutations_1, Existing_Mutations_2,
                                                                   Existing_Mutations_3, Existing_Mutations_4,
                                                                   Existing_Mutations_5, Existing_Mutations_6,
                                                                   Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Catalepsean Node.")
            Missing_Zygote_Base = "Catalepsean Node"
        elif num_one_lost_zygote <= 17 and "Preomnor" not in (Missing_Zygote_Base, Missing_Zygote_1, Missing_Zygote_2,
                                                              Missing_Zygote_3, Missing_Zygote_4, Missing_Zygote_5,
                                                              Missing_Zygote_6, Missing_Zygote_7, Missing_Zygote_8,
                                                              Existing_Mutations_Base, Existing_Mutations_1,
                                                              Existing_Mutations_2, Existing_Mutations_3,
                                                              Existing_Mutations_4, Existing_Mutations_5,
                                                              Existing_Mutations_6, Existing_Mutations_7,
                                                              Existing_Mutations_8):
            f.writelines(" Preomnor.")
            Missing_Zygote_Base = "Preomnor"
        elif num_one_lost_zygote <= 26 and "Omophagea" not in (Missing_Zygote_Base, Missing_Zygote_1, Missing_Zygote_2,
                                                               Missing_Zygote_3, Missing_Zygote_4, Missing_Zygote_5,
                                                               Missing_Zygote_6, Missing_Zygote_7, Missing_Zygote_8,
                                                               Existing_Mutations_Base, Existing_Mutations_1,
                                                               Existing_Mutations_2, Existing_Mutations_3,
                                                               Existing_Mutations_4, Existing_Mutations_5,
                                                               Existing_Mutations_6, Existing_Mutations_7,
                                                               Existing_Mutations_8):
            f.writelines(" Omophagea.")
            Missing_Zygote_Base = "Omophagea"
        elif num_one_lost_zygote <= 35 and "Occulobe" not in (Missing_Zygote_Base, Missing_Zygote_1, Missing_Zygote_2,
                                                              Missing_Zygote_3, Missing_Zygote_4, Missing_Zygote_5,
                                                              Missing_Zygote_6, Missing_Zygote_7, Missing_Zygote_8,
                                                              Existing_Mutations_Base, Existing_Mutations_1,
                                                              Existing_Mutations_2, Existing_Mutations_3,
                                                              Existing_Mutations_4, Existing_Mutations_5,
                                                              Existing_Mutations_6, Existing_Mutations_7,
                                                              Existing_Mutations_8):
            f.writelines(" Occulobe.")
            Missing_Zygote_Base = "Occulobe"
        elif num_one_lost_zygote <= 44 and "Lyman’s Ear" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                 Missing_Zygote_2, Missing_Zygote_3, Missing_Zygote_4,
                                                                 Missing_Zygote_5, Missing_Zygote_6, Missing_Zygote_7,
                                                                 Missing_Zygote_8, Existing_Mutations_Base,
                                                                 Existing_Mutations_1, Existing_Mutations_2,
                                                                 Existing_Mutations_3, Existing_Mutations_4,
                                                                 Existing_Mutations_5, Existing_Mutations_6,
                                                                 Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Lyman’s Ear.")
            Missing_Zygote_Base = "Lyman’s Ear"
        elif num_one_lost_zygote <= 53 and "Sus-an Membrane" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                     Missing_Zygote_2, Missing_Zygote_3,
                                                                     Missing_Zygote_4, Missing_Zygote_5,
                                                                     Missing_Zygote_6, Missing_Zygote_7,
                                                                     Missing_Zygote_8, Existing_Mutations_Base,
                                                                     Existing_Mutations_1, Existing_Mutations_2,
                                                                     Existing_Mutations_3, Existing_Mutations_4,
                                                                     Existing_Mutations_5, Existing_Mutations_6,
                                                                     Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Sus-an Membrane.")
            Missing_Zygote_Base = "Sus-an Membrane"
        elif num_one_lost_zygote <= 62 and "Oolitic Kidney" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                    Missing_Zygote_2, Missing_Zygote_3,
                                                                    Missing_Zygote_4, Missing_Zygote_5,
                                                                    Missing_Zygote_6, Missing_Zygote_7,
                                                                    Missing_Zygote_8, Existing_Mutations_Base,
                                                                    Existing_Mutations_1, Existing_Mutations_2,
                                                                    Existing_Mutations_3, Existing_Mutations_4,
                                                                    Existing_Mutations_5, Existing_Mutations_6,
                                                                    Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Oolitic Kidney.")
            Missing_Zygote_Base = "Oolitic Kidney"
        elif num_one_lost_zygote <= 71 and "Neuroglottis" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                  Missing_Zygote_2, Missing_Zygote_3, Missing_Zygote_4,
                                                                  Missing_Zygote_5, Missing_Zygote_6, Missing_Zygote_7,
                                                                  Missing_Zygote_8, Existing_Mutations_Base,
                                                                  Existing_Mutations_1, Existing_Mutations_2,
                                                                  Existing_Mutations_3, Existing_Mutations_4,
                                                                  Existing_Mutations_5, Existing_Mutations_6,
                                                                  Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Neuroglottis.")
            Missing_Zygote_Base = "Neuroglottis"
        elif num_one_lost_zygote <= 80 and "Mucranoid" not in (Missing_Zygote_Base, Missing_Zygote_1, Missing_Zygote_2,
                                                               Missing_Zygote_3, Missing_Zygote_4, Missing_Zygote_5,
                                                               Missing_Zygote_6, Missing_Zygote_7, Missing_Zygote_8,
                                                               Existing_Mutations_Base, Existing_Mutations_1,
                                                               Existing_Mutations_2, Existing_Mutations_3,
                                                               Existing_Mutations_4, Existing_Mutations_5,
                                                               Existing_Mutations_6, Existing_Mutations_7,
                                                               Existing_Mutations_8):
            f.writelines(" Mucranoid.")
            Missing_Zygote_Base = "Mucranoid"
        elif num_one_lost_zygote <= 89 and "Betcher's Gland" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                     Missing_Zygote_2, Missing_Zygote_3,
                                                                     Missing_Zygote_4, Missing_Zygote_5,
                                                                     Missing_Zygote_6, Missing_Zygote_7,
                                                                     Missing_Zygote_8, Existing_Mutations_Base,
                                                                     Existing_Mutations_1, Existing_Mutations_2,
                                                                     Existing_Mutations_3, Existing_Mutations_4,
                                                                     Existing_Mutations_5, Existing_Mutations_6,
                                                                     Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Betcher's Gland.")
            Missing_Zygote_Base = "Betcher's Gland"
        elif num_one_lost_zygote <= 98 and "Melanochromic Organ" not in (Missing_Zygote_Base, Missing_Zygote_1,
                                                                         Missing_Zygote_2, Missing_Zygote_3,
                                                                         Missing_Zygote_4, Missing_Zygote_5,
                                                                         Missing_Zygote_6, Missing_Zygote_7,
                                                                         Missing_Zygote_8, Existing_Mutations_Base,
                                                                         Existing_Mutations_1, Existing_Mutations_2,
                                                                         Existing_Mutations_3, Existing_Mutations_4,
                                                                         Existing_Mutations_5, Existing_Mutations_6,
                                                                         Existing_Mutations_7, Existing_Mutations_8):
            f.writelines(" Melanochromic Organ.")
            Missing_Zygote_Base = "Melanochromic Organ"
        elif num_one_lost_zygote <= 100:
            f.writelines(" choose any.")

    # The following code defines the Chapter's Progenitor-specific mutations

    def function_progenitor_mutations():
        global Existing_Mutations_Base
        global Existing_Mutations_1
        global Existing_Mutations_2
        global Existing_Mutations_3
        global Existing_Mutations_4
        global Existing_Mutations_5
        global Existing_Mutations_6
        global Existing_Mutations_7
        global Existing_Mutations_8
        global Progenitor_Chapter
        if Progenitor_Chapter == "Ultramarines":
            # Ultramarines
            function_lost_zygote()
        elif Progenitor_Chapter == "Blood Angels" and "Blood Angels" not in (Existing_Mutations_Base,
                                                                             Existing_Mutations_1, Existing_Mutations_2,
                                                                             Existing_Mutations_3, Existing_Mutations_4,
                                                                             Existing_Mutations_5, Existing_Mutations_6,
                                                                             Existing_Mutations_7,
                                                                             Existing_Mutations_8):
            # Blood Angels
            num_angels_mutation = random.randint(1, 6)
            print("Blood Angels Mutation Roll:")
            print(num_angels_mutation)
            if num_angels_mutation <= 3:
                f.writelines("\nAverage rate of the Red Thirst and the Black Rage.")
            elif num_angels_mutation <= 4:
                f.writelines("\nIncreased rate of the Red Thirst.")
            elif num_angels_mutation <= 5:
                f.writelines("\nIncreased rate of the Black Rage.")
            elif num_angels_mutation <= 6:
                f.writelines("\nIncreased rate of the Red Thirst and the Black Rage.")
            Existing_Mutations_Base = "Blood Angels"
        elif Progenitor_Chapter == "Dark Angels":
            # Dark Angels
            function_lost_zygote()
        elif Progenitor_Chapter == "Unknown" or Progenitor_Chapter == "Suspected Traitor":
            # Unknown
            function_lost_zygote()
        elif Progenitor_Chapter == "Imperial Fists":
            # Imperial Fists
            function_lost_zygote()
        elif Progenitor_Chapter == "White Scars":
            # White Scars
            function_lost_zygote()
        elif Progenitor_Chapter == "Raven Guard" and "Melanochromic Organ" not in (Existing_Mutations_Base,
                                                                                   Existing_Mutations_1,
                                                                                   Existing_Mutations_2,
                                                                                   Existing_Mutations_3,
                                                                                   Existing_Mutations_4,
                                                                                   Existing_Mutations_5,
                                                                                   Existing_Mutations_6,
                                                                                   Existing_Mutations_7,
                                                                                   Existing_Mutations_8):
            # Raven Guard
            f.writelines("\nMalfunctioning Melanochrome.")
            Existing_Mutations_Base = "Melanochromic Organ"
        elif Progenitor_Chapter == "Iron Hands" and "Dysphoria" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                                        Existing_Mutations_2, Existing_Mutations_3,
                                                                        Existing_Mutations_4, Existing_Mutations_5,
                                                                        Existing_Mutations_6, Existing_Mutations_7,
                                                                        Existing_Mutations_8):
            # Iron Hands
            f.writelines("\nBody Dysphoria.")
            Existing_Mutations_Base = "Dysphoria"
        elif Progenitor_Chapter == "Space Wolves" and "Unstable Helix" not in (Existing_Mutations_Base,
                                                                               Existing_Mutations_1,
                                                                               Existing_Mutations_2,
                                                                               Existing_Mutations_3,
                                                                               Existing_Mutations_4,
                                                                               Existing_Mutations_5,
                                                                               Existing_Mutations_6,
                                                                               Existing_Mutations_7,
                                                                               Existing_Mutations_8):
            # Space Wolves
            f.writelines("\nUnstable Canis Helix.")
            Existing_Mutations_Base = "Unstable Helix"
        elif Progenitor_Chapter == "Salamanders" and "Melanochromic Organ" not in (Existing_Mutations_Base,
                                                                                   Existing_Mutations_1,
                                                                                   Existing_Mutations_2,
                                                                                   Existing_Mutations_3,
                                                                                   Existing_Mutations_4,
                                                                                   Existing_Mutations_5,
                                                                                   Existing_Mutations_6,
                                                                                   Existing_Mutations_7,
                                                                                   Existing_Mutations_8,
                                                                                   Missing_Zygote_Base):
            # Salamanders
            f.writelines("\nMalfunctioning Melanochrome.")
            Existing_Mutations_Base = "Melanochromic Organ"
        else:
            function_lost_zygote()

    # The following code defines the Chapter's Mutations

    def function_mutations():
        global Existing_Mutations_Base
        global Existing_Mutations_1
        global Existing_Mutations_2
        global Existing_Mutations_3
        global Existing_Mutations_4
        global Existing_Mutations_5
        global Existing_Mutations_6
        global Existing_Mutations_7
        global Existing_Mutations_8
        num_mutations = random.randint(1, 21)
        print("Mutation Roll:")
        print(num_mutations)
        if num_mutations <= 1 and "Biscopea" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                     Existing_Mutations_2, Existing_Mutations_3, Existing_Mutations_4,
                                                     Existing_Mutations_5, Existing_Mutations_6, Existing_Mutations_7,
                                                     Existing_Mutations_8):
            f.writelines("\nMutated Biscopea.")
            Existing_Mutations_Base = "Biscopea"
        elif num_mutations <= 2 and "Occulobe" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                       Existing_Mutations_2, Existing_Mutations_3, Existing_Mutations_4,
                                                       Existing_Mutations_5, Existing_Mutations_6, Existing_Mutations_7,
                                                       Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Occulobe.")
            Existing_Mutations_Base = "Occulobe"
        elif num_mutations <= 3 and "Catalepsean Node" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                               Existing_Mutations_2, Existing_Mutations_3,
                                                               Existing_Mutations_4, Existing_Mutations_5,
                                                               Existing_Mutations_6, Existing_Mutations_7,
                                                               Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Catalepsean Node.")
            Existing_Mutations_Base = "Catalepsean Node"
        elif num_mutations <= 4 and "Melanochromic Organ" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                                  Existing_Mutations_2, Existing_Mutations_3,
                                                                  Existing_Mutations_4, Existing_Mutations_5,
                                                                  Existing_Mutations_6, Existing_Mutations_7,
                                                                  Existing_Mutations_8):
            f.writelines("\nMutated Melanochrome.")
            Existing_Mutations_Base = "Melanochromic Organ"
        elif num_mutations <= 5 and "Ossmodula" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                        Existing_Mutations_2, Existing_Mutations_3,
                                                        Existing_Mutations_4, Existing_Mutations_5,
                                                        Existing_Mutations_6, Existing_Mutations_7,
                                                        Existing_Mutations_8):
            f.writelines("\nMutated Ossmodula.")
            Existing_Mutations_Base = "Ossmodula"
        elif num_mutations <= 7:
            function_lost_zygote()
        elif num_mutations <= 8:
            function_progenitor_mutations()
        elif num_mutations <= 9 and "Larraman" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                       Existing_Mutations_2, Existing_Mutations_3, Existing_Mutations_4,
                                                       Existing_Mutations_5, Existing_Mutations_6, Existing_Mutations_7,
                                                       Existing_Mutations_8):
            f.writelines("\nMutated Larraman's Organ.")
            Existing_Mutations_Base = "Larraman"
        elif num_mutations <= 10 and "Preomnor" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                        Existing_Mutations_2, Existing_Mutations_3,
                                                        Existing_Mutations_4, Existing_Mutations_5,
                                                        Existing_Mutations_6, Existing_Mutations_7,
                                                        Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Preomnor.")
            Existing_Mutations_Base = "Preomnor"
        elif num_mutations <= 11 and "Omophagea" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                         Existing_Mutations_2, Existing_Mutations_3,
                                                         Existing_Mutations_4, Existing_Mutations_5,
                                                         Existing_Mutations_6, Existing_Mutations_7,
                                                         Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Omophagea.")
            Existing_Mutations_Base = "Omophagea"
        elif num_mutations <= 12 and "Multi-lung" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                          Existing_Mutations_2, Existing_Mutations_3,
                                                          Existing_Mutations_4, Existing_Mutations_5,
                                                          Existing_Mutations_6, Existing_Mutations_7,
                                                          Existing_Mutations_8):
            f.writelines("\nMutated Multi-lung.")
            Existing_Mutations_Base = "Multi-lung"
        elif num_mutations <= 13 and "Lyman’s Ear" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                           Existing_Mutations_2, Existing_Mutations_3,
                                                           Existing_Mutations_4, Existing_Mutations_5,
                                                           Existing_Mutations_6, Existing_Mutations_7,
                                                           Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Lyman's Ear.")
            Existing_Mutations_Base = "Lyman’s Ear"
        elif num_mutations <= 14 and "Sus-an Membrane" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                               Existing_Mutations_2, Existing_Mutations_3,
                                                               Existing_Mutations_4, Existing_Mutations_5,
                                                               Existing_Mutations_6, Existing_Mutations_7,
                                                               Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Sus-an Membrane.")
            Existing_Mutations_Base = "Sus-an Membrane"
        elif num_mutations <= 15 and "Oolitic Kidney" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                              Existing_Mutations_2, Existing_Mutations_3,
                                                              Existing_Mutations_4, Existing_Mutations_5,
                                                              Existing_Mutations_6, Existing_Mutations_7,
                                                              Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Oolitic Kidney.")
            Existing_Mutations_Base = "Oolitic Kidney"
        elif num_mutations <= 16 and "Neuroglottis" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                            Existing_Mutations_2, Existing_Mutations_3,
                                                            Existing_Mutations_4, Existing_Mutations_5,
                                                            Existing_Mutations_6, Existing_Mutations_7,
                                                            Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Neuroglottis.")
            Existing_Mutations_Base = "Neuroglottis"
        elif num_mutations <= 17 and "Mucranoid" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                         Existing_Mutations_2, Existing_Mutations_3,
                                                         Existing_Mutations_4, Existing_Mutations_5,
                                                         Existing_Mutations_6, Existing_Mutations_7,
                                                         Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Mucranoid.")
            Existing_Mutations_Base = "Mucranoid"
        elif num_mutations <= 18 and "Betcher's Gland" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                               Existing_Mutations_2, Existing_Mutations_3,
                                                               Existing_Mutations_4, Existing_Mutations_5,
                                                               Existing_Mutations_6, Existing_Mutations_7,
                                                               Existing_Mutations_8, Missing_Zygote_Base):
            f.writelines("\nMutated Betcher's Gland.")
            Existing_Mutations_Base = "Betcher's Gland"
        elif num_mutations <= 19 and "Haemastamen" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                           Existing_Mutations_2, Existing_Mutations_3,
                                                           Existing_Mutations_4, Existing_Mutations_5,
                                                           Existing_Mutations_6, Existing_Mutations_7,
                                                           Existing_Mutations_8):
            f.writelines("\nMutated Haemastamen.")
            Existing_Mutations_Base = "Haemastamen"
        elif num_mutations <= 20 and "Heart" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                     Existing_Mutations_2, Existing_Mutations_3, Existing_Mutations_4,
                                                     Existing_Mutations_5, Existing_Mutations_6, Existing_Mutations_7,
                                                     Existing_Mutations_8):
            f.writelines("\nMutated Secondary Heart.")
            Existing_Mutations_Base = "Heart"
        elif num_mutations <= 21 and "Carapace" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                        Existing_Mutations_2, Existing_Mutations_3,
                                                        Existing_Mutations_4, Existing_Mutations_5,
                                                        Existing_Mutations_6, Existing_Mutations_7,
                                                        Existing_Mutations_8):
            f.writelines("\nMutated Black Carapace.")
            Existing_Mutations_Base = "Carapace"
        else:
            function_lost_zygote()

    def function_chapter_quirks():
        global Unit_Restrictions
        global Chapter_Quirk_Base
        global Chapter_Quirk_1
        global Chapter_Quirk_2
        global Chapter_Quirk_3
        num_quirks = random.randint(1, 30)
        print("Quirk Roll:")
        print(num_quirks)
        if num_quirks <= 2 and "Absolute Colors" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                         Chapter_Quirk_3):
            f.writelines("\nAbsolute Colors: this Chapter will under no circumstances wear any colors but their own, "
                         "refusing to use camouflage, wear the partial silver and black of the Deathwatch, or the "
                         "absolute black of Black Shields.")
            Chapter_Quirk_Base = "Absolute Colors"
        elif num_quirks <= 4 and "Scarification" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                         Chapter_Quirk_3):
            f.writelines("\nScarification: this Chapter places cultural or practical emphasis on scarification. "
                         "This may be a means of tallying kills, recording events, a spiritual practice, or something "
                         "else entirely.")
            Chapter_Quirk_Base = "Scarification"
        elif num_quirks <= 6 and "Peculiar Cuisine" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                            Chapter_Quirk_3):
            f.writelines("\nPeculiar Cuisine: this Chapter has its own distinct food and drink, this being one of the "
                         "few luxuries afforded to Astartes.")
            Chapter_Quirk_Base = "Peculiar Cuisine"
        elif num_quirks <= 8 and "Particular Pastime" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                              Chapter_Quirk_3):
            f.writelines("\nParticular Pastime: this Chapter has certain activities its Astartes enjoy as a hobby of "
                         "sorts in their brief allotment of private time. This may be poetry, music, art, pet training,"
                         " or something else entirely.")
            Chapter_Quirk_Base = "Particular Pastime"
        elif num_quirks <= 10 and "Cultural Aesthetic" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                               Chapter_Quirk_3):
            f.writelines("\nCultural Aesthetic: this Chapter has its own notions of what is pleasing to the eye. These"
                         " notions may come across as strange to the wider Imperium.")
            Chapter_Quirk_Base = "Cultural Aesthetic"
        elif num_quirks <= 12 and Unit_Restrictions != "Librarian" and "Psychic Discipline" not in (Chapter_Quirk_Base,
                                                                                                    Chapter_Quirk_1,
                                                                                                    Chapter_Quirk_2,
                                                                                                    Chapter_Quirk_3):
            f.writelines("\nParticular Psychic Discipline: this Chapter's psykers have their own preferences for a "
                         "psychic discipline. This may be aeromancy, pyromancy, terramancy, or something else "
                         "entirely.")
            Chapter_Quirk_Base = "Psychic Discipline"
        elif num_quirks <= 14 and "Naming Convention" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                              Chapter_Quirk_3):
            f.writelines("\nUnusual Naming Conventions: this Chapter has its own system by which its Astartes name "
                         "themselves. While taking a new name upon induction into a Chapter is not unusual, these "
                         "Astartes name themselves in distinct ways, such as based on deeds, events, achievements, or "
                         "something else entirely.")
            Chapter_Quirk_Base = "Naming Convention"
        elif num_quirks <= 16 and "Hospitable" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                       Chapter_Quirk_3) and "Territorial" not in (Chapter_Quirk_Base,
                                                                                                  Chapter_Quirk_1,
                                                                                                  Chapter_Quirk_2,
                                                                                                  Chapter_Quirk_3):
            f.writelines("\nTerritorial: this Chapter places extraordinary importance on the integrity of their "
                         "holdings. Violating the sanctity of a space or place they consider their own is a grave "
                         "offense, and failing to protect their holdings is a serious stain on their honor.")
            Chapter_Quirk_Base = "Territorial"
        elif num_quirks <= 18 and "Territorial" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                        Chapter_Quirk_3) and "Hospitable" not in (Chapter_Quirk_Base,
                                                                                                  Chapter_Quirk_1,
                                                                                                  Chapter_Quirk_2,
                                                                                                  Chapter_Quirk_3):
            f.writelines("\nHospitable: this Chapter places extraordinary importance on the integrity of guest rights. "
                         "Imperilling anyone under their protection is considered a grave offense, and failing to "
                         "protect a guest is a serious stain on their honor.")
            Chapter_Quirk_Base = "Hospitable"
        elif num_quirks <= 20 and "Unique Language" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                            Chapter_Quirk_3):
            f.writelines("\nUnique Language: this Chapter maintains its own language, distinct enough from standard "
                         "Imperial High or Low Gothic that it cannot be mutually understood. This may be a tongue of "
                         "their own making, the language of their homeworld's native population, or something else "
                         "entirely.")
            Chapter_Quirk_Base = "Unique Language"
        elif num_quirks <= 22 and "Peculiar Honor" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                           Chapter_Quirk_3):
            f.writelines("\nPeculiar Honor: this Chapter's views on what is and isn't honorable might be considered "
                         "strange by the wider Imperium. This may be due to a unique internal code of conduct, cultural"
                         " associations brought over from their homeworld's native population, or something else "
                         "entirely.")
            Chapter_Quirk_Base = "Peculiar Honor"
        elif num_quirks <= 24 and "Unusual Penal Code" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                               Chapter_Quirk_3):
            f.writelines("\nUnusual Penal Code: this Chapter's means of policing itself, and the punishments it issues"
                         " to its Astartes, is unique to them, and may be entirely indecipherable to outsiders. They "
                         "may restrict this to themselves alone, or they may apply it to others as well, as and when "
                         "appropriate.")
            Chapter_Quirk_Base = "Unusual Penal Code"
        elif num_quirks <= 26 and "Faceless" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                     Chapter_Quirk_3):
            f.writelines("\nFaceless: this Chapter's Astartes, for one reason or another, never show their faces, even"
                         " when unarmored and when not deployed to a warzone, in which cases they use some other means"
                         " of concealing their countenances from others. This may extend even to their own brothers.")
            Chapter_Quirk_Base = "Faceless"
        elif num_quirks <= 28 and "Silent" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                   Chapter_Quirk_3):
            f.writelines("\nSilent: this Chapter's Astartes, for one reason or another, never speak with outsiders. "
                         "They might instead rely on trusted mortal intermediaries to represent them when communicating"
                         " with the wider Imperium. They may also have found some other means to do this, or even"
                         "outright refuse any communication at all.")
            Chapter_Quirk_Base = "Silent"
        elif num_quirks <= 30 and "Trophy Taking" not in (Chapter_Quirk_Base, Chapter_Quirk_1, Chapter_Quirk_2,
                                                          Chapter_Quirk_3):
            f.writelines("\nTrophy Taking: this Chapter traditionally takes trophies from enemies. This may take a "
                         "variety of forms, such as keeping eyes, preserving hearts, taking skulls, or something else "
                         "entirely. There may also be various criteria, such as trophies only being taken from worthy "
                         "foes, only from leaders, only at certain times, or something else entirely.")

    # The following code asks the user for input to set the Chapter's name

    global chapter_name
    print("Name your Chapter:")
    layout = [
        [Sg.Text("Clicking SUBMIT will generate a Chapter with that name."
                 "\nPlease note that generating a Chapter with a name already in use in the same folder will result in "
                 "that Chapter being overwritten."
                 "\nIf you want to make sure this does not happen, please move the generated .txt file to a different "
                 "folder.")],
        [Sg.Text('Chapter Name', size=(15, 1)), Sg.InputText()],
        [Sg.Submit("SUBMIT")]
    ]
    window = Sg.Window('CHAPTER CREATION SCRIPT', layout)
    event, values = window.read()
    chapter_name = values[0] + ".txt"
    print(chapter_name)

    # The following code opens (or creates, if none exists) the .txt file.
    # Upon execution, the file automatically saves and closes.

    with open("C:/Chapter Creator/" + chapter_name, "w") as f:

        # The following code defines the reason for the Chapter's Founding

        f.writelines("    Founding Reason")
        num_founding_reason = random.randint(1, 28)
        print("Founding Reason Roll:")
        print(num_founding_reason)
        if num_founding_reason <= 4:
            f.writelines("\nPrognostication: Imperial psykers determined a unique need for a particular Chapter at a"
                         " specific place at a certain time. This Chapter is, for all intents and purposes, the direct"
                         " result of prophecy. Even if that prophecy is no longer relevant for one reason nor another,"
                         " the Chapter's identity might still be strongly influenced by it.")
        elif num_founding_reason <= 8:
            f.writelines("\nPreparation: Imperial authorities identified the need for a Chapter to combat a specific"
                         " threat. Even if that threat no longer exists today, its original presence lead to the "
                         "founding of this Chapter.")
        elif num_founding_reason <= 12:
            f.writelines("\nDefense: Imperial authorities identified a part of the Imperium so crucial to its continued"
                         " existence that a Chapter was deemed necessary for its protection. Even if the aforementioned"
                         " part of the Imperium has now fallen, this Chapter was created for that express purpose, and"
                         " its identity might still be strongly influenced by it")
        elif num_founding_reason <= 16:
            f.writelines("\nOffense: Imperial authorities identified the need for a crusading Chapter, whether as part"
                         " of an organised offensive or as a flexible strike force. This Chapter was created for that"
                         " purpose, and is on its crusade to this very day. Even if the offensive that originally"
                         " justified its creation is no longer ongoing, the Chapter's identity might still be strongly"
                         " influenced by it.")
        elif num_founding_reason <= 20:
            f.writelines("\nUnknown: records of why this Chapter was founded have been lost. The Chapter's identity"
                         " might be strongly influenced by the loss of this important information.")
        elif num_founding_reason <= 24:
            f.writelines("\nSecret: the true reason for this Chapter being founded was of such importance that it was"
                         " kept secret to all but the High Lords of Terra and the Chapter itself. Other agencies of the"
                         " Imperium, such as the Inquisition, likely know at least part of the truth. The Chapter may"
                         " maintain an official founding cause to obfuscate the truth. Even if the secret circumstance"
                         " is no longer relevant, the Chapter's identity might still be strongly influenced by it.")
        elif num_founding_reason <= 28:
            f.writelines("\nRefounding: Imperial authorities decided to reform a Chapter that was once lost, either in"
                         " battle or by some other means. This Chapter likely, but not necessarily, maintains a similar"
                         " culture, organisation and demeanor to its namesake.")

        f.writelines("\n")

        # The following code defines the date of the Chapter's Founding

        f.writelines("\n    Founding Date")
        num_founding_date = random.randint(1, 140)
        print("Founding Date Roll:")
        print(num_founding_date)
        if num_founding_date <= 1:
            f.writelines("\n2nd Founding: although no concrete evidence exists, this Chapter claims to be have been"
                         " founded in the early 31st millennium. During the 2nd Founding, the original Legions were"
                         " split into many smaller Chapters immediately following the Horus Heresy. This time also saw"
                         " the 1st Black Crusade of Abaddon the Despoiler.")
        elif num_founding_date <= 5:
            f.writelines("\n3rd Founding: this Chapter was created in the early 32nd millennium, during the 3rd"
                         " Founding. Unlike the Second Founding, which was a reorganisation of existing Astartes from"
                         " Legions into Chapters, this was the first time truly new Chapters were raised. This time"
                         " also saw the 2nd and 3rd Black Crusades of Abaddon the Despoiler.")
        elif num_founding_date <= 10:
            f.writelines("\nUnknown: if any records of this Chapter's founding exist anywhere, they are not known to"
                         " the Chapter, nor indeed the Imperium at large.")
        elif num_founding_date <= 15:
            f.writelines("\n4th Founding: this Chapter was created in the mid 32nd millennium, during the 4th Founding."
                         " This was an uncertain and tumultuous time, following the cataclysmic War of the Beast.")
        elif num_founding_date <= 20:
            f.writelines("\n5th Founding: this Chapter was created at some point between the mid 32nd millennium and"
                         " the mid 34th millennium, during the 5th Founding. This time also saw the 4th Black Crusade"
                         " of Abaddon the Despoiler. The 6th and 7th Foundings occurred during the same period of ~2000"
                         " years.")
        elif num_founding_date <= 25:
            f.writelines("\n6th Founding: this Chapter was created at some point between the mid 32nd millennium and"
                         " the mid 34th millennium, during the 6th Founding. This time also saw the 4th Black Crusade"
                         " of Abaddon the Despoiler. The 5th and 7th Foundings occurred during the same period of ~2000"
                         " years.")
        elif num_founding_date <= 30:
            f.writelines("\n7th Founding: this Chapter was created at some point between the mid 32nd millennium and"
                         " the mid 34th millennium, during the 7th Founding. This time also saw the 4th Black Crusade"
                         " of Abaddon the Despoiler The 5th and 6th Foundings occurred during the same period of ~2000"
                         " years.")
        elif num_founding_date <= 45:
            f.writelines("\n8th Founding: this Chapter was created in the mid 34th millennium, during the 8th Founding."
                         " Like others of this Founding, accounts are fragmentary at best, and likely not"
                         " contemporary.")
        elif num_founding_date <= 50:
            f.writelines("\n9th Founding: this Chapter was created at some point between the mid 34th millennium and"
                         " the mid 35th millennium, during the 9th Founding. The 10th, 11th and 12th Foundings occurred"
                         " during the same period of ~1000 years.")
        elif num_founding_date <= 55:
            f.writelines("\n10th Founding: this Chapter was created at some point between the mid 34th millennium and"
                         " the mid 35th millennium, during the 10th Founding. The 9th, 11th and 12th Foundings occurred"
                         " during the same period of ~1000 years.")
        elif num_founding_date <= 60:
            f.writelines("\n11th Founding: this Chapter was created at some point between the mid 34th millennium and"
                         " the mid 35th millennium, during the 11th Founding. The 9th, 10th and 12th Foundings occurred"
                         " during the same period of ~1000 years.")
        elif num_founding_date <= 65:
            f.writelines("\n12th Founding: this Chapter was created at some point between the mid 34th millennium and"
                         " the mid 35th millennium, during the 12th Founding. The 9th, 10th and 11th Foundings occurred"
                         " during the same period of ~1000 years.")
        elif num_founding_date <= 70:
            f.writelines("\n13th Founding: this Chapter claims to have been created in the mid 35th millennium, during"
                         " the 13th 'Dark' Founding. However, the Adeptus Terra possesses no original samples of"
                         " gene-seed from any Chapters of the 13th Founding, so this claim is disputed.")
        elif num_founding_date <= 75:
            f.writelines("\n14th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 14th Founding. The 15th, 16th, 17th, 18th, 19th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 80:
            f.writelines("\n15th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 15th Founding. The 14th, 16th, 17th, 18th, 19th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 85:
            f.writelines("\n16th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 16th Founding. The 14th, 15th, 17th, 18th, 19th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 90:
            f.writelines("\n17th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 17th Founding. The 14th, 15th, 16th, 18th, 19th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 95:
            f.writelines("\n18th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 18th Founding. The 14th, 15th, 16th, 17th, 19th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 100:
            f.writelines("\n19th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 19th Founding. The 14th, 15th, 16th, 17th, 18th and"
                         " 20th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 105:
            f.writelines("\n20th Founding: this Chapter was created at some point between the mid 35th millennium and"
                         " the late 35th millennium, during the 20th Founding. The 14th, 15th, 16th, 17th, 18th and"
                         " 19th Foundings occurred during the same period of ~500 years.")
        elif num_founding_date <= 110:
            f.writelines("\n21st Founding: this Chapter was created in the late 35th millennium, immediately prior to"
                         " the Age of Apostasy, during the 21st 'Cursed' Founding. The single largest Founding since"
                         " the 2nd, only a scant few have survived unscathed to the 42nd millennium. A dark omen hangs"
                         " over the Chapter.")
            Founding = "Cursed Founding"
        elif num_founding_date <= 115:
            f.writelines("\n22nd Founding: this Chapter was created in the early 36th millennium to the late 37th"
                         " millennium, during the 22nd Founding. These were the years following the Age of Apostasy,"
                         " which also saw the Great Cull carried out, as well as the 5th, 6th, 7th and 8th Black"
                         " Crusades of Abaddon the Despoiler.")
        elif num_founding_date <= 120:
            f.writelines("\n23rd Founding: this Chapter was created in the late 37th millennium to early 38th"
                         " millennium, during the 23rd 'Sentinel' Founding. It was intended to replace the"
                         " catastrophic losses of at least 57 Chapters in the preceding years and close vital gaps in"
                         " the Imperium's defenses. This time also saw the 9th Black Crusade of Abaddon the Despoiler.")
        elif num_founding_date <= 125:
            f.writelines("\n24th Founding: this Chapter was created between the 38th millennium and the 39th"
                         " millennium, during the 24th Founding. This time also saw the beginning of The Waning,"
                         " which was a gradual decrease in stability within the Imperium, the Redemption Crusades,"
                         " and the 10th and 11th Black Crusades of Abaddon the Despoiler.")
        elif num_founding_date <= 130:
            f.writelines("\n25th Founding: this Chapter was created in the 40th millennium, during the 25th 'Bastion'"
                         " Founding. This time also saw the return of Krieg to Imperial rule and the beginning of the"
                         " Macharian Crusade. A comparatively stable and peaceful time for the Imperium, allowing"
                         " borders to be both expanded and reinforced.")
        elif num_founding_date <= 135:
            f.writelines("\n26th Founding: this Chapter was created in the 41st millennium, during the 26th Founding,"
                         " making them the last of the original breed of Astartes, who would later become known as The"
                         " Firstborn. This time also saw the 12th and ultimate 13th Black Crusades of Abaddon the"
                         " Despoiler, as well as the consequential creation of the Cicatrix Maledictum, or the Great"
                         " Rift.")
        elif num_founding_date <= 140:
            f.writelines("\nUltima Founding: this Chapter was created in the early 42nd millennium, during the Ultima"
                         " Founding, and accordingly consists entirely of Primaris Astartes. Freshly formed, they face"
                         " a galaxy split in two by the Cicatrix Maledictum, the culmination of the Archenemy's Long"
                         " War, and the realisation of the Chaos Gods' plans.")
            Founding = "Ultima Founding"

        f.writelines("\n")

        # The following code defines whether the Chapter is pre- or post-42nd Millennium
        # Also whether Primaris reinforcements have been received

        if Founding != "Ultima Founding":
            f.writelines("\n    Timeline Status")
            num_timeline = random.randint(1, 100)
            print("Timeline Status Roll")
            print(num_timeline)
            if num_timeline <= 50:
                f.writelines("\nPre-42nd Millennium.")
            elif num_timeline <= 100:
                f.writelines("\nPost-42nd Millennium.")
                f.writelines("\n")
                f.writelines("\n    Primaris Reinforcements Status")
                num_primaris_reinforcements = random.randint(1, 100)
                print("Primaris Reinforcements Roll")
                print(num_primaris_reinforcements)
                if num_primaris_reinforcements <= 80:
                    f.writelines("\nReceived.")
                    Primaris_Reinforcements = "Yes"
                elif num_primaris_reinforcements <= 100:
                    f.writelines("\nNot received.")

            f.writelines("\n")

        # The following code defines curses for Chapters of the 21st Founding

        if Founding == "Cursed Founding":
            f.writelines("\n    Curse")
            num_curse = random.randint(1, 12)
            print("Curse Roll")
            print(num_curse)
            if num_curse <= 1:
                f.writelines("\nBad Luck: this Chapter suffers from some unquantifiable misfortune, resulting in"
                             " extraordinarily bad luck. Bad things always seem to happen at the worst of times. And,"
                             " worse still, even at the best of times.")
            elif num_curse <= 2:
                f.writelines("\nEverything Is Fine: this Chapter is fine. There's absolutely nothing to worry about."
                             " Nothing at all is wrong. Everything is as it ought to be. The Chapter is doing well and"
                             " will definitely continue to do well. Don't worry about it.")
            elif num_curse <= 3:
                f.writelines("\nNothing: this Chapter got lucky and is one of the very, very few from the Cursed"
                             " Founding to have no curse. Even so, some may still treat them with suspicion.")
            elif num_curse <= 4 and "DOOMED" not in (Existing_Mutations_Base, Existing_Mutations_1,
                                                     Existing_Mutations_2, Existing_Mutations_3, Existing_Mutations_4,
                                                     Existing_Mutations_5, Existing_Mutations_6, Existing_Mutations_7,
                                                     Existing_Mutations_8):
                f.writelines("\nDOOMED: this Chapter has lost the ability to create new Progenoid Glands. "
                             "Unless this is somehow fixed, they are doomed to suffer a slow death by attrition.")
                Existing_Mutations_Base = "DOOMED"
            elif num_curse <= 5:
                f.writelines("\nExcessive Mutation: this Chapter suffers from an inexplicable overabundance of "
                             "mutations. Whether from a defective gene-seed, deliberate tampering, or some sinister "
                             "element is unknown.")
                function_mutations()
                Existing_Mutations_5 = Existing_Mutations_Base
                Missing_Zygote_5 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_6 = Existing_Mutations_Base
                Missing_Zygote_6 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_7 = Existing_Mutations_Base
                Missing_Zygote_7 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_8 = Existing_Mutations_Base
                Missing_Zygote_8 = Missing_Zygote_Base
            elif num_curse <= 6:
                f.writelines("\nProphetic Treason: this Chapter is prophesied to betray the Imperium of Man. The"
                             " details of the prophecy have been lost, and so these Astartes are left with an "
                             "ostensible guarantee of treason, without the how, the why and the when of it all.")
            elif num_curse <= 7:
                f.writelines("\nLoathed: this Chapter is intensely hated by everyone they encounter. Regardless of "
                             "their actions, no matter their cooperative spirit, benevolent endeavors or altruistic "
                             "outreach, they are met with universal scorn. Some justify their hatred. Others may find"
                             " it difficult to explain.")
            elif num_curse <= 8:
                f.writelines("\nSudden Death: this Chapter is subject to a curious condition by which its Astartes "
                             "universally, without exception, die upon reaching 100 years of age. Marines who perish "
                             "in this manner carry no indications or symptoms that might explain their passing.")
            elif num_curse <= 9:
                f.writelines("\nCursed Providence: this Chapter has found that it must always consult the Emperor's "
                             "Tarot when making decisions. Any choice made without doing so inevitably results in "
                             "failure.")
            elif num_curse <= 10:
                f.writelines("\nScotophobia: this Chapter is subject to a strange calamity, by which its Astartes "
                             "always go missing in dark places. The darker it is, the greater the likelihood of "
                             "disappearance. Where they go and what happens to them is unknown. None ever return.")
            elif num_curse <= 11:
                f.writelines("\nHomichlophobia: this Chapter suffers from an unusual condition. Without exception, "
                             "its Astartes will lose consciousness upon entering a certain concentration of mist or "
                             "fog.")
            elif num_curse <= 12:
                f.writelines("\nSudden Mutation: this Chapter suffers from an unidentified condition, by which its "
                             "Astartes suffer spontaneous mutations of varying severity when subjected to some hitherto"
                             " unidentified criteria.")
            elif num_curse <= 13:
                f.writelines("\nLost: this Chapter is perpetually lost. They never reach their intended destination,"
                             " always somehow ending up in a different place, sometimes entirely removed from their "
                             "original target.")

            f.writelines("\n")

        # The following code defines the Chapter's Progenitor

        f.writelines("\n    Progenitor")
        if Founding != "Ultima Founding":
            num_progenitor = random.randint(1, 160)
            print("Progenitor Roll:")
            print(num_progenitor)
            if num_progenitor <= 50:
                f.writelines("\nUltramarines: this Chapter is of Roboute Guilliman's accomplished lineage, whether from"
                             " original Ultramarines stock or through a successor Chapter.")
                Progenitor_Chapter = "Ultramarines"
            elif num_progenitor <= 75:
                f.writelines("\nUnknown: this Chapter, as well as the Imperium at large, has lost all records of its"
                             " progenitor. There may be claims of one progenitor or another, but nothing can be"
                             " proven.")
                Progenitor_Chapter = "Unknown"
            elif num_progenitor <= 90:
                f.writelines("\nDark Angels: this Chapter is of the Lion El'Jonson's proud lineage, whether from "
                             "original Dark Angels stock or through a successor Chapter.")
                Progenitor_Chapter = "Dark Angels"
            elif num_progenitor <= 105:
                f.writelines("\nBlood Angels: this Chapter is of Sanguinius' esteemed lineage, whether from original "
                             "Blood Angels stock or through a successor Chapter.")
                Progenitor_Chapter = "Blood Angels"
            elif num_progenitor <= 120:
                f.writelines("\nImperial Fists: this Chapter is of Rogal Dorn's stubborn lineage, whether from original"
                             " Imperial Fists stock or through a successor Chapter.")
                Progenitor_Chapter = "Imperial Fists"
            elif num_progenitor <= 130:
                f.writelines("\nWhite Scars: this Chapter is of Jaghatai Khan's fierce lineage, whether from original"
                             " White Scars stock or through a successor Chapter.")
                Progenitor_Chapter = "White Scars"
            elif num_progenitor <= 140:
                f.writelines("\nRaven Guard: this Chapter is of Corvus Corax' noble lineage, whether from original"
                             " Raven Guard stock or through a successor Chapter.")
                Progenitor_Chapter = "Raven Guard"
            elif num_progenitor <= 150:
                f.writelines("\nIron Hands: this Chapter is of Ferrus Manus' troubled lineage, whether from original"
                             " Iron Hands stock or through a successor Chapter.")
                Progenitor_Chapter = "Iron Hands"
            elif num_progenitor <= 151:
                f.writelines("\nSpace Wolves: this Chapter claims to be of Leman Russ' savage lineage. However, the"
                             " Space Wolves themselves deny this claim, and no solid evidence exists to substantiate"
                             " it.")
                Progenitor_Chapter = "Space Wolves"
            elif num_progenitor <= 152:
                f.writelines("\nSalamanders: this Chapter claims to be of Vulkan's benevolent lineage. However, the"
                             " Salamanders themselves deny this claim, and no solid evidence exists to substantiate"
                             " it.")
                Progenitor_Chapter = "Salamanders"
            elif num_progenitor <= 160:
                f.writelines("\nSuspected Traitor: this Chapter, as well as the Imperium at large, has lost all records"
                             " of its progenitor. There may be claims of one progenitor or another, but nothing can be"
                             " proven, and rumors abound that their gene-seed was actually sourced from one of the 9"
                             " traitor Legions.")
                Progenitor_Chapter = "Suspected Traitor"
        if Founding == "Ultima Founding":
            num_ultima_progenitor = random.randint(1, 170)
            print("Progenitor Roll:")
            print(num_ultima_progenitor)
            if num_ultima_progenitor <= 50:
                f.writelines("\nUltramarines: this Chapter is of Roboute Guilliman's accomplished lineage, whether from"
                             " original Ultramarines stock or through a successor Chapter.")
                Progenitor_Chapter = "Ultramarines"
            elif num_ultima_progenitor <= 75:
                f.writelines("\nUnknown: this Chapter was created from gene-seed stocks whose records of origin have"
                             " been lost. There may be claims of one progenitor or another, but nothing can be proven.")
                Progenitor_Chapter = "Unknown"
            elif num_ultima_progenitor <= 90:
                f.writelines("\nDark Angels: this Chapter is of the Lion El'Jonson's proud lineage, whether from"
                             " original Dark Angels stock or through a successor Chapter.")
                Progenitor_Chapter = "Dark Angels"
            elif num_ultima_progenitor <= 105:
                f.writelines("\nBlood Angels: this Chapter is of Sanguinius' esteemed lineage, whether from original"
                             " Blood Angels stock or through a successor Chapter.")
                Progenitor_Chapter = "Blood Angels"
            elif num_ultima_progenitor <= 120:
                f.writelines("\nImperial Fists: this Chapter is of Rogal Dorn's stubborn lineage, whether from original"
                             " Imperial Fists stock or through a successor Chapter.")
                Progenitor_Chapter = "Imperial Fists"
            elif num_ultima_progenitor <= 130:
                f.writelines("\nWhite Scars: this Chapter is of Jaghatai Khan's fierce lineage, whether from original"
                             " White Scars stock or through a successor Chapter.")
                Progenitor_Chapter = "White Scars"
            elif num_ultima_progenitor <= 140:
                f.writelines("\nRaven Guard: this Chapter is of Corvus Corax' noble lineage, whether from original"
                             " Raven Guard stock or through a successor Chapter.")
                Progenitor_Chapter = "Raven Guard"
            elif num_ultima_progenitor <= 150:
                f.writelines("\nIron Hands: this Chapter is of Ferrus Manus' troubled lineage, whether from original"
                             " Iron Hands stock or through a successor Chapter.")
                Progenitor_Chapter = "Iron Hands"
            elif num_ultima_progenitor <= 155:
                f.writelines("\nSpace Wolves: this Chapter is of Leman Russ' savage lineage.")
                Progenitor_Chapter = "Space Wolves"
            elif num_ultima_progenitor <= 160:
                f.writelines("\nSalamanders: this Chapter is of Vulkan's benevolent lineage.")
                Progenitor_Chapter = "Salamanders"
            elif num_ultima_progenitor <= 170:
                f.writelines("\nSuspected Traitor: this Chapter was created from gene-seed stocks whose records of"
                             " origin have been lost. There may be claims of one progenitor or another, but nothing can"
                             " be proven, and rumors abound that their gene-seed was actually sourced from one of the 9"
                             " traitor Legions.")
                Progenitor_Chapter = "Suspected Traitor"

        f.writelines("\n")

        # The following code defines the purity of the Chapter's Gene-seed

        f.writelines("\n    Gene-seed purity")
        num_purity = random.randint(1, 20)
        print("Purity Roll:")
        print(num_purity)
        if num_purity <= 1:
            f.writelines("\nPure: this Chapter's gene-seed is, for all intents and purposes, purer than even its"
                         " progenitor's.")
            if Progenitor_Chapter == "Blood Angels":
                f.writelines(" Regardless of purity, they of course still suffer from the Red Thirst and the Black"
                             " Rage.")
        elif num_purity <= 10:
            f.writelines("\nMatches progenitor: this Chapter's gene-seed is largely identical to its progenitor's."
                         " Consequently, it likely suffers similar flaws.")
            if Progenitor_Chapter == "Blood Angels":
                f.writelines(" Regardless of purity, they of course still suffer from the Red Thirst and the Black Rage"
                             " to some extent.")
            num_mutations_1 = random.randint(1, 10)
            print("Progenitor Match Roll:")
            print(num_mutations_1)
            if num_mutations_1 > 5:
                f.writelines("\n")
                f.writelines("\n    Mutations")
                function_progenitor_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
        elif num_purity <= 16:
            f.writelines("\nDeviant: this Chapter's gene-seed has undergone small changes, whether deliberate or"
                         " accidental, deviating from its progenitor.")
            if Progenitor_Chapter == "Blood Angels":
                f.writelines(" Regardless of purity, they of course still suffer from the Red Thirst and the Black Rage"
                             " to some extent.")
            f.writelines("\n")
            f.writelines("\n    Mutations")
            num_mutations_1 = random.randint(1, 10)
            print("Mutations Roll:")
            print(num_mutations_1)
            if num_mutations_1 <= 7:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
            elif num_mutations_1 <= 10:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
        elif num_purity <= 19:
            f.writelines("\nMutated: this Chapter's gene-seed has undergone substantial changes, whether deliberate or"
                         " accidental, resulting in mutations significantly different from its progenitor.")
            if Progenitor_Chapter == "Blood Angels":
                f.writelines(" Regardless of purity, they of course still suffer from the Red Thirst and the Black Rage"
                             " to some extent.")
            f.writelines("\n")
            f.writelines("\n    Mutations")
            num_mutations_1 = random.randint(1, 10)
            print("Mutations Roll:")
            print(num_mutations_1)
            if num_mutations_1 <= 7:
                function_mutations()
            elif num_mutations_1 <= 9:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
            elif num_mutations_1 <= 10:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_3 = Existing_Mutations_Base
                Missing_Zygote_3 = Missing_Zygote_Base
                function_doomed()
        elif num_purity <= 20:
            f.writelines("\nDamaged: this Chapter's gene-seed has suffered catastrophic damage, whether from deliberate"
                         " tampering or some critical accident, resulting in severe flaws that make it unrecognisable"
                         " when compared to its progenitor.")
            if Progenitor_Chapter == "Blood Angels":
                f.writelines(" Regardless of purity, they of course still suffer from the Red Thirst and the Black"
                             " Rage.")
            f.writelines("\n")
            f.writelines("\n    Mutations")
            num_mutations_1 = random.randint(10, 10)
            print("Mutations Roll:")
            print(num_mutations_1)
            if num_mutations_1 <= 7:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
            elif num_mutations_1 <= 9:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_3 = Existing_Mutations_Base
                Missing_Zygote_3 = Missing_Zygote_Base
            elif num_mutations_1 <= 10:
                function_mutations()
                Existing_Mutations_1 = Existing_Mutations_Base
                Missing_Zygote_1 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_2 = Existing_Mutations_Base
                Missing_Zygote_2 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_3 = Existing_Mutations_Base
                Missing_Zygote_3 = Missing_Zygote_Base
                function_mutations()
                Existing_Mutations_4 = Existing_Mutations_Base
                Missing_Zygote_4 = Missing_Zygote_Base
                function_doomed()

        f.writelines("\n")

        # The following code defines the stability of the Chapter's gene-seed

        f.writelines("\n    Gene-Seed Stability")
        num_stability = random.randint(1, 10)
        print("Gene-Seed Stability Roll:")
        print(num_stability)
        if num_stability <= 2:
            f.writelines("\nStable: this Chapter's gene-seed is remarkably stable, significantly more so than what is"
                         " average. New flaws, deficiencies and mutations are practically unheard of, even when used to"
                         " found a new Chapter.")
        elif num_stability <= 7:
            f.writelines("\nAverage: this Chapter's gene-seed is, for all intents and purposes, run-of-the-mill. New"
                         " flaws, deficiencies and mutations are not unheard of, particularly when used to found a new"
                         " Chapter, but are manageable enough to be considered a non-issue.")
        elif num_stability <= 8:
            f.writelines("\nSlightly Unstable: this Chapter's gene-seed is less stable than what is average. New flaws,"
                         " deficiencies and mutations are relatively common, even when used to found a new Chapter, but"
                         " sufficiently frequent to be considered an issue.")
        elif num_stability <= 9:
            f.writelines("\nQuite Unstable: this Chapter's gene-seed is significantly less stable than what is average."
                         " New flaws, deficiencies and mutations are common, particularly when used to found a new"
                         " Chapter, and sufficiently frequent to be considered a considerable issue.")
        elif num_stability <= 10:
            f.writelines("\nVery Unstable: this Chapter's gene-seed is unstable. New flaws, deficiencies and mutations"
                         " are widespread, particularly when used to found a new Chapter, if such a thing will ever be"
                         " considered.")

        f.writelines("\n")

        # The following code defines the Chapter's Demeanor

        f.writelines("\n    Chapter Demeanor")
        num_demeanor = random.randint(1, 34)
        print("Demeanor Roll:")
        print(num_demeanor)
        if num_demeanor <= 1:
            f.writelines("\nAudacious: this Chapter prides itself on its willingness to make bold decisions and perform"
                         " daring actions; some, however, may call it recklessness.")
        elif num_demeanor <= 2:
            f.writelines("\nMeticulous: this Chapter is well-known for its thorough approach to any given situation,"
                         " though detractors may argue it can be to a fault.")
        elif num_demeanor <= 3:
            f.writelines("\nCallous: this Chapter is famous (or infamous) for its indifference to suffering, whether"
                         " it be their own, that of their enemies, or that of their allies.")
        elif num_demeanor <= 4:
            f.writelines("\nTactical: this Chapter regards the proverbial 'small picture' to be paramount. Accordingly,"
                         " their focus in battle is largely on tactical movements, possibly at the risk of ignoring"
                         " grander elements.")
        elif num_demeanor <= 5:
            f.writelines("\nStrategic: this Chapter regards the proverbial 'big picture' to be paramount. Accordingly,"
                         " their focus in battle is largely on strategic movements, possibly at the risk of ignoring"
                         " more minute elements.")
        elif num_demeanor <= 6:
            f.writelines("\nCunning: this Chapter emphasizes the necessity of cleverness. While it serves them well,"
                         " both on the battlefield and in the politics of the Adeptus Astartes and the wider Imperium"
                         " alike, this guile might lead some to view them as scheming, or downright untrustworthy.")
        elif num_demeanor <= 7:
            f.writelines("\nZealous: this Chapter pursues every task with a level of fervor uncommon even among"
                         " Astartes. Such is their drive and certainty in their actions that it may blind them to"
                         " alternatives.")
        elif num_demeanor <= 8:
            f.writelines("\nRelentless: this Chapter has been known to pursue a given task with such adamant "
                         "stubbornness that they have been compared to an unstoppable force. Some may wonder what "
                         "happens if they meet an immovable object. Others may call them inflexible.")
        elif num_demeanor <= 9:
            f.writelines("\nRepentless: this Chapter has never been known to apologize, viewing such a thing as beneath"
                         " them. While some appreciate such dedication and willingness to stand by their every action,"
                         " others may chafe under perceived arrogance.")
        elif num_demeanor <= 10:
            f.writelines("\nImperial: this Chapter, more so than most of their peers, are dedicated to the expansion of"
                         " the Imperium and the vision of the Emperor. This may come at the expense of other concerns,"
                         " and some may question their interpretation of the Emperor's vision.")
        elif num_demeanor <= 11:
            f.writelines("\nPenitent: this Chapter has a considerable focus on repentance - typically their own. While"
                         " their endeavors to right wrongs they have done are admirable, some might argue they have a"
                         " tendency to exaggerate a given situation.")
        elif num_demeanor <= 12:
            f.writelines("\nHonorable: this Chapter holds honor in high regard, although some may call it an obsession."
                         " They exist by some code or another, whether of their own making or one given to them; any"
                         " breach of this code, whether by themselves or a third party, is seen as unacceptable.")
        elif num_demeanor <= 13:
            f.writelines("\nHonest: this Chapter cannot tell a lie, for one reason or another. While some will"
                         " appreciate their sincerity, others might consider them neurotic in their obsession with"
                         " honesty. Others again might point out that lies can be avoided by telling technical or"
                         " half-truths... or by absolute silence.")
        elif num_demeanor <= 14:
            f.writelines("\nCalm: this Chapter is known to be very slow to stir, possessing an overabundance of "
                         "patience. Lauded by some for this trait, others may consider them placid or even "
                         "lackadaisical.")
        elif num_demeanor <= 15:
            f.writelines("\nIrate: this Chapter is known to be very quick to stir, possessing a shortage of patience."
                         " While some might argue they're simply decisive and bold, others may instead consider them"
                         " reckless and prone to outbursts.")
        elif num_demeanor <= 16:
            f.writelines("\nMorose: this Chapter is prone to dour moods, often paying excessive attention to the"
                         " negatives of a given situation. Some consider them realists, but many consider them "
                         "pessimists.")
        elif num_demeanor <= 17:
            f.writelines("\nJovial: this Chapter is widely considered good-natured, even sociable by Astartes "
                         "standards. Although this makes them many friends, there are those who deride them as naive"
                         " and even flippant.")
        elif num_demeanor <= 18:
            f.writelines("\nDire: this Chapter possessed of a grim determination, and a penchant for stoicism besides."
                         " Thought to be steadfast and reliable by some, others may decry them as a dismal lot whose"
                         " moods are altogether disheartening.")
        elif num_demeanor <= 19:
            f.writelines("\nSecretive: this Chapter values privacy and secrecy, none more so than their own. Certainly"
                         " a great boon insofar as operational security is concerned, some may find them difficult to"
                         " trust, given their furtive nature.")
        elif num_demeanor <= 20:
            f.writelines("\nUnyielding: this Chapter is uncompromising, possessing a determination so thoroughly"
                         " impenetrable that rumors hold they have never once retreated. True or not, they certainly"
                         " are implacable, even if detractors may prefer to call them obstinate.")
        elif num_demeanor <= 21:
            f.writelines("\nParanoid: this Chapter is often charitably described as unreasonable due to their "
                         "suspicious nature. Others might instead consider them mad, always expecting the worst, even"
                         " from their allies, though such accusations will seldom be forthcoming when face-to-face.")
        elif num_demeanor <= 22:
            f.writelines("\nInquisitive: this Chapter this Chapter is both skillful in information gathering, and "
                         "possessed of a drive to do so. Praised by some for their dedication to such intelligence, "
                         "others may consider them nosey at best, and a threat at worst.")
        elif num_demeanor <= 23:
            f.writelines("\nSoft-hearted: this Chapter possesses a great affinity for the civilian population of the"
                         " Imperium, often going to great extents to safeguard them, and perhaps even interact with "
                         "them. Many praise this altruism, although detractors may consider them weak, and may even "
                         "question their dedication to waging war as Astartes ought.")
        elif num_demeanor <= 24:
            f.writelines("\nHard-hearted: this Chapter has little care for the civilian population of the Imperium, "
                         "often pre-emptively writing off their presence in theatres of war as acceptable casualties. "
                         "Condemned by many for being so dismissive, others praise them for their perceived "
                         "pragmatism.")
        elif num_demeanor <= 25:
            f.writelines("\nIndustrious: this Chapter has little care for anything other than their own work and "
                         "endeavors. Although unconfirmed rumors hold that they spend what precious little time "
                         "Astartes are afforded for free time on more practical pursuits, it certainly is known that "
                         "they never rest until their work is done. It is said Astartes know no fear, but these in "
                         "particular may fear a task left unfinished.")
        elif num_demeanor <= 26:
            f.writelines("\nSpiritual: this Chapter dedicates an extraordinary amount of time to matters of reverence. "
                         "Certainly well-received by others of similar inclinations, others may deride them as "
                         "misguided, or even superstitious.")
        elif num_demeanor <= 27:
            f.writelines("\nMundane: this Chapter cares little for matters of spirituality, religion and the like. "
                         "Certainly well-received by others of similar inclinations, others may deride them as "
                         "irreverent, or even profane.")
        elif num_demeanor <= 28:
            f.writelines("\nGenealogical: this Chapter places great importance on, and has great interest in, matters "
                         "of ancestry, particularly their own. This may border on obsessive behavior, leading some to "
                         "consider them lost in the past, while others may praise them for their record keeping and "
                         "reverence for history.")
        elif num_demeanor <= 29:
            f.writelines("\nShameful: this Chapter believes itself disgraced. Whether true or merely perceived, they "
                         "may either go to great lengths to rectify whatever transpired to cause this state of mind, "
                         "or take great care to hide it from outsiders - perhaps even from their own brothers.")
        elif num_demeanor <= 30:
            f.writelines("\nLogistical: this Chapter is deeply fascinated by the bureaucratic web of supply lines. "
                         "This, in turn, has lead to significant proficiency in such matters, although some may "
                         "disparage such endeavors as unworthy of Astartes warriors and better left to mortal humans.")
        elif num_demeanor <= 31:
            f.writelines("\nLogical: this Chapter is deeply fascinated by systems of logic. Endeavoring to create a "
                         "system by which all things might be organised is certainly impressive, particularly to the "
                         "Tech-Priests of Mars, to whom others may instead believe such matters should be reserved.")
        elif num_demeanor <= 32:
            f.writelines("\nProud: this Chapter is well-known for taking great pleasure in its own accomplishments. "
                         "While many will agree that such pride has been earned, others may instead find them arrogant."
                         " They certainly do not suffer insults to their achievements lightly.")
        elif num_demeanor <= 33:
            f.writelines("\nHumble: this Chapter is well-known for placing little import on honor rolls and the "
                         "recording of deeds, although such records are still made and kept. Some view this as a "
                         "virtue, while others may consider these Astartes timid.")
        elif num_demeanor <= 34:
            f.writelines("\nPerfectionist: this Chapter is famous, or infamous, for its pursuit of perfection. While"
                         " certainly a useful trait insofar as their prowess is concerned, these Astartes are "
                         "nonetheless known to fall victim to malaise, or even anger, if they consider their deeds "
                         "and endeavors insufficient.")

        f.writelines("\n")

        # The following code defines the Chapter's quirks

        num_quirky_chapter = random.randint(1, 20)
        print("Quirky Chapter Roll:")
        print(num_quirky_chapter)
        f.writelines("\n    Chapter Quirks")
        if num_quirky_chapter <= 16:
            function_chapter_quirks()
            Chapter_Quirk_1 = Chapter_Quirk_Base
        elif num_quirky_chapter <= 18:
            function_chapter_quirks()
            Chapter_Quirk_1 = Chapter_Quirk_Base
            function_chapter_quirks()
            Chapter_Quirk_2 = Chapter_Quirk_Base
        elif num_quirky_chapter <= 20:
            function_chapter_quirks()
            Chapter_Quirk_1 = Chapter_Quirk_Base
            function_chapter_quirks()
            Chapter_Quirk_2 = Chapter_Quirk_Base
            function_chapter_quirks()
            Chapter_Quirk_3 = Chapter_Quirk_Base

        f.writelines("\n")

        # The following code defines the Chapter's Legend

        f.writelines("\n    Legendary Figure")
        num_legend_figure = random.randint(1, 130)
        print("Legendary Figure Roll:")
        print(num_legend_figure)
        if num_legend_figure <= 20:
            f.writelines("\nA Founding Chapter member:")
            num_founding_legend = random.randint(21, 130)
            print("Founding Legend Roll:")
            print(num_founding_legend)
            if num_founding_legend <= 40:
                f.writelines(" Chapter Master, or equivalent.")
                Legendary_Figure = "Chapter Master"
            elif num_founding_legend <= 50:
                num_founding_champ_select_1 = random.randint(1, 2)
                print("Founding Champion Roll:")
                print(num_founding_champ_select_1)
                if num_founding_champ_select_1 == 1:
                    f.writelines(" Chapter Champion, or equivalent.")
                elif num_founding_champ_select_1 == 2:
                    num_founding_champ_select_2 = random.randint(1, 10)
                    print("Founding Champion Company Roll:")
                    print(num_founding_champ_select_2)
                    if num_founding_champ_select_2 == 1:
                        f.writelines(" 1st Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 2:
                        f.writelines(" 2nd Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 3:
                        f.writelines(" 3rd Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 4:
                        f.writelines(" 4th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 5:
                        f.writelines(" 5th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 6:
                        f.writelines(" 6th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 7:
                        f.writelines(" 7th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 8:
                        f.writelines(" 8th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 9:
                        f.writelines(" 9th Company Champion, or equivalent.")
                    elif num_founding_champ_select_2 == 10:
                        f.writelines(" 10th Company Champion, or equivalent.")
                Legendary_Figure = "Champion"
            elif num_founding_legend <= 60:
                f.writelines(" Librarian, or equivalent.")
                Legendary_Figure = "Librarian"
            elif num_founding_legend <= 70:
                f.writelines(" Chaplain, or equivalent.")
                Legendary_Figure = "Chaplain"
            elif num_founding_legend <= 80:
                f.writelines(" Techmarine, or equivalent.")
                Legendary_Figure = "Techmarine"
            elif num_founding_legend <= 90 and Founding == "Ultima Founding":
                f.writelines(" Lieutenant, or equivalent.")
                Legendary_Figure = "Lieutenant"
            elif num_founding_legend <= 100:
                f.writelines(" Force Commander, or equivalent.")
                Legendary_Figure = "Force Commander"
            elif num_founding_legend <= 110:
                f.writelines(" Apothecary, or equivalent.")
                Legendary_Figure = "Apothecary"
            elif num_founding_legend <= 120:
                num_founding_cpt_select = random.randint(1, 10)
                print("Founding Captain Roll:")
                print(num_founding_cpt_select)
                if num_founding_cpt_select == 1:
                    f.writelines(" 1st Company Captain, or equivalent.")
                elif num_founding_cpt_select == 2:
                    f.writelines(" 2nd Company Captain, or equivalent.")
                elif num_founding_cpt_select == 3:
                    f.writelines(" 3rd Company Captain, or equivalent.")
                elif num_founding_cpt_select == 4:
                    f.writelines(" 4th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 5:
                    f.writelines(" 5th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 6:
                    f.writelines(" 6th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 7:
                    f.writelines(" 7th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 8:
                    f.writelines(" 8th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 9:
                    f.writelines(" 9th Company Captain, or equivalent.")
                elif num_founding_cpt_select == 10:
                    f.writelines(" 10th Company Captain, or equivalent.")
                Legendary_Figure = "Captain"
            elif num_founding_legend <= 130:
                f.writelines(" Dreadnought, or equivalent.")
                Legendary_Figure = "Dreadnought"
            elif num_founding_legend <= 135:
                f.writelines(" Sergeant, or equivalent.")
                Legendary_Figure = "Sergeant"
            elif num_founding_legend <= 138:
                f.writelines(" Battle-Brother, or equivalent.")
                Legendary_Figure = "Battle-Brother"
            elif num_founding_legend == 140:
                f.writelines(" A Chapter member of your choice.")
        elif num_legend_figure <= 40:
            f.writelines("\nChapter Master, or equivalent.")
            Legendary_Figure = "Chapter Master"
        elif num_legend_figure <= 50:
            num_champ_select_1 = random.randint(1, 2)
            print("Champion Roll:")
            print(num_champ_select_1)
            if num_champ_select_1 == 1:
                f.writelines("\nChapter Champion, or equivalent.")
            elif num_champ_select_1 == 2:
                num_champ_select_2 = random.randint(1, 10)
                print("Champion Company Roll:")
                print(num_champ_select_2)
                if num_champ_select_2 == 1:
                    f.writelines("\n1st Company Champion, or equivalent.")
                elif num_champ_select_2 == 2:
                    f.writelines("\n2nd Company Champion, or equivalent.")
                elif num_champ_select_2 == 3:
                    f.writelines("\n3rd Company Champion, or equivalent.")
                elif num_champ_select_2 == 4:
                    f.writelines("\n4th Company Champion, or equivalent.")
                elif num_champ_select_2 == 5:
                    f.writelines("\n5th Company Champion, or equivalent.")
                elif num_champ_select_2 == 6:
                    f.writelines("\n6th Company Champion, or equivalent.")
                elif num_champ_select_2 == 7:
                    f.writelines("\n7th Company Champion, or equivalent.")
                elif num_champ_select_2 == 8:
                    f.writelines("\n8th Company Champion, or equivalent.")
                elif num_champ_select_2 == 9:
                    f.writelines("\n9th Company Champion, or equivalent.")
                elif num_champ_select_2 == 10:
                    f.writelines("\n10th Company Champion, or equivalent.")
            Legendary_Figure = "Champion"
        elif num_legend_figure <= 60:
            f.writelines("\nLibrarian, or equivalent.")
            Legendary_Figure = "Librarian"
        elif num_legend_figure <= 70:
            f.writelines("\nChaplain, or equivalent.")
            Legendary_Figure = "Chaplain"
        elif num_legend_figure <= 80:
            f.writelines("\nTechmarine, or equivalent.")
            Legendary_Figure = "Techmarine"
        elif num_legend_figure <= 90 and Primaris_Reinforcements == "Yes" or Founding == "Ultima Founding":
            f.writelines("\nLieutenant, or equivalent.")
            Legendary_Figure = "Lieutenant"
        elif num_legend_figure <= 100:
            f.writelines("\nForce Commander, or equivalent.")
            Legendary_Figure = "Force Commander"
        elif num_legend_figure <= 110:
            f.writelines("\nApothecary, or equivalent.")
            Legendary_Figure = "Apothecary"
        elif num_legend_figure <= 120:
            num_cpt_select = random.randint(1, 10)
            print("Captain Roll:")
            print(num_cpt_select)
            if num_cpt_select == 1:
                f.writelines("\n1st Company Captain, or equivalent.")
            elif num_cpt_select == 2:
                f.writelines("\n2nd Company Captain, or equivalent.")
            elif num_cpt_select == 3:
                f.writelines("\n3rd Company Captain, or equivalent.")
            elif num_cpt_select == 4:
                f.writelines("\n4th Company Captain, or equivalent.")
            elif num_cpt_select == 5:
                f.writelines("\n5th Company Captain, or equivalent.")
            elif num_cpt_select == 6:
                f.writelines("\n6th Company Captain, or equivalent.")
            elif num_cpt_select == 7:
                f.writelines("\n7th Company Captain, or equivalent.")
            elif num_cpt_select == 8:
                f.writelines("\n8th Company Captain, or equivalent.")
            elif num_cpt_select == 9:
                f.writelines("\n9th Company Captain, or equivalent.")
            elif num_cpt_select == 10:
                f.writelines("\n10th Company Captain, or equivalent.")
            Legendary_Figure = "Captain"
        elif num_legend_figure <= 130:
            f.writelines("\nDreadnought, or equivalent.")
            Legendary_Figure = "Dreadnought"
        elif num_legend_figure <= 135:
            f.writelines("\nSergeant, or equivalent.")
            Legendary_Figure = "Sergeant"
        elif num_legend_figure <= 138:
            f.writelines("\nBattle-Brother, or equivalent.")
            Legendary_Figure = "Battle-Brother"
        elif num_legend_figure == 140:
            f.writelines("\nA Chapter member of your choice.")

        f.writelines("\n")

        # The following code defines the deeds of the Chapter's Legend

        f.writelines("\n    Legendary Deeds")
        num_legend_deeds = random.randint(1, 201)
        print("Legendary Deed Roll:")
        print(num_legend_deeds)
        if num_legend_deeds <= 15:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the foul orks.")
            num_ork_deeds = random.randint(1, 100)
            print("Ork Deeds Roll:")
            print(num_ork_deeds)
            if num_ork_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many greenskins across so many"
                             " battlefields that some among the repulsive xenos themselves have become familiar with"
                             " his name.")
            elif num_ork_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he foiled the plans of enough Warbosses that a wealth of"
                             " bounties were placed on his head. Freebootaz tell stories about failed attempts to "
                             "claim it.")
            elif num_ork_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he was instrumental in putting such a grinding halt to a "
                             "Waaagh! that the resulting infighting over who was to blame lead directly to its "
                             "dissolution into warring factions.")
            elif num_ork_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he single-handedly felled a Gargant. Apocryphal stories are "
                             "told by allies about how a lone Astartes boarded the colossal machine and did not emerge"
                             " until it was destroyed.")
            elif num_ork_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the greenskins so many times that a"
                             " persisting rumor now holds that he is deathless. Some among their number have taken to"
                             " telling stories of dread about his impending return, even in the absence of his "
                             "Chapter.")
        elif num_legend_deeds <= 30:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the perfidious eldar.")
            num_eldar_deeds = random.randint(1, 100)
            print("Eldar Deeds Roll:")
            print(num_eldar_deeds)
            if num_eldar_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many eldar across so many battlefields"
                             " that some among the deceitful xenos themselves have become familiar with his name.")
            elif num_eldar_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he interrupted so many prophecies that some Farseers have come"
                             " to suspect that he is somehow beyond their sight or means of intervention.")
            elif num_eldar_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he was instrumental in stopping so many drukhari slave raids"
                             " that various Kabals began blaming one another for somehow being responsible for his"
                             " presence, allegedly to sabotage their rivals. The ensuing infighting crippled their"
                             " operations for a considerable time.")
            elif num_eldar_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he was directly responsible for the harming of an exodite "
                             "World Spirit. This monumental blow to their society, pride and spiritual well-being "
                             "earned him the eternal ire of that world's exodites, and likely any Craftworld "
                             "benefactors they might have.")
            elif num_eldar_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the eldar so many times that a "
                             "persisting rumor now holds that he is deathless. Some among their number have taken to "
                             "telling stories of dread about his impending return, even in the absence of his Chapter.")
        elif num_legend_deeds <= 45:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the vile tyranids.")
            num_tyranid_deeds = random.randint(1, 100)
            print("Tyranid Deeds Roll:")
            print(num_tyranid_deeds)
            if num_tyranid_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many tyranids across so many "
                             "battlefields that some among the ravenous xenos themselves have become familiar with him "
                             "on some instinctive level.")
            elif num_tyranid_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he was instrumental in halting the invasion and preventing the"
                             " subsequent consumption of an Imperial world. The surviving populace hailed him as their"
                             " savior.")
            elif num_tyranid_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he hunted down and destroyed a plethora of Genestealer Cults,"
                             " ending their sinister plans of rebellion. Depending on the brutality of the purges, the"
                             " local populaces may remember him as a necessary evil.")
            elif num_tyranid_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he cleansed a space hulk of its genestealer infestation, "
                             "aboard which he was thought lost when it disappeared into the Warp. When it reappeared, "
                             "his was the only life sign detected aboard.")
            elif num_tyranid_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was assumed dead by the tyranids so many times that some"
                             " base instinct now seems to hold that he is deathless. Some among their number have taken"
                             " to making sure their prey is dead, even in the absence of his Chapter.")
        elif num_legend_deeds <= 60:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the upstart tau.")
            num_tau_deeds = random.randint(1, 100)
            print("Tau Deeds Roll:")
            print(num_tau_deeds)
            if num_tau_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many tau across so many battlefields"
                             " that some among the ignorant xenos themselves have become familiar with his name.")
            elif num_tau_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he was responsible for the deaths of multiple ethereals, "
                             "demoralising their people. There has been no shortage of tau curses directed at him.")
            elif num_tau_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he wiped out an entire kroot Kindred. Others swore to hunt him"
                             " down and avenge their kin.")
            elif num_tau_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he was instrumental in a planetary invasion that saw local "
                             "Gue'vesa traitors purged and Imperial rule restored.")
            elif num_tau_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the tau so many times that a "
                             "persisting rumor now holds that he is deathless. Some among their number have taken to "
                             "telling stories of dread about his impending return, even in the absence of his Chapter.")
        elif num_legend_deeds <= 75:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the abominable necrons.")
            num_necron_deeds = random.randint(1, 100)
            print("Necron Deeds Roll:")
            print(num_necron_deeds)
            if num_necron_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many necrons across so many "
                             "battlefields that some among the aberrant xenos themselves have become familiar with his "
                             "name.")
            elif num_necron_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he recognised that if the monolith was destroyed, the battle "
                             "would be over. Field reports indicate that he led a charge against the xenos construct, "
                             "resulting in its annihilation.")
            elif num_necron_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he personally fought through a throng of immortals and slew "
                             "the Lord who was coordinating the battle. The subsequent victory was attributed to him.")
            elif num_necron_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he was responsible for the destruction of an entire Destroyer "
                             "Cult. The irony of the situation became something of a joke within the Chapter - at least"
                             " as far as Astartes humor goes.")
            elif num_necron_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the necrons so many times that a "
                             "persisting rumor now holds that he is deathless. Some among their number have taken to "
                             "making sure their enemies are dead, even in the absence of his Chapter.")
        elif num_legend_deeds <= 90:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the heretical minions of Chaos.")
            num_chaos_deeds = random.randint(1, 100)
            print("Chaos Deeds Roll:")
            print(num_chaos_deeds)
            if num_chaos_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many of them across so many "
                             "battlefields that some among the contemptible heretics themselves have become familiar "
                             "with his name.")
            elif num_chaos_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he hunted down and destroyed a plethora of cults dedicated to"
                             " the ruinous powers, ending their heretical plans of rebellion. Depending on the "
                             "brutality of the purges, the local populaces may remember him as a necessary evil.")
            elif num_chaos_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he so thoroughly foiled the plans of a Chaos Lord. The failure"
                             " was so absolute that the Lord was punished for his shortcomings by being transformed "
                             "into a gibbering, witless Chaos Spawn.")
            elif num_chaos_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he personally slew a daemon prince")
                num_daemon_prince_god = random.randint(1, 41)
                print("Daemon Prince God Roll:")
                print(num_daemon_prince_god)
                if num_daemon_prince_god <= 10:
                    f.writelines(" of Khorne")
                elif num_daemon_prince_god <= 20:
                    f.writelines(" of Tzeentch")
                elif num_daemon_prince_god <= 30:
                    f.writelines(" of Nurgle")
                elif num_daemon_prince_god <= 40:
                    f.writelines(" of Slaanesh")
                elif num_daemon_prince_god <= 41:
                    f.writelines(" of Chaos Undivided")
                f.writelines(", banishing it back to the Warp and ending the threat it posed for numerous generations.")
            elif num_chaos_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the followers of Chaos so many times"
                             " that a persisting rumor now holds that he is deathless. Some among their number have "
                             "taken to telling stories of dread about his impending return, even in the absence of his"
                             " Chapter.")
        elif num_legend_deeds <= 100:
            f.writelines("\nThis Astartes is remembered for his dedication to battling the misguided humans from "
                         "non-Imperial factions.")
            num_rebel_deeds = random.randint(1, 100)
            print("Rebel Deeds Roll:")
            print(num_rebel_deeds)
            if num_rebel_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally killed so many of them across so many "
                             "battlefields that the dissidents themselves have become familiar with his name.")
            elif num_rebel_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he was instrumental in the defeat of a rebel uprising, "
                             "preventing their secession from the Imperium.")
            elif num_rebel_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he was responsible for bringing a hitherto undiscovered lesser"
                             " human empire into the light of the Emperor, absorbing it into the Imperium.")
            elif num_rebel_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he discovered the existence of a human-xenos alliance that had"
                             " gone unnoticed until then. The humans were punished for their betrayal of human "
                             "supremacy. The xenos were exterminated.")
            elif num_rebel_deeds <= 100:
                f.writelines("\nAcross numerous conflicts, he was reported dead by the dissenters so many times that a"
                             " persisting rumor now holds that he is deathless. Some among their number have taken to "
                             "telling stories of dread about his impending return, even in the absence of his Chapter.")
        elif num_legend_deeds <= 115:
            f.writelines("\nThis Astartes is remembered for his dedication to upholding the Chapter's honor.")
            num_honor_deeds = random.randint(1, 100)
            print("Honor Deeds Roll:")
            print(num_honor_deeds)
            if num_honor_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally recovered a standard of the Chapter that had "
                             "long been lost to the enemy.")
            elif num_honor_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he slew a sworn enemy of the Chapter in single combat, "
                             "settling a grudge and ending a long-standing rivalry.")
            elif num_honor_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he was instrumental in recovering a land raider that was "
                             "thought to have been lost, or even destroyed.")
            elif num_honor_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he was directly responsible for lifting a siege of the "
                             "Chapter's Fortress-Monastery, preventing its destruction, or worse, desecration.")
            elif num_honor_deeds <= 100:
                f.writelines("\nAmong other heroic acts, he personally recovered a suit of terminator armor that had "
                             "long been absent from the Chapter's armory.")
            elif num_honor_deeds <= 110:
                f.writelines("\nAmong other heroic acts, he helped hunt down and kill a number of traitorous brothers "
                             "who had gone renegade, or worse, fallen to the Ruinous Powers.")
            elif num_honor_deeds <= 120:
                f.writelines("\nAmong other heroic acts, he was instrumental in recovering an amount of precious "
                             "gene-seed that was thought to have been lost, or even destroyed.")
            elif num_honor_deeds <= 130:
                f.writelines("\nAmong other heroic acts, he was instrumental in the preservation of an amount of "
                             "Chapter lore, which would otherwise have been lost.")
        elif num_legend_deeds <= 130:
            f.writelines("\nThis Astartes is remembered for his dedication to the people of the Imperium.")
            num_imperium_deeds = random.randint(1, 100)
            print("Imperium Deeds Roll:")
            print(num_imperium_deeds)
            if num_imperium_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he personally retrieved a vital replacement component, "
                             "instrumental in the continued operation of a hive city, as well as the survival of its "
                             "inhabitants.")
            elif num_imperium_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he was directly responsible for enduring a siege laid against "
                             "a hive city, as well as subsequently repulsing the attack and scattering the enemy before"
                             " the city's walls.")
            elif num_imperium_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he once stood alone between a civilian shelter and the enemies"
                             " of the Imperium. The Chapter maintains he held this position for at least 20 hours, "
                             "without pause.")
            elif num_imperium_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he was instrumental in staging a fighting retreat when battle "
                             "lines collapsed, which bought time for a civilian evacuation and ensured the survival of "
                             "countless non-combatants.")
            elif num_imperium_deeds <= 100:
                f.writelines("\nAmong other heroic acts, he helped rebuild planetary infrastructure following a "
                             "particularly destructive war.")
        elif num_legend_deeds <= 145:
            f.writelines("\nThis Astartes is remembered as an accomplished warrior.")
            num_warrior_deeds = random.randint(1, 100)
            print("Warrior Deeds Roll:")
            print(num_warrior_deeds)
            if num_warrior_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he spent countless hours familiarising himself with the "
                             "Chapter's arsenal, eventually mastering every weapon in the armory, a feat not achieved "
                             "by his brothers before or since.")
            elif num_warrior_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he slew countless enemy champions across his lifetime. "
                             "Occasionally, such feats would effectively end a battle prematurely, as his victory "
                             "bolstered the morale of his allies, while crushing that of his foes.")
            elif num_warrior_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he spent countless hours familiarising himself with his weapon"
                             " of choice, eventually mastering it to a degree that was unparalleled in the Chapter. "
                             "Some hold that he is unsurpassed to this day.")
            elif num_warrior_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he fought in more battles than anyone else in the Chapter, "
                             "seeing deployment on a myriad worlds across innumerable theaters.")
            elif num_warrior_deeds <= 100:
                f.writelines("\nAmong other heroic acts, the Chapter claims he never once suffered an injury in battle."
                             " Whether through skill or luck, the legend persists, although outsiders are typically "
                             "skeptical of these claims.")
        elif num_legend_deeds <= 160:
            f.writelines("\nThis Astartes is remembered as an inspiring leader.")
            num_leader_deeds = random.randint(1, 100)
            print("Leader Deeds Roll:")
            print(num_leader_deeds)
            if num_leader_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he roused his battle brothers to perform great deeds against "
                             "insurmountable odds across many battles, turning the tide in an otherwise bleak "
                             "situation.")
            elif num_leader_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he roused mortal warriors to perform great deeds against "
                             "insurmountable odds across many battles, turning the tide in an otherwise bleak "
                             "situation.")
            elif num_leader_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he served on the leading council of an Imperial crusade. His"
                             " counsel directly resulted in countless battles, and some might argue he was largely "
                             "responsible for the crusade's success.")
            elif num_leader_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he wrote a treatise on strategy. Although not comparable in "
                             "scope or complexity to the Codex Astartes, it was nonetheless comprehensive, and is still"
                             " used by the Chapter to this day.")
            elif num_leader_deeds <= 100:
                f.writelines("\nAmong other heroic acts, the Chapter claims he once won a battle with words alone, "
                             "convincing the enemy to surrender without a fight.")
        elif num_legend_deeds <= 175:
            f.writelines("\nThis Astartes is remembered as a paragon of his craft.")
            print("Paragon Deeds Roll:")
            print(Legendary_Figure)
            if Legendary_Figure == "Chapter Master":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient Chapter"
                             " Masters in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable leadership skills.")
            elif Legendary_Figure == "Champion":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Champions in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable duelling skills.")
            elif Legendary_Figure == "Librarian":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Librarians in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable knowledge of the eldritch and arcane.")
            elif Legendary_Figure == "Chaplain":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Chaplains in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable oratory skills.")
            elif Legendary_Figure == "Techmarine":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Techmarines in its history. Those who follow in his footsteps will inevitably be measured"
                             " against his considerable mastery of machines and cogitators.")
            elif Legendary_Figure == "Force Commander":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient Force "
                             "Commanders in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable leadership skills.")
            elif Legendary_Figure == "Apothecary":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Apothecaries in its history. Those who follow in his footsteps will inevitably be "
                             "measured against his considerable medical knowledge and healing skills.")
            elif Legendary_Figure == "Captain":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient Captains"
                             " in its history. Those who follow in his footsteps will inevitably be measured against "
                             "his considerable leadership skills.")
            elif Legendary_Figure == "Dreadnought":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Dreadnoughts in its history. Those who follow in his footsteps will inevitably be "
                             "measured against his considerable historical knowledge and martial skills.")
            elif Legendary_Figure == "Sergeant":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Sergeants in its history. Those who follow in his footsteps will inevitably be measured "
                             "against his considerable leadership skills.")
            elif Legendary_Figure == "Battle-Brother":
                f.writelines("\nAmong other heroic acts, his Chapter holds him to be among the most proficient "
                             "Battle-Brothers in its history. Those who follow in his footsteps will inevitably be "
                             "measured against his considerable martial skills.")
        elif num_legend_deeds <= 200:
            f.writelines("\nThis Astartes is remembered for having recovered an STC fragment.")
            num_stc_fragment_deeds = random.randint(1, 100)
            print("STC Fragment Deeds Roll:")
            print(num_stc_fragment_deeds)
            if num_stc_fragment_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a barely functional "
                             "fragment of a Standard Template Construct. However, a barely functional STC fragment is "
                             "still a considerable boon.")
            elif num_stc_fragment_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a mostly functional "
                             "fragment of a Standard Template Construct. Although not fully functional, any STC "
                             "fragment is still a considerable boon.")
            elif num_stc_fragment_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a functional fragment of"
                             " a Standard Template Construct. While not a complete STC, a fragment of one is still a "
                             "considerable boon.")
            elif num_stc_fragment_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a pristine fragment of a "
                             "Standard Template Construct. While not a complete STC, this fragment is almost "
                             "immaculate, representing a considerable boon.")
            elif num_stc_fragment_deeds <= 100:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, multiple fragments of a "
                             "Standard Template Construct of varying quality. Finding one is extraordinary, but finding"
                             " multiple is particularly rare.")
        elif num_legend_deeds <= 201:
            f.writelines("\nThis Astartes is remembered for having recovered a full STC.")
            num_full_stc_deeds = random.randint(1, 100)
            print("Full STC Deeds Roll")
            print(num_full_stc_deeds)
            if num_full_stc_deeds <= 20:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a barely functional "
                             "Standard Template Construct. However, a barely functional STC is still an incomparable "
                             "boon.")
            elif num_full_stc_deeds <= 40:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a mostly functional "
                             "Standard Template Construct. Although not fully functional, any STC is still an "
                             "incomparable boon.")
            elif num_full_stc_deeds <= 60:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a functional Standard "
                             "Template Construct. Such a discovery represents an incomparable boon.")
            elif num_full_stc_deeds <= 80:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a pristine Standard "
                             "Template Construct. This STC is almost immaculate, representing an incomparable boon.")
            elif num_full_stc_deeds <= 100:
                f.writelines("\nAmong other heroic acts, he managed to discover, and recover, a multiple Standard "
                             "Template Constructs of varying quality. Finding one is almost unheard of, but finding "
                             "multiple is incomprehensibly rare.")

        f.writelines("\n")

        # The following code defines the fate of the legend

        f.writelines("\n    Legendary Figure's Fate")
        num_legend_fate = random.randint(1, 21)
        print("Legend Fate Roll:")
        print(num_legend_fate)
        if num_legend_fate <= 10:
            f.writelines("\nDead: no man lives forever, even among the Adeptus Astartes. Whether by the hands of the "
                         "Chapter's enemies, due to some catastrophe, or something else entirely, he no longer lives.")
        elif num_legend_fate <= 15:
            f.writelines("\nMissing: having vanished without a trace, many outside the Chapter have written him off as "
                         "dead. However, his brothers claim he yet lives, and may even believe he will return.")
        elif num_legend_fate <= 20:
            f.writelines("\nAlive: undeterred by age, wounds and foes, he still serves within the Chapter to this very "
                         "day.")
        elif num_legend_fate <= 21:
            f.writelines("\nTraitor: it happens on occasion that Astartes must either die, lest they live long enough "
                         "to betray their brothers. Whether falling to Chaos or simply going rogue as a renegade "
                         "Astartes, whatever the reason might have been, he turned his back on the Chapter, and may "
                         "even have taken others with him.")

        f.writelines("\n")

        # The following code defines the Chapter's Homeworld

        f.writelines("\n    Chapter Homeworld")
        num_chapter_homeworld = random.randint(1, 100)
        print("Homeworld Roll:")
        print(num_chapter_homeworld)
        if num_chapter_homeworld <= 15:
            function_homeworld_modifier()
            f.writelines("Hive World: this Chapter's homeworld is the site of numerous hive cities, each home to "
                         "billions of Imperial citizens, spanning entire continents.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 30:
            function_homeworld_modifier()
            f.writelines("Civilised World: this Chapter's homeworld is not dissimilar to Old Earth during the Age of "
                         "Terra, in and around the 3rd millennium.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 60:
            function_homeworld_modifier()
            f.writelines("Feudal World: this Chapter's homeworld has not yet developed past a medieval stage, whether "
                         "by design or by chance, although it may exist amidst the ruins of a more technologically "
                         "advanced civilisation.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 70:
            function_homeworld_modifier()
            f.writelines("Fortress World: this Chapter's homeworld has been transformed into a virtually unassailable "
                         "stronghold. Even beyond the Fortress-Monastery, planetary defences are both extensive and "
                         "vast.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 80:
            function_homeworld_modifier()
            f.writelines("Death World: this Chapter's homeworld is entirely hostile to human life. This may be limited "
                         "to the biosphere, but can also include the entirety of the planetary environment in one way "
                         "or another.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 90:
            function_homeworld_modifier()
            f.writelines("Armory World: this Chapter's homeworld is home to a vast store of arms, armor and munitions, "
                         "some of it new, some of it ancient.")
            function_homeworld_modifier_text()
            function_homeworld_rule()
        elif num_chapter_homeworld <= 100:
            f.writelines("\nFleet-based: this Chapter, whether or not by choice, has no homeworld. Instead, they roam "
                         "the stars aboard ~")
            num_fleet_size = str(random.randint(10 + 1, 10 + 10))
            print("Fleet Size Roll:")
            print(num_fleet_size)
            f.write(num_fleet_size)
            f.write(" ships. In most fleet-based Chapters, a battle-barge typically fills the role of "
                    "Fortress-Monastery.")
            num_unique_flagship = random.randint(10, 10)
            print("Unique Flagship Roll:")
            print(num_unique_flagship)
            if num_unique_flagship == 10:
                f.writelines("\nHowever, this Chapter makes use of a unique vessel instead of a 'standard' "
                             "battle-barge.")
            Homeworld = "Fleet-Based"

        f.writelines("\n")

        # The following code defines the Chapter's means of recruitment if fleet-based

        if Homeworld == "Fleet-Based":
            f.writelines("\n    Fleet-Based Recruitment")
            num_fleet_recruitment = random.randint(1, 8)
            print("Fleet Recruitment Roll:")
            print(num_fleet_recruitment)
            if num_fleet_recruitment <= 2:
                f.writelines("\nKeeps: this Chapter maintains a number of keeps throughout the Imperium, from which are"
                             " used to stage recruitment efforts.")
            elif num_fleet_recruitment <= 4:
                f.writelines("\nLocals: this Chapter draws its Aspirants from worlds they come across during their "
                             "voyage through the void, probably most frequently from worlds on which the Chapter has "
                             "been deployed.")
            elif num_fleet_recruitment <= 6:
                f.writelines("\nRecruitment Worlds: this Chapter has ")
                num_fleet_recruitment_worlds = random.randint(1, 14)
                print("Chapter Endangered Roll:")
                print(num_fleet_recruitment_worlds)
                if num_fleet_recruitment_worlds <= 5:
                    f.writelines("a recruitment world")
                elif num_fleet_recruitment_worlds <= 8:
                    f.writelines("two recruitment worlds")
                elif num_fleet_recruitment_worlds <= 11:
                    f.writelines("three recruitment worlds")
                elif num_fleet_recruitment_worlds <= 13:
                    f.writelines("four recruitment worlds")
                elif num_fleet_recruitment_worlds <= 14:
                    f.writelines("five recruitment worlds")
                f.writelines(" from which it can draw its Aspirants.")
            elif num_fleet_recruitment <= 8:
                f.writelines("\nShip Crews: this Chapter draws its Aspirant from ship crews, whether those manning its"
                             " own vessels, or from Imperial Navy vessels active in the same theater.")
            f.writelines("\n")

        # The following code defines the nature of the Chapter's Fortress-Monastery

        if Homeworld != "Fleet-Based":
            f.writelines("\n    Fortress-Monastery Type")
            num_monastery_type = random.randint(1, 20)
            print("Fortress-Monastery Type Roll:")
            print(num_monastery_type)
            if num_monastery_type <= 10:
                f.writelines("\nClassic Fortress: this Chapter's Fortress-Monastery is as 'normal' as such things get,"
                             " taking the form of a massive, static planetside fortification. In rare cases, it may "
                             "also be multiple such locations, though likely smaller in size. In even rarer cases, the "
                             "site, or sites, may be subterranean.")
            elif num_monastery_type <= 12:
                f.writelines("\nMobile Land Fortress: this Chapter's Fortress-Monastery is landbound and mobile, taking"
                             " the form of a great machine capable of moving across the planet's surface. In rare "
                             "cases, it may also be multiple such machines, though likely smaller in size. In even "
                             "rarer cases, the machine, or machines, may be subterranean.")
            elif num_monastery_type <= 14:
                f.writelines("\nMobile Air Fortress: this Chapter's Fortress-Monastery is aerial and mobile, taking the"
                             " form of a great machine capable of moving through the planet's skies. In rare cases, it "
                             "may also be multiple such machines, though likely smaller in size.")
            elif num_monastery_type <= 16 and Homeworld_Modifier != "Frozen" and Homeworld_Modifier != "Sunless":
                f.writelines("\nMobile Sea Fortress: this Chapter's Fortress-Monastery is nautical and mobile, taking "
                             "the form of a great machine capable of moving across the planet's seas. In rare cases, it"
                             " may also be multiple such machines, though likely smaller in size. In even rarer cases,"
                             " the machine, or machines, may be submersible.")
            elif num_monastery_type <= 18:
                f.writelines("\nRepurposed Voidship: this Chapter's Fortress-Monastery was built from the hull of a "
                             "voidship, likely having been previously active in the Chapter's own fleet. Whether it was"
                             " deliberately landed on the planet or crashed for one reason or another, its size may "
                             "range from a light cruiser to a battle-barge.")
            elif num_monastery_type <= 19:
                f.writelines("\nOrbital Space Station: this Chapter's Fortress-Monastery takes the form of a large "
                             "station orbiting their homeworld. In rare cases, it may also be multiple such orbital "
                             "structures, though likely smaller in size. In even rarer cases, the station, or stations,"
                             " may be capable of relocation by some means.")
            elif num_monastery_type <= 20:
                f.writelines("\nChoose something truly unusual.")
            f.writelines("\n")

        # The following code defines additional recruiting worlds

        if Homeworld != "Fleet-Based":
            num_additional_worlds = random.randint(1, 10)
            print("Additional Recruiting Worlds Roll:")
            print(num_additional_worlds)
            if num_additional_worlds <= 8:
                f.writelines("")
            elif num_additional_worlds <= 10:
                f.writelines("\n    Additional Recruiting Worlds")
                num_recruiting_world_number = random.randint(1, 14)
                print("Recruiting World Number Roll:")
                print(num_recruiting_world_number)
                if num_recruiting_world_number <= 5:
                    f.writelines("\nThis Chapter has one recruiting world in addition to its homeworld.")
                elif num_recruiting_world_number <= 8:
                    f.writelines("\nThis Chapter has two recruiting worlds in addition to its homeworld.")
                elif num_recruiting_world_number <= 11:
                    f.writelines("\nThis Chapter has three recruiting worlds in addition to its homeworld.")
                elif num_recruiting_world_number <= 13:
                    f.writelines("\nThis Chapter has four recruiting worlds in addition to its homeworld.")
                elif num_recruiting_world_number <= 14:
                    f.writelines("\nThis Chapter has five recruiting worlds in addition to its homeworld.")
                f.writelines("\n")

        # The following code defines the Chapter's Organisation

        f.writelines("\n    Organisation")
        if Progenitor_Chapter == "Ultramarines":
            num_chapter_org = random.randint(1, 11)
            print("Chapter Organisation Roll:")
            print(num_chapter_org)
            if num_chapter_org <= 7:
                f.writelines("\nThis Chapter adheres to the Codex Astartes")
                f.writelines("\n")
                f.writelines("\n    Codex Elements")
                function_codex_element()
            elif num_chapter_org <= 9:
                f.writelines("\nThis Chapter has somewhat diverged from the Codex Astartes")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
            elif num_chapter_org <= 10:
                f.writelines("\nThis Chapter has significantly diverged from the Codex Astartes")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
            elif num_chapter_org <= 11:
                f.writelines("\nThis Chapter's Organisation is unique")
                function_unit_restrictions()
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
                function_non_codex_element()
        elif Progenitor_Chapter == "Imperial Fists" or Progenitor_Chapter == "White Scars" or Progenitor_Chapter == \
                "Raven Guard":
            num_chapter_org = random.randint(1, 11)
            print("Chapter Organisation Roll:")
            print(num_chapter_org)
            if num_chapter_org <= 5:
                f.writelines("\nThis Chapter adheres to the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Codex Elements")
                function_codex_element()
            elif num_chapter_org <= 9:
                f.writelines("\nThis Chapter has somewhat diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
            elif num_chapter_org <= 10:
                f.writelines("\nThis Chapter has significantly diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
            elif num_chapter_org <= 11:
                f.writelines("\nThis Chapter's Organisation is unique.")
                function_unit_restrictions()
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
                function_non_codex_element()
        elif Progenitor_Chapter == "Dark Angels" or Progenitor_Chapter == "Blood Angels" or Progenitor_Chapter == \
                "Iron Hands" or Progenitor_Chapter == "Space Wolves" or Progenitor_Chapter == "Salamanders":
            num_chapter_org = random.randint(1, 11)
            print("Chapter Organisation Roll:")
            print(num_chapter_org)
            if num_chapter_org <= 3:
                f.writelines("\nThis Chapter matches its progenitor's organisation.")
            elif num_chapter_org <= 5:
                f.writelines("\nThis Chapter adheres to the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Codex Elements")
                function_codex_element()
            elif num_chapter_org <= 7:
                f.writelines("\nThis Chapter has somewhat diverged from its progenitor's organisation.")
                f.writelines("\n")
                f.writelines("\n    Non-Progenitor Elements")
                function_non_progenitor_element()
            elif num_chapter_org <= 8:
                f.writelines("\nThis Chapter has significantly diverged from its progenitor's organisation.")
                f.writelines("\n")
                f.writelines("\n    Non-Progenitor Elements")
                function_non_progenitor_element()
                function_non_progenitor_element()
            elif num_chapter_org <= 9:
                f.writelines("\nThis Chapter has somewhat diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
            elif num_chapter_org <= 10:
                f.writelines("\nThis Chapter has significantly diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
            elif num_chapter_org <= 11:
                f.writelines("\nThis Chapter's Organisation is unique.")
                function_unit_restrictions()
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
                function_non_codex_element()
        elif Progenitor_Chapter == "Unknown" or Progenitor_Chapter == "Suspected Traitor":
            num_chapter_org = random.randint(1, 11)
            print("Chapter Organisation Roll:")
            print(num_chapter_org)
            if num_chapter_org <= 3:
                f.writelines("\nThis Chapter adheres to the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Codex Elements")
                function_codex_element()
            elif num_chapter_org <= 8:
                f.writelines("\nThis Chapter has somewhat diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
            elif num_chapter_org <= 9:
                f.writelines("\nThis Chapter has significantly diverged from the Codex Astartes.")
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
            elif num_chapter_org <= 11:
                f.writelines("\nThis Chapter's Organisation is unique.")
                function_unit_restrictions()
                f.writelines("\n")
                f.writelines("\n    Non-Codex Elements")
                function_non_codex_element()
                function_non_codex_element()
                function_non_codex_element()

        f.writelines("\n")

        # The following code defines the Chapter's unity

        f.writelines("\n    Chapter Unity")
        num_chapter_unity = random.randint(1, 100)
        print("Chapter Unity Roll:")
        print(num_chapter_unity)
        if num_chapter_unity <= 85:
            f.writelines("\nUnited: this Chapter is, regardless of more minute details of organisation, a single, "
                         "cohesive group. There are no internal conflicts beyond what is the norm for the Adeptus "
                         "Astartes.")
        elif num_chapter_unity <= 90:
            f.writelines("\nMostly United: this Chapter can, regardless of more minute details of organisation, for the"
                         " most part be considered a cohesive group. However, internal conflicts are more common than"
                         " among their peers, and there may be external concerns about this.")
        elif num_chapter_unity <= 95:
            f.writelines("\nBarely United: this Chapter is held together by name and affiliation alone. Internal "
                         "conflicts are frequent, and while the Chapter still functions as a Chapter, the wider "
                         "Imperium is well aware that the fabric of the Chapter is thoroughly frayed.")
        elif num_chapter_unity <= 100:
            f.writelines("\nFractured: this Chapter is a Chapter in name only. Its Astartes have split into factions "
                         "that only share a name, roaming around with their own agendas. Their Fortress-Monastery "
                         "likely reflects this internal turmoil. These Astartes are infamous in the wider Imperium for "
                         "their inability to cooperate with their own brothers.")

        f.writelines("\n")

        # The following code defines the Chapter's Doctrine

        f.writelines("\n    Combat Doctrine")
        num_combat_doctrine = random.randint(1, 28)
        print("Combat Doctrine Roll:")
        print(num_combat_doctrine)
        if num_combat_doctrine <= 1:
            f.writelines("\nClose Combat: this Chapter favors engaging the enemy in close quarters. While still "
                         "proficient at range, these Astartes are truly in their element when crossing blades with "
                         "their foes, eye to eye.")
        elif num_combat_doctrine <= 2:
            f.writelines("\nRanged Combat: this Chapter favors engaging the enemy at range. While still proficient in "
                         "melee, these Astartes are truly in their element when allowed to fight from a distance.")
        elif num_combat_doctrine <= 3:
            f.writelines("\nArmoured Assault: this Chapter favors engaging the enemy as an entirely mechanized force, "
                         "affording them excellent tactical mobility.")
        elif num_combat_doctrine <= 4:
            f.writelines("\nStealth: this Chapter favors engaging the enemy while they're unaware, having mastered the "
                         "art of ambushes and the use of traps.")
        elif num_combat_doctrine <= 5:
            f.writelines("\nLightning Strike: this Chapter favors engaging the enemy hard and fast, using hit-and-run "
                         "tactics if the initial assault fails to destroy them entirely.")
        elif num_combat_doctrine <= 6:
            f.writelines("\nDrop Pod Assault: this Chapter favors engaging the enemy via orbital insertion, relying on "
                         "the element of surprise by suddenly appearing amidst or behind enemy lines.")
        elif num_combat_doctrine <= 7:
            f.writelines("\nThunderhawk Assault: this Chapter favors engaging the enemy via aerial insertion, using "
                         "their armed transports to clear a landing zone before rapidly disembarking.")
        elif num_combat_doctrine <= 8:
            f.writelines("\nSiege: this Chapter favors engaging the enemy via encirclement and with massed artillery, "
                         "or using an assortment of other siege methods to crack hostile fortresses.")
        elif num_combat_doctrine <= 9:
            f.writelines("\nShock & Awe: this Chapter favors engaging the enemy with overwhelming firepower, relying in"
                         " part on its sheer concussive effect, and in part on its destructive force.")
        elif num_combat_doctrine <= 10:
            f.writelines("\nBoarding Actions: this Chapter favors engaging the enemy during fleet actions as true space"
                         " marines, boarding their enemies and killing them from inside out.")
        elif num_combat_doctrine <= 11:
            f.writelines("\nUrban Combat: this Chapter favors engaging the enemy in cities, hives and factories. Where "
                         "others lay siege, these Astartes breach and attack.")
        elif num_combat_doctrine <= 12:
            f.writelines("\nForce Recon: this Chapter favors a doctrine of using smaller detachment to scout and "
                         "sabotage their enemies immediately prior to attacking.")
        elif num_combat_doctrine <= 13:
            f.writelines("\nAerial Supremacy: this Chapter favors engaging the enemy with superior air support, relying"
                         " heavily on the substantial arsenal of combat aircraft available to the Adeptus Astartes.")
        elif num_combat_doctrine <= 14:
            f.writelines("\nDefensive Operations: this Chapter favors fighting from a static or semi-static position of"
                         " strength, relying on the substantial resources and expertise the Adeptus Astartes can call "
                         "upon to create strong defenses.")
        elif num_combat_doctrine <= 15:
            f.writelines("\nAll Or Nothing: this Chapter favors fighting as a single comprehensive force, deploying the"
                         " entirety of its available Astartes when possible.")
        elif num_combat_doctrine <= 16:
            f.writelines("\nTask Force: this Chapter favors deploying the minimum practical number of Astartes, "
                         "focusing instead on putting as many marines in as many right places at the right time as "
                         "possible.")
        elif num_combat_doctrine <= 17:
            f.writelines("\nMinimize Losses: this Chapter favors a cautious form of combat, whereby they seek to "
                         "inflict as many casualties on their enemies as possible, while suffering as few of their own "
                         "as possible.")
        elif num_combat_doctrine <= 18 and Unit_Restrictions != "Librarian":
            f.writelines("\nMartial Psykers: this Chapter favors bringing psychic powers to bear on their enemies, "
                         "relying heavily on their Librarians to augment their fighting forces.")
            Combat_Doctrine = "Martial Psykers"
        elif num_combat_doctrine <= 19:
            f.writelines("\nEndurance: this Chapter favors leveraging the raw staying power of superhuman Astartes over"
                         " tactical or strategic considerations.")
        elif num_combat_doctrine <= 20:
            f.writelines("\nFlanking Strikes: this Chapter favors engaging the enemy where they aren't, rather than "
                         "where they are, preferring to strike at the weakest points.")
        elif num_combat_doctrine <= 21 and Unit_Restrictions != "Terminator":
            f.writelines("\nTerminator Assault: this Chapter favors engaging the enemy using Terminators as a "
                         "proverbial speartip, relying heavily on their sheer durability and awesome firepower.")
        elif num_combat_doctrine <= 22 and Unit_Restrictions != "Dreadnought":
            f.writelines("\nDreadnought Assault: this Chapter favors engaging the enemy using Dreadnoughts as a "
                         "proverbial speartip, relying heavily on their sheer durability and awesome firepower.")
        elif num_combat_doctrine <= 23:
            f.writelines("\nHonorable Conduct: this Chapter favors fighting according to a set of rules by which they "
                         "believe a proper and just war ought to be waged.")
        elif num_combat_doctrine <= 24:
            f.writelines("\nTerror: this Chapter favors engaging the enemy using psychological warfare, employing fear "
                         "as its foremost weapon.")
        elif num_combat_doctrine <= 25:
            f.writelines("\nRaiding: this Chapter favors attacking exposed or poorly defended enemy elements and "
                         "infrastructure and withdrawing before a counter-attack can be organised. While some decry "
                         "this practice as dishonorable, these Astartes either disagree with such assessments, or "
                         "simply don't care.")
        elif num_combat_doctrine <= 26:
            f.writelines("\nArchaic: this Chapter favors methods of waging war that are considered archaic by its "
                         "contemporaries.")
        elif num_combat_doctrine <= 27:
            f.writelines("\nSpecialists: this Chapter favors tactics and strategies that emphasize the use of "
                         "specialists over the otherwise widespread importance of the Tactical Squad or its Primaris "
                         "Intercessor equivalent.")
        elif num_combat_doctrine <= 28:
            f.writelines("\nGeneralists: this Chapter favors tactics and strategies that emphasize the use of "
                         "generalists over the otherwise widespread importance of specialist force multipliers.")
        f.writelines("\nNeedless to say, this is highly unlikely to be their sole means of fighting their enemies, but "
                     "instead a preferred doctrine at which the Chapter excels.")

        f.writelines("\n")

        # The following code defines the Chapter's Training

        f.writelines("\n    Characteristic Chapter Training")
        num_chapter_training = random.randint(1, 120)
        print("Chapter Training Roll:")
        print(num_chapter_training)
        if num_chapter_training <= 10:
            f.writelines("\nPersonal Weapon Focus: this Chapter instills in its Astartes the vital importance of "
                         "intimate familiarity with their weapons. They may do this in a variety of ways, for example "
                         "by meditation, consecration, or frequent maintenance.")
        elif num_chapter_training <= 20:
            f.writelines("\nBrotherhood: this Chapter instills in its Astartes the paramount value of their bond with "
                         "their brothers in arms. Consequently, their performance is noticeably higher when in the "
                         "company of their brothers.")
        elif num_chapter_training <= 30:
            f.writelines("\nEndurance: this Chapter instills in its Astartes both the utility and the virtue of "
                         "endurance. Whether mental or physical, no trial is unbearable to these marines.")
        elif num_chapter_training <= 40:
            f.writelines("\nAccuracy: this Chapter instills in its Astartes the shame of missing a target. Whether in "
                         "melee or at range, these marines maintain an almost neurotic dedication to precision. Perhaps"
                         " incidentally, they're also very punctual.")
        elif num_chapter_training <= 50:
            f.writelines("\nStrength: this Chapter instills in its Astartes the overriding principle of strength. With "
                         "enough force, there is no hide tough enough, no armour resilient enough, and no wall thick "
                         "enough to withstand their attacks.")
        elif num_chapter_training <= 60:
            f.writelines("\nInspiration: this Chapter instills in its Astartes an appreciation for the "
                         "oft-misunderstood art of lifting the hearts of others. Great orators all, they always seem to"
                         " know exactly what to say, and when to say it, and have used this skill to turn the tide of "
                         "many battles.")
        elif num_chapter_training <= 70:
            f.writelines("\nIndividual Skill: this Chapter instills in its Astartes a notion that the performance of "
                         "the Chapter is reliant on the performance of the individual. Consequently, they perform "
                         "exceptionally well, even when apart from their brothers.")
        elif num_chapter_training <= 80:
            f.writelines("\nFlexibility: this Chapter instills in its Astartes a jack-of-all-trades mentality, whereby "
                         "they perform admirably in most roles. While it comes with a cost, most likely in the form of "
                         "less efficient specialists, this can afford them tremendous tactical flexibility.")
        elif num_chapter_training <= 90:
            f.writelines("\nPersonal Armor Focus: this Chapter instills in its Astartes the vital importance of "
                         "intimate familiarity with their armor. They may do this in a variety of ways, for example by "
                         "meditation, consecration, or frequent maintenance.")
        elif num_chapter_training <= 100:
            f.writelines("\nAgility: this Chapter instills in its Astartes the life-saving nature of speed and "
                         "alacrity. A static marine is a dead marine, and they will be in constant motion once battle "
                         "is joined.")
        elif num_chapter_training <= 110:
            f.writelines("\nCooperation: this Chapter instills in its Astartes the value of fighting alongside the "
                         "mortal humans whose Imperium they protect. Accordingly, they may frequently integrate with "
                         "Imperial military forces, rather than stand apart from them, and either way work well with "
                         "non-Astartes forces.")
        elif num_chapter_training <= 120:
            f.writelines("\nSeclusion: this Chapter instills in its Astartes the superiority of space marines over any "
                         "other fighting force. Consequently, they frequently fight apart from other Imperial military "
                         "forces, preferring the prowess of their own kind.")

        f.writelines("\n")

        f.writelines("\n    Aspirant Recruitment")
        num_aspirant_recruitment = random.randint(1, 100)
        print("Aspirant Recruitment Roll:")
        print(num_aspirant_recruitment)
        if num_aspirant_recruitment <= 10:
            f.writelines("\nTrial by Combat: this Chapter recruits its Aspirants based on their fighting skills. This"
                         " may be tested by some manner of organised tournament, observing battles potential Aspirants "
                         "take part in, or something else entirely.")
        elif num_aspirant_recruitment <= 20:
            f.writelines("\nExposure: this Chapter recruits its Aspirants based on their survival skills, or just sheer"
                         " endurance. This may be tested by expecting potential Aspirants to travel through hazardous "
                         "environments to a recruitment location of their own volition, finding outcasts that have "
                         "survived despite the odds, or something else entirely.")
        elif num_aspirant_recruitment <= 30:
            f.writelines("\nTest of Will: this Chapter recruits its Aspirants based on their resolve. This may be "
                         "tested by engineering impossible tests and observing who still undertake them, offering "
                         "temptations that must be rejected, or something else entirely.")
        elif num_aspirant_recruitment <= 40:
            f.writelines("\nSelf-Discovery: this Chapter recruits its Aspirants based on their capacity for "
                         "introspection. This may be tested by extended meditation, consumption of hallucinogenics, or "
                         "something else entirely.")
        elif num_aspirant_recruitment <= 50:
            f.writelines("\nChance: this Chapter recruits its Aspirants based on chance. This may be tested by a "
                         "lottery, an interpretation of causality, or something else entirely.")
        elif num_aspirant_recruitment <= 60:
            f.writelines("\nMentorship: this Chapter recruits its Aspirants via a mentor program. This may take the "
                         "form of serving as a squire of sorts for an Astartes, living and working among the Serfs for "
                         "a period, or something else entirely.")
        elif num_aspirant_recruitment <= 70:
            f.writelines("\nTest of Strength: this Chapter recruits its Aspirants based on their strength. This may be "
                         "tested by a series of feats of strength, a physical competition against an Astartes, or "
                         "something else entirely.")
        elif num_aspirant_recruitment <= 80:
            f.writelines("\nEsotericism: this Chapter recruits its Aspirants based on their pool of hidden knowledge. "
                         "This may be tested by some occult ritual the potential Aspirant must conceive and perform, "
                         "secrets they must discover, or something else entirely.")
        elif num_aspirant_recruitment <= 90:
            f.writelines("\nTest of Wit: this Chapter recruits its Aspirants based on their wit. This may be tested by "
                         "a sequence of increasingly obscure riddles, placing the Aspirant in a situation from which "
                         "they can only be delivered by devising a clever means of escape, or something else entirely.")
        elif num_aspirant_recruitment <= 100:
            f.writelines("\nTest of Courage: this Chapter recruits its Aspirants based on their bravery. This may be "
                         "tested by a ritualised confrontation with their innermost fears, orchestrating events by "
                         "which they must sacrifice themselves to save someone else, or something else entirely.")
        f.writelines("\nFollowing this, they are examined by the Chapter's apothecaries to determine whether they are "
                     "suited for gene-seed implantation.")

        f.writelines("\n")

        # The following code defines the Chapter's rite of passage for Neophytes

        f.writelines("\n    Recruitment Style")
        num_recruitment_style = random.randint(1, 30)
        print("Recruitment Style Roll:")
        print(num_recruitment_style)
        if num_recruitment_style <= 10:
            f.writelines("\nVolunteers: this Chapter only draws its Aspirants from a pool of volunteers.")
        elif num_recruitment_style <= 20:
            f.writelines("\nKidnapping: this Chapter only draws its Aspirants from non-voluntary youths.")
        elif num_recruitment_style <= 30:
            f.writelines("\nMix: this Chapter draws its Aspirants from both a pool of volunteers and non-voluntary "
                         "youths.")

        f.writelines("\n")

        # The following code defines what happens to the Chapter's failed Aspirants

        f.writelines("\n    Failed Aspirant Fate")
        num_failed_aspirant = random.randint(1, 100)
        print("Failed Aspirant Roll:")
        print(num_failed_aspirant)
        if num_failed_aspirant <= 50:
            f.writelines("\nSerf Induction: Aspirants whose bodies reject the gene-seed implants and survive are "
                         "permitted to join the Chapter's Serfs.")
        elif num_failed_aspirant <= 60:
            f.writelines("\nServitor Conversion: Aspirants whose bodies reject the gene-seed implants and survive are "
                         "turned into servitors.")
        elif num_failed_aspirant <= 70:
            f.writelines("\nEuthanasia: Aspirants whose bodies reject the gene-seed implants and survive are killed.")
        elif num_failed_aspirant <= 80:
            f.writelines("\nReplacement Parts: Aspirants whose bodies reject the gene-seed implants and survive are put"
                         " in some form of suspended animation so they can be used to harvest replacement body parts.")
        elif num_failed_aspirant <= 90:
            f.writelines("\nBanishment: Aspirants whose bodies reject the gene-seed implants and survive are ejected "
                         "from the Chapter and may or may not be returned to their family.")
        elif num_failed_aspirant <= 100 and Existing_Mutations_Base != "DOOMED":
            f.writelines("\nProgenoid Slave: Aspirants whose bodies reject the gene-seed implants and survive are used"
                         " as an incubator for progenoid glands, provided his body didn't reject those.")
        else:
            f.writelines("\nSerf Induction: Aspirants whose bodies reject the gene-seed implants and survive are "
                         "permitted to join the Chapter's Serfs.")

        f.writelines("\n")

        # The following code defines the Chapter's treatment of its Serfs

        f.writelines("\n    Serf Treatment")
        num_serf_treatment = random.randint(1, 10)
        print("Serf Treatment Roll:")
        print(num_serf_treatment)
        if num_serf_treatment <= 5:
            f.writelines("\nIndifferent: this Chapter treats its Serfs fairly, but largely disregard their presence "
                         "when interaction is not necessary.")
        elif num_serf_treatment <= 7:
            f.writelines("\nRespectful: this Chapter treats its Serfs well, recognising the significance of their "
                         "work. Interaction is fairly common, even when not strictly necessary.")
        elif num_serf_treatment <= 9:
            f.writelines("\nSlavery: this Chapter treats its Serfs like chattel, considering them to be inferior, "
                         "worth only what labor they can perform.")
        elif num_serf_treatment <= 10:
            f.writelines("\nEquals: this Chapter treats its Serfs extraordinarily well, viewing them as equals, "
                         "without whom the Adeptus Astartes would be unable to carry out their tasks.")

        f.writelines("\n")

        # The following code defines the Chapter's Beliefs

        f.writelines("\n    Chapter Beliefs")
        num_chapter_beliefs = random.randint(1, 190)
        print("Chapter Beliefs Roll:")
        print(num_chapter_beliefs)
        if num_chapter_beliefs <= 60 and Progenitor_Chapter != "Unknown" and Progenitor_Chapter != "Suspected Traitor":
            f.writelines("\nMatches Progenitor: this Chapter maintains beliefs and a culture closely related to the ")
            if Progenitor_Chapter == "Ultramarines":
                f.writelines("Ultramarines")
            elif Progenitor_Chapter == "Dark Angels":
                f.writelines("Dark Angels")
            elif Progenitor_Chapter == "Blood Angels":
                f.writelines("Blood Angels")
            elif Progenitor_Chapter == "Imperial Fists":
                f.writelines("Imperial Fists")
            elif Progenitor_Chapter == "White Scars":
                f.writelines("White Scars")
            elif Progenitor_Chapter == "Raven Guard":
                f.writelines("Raven Guard")
            elif Progenitor_Chapter == "Iron Hands":
                f.writelines("Iron Hands")
            elif Progenitor_Chapter == "Space Wolves":
                f.writelines("Space Wolves")
            elif Progenitor_Chapter == "Salamanders":
                f.writelines("Salamanders")
            f.writelines(", even in the event that there has been a doctrinal or organisational divergence from their "
                         "progenitor.")
        elif num_chapter_beliefs <= 80:
            f.writelines("\nPrimarch Worship: this Chapter reveres its Primarch as the ultimate example of everything "
                         "all Astartes should be... perhaps even what all humans ought to be.")
        elif num_chapter_beliefs <= 100:
            f.writelines("\nEmperor Worship: this Chapter reveres the Emperor as the ultimate example of everything an "
                         "Astartes should strive to be, and everything humanity could be. They may even have adopted "
                         "the Ecclesiarchy's belief in the Emperor's divinity, which might ingratiate the Chapter with "
                         "the priesthood.\nHowever, should the worship be of a nature deemed heretical by the "
                         "Ecclesiarchy, it may actually harm relations instead.")
        elif num_chapter_beliefs <= 115:
            f.writelines("\nAncestor Worship: this Chapter reveres its own ancestors. Having made the ultimate "
                         "sacrifice, their actions represent a measuring stick by which the Chapter's contemporary "
                         "marines judge the worth of their own actions.")
        elif num_chapter_beliefs <= 130:
            f.writelines("\nDeath Cult: this Chapter views death in service to the Emperor as the ultimate duty of any "
                         "Astartes. Mortality, therefore, occupies a central position in their culture.")
        elif num_chapter_beliefs <= 135:
            f.writelines("\nIconography: this Chapter has a certain symbol that holds special meaning to them. "
                         "Consequently, it can be found throughout their culture, always held in reverence. Insulting "
                         "it or even expressing ignorance of it may be met with anger.")
        elif num_chapter_beliefs <= 140:
            f.writelines("\nPurity: this Chapter believes that the human form is sacred in some way, and therefore must"
                         " be preserved at all costs. They may even view themselves as the ultimate expression of human"
                         " excellence and potential.")
        elif num_chapter_beliefs <= 145:
            f.writelines("\nTranshumanism: this Chapter views humanity as inferior to themselves, and Astartes as "
                         "entirely separate. This may take on a patronising view, whereby humanity must be protected by"
                         " their betters, or a dismissive view, whereby humanity is disregarded as unimportant to the "
                         "Chapter.")
        elif num_chapter_beliefs <= 150:
            f.writelines("\nEsoteric: this Chapter's culture is strange, perhaps even unpalatable, to the wider "
                         "Imperium. While important to themselves, their allies may not fully understand the Chapter's "
                         "beliefs. Some may even respond with hostility should they become privy to it.")
        elif num_chapter_beliefs <= 155:
            f.writelines("\nIconoclasm: this Chapter holds a peculiar view of iconography, namely that such things are "
                         "frivolous and should be scorned if not serving some immediately practical function. Needless "
                         "to say, this belief may not be particularly well-received by the wider Imperium.")
        elif num_chapter_beliefs <= 160:
            f.writelines("\nNative Faith: this Chapter maintains the faith of its homeworld. While it has likely been "
                         "sanctioned by the Ecclesiarchy, it may nonetheless tread a fine line.")
        elif num_chapter_beliefs <= 165:
            f.writelines("\nNative Philosophy: this Chapter maintains the secular beliefs of its homeworld. While such "
                         "things are not necessarily subject to scrutiny from the Ecclesiarchy, it may nonetheless "
                         "tread a fine line.")
        elif num_chapter_beliefs <= 170:
            f.writelines("\nLife Cult: this Chapter views death in service to the Emperor as inevitable, but "
                         "simultaneously holds that any death in vain is a grave affront to His Imperium and His great "
                         "endeavor to safeguard humanity. Human life is precious; Astartes lives more so, having been "
                         "forged by the Emperor himself.")
        elif num_chapter_beliefs <= 175:
            f.writelines("\nMachine Worship: this Chapter reveres machines. This may take the form of officially "
                         "adopting the Cult Mechanicus, some unique worship of their own design, or something else "
                         "entirely. Although this may ingratiate the Chapter with the Adeptus Mechanicus, it may also "
                         "alienate parts of the wider Imperium.\nMoreover, should the machine worship be of a nature "
                         "incompatible with Mechanicus views, it may actually harm relations rather than improve them.")
        elif num_chapter_beliefs <= 180:
            f.writelines("\nMight Makes Right: this Chapter reveres power, maybe even at the expense of all else. Care "
                         "should be taken, for although certainly lending themselves well to warriors, such views may "
                         "ultimately lead down a dark path.")
        elif num_chapter_beliefs <= 185:
            f.writelines("\nSacred Liberty: this Chapter reveres freedom as an ultimate ideal, maybe even at the "
                         "expense of all else. Care should be taken, for although certainly lending themselves well to "
                         "liberators, such views may ultimately lead down a rebellious path.")
        elif num_chapter_beliefs <= 190:
            f.writelines("\nCult of Personality: this Chapter reveres one of its leading figures. This may be limited "
                         "to high esteem for his deeds or the contents of his character, but it may also develop into "
                         "something that might not be accepted by the wider Imperium.")

        f.writelines("\n")

        # The following code defines the Chapter's Strength

        f.writelines("\n    Chapter Strength")
        num_chapter_strength = random.randint(1, 13)
        print("Chapter Strength Roll:")
        print(num_chapter_strength)
        if num_chapter_strength <= 1:
            f.writelines("\nEndangered: this Chapter numbers ~")
            num_chapter_endangered = str(random.randint(50, 500))
            print("Chapter Endangered Roll:")
            print(num_chapter_endangered)
            f.writelines(num_chapter_endangered)
            f.write(" Astartes. This may be a temporary state of affairs due to recent heavy losses, a permanent side "
                    "effect of relentless fighting, or something else entirely.")
        elif num_chapter_strength <= 2:
            f.writelines("\nSignificantly Under Strength: this Chapter numbers ~")
            num_chapter_under_strength = str(random.randint(500, 700))
            print("Chapter Significantly Under Strength Roll:")
            print(num_chapter_under_strength)
            f.write(num_chapter_under_strength)
            f.writelines(" Astartes. This may be a temporary state of affairs due to recent heavy losses, a permanent "
                         "side effect of relentless fighting, or something else entirely.")
        elif num_chapter_strength <= 3:
            f.writelines("\nUnder Strength: this Chapter numbers ~")
            num_chapter_under_strength = str(random.randint(700, 900))
            print("Chapter Under Strength Roll:")
            print(num_chapter_under_strength)
            f.write(num_chapter_under_strength)
            f.writelines(" Astartes. This may be a temporary state of affairs due to recent heavy losses, a permanent "
                         "side effect of relentless fighting, or something else entirely.")
        elif num_chapter_strength <= 10:
            f.writelines("\nNormal: this Chapter numbers ~1000 Astartes. This number is likely to occasionally fall, "
                         "but their current numbers are largely stable.")
        elif num_chapter_strength <= 12:
            f.writelines("\nOver Strength: this Chapter numbers ~")
            num_chapter_over_strength = str(random.randint(1100, 1500))
            print("Chapter Over Strength Roll:")
            print(num_chapter_over_strength)
            f.write(num_chapter_over_strength)
            f.writelines(" Astartes. This may be due to a loophole they found in the Codex Astartes, simple disregard "
                         "for the part of the Codex that mandates Chapter numbers, or something else entirely.")
        elif num_chapter_strength <= 13:
            f.writelines("\nUnknown: somehow, records detailing the number of Astartes in this Chapter have been lost. "
                         "Or, perhaps, deliberately hidden. They may simply be so thinly spread across the galaxy that "
                         "an accurate account is borderline impossible, or some other cause entirely is to blame.")
        f.writelines("\nThe Codex Astartes prescribes a standing force of 1000 marines spread across 10 Companies of "
                     "100 marines.")
        f.writelines("\nThat number specifically refers to fighting men and does not include command or support staff.")
        f.writelines("\nMortal human serfs are also not included.")

        f.writelines("\n")

        # The following code defines the size of the Chapter's vehicle pool

        f.writelines("\n    Vehicle Pool")
        num_vehicle_strength = random.randint(1, 13)
        print("Vehicle Strength Roll:")
        print(num_vehicle_strength)
        if num_vehicle_strength <= 1:
            f.writelines("\nSeverely Under-Strength: this Chapter's vehicle pool is in an extremely depleted state. "
                         "The Chapter likely struggled to field any meaningful number of even basic Astartes vehicles, "
                         "let alone rare ones.")
        elif num_vehicle_strength <= 2:
            f.writelines("\nSignificantly Under-strength: this Chapter's vehicle pool is so small that its worth as a "
                         "force multiplier has been noticeably impacted. The Chapter is likely unable to field some of "
                         "the rarer vehicles otherwise available to the Adeptus Astartes.")
        elif num_vehicle_strength <= 3:
            f.writelines("\nUnder-strength: this Chapter's vehicle pool is smaller than average, although it still "
                         "represents a significant force multiplier. The Chapter most likely has a shortage of rare "
                         "vehicles in particular.")
        elif num_vehicle_strength <= 10:
            f.writelines("\nNormal: this Chapter's vehicle pool is of average size and makeup, as one might expect from"
                         " a baseline Chapter. It can most likely field a few rare vehicles as well.")
        elif num_vehicle_strength <= 12:
            f.writelines("\nOver-Strength: this Chapter's vehicle pool is larger than average, providing a powerful "
                         "advantage. The Chapter most likely also has greater access to rare vehicles.")
        elif num_vehicle_strength <= 13:
            f.writelines("\nUnknown: somehow, records detailing the vehicle inventory of this Chapter have been lost. "
                         "Or, perhaps, deliberately hidden. They may simply be so thinly spread across the galaxy that "
                         "an accurate account is borderline impossible, or some other cause entirely is to blame.")
        f.writelines("\nNote that the Codex Astartes places no limitations on a Chapter's vehicle pool. Instead, there "
                     "are practical limits to consider; mainly matters of logistics, attrition, production and "
                     "crewing.")

        f.writelines("\n")

        # The following code defines the Chapter's available terminator armor

        f.writelines("\n    Terminator Armor Availability")
        num_terminator_availability = random.randint(1, 13)
        print("Terminator Armor Availability Roll:")
        print(num_terminator_availability)
        if num_terminator_availability <= 1:
            f.writelines("\nFar Below Average: this Chapter's supply of terminator armor is so low that it might not be"
                         " able to field any at all. It certainly has no access to rarer suits.")
        elif num_terminator_availability <= 2:
            f.writelines("\nSignificantly Below Average: this Chapter's supply of terminator armor is much smaller than"
                         " what one might expect. The Chapter is unlikely to have any access to rarer suits.")
        elif num_terminator_availability <= 3:
            f.writelines("\nBelow Average: this Chapter's supply of terminator armor is subpar, but still enough to "
                         "provide a serious advantage. The Chapter likely has a shortage of rarer suits in particular.")
        elif num_terminator_availability <= 10:
            f.writelines("\nAverage: this Chapter's supply of terminator armor is on par with expectations. The Chapter"
                         " likely even has access to a number of rarer suits as well.")
        elif num_terminator_availability <= 12:
            f.writelines("\nAbove Average: this Chapter's supply of terminator armor is beyond what one might expect, "
                         "representing a potent advantage. The Chapter likely also has greater access to rarer suits.")
        elif num_terminator_availability <= 13:
            f.writelines("\nUnknown: somehow, records detailing the availability of terminator armor in this Chapter "
                         "have been lost. Or, perhaps, deliberately hidden. They may simply be so thinly spread across "
                         "the galaxy that an accurate account is borderline impossible, or some other cause entirely is"
                         " to blame.")
        f.writelines("\nNote that the Codex Astartes places no limitations on a Chapter's inventory of power armor, let"
                     " alone terminator armor. However, these suits are prohibitively expensive and difficult to create"
                     " and maintain.")
        f.writelines("\nSome Chapters, however, are more likely to have a greater number of suits available than "
                     "others. As an example, this is particularly true for Dark Angels successors who maintain the "
                     "tradition of the Deathwing formation.")

        f.writelines("\n")

        # The following code defines the condition of the Chapter's armory

        f.writelines("\n    Armory Condition")
        num_armory_condition = random.randint(1, 13)
        print("Armory Condition Roll:")
        print(num_armory_condition)
        if num_armory_condition <= 1:
            f.writelines("\nDreadful: this Chapter's armory is in a sorry state, and it will need to equip the majority"
                         " of Astartes with inferior gear. If the Chapter has any rare equipment at all, it will "
                         "probably be closely guarded and seldom issued.")
        elif num_armory_condition <= 2:
            f.writelines("\nPoor: this Chapter's armory is well below expectations, and it will need to equip many "
                         "Astartes with inferior gear. The Chapter is unlikely to have much in the way of rare "
                         "equipment.")
        elif num_armory_condition <= 3:
            f.writelines("\nSubpar: this Chapter's armory is somewhat lower than ordinary expectations, and it may "
                         "need to equip some Astartes with inferior gear. The Chapter likely has a shortage of rare "
                         "equipment in particular.")
        elif num_armory_condition <= 10:
            f.writelines("\nAverage: this Chapter's armory is on par with expectations, and it can fully equip every "
                         "Astartes with adequate gear. The Chapter likely has access to some rare equipment in addition"
                         " to its standard inventory.")
        elif num_armory_condition <= 12:
            f.writelines("\nExceptional: this Chapter's armory is unusually well-stocked, and it can fully equip every"
                         " Astartes with adequate gear, and even a considerable number with superior gear. The Chapter "
                         "likely has greater access to rare equipment in addition to its standard inventory.")
        elif num_armory_condition <= 13:
            f.writelines("\nUnknown: somehow, records detailing the condition of the Chapter's armory have been lost."
                         " Or, perhaps, deliberately hidden. They may simply be so thinly spread across the galaxy that"
                         " an accurate account is borderline impossible, or some other cause entirely is to blame.")
        f.writelines("\nNote that the Codex Astartes places no limitations on a Chapter's armory. Instead, there are "
                     "practical limits to consider; mainly matters of logistics, attrition and production.")
        f.writelines("\nSome Chapters, however, are more likely to have a greater amount of rare or superior equipment."
                     " As an example, this is particularly true for Salamanders successors who maintain their "
                     "progenitor's strong emphasis on craftsmanship.")

        f.writelines("\n")

        # The following code defines psyker prevalence within the Chapter

        f.writelines("\n    Psyker Prevalence")
        num_psyker_prevalence = random.randint(1, 13)
        print("Psyker Prevalence Roll:")
        print(num_psyker_prevalence)
        if num_psyker_prevalence <= 1 and "Psychic Discipline" not in (Chapter_Quirk_Base, Chapter_Quirk_1,
                                                                       Chapter_Quirk_2, Chapter_Quirk_3) \
                and Combat_Doctrine != "Martial Psykers":
            f.writelines("\nNone: this Chapter has no psykers at all. Whether due to some mutation in their gene-seed "
                         "or the population from which they recruit, or just simple scorn, they eschew an otherwise "
                         "powerful asset.")
        elif num_psyker_prevalence <= 2:
            f.writelines("\nVery Few: this Chapter has much fewer psykers in its ranks than most of its peers. "
                         "Regardless of this heavily diminished number and how these psykers employ their abilities, "
                         "they represent a powerful asset.")
        elif num_psyker_prevalence <= 3:
            f.writelines("\nFew: this Chapter has fewer psykers in its ranks than most of its peers. Regardless of this"
                         " diminished number and how these psykers employ their abilities, they represent a powerful "
                         "asset.")
        elif num_psyker_prevalence <= 10:
            f.writelines("\nAverage: this Chapter has an average number of psykers in its ranks. Regardless of how "
                         "these psykers employ their abilities, they represent a powerful asset.")
        elif num_psyker_prevalence <= 12:
            f.writelines("\nMany: this Chapter has more psykers in its ranks than most of its peers. Regardless of how "
                         "these psykers employ their abilities, they represent a powerful asset, particularly in such "
                         "numbers.")
        elif num_psyker_prevalence <= 13:
            f.writelines("\nUnknown: somehow, records detailing the number of the Chapter's psykers have been lost. Or,"
                         " perhaps, deliberately hidden. They may simply be so thinly spread across the galaxy that an "
                         "accurate account is borderline impossible, or some other cause entirely is to blame.")

        f.writelines("\n")

        # The following code defines the Chapter's Allies

        f.writelines("\n    Chapter Allies")
        num_chapter_allies = random.randint(1, 100)
        print("Chapter Allies Roll:")
        print(num_chapter_allies)
        if num_chapter_allies <= 1:
            num_chapter_allied_enemies = random.randint(1, 100)
            print("Chapter Allied Enemies Roll:")
            print(num_chapter_allied_enemies)
            if num_chapter_allied_enemies <= 21:
                f.writelines("\nOrks: this Chapter has made the questionable decision to weaponize the greenskins. This"
                             " is most likely done by somehow exploiting the nature and mentality of the orks to "
                             "manipulate them into doing things that benefit the Chapter or the wider Imperium in some "
                             "way, at which these Astartes must then be quite proficient.\nHowever, there is a chance "
                             "that they have made the EXTREMELY questionable decision to outright ally with the orks."
                             "\nThis is effectively treason, so unless the Chapter is in a hurry to be declared "
                             "traitors, this will likely be a very, very closely guarded secret.")
            elif num_chapter_allied_enemies <= 30:
                f.writelines("\nTau Empire: this Chapter has made the questionable decision to weaponize the tau. This "
                             "is most likely done by somehow exploiting the nature and mentality of the tau to "
                             "manipulate them into doing things that benefit the Chapter or the wider Imperium in some "
                             "way, at which these Astartes must then be quite proficient.\nHowever, there is a chance "
                             "that they have made the very questionable decision to outright ally with the tau.\nThis "
                             "is effectively treason, so unless the Chapter is in a hurry to be declared traitors, this"
                             " will likely be a very, very closely guarded secret.")
            elif num_chapter_allied_enemies <= 31:
                f.writelines("\nYnnari: this Chapter has formed a tentative alliance with the followers of Ynnead. "
                             "Despite their recent endeavors to resurrect Roboute Guilliman, at best, the wider "
                             "Imperium views all eldar with suspicion.")
            elif num_chapter_allied_enemies <= 42:
                f.writelines("\nAsuryani: this Chapter has made the questionable very decision to form a very tentative"
                             " alliance with the eldar of a particular Craftworld. Despite the recent endeavors of the "
                             "Ynnari to resurrect Roboute Guilliman, far from all eldar support them, and, at best, the"
                             " wider Imperium views all eldar with suspicion.")
            elif num_chapter_allied_enemies <= 51:
                f.writelines("\nTyranids: this Chapter has made the extremely questionable decision to weaponize the "
                             "invading Hive Fleets. This is most likely done by somehow exploiting the nature and "
                             "mentality of the tyranids to manipulate them into doing things that benefit the Chapter "
                             "or the wider Imperium in some way, at which these Astartes must then be quite proficient."
                             " They must also, rather likely, be quite mad.")
            elif num_chapter_allied_enemies <= 60:
                f.writelines("\nRenegade Space Marines: this Chapter has made the rather questionable decision to form "
                             "a tentative alliance with a group of renegade Astartes. Although renegade doesn't "
                             "automatically mean traitor or Chaos, the wider Imperium is unlikely to be very "
                             "understanding of the situation. This is likely a closely guarded secret.")
            elif num_chapter_allied_enemies <= 70:
                f.writelines("\nChaos Space Marines: this Chapter has made the extremely questionable decision to form "
                             "a very tentative alliance with a group of traitor Astartes. This is effectively treason, "
                             "so unless the Chapter is in a hurry to be declared traitors themselves, this will likely "
                             "be a very, very closely guarded secret.")
            elif num_chapter_allied_enemies <= 75:
                f.writelines("\nDaemons: this Chapter has made the extremely questionable decision to weaponize the "
                             "minions of the Archenemy. This is most likely done by forcing daemons to serve them by a "
                             "variety of means, such as binding them to a host or object. However, there is the slim "
                             "possibility that they have made the arguably outright stupid decision to ally themselves "
                             "with one or more daemons.\nThis is effectively treason, so unless the Chapter is in a "
                             "hurry to be declared traitors, this will likely be a very, very closely guarded secret.")
            elif num_chapter_allied_enemies <= 80:
                f.writelines("\nNon-Imperial Humans: this Chapter has made the rather questionable decision to form a "
                             "tentative alliance with a group of non-Imperial humans. While technically this is not "
                             "necessarily treason outright, the wider Imperium is highly unlikely to be understanding "
                             "of the situation.")
            elif num_chapter_allied_enemies <= 90:
                f.writelines("\nDrukhari: this Chapter has made the very, very questionable decision to weaponize the "
                             "Dark Eldar. This is most likely done by somehow exploiting the nature and mentality of "
                             "the Drukhari to manipulate them into doing things that benefit the Chapter or the wider "
                             "Imperium in some way, at which these Astartes must then be quite proficient.\nHowever, "
                             "there is a chance that they have made the very, very questionable decision to outright "
                             "ally with the Dark Eldar.\nThis is effectively treason, so unless the Chapter is in a "
                             "hurry to be declared traitors, this will likely be a very, very closely guarded secret.")
            elif num_chapter_allied_enemies <= 99:
                f.writelines("\nNecrons: this Chapter has made the extraordinarily questionable decision to weaponize "
                             "the Necron Dynasties. This is most likely done by somehow exploiting the nature and "
                             "mentality of the necrons to manipulate them into doing things that benefit the Chapter or"
                             " the wider Imperium in some way, at which these Astartes must then be quite proficient."
                             "\nHowever, there is a chance that they have made the extraordinarily questionable "
                             "decision to outright ally with the necrons.\nThis is effectively treason, so unless the "
                             "Chapter is in a hurry to be declared traitors, this will likely be a very, very closely "
                             "guarded secret.")
            elif num_chapter_allied_enemies <= 100:
                num_chapter_other_allied_enemies = random.randint(1, 100)
                print("Chapter Other Enemies Roll:")
                print(num_chapter_other_allied_enemies)
                if num_chapter_other_allied_enemies <= 15:
                    f.writelines("\nUmbra: this Chapter has made the extremely questionable decision to weaponize the "
                                 "umbra. This is most likely done by somehow exploiting the nature and mentality of the"
                                 " umbra to manipulate them into doing things that benefit the Chapter or the wider "
                                 "Imperium in some way, at which these Astartes must then be quite proficient. They "
                                 "must also, rather likely, be quite mad. Alternatively, they may also have a number of"
                                 " specimens in captivity that can be used against their enemies.")
                elif num_chapter_other_allied_enemies <= 25:
                    f.writelines("\nHrud: this Chapter has made the exceptionally questionable decision to weaponize "
                                 "the hrud. This is most likely done by somehow exploiting the nature and mentality of "
                                 "the hrud to manipulate them into doing things that benefit the Chapter or the wider "
                                 "Imperium in some way, at which these Astartes must then be quite proficient. "
                                 "Alternatively, they may also have a number of specimens in captivity that can be used"
                                 " against their enemies.")
                elif num_chapter_other_allied_enemies <= 35:
                    f.writelines("\nFra'al: this Chapter has made the highly questionable decision to form a very "
                                 "tentative alliance with the fra'al. This is effectively treason, so unless the "
                                 "Chapter is in a hurry to be declared traitors, this will likely be a very, very "
                                 "closely guarded secret.")
                elif num_chapter_other_allied_enemies <= 45:
                    f.writelines("\nKhrave: this Chapter has made the extremely questionable decision to weaponize the "
                                 "khrave. This is most likely done by somehow exploiting the nature and mentality of "
                                 "the khrave to manipulate them into doing things that benefit the Chapter or the wider"
                                 " Imperium in some way, at which these Astartes must then be quite proficient. They "
                                 "must also, rather likely, be quite mad. Alternatively, they may also have a number of"
                                 " specimens in captivity that can be used against their enemies.")
                elif num_chapter_other_allied_enemies <= 55:
                    f.writelines("\nRak'gol: this Chapter has made the extremely questionable decision to weaponize the"
                                 " rak'gol. This is most likely done by somehow exploiting the nature and mentality of "
                                 "the rak'gol to manipulate them into doing things that benefit the Chapter or the "
                                 "wider Imperium in some way, at which these Astartes must then be quite proficient. "
                                 "Alternatively, they may also have a number of specimens in captivity that can be used"
                                 " against their enemies.")
                elif num_chapter_other_allied_enemies <= 65:
                    f.writelines("\nEnslavers: this Chapter has made the insane decision to weaponize enslavers. This "
                                 "is most likely done by somehow exploiting the nature of the enslavers to manipulate "
                                 "them into doing things that benefit the Chapter or the wider Imperium in some way, at"
                                 " which these Astartes must then be quite proficient. They must also be quite mad. "
                                 "Alternatively, they may also have a number of specimens in captivity that can be used"
                                 " against their enemies.")
                elif num_chapter_other_allied_enemies <= 70:
                    f.writelines("\nQ'Orl: this Chapter has made the highly questionable decision to form a very "
                                 "tentative alliance with the Q'Orl Swarmhood. This is effectively treason, so unless "
                                 "the Chapter is in a hurry to be declared traitors, this will likely be a very, very "
                                 "closely guarded secret.")
                elif num_chapter_other_allied_enemies <= 75:
                    f.writelines("\nSlaugth: this Chapter has made the monumentally questionable decision to bargain "
                                 "with the dream eaters. In a worst case scenario, their dealings are with the "
                                 "Amaranthine Syndicate.")
                elif num_chapter_other_allied_enemies <= 80:
                    f.writelines("\nHellgrammite: this Chapter has made the extremely questionable decision to "
                                 "weaponize the hellgrammites. This is most likely done by somehow exploiting the "
                                 "nature and mentality of the hellgrammites to manipulate them into doing things that "
                                 "benefit the Chapter or the wider Imperium in some way, at which these Astartes must "
                                 "then be quite proficient. Alternatively, they may also have a number of specimens in "
                                 "captivity that can be used against their enemies.")
                elif num_chapter_other_allied_enemies <= 85:
                    f.writelines("\nLoxatl: this Chapter has made the questionable decision to weaponize the loxatl. "
                                 "They might somehow have secured a mercenary contract, but this is most likely done by"
                                 " somehow exploiting the nature and mentality of the loxatl to manipulate them into "
                                 "doing things that benefit the Chapter or the wider Imperium in some way, at which "
                                 "these Astartes must then be quite proficient. Alternatively, they may also have a "
                                 "number of specimens in captivity that can be used against their enemies.")
                elif num_chapter_other_allied_enemies <= 90:
                    f.writelines("\nAbominable Intelligences: this Chapter has made the extremely questionable decision"
                                 " to weaponize artificial intelligences. Regardless of how precisely this is achieved,"
                                 " the wider Imperium, and the Mechanicus in particular, are unlikely to be very "
                                 "understanding of this choice. This is likely a very, very closely guarded secret.")
                elif num_chapter_other_allied_enemies <= 92:
                    f.writelines("\nCreate your own lesser xenos faction.")
                elif num_chapter_other_allied_enemies <= 100:
                    f.writelines("\nPick literally anyone.")
        elif num_chapter_allies <= 5:
            f.writelines("\nAdministratum: this Chapter has ingratiated itself with some in the bureaucratic apparatus "
                         "of the Imperium. This may, for example, allow them to get certain things done in a more "
                         "expedient fashion when dealing with other bodies of the Imperium.")
        elif num_chapter_allies <= 10:
            f.writelines("\nAdeptus Arbites: this Chapter has made friends among the enforcers of Imperial law. This "
                         "may, for example, allow them to expedite recruitment from criminal elements, or make them "
                         "more capable of rooting out heretics and other undesirables.")
        elif num_chapter_allies <= 20:
            f.writelines("\nLeagues of Votann: this Chapter has allied itself with a squat Stronghold, or even an "
                         "entire League. This may, for example, allow them access to advanced technology, improve the "
                         "quality of their techmarines, or even allow them to call upon reinforcements.")
        elif num_chapter_allies <= 30:
            f.writelines("\nAnother Chapter: this Chapter has a strong bond with another Chapter of the Adeptus "
                         "Astartes. This may, for example, allow them to call upon reinforcements, or draw from their "
                         "allies' specialist expertise, which they might otherwise lack.")
        elif num_chapter_allies <= 35:
            f.writelines("\nAdeptus Astra Telepathica: this Chapter has connections among the sanctioned psykers of "
                         "the Imperium. This may, for example, allow them to enhance their astropath communications, or"
                         " even perhaps recruit psykers from the League of Blackships.")
        elif num_chapter_allies <= 45:
            f.writelines("\nAdeptus Mechanicus: this Chapter has allied itself with either a forge world, or Mars "
                         "itself. This may, for example, allow them access to advanced technology, improve the quality "
                         "of their techmarines, or even allow them to call upon reinforcements.")
        elif num_chapter_allies <= 50:
            f.writelines("\nAdepta Sororitas: this Chapter has garnered a significant reputation amongst an Order of "
                         "the fearsome Sisters of Battle. This may, for example, allow them to call upon "
                         "reinforcements, or make them more capable of rooting out heretics.")
        elif num_chapter_allies <= 53:
            f.writelines("\nCollegia Titanica: this Chapter has gained the fierce friendship of a titan legion. This "
                         "may, for example, allow them to call upon the god-machines themselves as reinforcements, or "
                         "give them significant leverage in Mechanicus politics.")
        elif num_chapter_allies <= 55:
            f.writelines("\nQuestor Imperialis: this Chapter has earned the proud loyalty of a knight, or an entire "
                         "Household. This may, for example, allow them to call upon reinforcements, or allow them to "
                         "recruit from a Knight World's population.")
        elif num_chapter_allies <= 58:
            f.writelines("\nLogis Strategos: this Chapter has ingratiated itself with some in the Imperial intelligence"
                         " agency. This may, for example, give them access to significantly superior information of "
                         "strategic value.")
        elif num_chapter_allies <= 60:
            f.writelines("\nChartist Captains: this Chapter has obtained influence amongst the civilian merchant fleet "
                         "of the Imperium. This may, for example, allow them to draw upon the inflexible, but "
                         "considerable, logistical network the captains maintain.")
        elif num_chapter_allies <= 65:
            f.writelines("\nAdeptus Ministorum: this Chapter has earned the zealous favor of some in the Ecclesiarchy. "
                         "This may, for example, allow them access to a considerable recruitment pool of faithful "
                         "people who view them as the Emperor's own angels.")
        elif num_chapter_allies <= 75:
            f.writelines("\nAstra Militarum: this Chapter has allied itself with a regiment of the Imperial Guard. "
                         "This may, for example, allow them to call upon the ponderous but awesome force of the "
                         "Imperial war machine.")
        elif num_chapter_allies <= 79:
            f.writelines("\nNavis Imperialis: this Chapter has gained a measure of influence with a battlegroup of the "
                         "Imperial Navy. This may, for example, allow them to call upon the frightful firepower "
                         "available to the great ships of the Imperium.")
        elif num_chapter_allies <= 85:
            f.writelines("\nInquisition: this Chapter has the questionable honor of being on an Inquisitor's good side."
                         " For however long that lasts, they may, for example, have considerable leverage in most "
                         "Imperial affairs... at a cost.")
        elif num_chapter_allies <= 88:
            f.writelines("\nNavis Nobilite: this Chapter has somehow pierced the unfathomable politics of the "
                         "Navigators and gained the favor of one of their Houses. This may, for example, give them "
                         "considerable benefits when traveling the void.")
        elif num_chapter_allies <= 91:
            f.writelines("\nOfficio Assassinorum: this Chapter has ingratiated itself with some in the Assassin "
                         "Temples. This may, for example, give them access to a covert and extraordinarily efficient "
                         "means of resolving conflicts before they even truly begin.")
        elif num_chapter_allies <= 93:
            f.writelines("\nPlanetary Defence Force: this Chapter has obtained the loyalty of a local PDF. This may, "
                         "for example, give them access to very earnest reinforcements of dubious worth in battle.")
        elif num_chapter_allies <= 98:
            f.writelines("\nRogue Traders: this Chapter has connections among some of the Imperium's very own frontier "
                         "explorers. This may, for example, give them access to all sorts of exotic inventories of "
                         "questionable origins.")
        elif num_chapter_allies == 99:
            f.writelines("\nSchola Progenium: this Chapter has made friends among some in the orphanages of the "
                         "Ministorum. This may, for example, give them access to a small but extremely determined "
                         "recruitment pool.")
        elif num_chapter_allies == 100:
            f.writelines("\nAdeptus Custodes: this Chapter has somehow gained a small measure of influence with some of"
                         " the Emperor's own guards. This may, for example, give them considerable leverage in most "
                         "Imperial affairs.")

        f.writelines("\n")

        # The following code defines the Chapter's Enemies

        f.writelines("\n    Chapter Enemies")
        num_chapter_enemies = random.randint(1, 100)
        print("Chapter Enemies Roll:")
        print(num_chapter_enemies)
        if num_chapter_enemies <= 2:
            num_chapter_enemy_allies = random.randint(1, 100)
            print("Chapter Enemy Allies Roll:")
            print(num_chapter_enemy_allies)
            if num_chapter_enemy_allies <= 5:
                f.writelines("\nAdministratum: this Chapter has earned the ire of some in the bureaucratic apparatus of"
                             " the Imperium. This may, for example, prevent them from getting certain things done in a "
                             "more expedient fashion when dealing with other bodies of the Imperium. It may also be "
                             "worse.")
            elif num_chapter_enemy_allies <= 10:
                f.writelines("\nAdeptus Arbites: this Chapter has made enemies among the enforcers of Imperial law. "
                             "This may, for example, hinder recruitment from criminal elements, or make them less "
                             "capable of rooting out heretics and other undesirables. It may also be worse.")
            elif num_chapter_enemy_allies <= 20:
                f.writelines("\nLeagues of Votann: this Chapter has become the subject of one or more grudges in a "
                             "squat Stronghold, or even an entire League. This may, for example, result in open "
                             "conflict. It may also be worse.")
            elif num_chapter_enemy_allies <= 30:
                f.writelines("\nAnother Chapter: this Chapter has a hostile relationship another Chapter of the Adeptus"
                             " Astartes. This may, for example, result in open conflict, or disrupt their activities "
                             "during joint missions. It may also be worse.")
            elif num_chapter_enemy_allies <= 35:
                f.writelines("\nAdeptus Astra Telepathica: this Chapter has enemies among the sanctioned psykers of the"
                             " Imperium. This may, for example, reduce the quality of their astropath communications, "
                             "or prevent them from recruiting psykers from the League of Blackships. It may also be "
                             "worse.")
            elif num_chapter_enemy_allies <= 45:
                f.writelines("\nAdeptus Mechanicus: this Chapter has angered either a forge world, or Mars itself. This"
                             " may, for example, prevent access to advanced technology, or outright reduce the quality "
                             "of their techmarines. It may also be worse.")
            elif num_chapter_enemy_allies <= 50:
                f.writelines("\nAdepta Sororitas: this Chapter has a negative reputation amongst an Order of the "
                             "fearsome Sisters of Battle. This may, for example, result in open conflict, or make them "
                             "less capable of rooting out heretics. It may also be worse.")
            elif num_chapter_enemy_allies <= 53:
                f.writelines("\nCollegia Titanica: this Chapter has earned the fierce anger of a titan legion. This "
                             "may, for example, result in open conflict, or significantly reduce their leverage in "
                             "Mechanicus politics. It may also be worse.")
            elif num_chapter_enemy_allies <= 55:
                f.writelines("\nQuestor Imperialis: this Chapter has earned the proud contempt of a knight, or an "
                             "entire Household. This may, for example, result in open conflict, or bar them from "
                             "recruiting from a Knight World's population. It may also be worse.")
            elif num_chapter_enemy_allies <= 58:
                f.writelines("\nLogis Strategos: this Chapter has somehow antagonized some in the Imperial intelligence"
                             " agency. This may, for example, result in significantly inferior information of strategic"
                             " value. It may also be worse.")
            elif num_chapter_enemy_allies <= 60:
                f.writelines("\nChartist Captains: this Chapter has angered many amongst the civilian merchant fleet of"
                             " the Imperium. This may, for example, prevent them from drawing upon the inflexible, but "
                             "considerable, logistical network the captains maintain. It may also be worse.")
            elif num_chapter_enemy_allies <= 65:
                f.writelines("\nAdeptus Ministorum: this Chapter has earned the zealous ire of some in the "
                             "Ecclesiarchy. This may, for example, bar them from a considerable recruitment pool of "
                             "faithful, or even result in open conflict. It may also be worse.")
            elif num_chapter_enemy_allies <= 75:
                f.writelines("\nAstra Militarum: this Chapter has made enemies with a Regiment of the Imperial Guard. "
                             "This may, for example, result in open conflict. It may also be worse.")
            elif num_chapter_enemy_allies <= 79:
                f.writelines("\nNavis Imperialis: this Chapter has gained the displeasure of a battlegroup of the "
                             "Imperial Navy. This may, for example, result in open conflict. It may also be worse.")
            elif num_chapter_enemy_allies <= 85:
                f.writelines("\nInquisition: this Chapter has the questionable honor of being on an Inquisitor's bad "
                             "side. For however long that lasts, they may, for example, suffer a series of unfortunate "
                             "events. It may also be worse.")
            elif num_chapter_enemy_allies <= 88:
                f.writelines("\nNavis Nobilite: this Chapter has somehow pierced the unfathomable politics of the "
                             "Navigators in such a way that it angered one of their Houses. This may, for example, give"
                             " them considerable drawbacks when traveling the void. It may also be worse.")
            elif num_chapter_enemy_allies <= 91:
                f.writelines("\nOfficio Assassinorum: this Chapter has angered some in the Assassin Temples. This may, "
                             "for example, result in open conflict, or, if they're very unlucky, hidden conflict. It "
                             "may also be worse.")
            elif num_chapter_enemy_allies <= 93:
                f.writelines("\nPlanetary Defence Force: this Chapter has earned the ire of a local PDF. This may, for"
                             " example, result in open conflict. It may also be worse.")
            elif num_chapter_enemy_allies <= 98:
                f.writelines("\nRogue Traders: this Chapter has enemies among some of the Imperium's very own frontier "
                             "explorers. This may, for example, result in open conflict. It may also be worse.")
            elif num_chapter_enemy_allies == 99:
                f.writelines("\nSchola Progenium: this Chapter has made enemies among the orphanages of the Ministorum."
                             " This may, for example, bar them access from a small but extremely determined recruitment"
                             " pool. It may also be worse.")
            elif num_chapter_enemy_allies == 100:
                f.writelines("\nAdeptus Custodes: this Chapter has somehow gained a small measure of indignation from "
                             "some of the Emperor's own guards. This may, for example, give them considerable drawbacks"
                             " in most Imperial affairs, or result in open conflict. It may also be worse.")
        elif num_chapter_enemies <= 21:
            f.writelines("\nOrks: this Chapter has become proficient fighting greenskins. Where some disregard them as"
                         " disorganised rabble, these Astartes recognise them for the true threat they are.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 30:
            f.writelines("\nTau Empire: this Chapter has become proficient fighting tau. Ignored by some in the "
                         "Imperium as insignificant upstarts, these Astartes see the long-term potential of the tau, "
                         "and the danger of it being realised.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 31:
            f.writelines("\nYnnari: this Chapter has become proficient fighting the followers of Ynnead. Despite their "
                         "recent endeavors to resurrect Roboute Guilliman, these Astartes fully expect betrayal before "
                         "long.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 42:
            f.writelines("\nAsuryani: this Chapter has become proficient fighting Craftworld Eldar. Thought by some to "
                         "be the irrelevant remnants of a dying species, these Astartes know all too well the perfidy "
                         "of these farsighted xenos.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 51:
            f.writelines("\nTyranids: this Chapter has become proficient fighting the invading Hive Fleets. There are "
                         "voices in the Imperium who consider the threat to have been dealt with, but these Astartes "
                         "know that so long as a single hive organism remains, the war is not over.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 60:
            f.writelines("\nGenestealer Cults: this Chapter has become proficient rooting out the insidious cults "
                         "paving the path for their tyranid masters. While often overlooked by others, these Astartes "
                         "view the premature end of the cults as the ultimate means of preventing tyranid attacks.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 70:
            f.writelines("\nChaos Space Marines: this Chapter has become proficient opposing the Long War. While the "
                         "threat of the Traitor Legions waxes and wanes, these Astartes are ever vigilant in their "
                         "persecution of traitor marines, whether the betrayal be ancient or recent.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 75:
            f.writelines("\nDaemons: this Chapter has become proficient combating the Archenemy. While tentatively "
                         "attempted to be kept secret from the Imperium at large, these Astartes are fully aware of the"
                         " danger presented by the empyreal minions Chaos.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 80:
            f.writelines("\nNon-Imperial Humans: this Chapter has become proficient crushing rebellions, reconquering "
                         "secessionist territory and bringing forgotten pockets of humanity into the Imperial fold. "
                         "While some may doubt the decision to send marines to accomplish such tasks, these Astartes "
                         "are convinced that their presence during such endeavors is a necessity, being the Emperor's "
                         "angels of death.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 90:
            f.writelines("\nDrukhari: this Chapter has become proficient fighting the Dark Eldar. While often forgotten"
                         " due to their reclusive nature and penchant for obfuscation, these Astartes are acutely aware"
                         " of the toll these insidious xenos take on the Imperium.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies <= 99:
            f.writelines("\nNecrons: this Chapter has become proficient fighting the Necron Dynasties. While sometimes "
                         "forgotten, and even occasionally attempted controlled, these Astartes have come to understand"
                         " the true scope of the empire buried beneath countless worlds, and the threat of it awakening"
                         " and rising once more under their very feet.")
            f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                         "attention.")
            f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often than"
                         " not, be considered a preferred enemy.")
        elif num_chapter_enemies == 100:
            num_chapter_other_enemies = random.randint(1, 100)
            print("Chapter Other Enemies Roll:")
            print(num_chapter_other_enemies)
            if num_chapter_other_enemies <= 15:
                f.writelines("\nUmbra: this Chapter has become proficient fighting the mysterious Umbra. Rare enough "
                             "that most give them little thought, these Astartes have seen what the eldritch fiends are"
                             " capable of.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 25:
                f.writelines("\nHrud: this Chapter has become proficient fighting the repulsive Hrud. Although a lesser"
                             " xenos species, what little presence they have on the galactic scale is recognised by "
                             "these Astartes as potentially catastrophic if left unchecked.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 35:
                f.writelines("\nFra'al: this Chapter has become proficient fighting the monstrous Fra'al. While not a "
                             "major faction in the galaxy, these Astartes view their nomadic empire as a menace to the "
                             "Imperium that needs to be stopped before it evolved beyond a minor threat.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 45:
                f.writelines("\nKhrave: this Chapter has become proficient fighting the sinister Khrave. A "
                             "long-standing, but relatively minor enemy of the Imperium, they are frequently overlooked"
                             " in favor of more pressing matters. These Astartes, however, consider the mind-eaters and"
                             " their expansionist empire to be one such pressing matter.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 55:
                f.writelines("\nRak'gol: this Chapter has become proficient fighting the abominable Rak'gol. Considered"
                             " by some to be little more than a minor pirate problem, these Astartes believe that, if "
                             "left unchecked, the Rak'gol and their ramshackle technology could become a problem "
                             "similar to the Tau Empire.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 65:
                f.writelines("\nEnslavers: this Chapter has become proficient fighting the despicable enslavers. Known "
                             "also as Krell, or Psyrens, there are some who view the endeavor of exterminating them as "
                             "futile. These Astartes are of the contrary position, viewing them as a potentially "
                             "apocalyptic threat to the Imperium, as well as the galaxy at large.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 70:
                f.writelines("\nQ'orl: this Chapter has become proficient fighting the Swarmhood. Often forgotten "
                             "about, these Astartes consider their empire's size and proximity to Terra alone to mark "
                             "them as a grave threat.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 75:
                f.writelines("\nSlaugth: this Chapter has become proficient fighting the vile dream eaters. Inhabiting "
                             "forgotten and obscure places, many have never heard of the carrion masters, let alone "
                             "seen them. These Astartes have, and they are determined to destroy the Slaugth wherever "
                             "they surface.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 80:
                f.writelines("\nHellgrammite: this Chapter has become proficient fighting the remnants of the "
                             "Hellgrammite Empire. While many consider them to have been crushed, these Astartes have "
                             "yet to relent in the persecution of the vile xenos and their occult ways.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 85:
                f.writelines("\nLoxatl: this Chapter has become proficient fighting the amphibious mercenaries known as"
                             " the Loxatl. Although their homeworld has yet to be found, these Astartes have "
                             "encountered them on enough battlefields to understand the danger posed by their continued"
                             " employment by the Imperium's enemies.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 90:
                f.writelines("\nAbominable Intelligences: this Chapter has become proficient fighting the mechanical "
                             "minds of rogue machine spirits, self-aware cogitators and other Abominable Intelligences."
                             " Forgotten by many outside the Mechanicus, these Astartes have learned to maintain a "
                             "vigilant watch for any signs of renegade machines.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 92:
                f.writelines("\nCreate your own lesser xenos faction.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")
            elif num_chapter_other_enemies <= 100:
                f.writelines("\nPick literally anyone.")
                f.writelines("\nNaturally, this is unlikely to be their only opponent or the sole subject of their "
                             "attention.")
                f.writelines("\nNor is it likely they're incapable of combating other threats. This should, more often "
                             "than not, be considered a preferred enemy.")


def function_open_chapter_txt():
    chapter_txt_path = str(chapter_name)
    os.startfile("C:/Chapter Creator/" + chapter_txt_path)


# The following code executes the Chapter creation script
if __name__ == "__Chapter_Creator_Main__":
    function_chapter_creation_table()
    function_open_chapter_txt()
