import pandas as pd
import os 
import pickle


def save_file(data, fname, dname):
    
    if not os.path.exists(dname):
        os.mkdir(dname)
        print(f'Directory {dname} was created.')
        
    fpath = os.path.join(dname,fname)
    
    if os.path.exists(fpath):
        print(" A file already exists with this name.\n")
        
        yesno = None
        while yesno != "Y" and yesno !="N":
            yesno = input('Do you want to override? (Y/N)').strip()[0].capitalize()
            if yesno =="Y":
                print(f'Writing file. "{fpath}"')
                _save_file(data, fpath)
            elif yeno =="N":
                print('\nPlease re-run this cell with new filename.')
            else:
                print('\nUnknown input, please enter "Y" or "N".')
                
    else:
        print(f'Writing file. "{fpath}"')
        _save_file(data, fpath)
        
        
def _safe_file(data, fpath):
    valid_ftypes = ['.csv','.pkl']
    
    assert(fpath[:-4] in valid_fypes), "Invalid file type. Use '.csv' or '.pkl'"
    
    if fpath[-3] =='csv':
        data.to_csv(fpath, index=False)
    elif fpath[-3] == 'pkl':
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)