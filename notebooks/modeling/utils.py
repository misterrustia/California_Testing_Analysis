import pandas as pd
import os 
import pickle

        
def _save_file(data, fpath):
    valid_ftypes = ['.csv', '.pkl']
    
    assert (fpath[-4:] in valid_ftypes), "Invalid file type.  Use '.csv' or '.pkl'"

    # Figure out what kind of file we're dealing with by name
    if fpath[-3:] == 'csv':
        data.to_csv(fpath, index=False)
    elif fpath[-3:] == 'pkl':
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)
            
            
def save_file(data, fname, dname):
    """Save a datafile (data) to a specific location (dname) and filename (fname)
    
    Currently valid formats are limited to CSV or PKL."""
    
    if not os.path.exists(dname):
        os.mkdir(dname)
        print(f'Directory {dname} was created.')
        
    fpath = os.path.join(dname, fname)
    
    
    if os.path.exists(fpath):
        print("A file already exists with this name.\n")

        yesno = None
        while yesno != "Y" and yesno != "N":
            yesno = input('Do you want to overwrite? (Y/N)').strip()[0].capitalize()
            if yesno == "Y":
                print(f'Writing file.  "{fpath}"')
                _save_file(data, fpath)
                break  # Not required
            elif yesno == "N":
                print('\nPlease re-run this cell with a new filename.')
                break  # Not required
            else:
                print('\nUnknown input, please enter "Y" or "N".')

    else:  # path does not exist, ok to save the file
        print(f'Writing file.  "{fpath}"')
        _save_file(data, fpath)
        
        
        
        
        
        
def _save_file(data, fpath):
    valid_ftypes = ['.csv', '.pkl']
    
    assert (fpath[-4:] in valid_ftypes), "Invalid file type.  Use '.csv' or '.pkl'"

    # Figure out what kind of file we're dealing with by name
    if fpath[-3:] == 'csv':
        data.to_csv(fpath, index=False)
    elif fpath[-3:] == 'pkl':
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)
            
            
# def to_pickle(data, fpath):
#     valid_ftypes = ['.csv','.pkl','.joblib']
    
#     assert(fpath[:-4] in valid_fypes), "Invalid file type. Use '.csv' or '.pkl' or '.joblib'"
    
#     if fpath[-3] =='csv':
#         data.to_csv(fpath, index=False)
#     elif fpath[-3] == 'pkl':
#         with open(fpath, 'wb') as f:
#             pickle.dump(data, f)
#     elif fpath[-6] =='joblib':
#         with open(fpath, 'wb') as f:
#             dump(data, )
            
# def save_file(data, fname, dname):
    
#     if not os.path.exists(dname):
#         os.mkdir(dname)
#         print(f'Directory {dname} was created.')
        
#     fpath = os.path.join(dname,fname)
    
#     if os.path.exists(fpath):
#         print(" A file already exists with this name.\n")
        
#         yesno = None
#         while yesno != "Y" and yesno !="N":
#             yesno = input('Do you want to override? (Y/N)').strip()[0].capitalize()
#             if yesno =="Y":
#                 print(f'Writing file. "{fpath}"')
#                 _save_file(data, fpath)
#             elif yeno =="N":
#                 print('\nPlease re-run this cell with new filename.')
#             else:
#                 print('\nUnknown input, please enter "Y" or "N".')
                
#     else:
#         print(f'Writing file. "{fpath}"')
#         _save_file(data, fpath)
        
        
# def _safe_file(data, fpath):
#     valid_ftypes = ['.csv','.pkl','.joblib']
    
#     assert(fpath[:-4] in valid_fypes), "Invalid file type. Use '.csv' or '.pkl' or '.joblib'"
    
#     if fpath[-3] =='csv':
#         data.to_csv(fpath, index=False)
#     elif fpath[-3] == 'pkl':
#         with open(fpath, 'wb') as f:
#             pickle.dump(data, f)
#     elif fpath[-6] =='joblib':
#         with open(fpath, 'wb') as f:
#             dump(data, )