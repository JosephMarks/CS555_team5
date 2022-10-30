from datetime import datetime, timedelta

# parse the date
def yearsDifferenceChecker(date1, date2):
    date1List = date1.split('-')
    date2List = date2.split('-')
    dateTime1 = datetime(int(date1List[0]), int(date1List[1]), int(date1List[2]))
    dateTime2 = datetime(int(date2List[0]), int(date2List[1]), int(date2List[2]))
    if dateTime2 > dateTime1:
        variance = dateTime2 - dateTime1
        return variance.days / 365.2425
    else:
        variance = dateTime1 - dateTime2
        return variance.days / 365.2425

def modifiedDate(date, days):
    if days >= 0:
        return str(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=days))[:10]
    else:
        return str(datetime.strptime(date, '%Y-%m-%d') - timedelta(days=days))[:10]

def printError(us, id, message):
    print("ERROR US"+ us + " " + id + " " + message)

# US17 - No marriages to descendants
def noMarriagesToDescendants(individualDictionary, familyDictionary):
    flag = True
    for indi in individualDictionary:
        parentsFamily = individualDictionary[indi]['Child']
        childFamily = individualDictionary[indi]['Spouse']
        if (childFamily != [] and parentsFamily != 'NA'):
            father = familyDictionary[parentsFamily]['Husband_ID']
            mother = familyDictionary[parentsFamily]['Wife_ID']
            for fam in childFamily:
                if (familyDictionary[fam]['Husband_ID'] == father):
                    flag = False
                    printError("17", indi, "is married to her father.")
                if (familyDictionary[fam]['Wife_ID'] == mother):
                    flag = False
                    printError("17", indi, "is married to his mother.")
    return flag

# US18 - Siblings should not marry
def siblingsShouldNotMarry(individualDictionary, familyDictionary):
    flag = True
    for fami in familyDictionary:
        wifeFamily = individualDictionary[familyDictionary[fami]["Wife_ID"]]['Child']
        husbandFamily = individualDictionary[familyDictionary[fami]["Husband_ID"]]['Child']
        if(wifeFamily != 'NA' and husbandFamily != 'NA'):
            if (wifeFamily == husbandFamily):
                flag = False
                printError("18", fami, "Siblings marry one another.")
    return flag

