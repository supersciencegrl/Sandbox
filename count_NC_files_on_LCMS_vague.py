import glob
import os
import re

mydir = r'\\gbjhxnsmasx1026\masslynx\ChemRobot.PRO\Data'

filenames = glob.glob(os.path.join(mydir, '*.raw'))
filenames = [f.split(os.sep)[-1] for f in filenames]

possible = [f for f in filenames if f.startswith('20-') or f.startswith('21-')]
flags = [' ', 'pre', 'wu', 'crude', 'batch', 'qc']
possible = [p for p in possible if not any(ele in p.lower() for ele in flags)]

regex = re.compile('2[0-1]-\d{5}-\d{3}')
print('Working...')
results = [p for p in possible if re.match(regex, p)]
print('Complete.')
print(len(results), 'files found.')

''' Don't forget about ones in the NC subfolder: currently 368 total '''
