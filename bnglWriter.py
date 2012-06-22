#!/usr/bin/env python

import re

def bnglReaction(reactant,product,rate,tags,translator=[]):
    finalString = ''
    for index in range(0,len(reactant)):
        if reactant[index] in tags:
            finalString += tags[reactant[index]]
        finalString += printTranslate(reactant[index],translator)
        if index < len(reactant) -1:
            finalString += ' + '
    finalString += ' -> '
    for index in range(0,len(product)):
        if product[index] in tags:
            finalString += tags[product[index]]    
        finalString +=  printTranslate(product[index],translator) 
        if index < len(product) -1:
            finalString += ' + '
    finalString += ' ' + rate
    return finalString
    

def printTranslate(chemical,translator={}):
    if chemical not in translator:
        return chemical + '()'
    else:
        return str(translator[chemical])




    
def bnglFunction(rule,functionTitle,compartments=[]):
    tmp = rule
    for compartment in compartments:
        tmp = re.sub('{0}\\s*\\*'.format(compartment),'',tmp)
        tmp = re.sub('\\*\\s*{0}'.format(compartment),'',tmp)
    finalString = '%s = %s' % (functionTitle,tmp)
    return finalString

    
def finalText(param,molecules,species,observables,rules,functions,compartments,fileName):
    output = open(fileName,'w')
    output.write('begin model\n')
    output.write(sectionTemplate('parameters',param))
    output.write(sectionTemplate('compartments',compartments))          
    output.write(sectionTemplate('molecules',molecules))
    output.write(sectionTemplate('seed species',species))
    output.write(sectionTemplate('functions',functions))
    output.write(sectionTemplate('observables',observables))
    output.write(sectionTemplate('rules',rules))
    output.write('end model\n')
    output.write('generate_network();\n')
    output.write('simulate_ode({t_end=>400,n_steps=>50});')
    
def sectionTemplate(name,content):
    section = 'begin %s\n' % name
    temp = ['\t%s\n' % line for line in content]
    section += ''.join(temp)
    section += 'end %s\n' % name
    return section
