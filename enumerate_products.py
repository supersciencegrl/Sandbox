'''
    TEMPORARY FILE CLONED FROM CATA-LIST UPDATE
    '''
# Created by Nessa Carson 2021

import molmass
import pyperclip

def remove_boronic_acid(mf):
    ''' ONLY WORKS FOR <10 TOTAL B and O ATOMS!!! '''
    mf_orig = mf
    Bcount = []
    Ocount = []
    Ocount2 = False

    for i, char in enumerate(mf):
        if char == 'B':
            try:
                nextchar = mf[i+1]
                if nextchar.islower():
                    pass
                else:
                    Bcount.append(i)
            except IndexError:
                Bcount.append(i)

    if not Bcount:
        print(f'Boronic acid elements not present in {mf_orig}!')
        return None

    for B in Bcount[::-1]:
        try:
            nextchar = mf[B+1]
        except IndexError:
            mf = mf[:-1]
            break
        if nextchar.isdigit():
            newchar = int(nextchar) - 1
            if newchar == 1:
                mf = f'{mf[:B+1]}{mf[B+2:]}'
            elif not newchar:
                mf = f'{mf[:B]}{mf[B+2:]}'
            else:
                mf = f'{mf[:B+1]}{newchar}{mf[B+2:]}'
            break
        else:
            mf = f'{mf[:B]}{mf[B+1:]}'
            break

    for i, char in enumerate(mf):
        if char == 'O':
            try:
                nextchar = mf[i+1]
                if nextchar.islower():
                    pass
                elif nextchar.isdigit():
                    Ocount.append(i)
                    Ocount2 = True
                else:
                    Ocount.append(i)
            except IndexError:
                Ocount.append(i)

    if not len(Ocount) or (len(Ocount) == 1 and not Ocount2):
        print(f'Boronic acid elements not present in {mf_orig}!')
        return None

    Oremoved = 0
    while Oremoved < 2:
        for O in Ocount[::-1]:
            try:
                nextchar = mf[O+1]
            except IndexError:
                nextchar = ''
                mf = mf[:-1]
                Oremoved += 1
            if nextchar.isdigit():
                minus = 2 - Oremoved
                newchar = int(nextchar) - minus
                if newchar == 1:
                    mf = f'{mf[:O+1]}{mf[O+2:]}'
                elif not newchar:
                    mf = f'{mf[:O]}{mf[O+2:]}'
                else:
                    mf = f'{mf[:O+1]}{newchar}{mf[O+2:]}'
                Oremoved += 2
            elif nextchar:
                if not Oremoved:
                    mf = f'{mf[:O]}{mf[O+1:]}'
                elif Oremoved == 1:
                    mf = f'{mf[:O-1]}{mf[O:]}'
                Oremoved += 1

    return mf

def remove_halide(mf):
    ''' ONLY WORKS FOR <10 TOTAL HALOGENS!!!
        Assumes reactivity I > Br > Cl '''
    mf_orig = mf

    halides = ['I', 'Br', 'Cl']

    for hal in halides:
        if hal in mf:
            posn = mf.index(hal)
            try:
                nextchar = mf[posn+len(hal)]
                if nextchar.isdigit():
                    newchar = int(nextchar) - 1
                    if newchar == 1:
                        mf = f'{mf[:posn+len(hal)]}{mf[posn+len(hal)+1:]}'
                    elif not newchar:
                        mf = f'{mf[:posn]}{mf[posn+len(hal)+1:]}'
                    else:
                        mf = f'{mf[:posn+len(hal)]}{newchar}{mf[posn+len(hal)+1:]}'
                    return mf
                else:
                    mf = f'{mf[:posn]}{mf[posn+len(hal):]}'
                    return mf
            except IndexError:
                nextchar = ''
                mf = f'{mf[:posn]}{mf[posn+2:]}'
                return mf

    return mf

def dp_mf(string):
    ''' For an input string such as:
        'C6H8BNO2	225.01	C7H4BrF3	237.22	237.02'
    This would be pasted from Excel
    See 21-18697 enumeration.xlsm for an example
    '''

    listy = [y.strip() for y in string.split('\t')]
    try:
        sm1_mf = listy[0]
        sm2_mf = listy[2]
    except IndexError:
        print('Index error')
        return None

    sm1_frag = remove_boronic_acid(sm1_mf)
    sm2_frag = remove_halide(sm2_mf)

    newmf = sm1_frag + sm2_frag
    newmf = molmass.Formula(newmf).formula

    pyperclip.copy(newmf)
    print(newmf)
    return newmf

def run():
    global outputlist
    
    while True:
        inputstring = input('Input 4 cells: ')
        result = dp_mf(inputstring)
        if result:
            outputlist.append(result)
        
def report():
    global outputlist
    report_output = ('\n').join(outputlist)

    pyperclip.copy(report_output)
    print(report_output)
    return report_output

outputlist = []
run()
