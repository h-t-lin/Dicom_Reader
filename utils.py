import os

def DicomFinder(root):
    '''
    return: list of dictionaries.  
    > ```python
    dictionary = {
        'path':  path of dicom,
        'folder':  path of folder of dicoms,
        'subject':  name of subject
    }
    > ```
    '''
    if os.path.isdir(root):
        dcmlist = traverser(root, [], root)
        return dcmlist

def traverser(folder, dcmlist, root):
    if os.path.isdir(folder):
        filelist = os.listdir(folder)
        if len(filelist)==0:
            pass
        elif filelist[0].endswith('.dcm'):
            pathdict = {}
            pathdict['path'] = os.path.join(folder, filelist[0])
            pathdict['folder'] = folder
            pathdict['subject'] = subjectname(folder, root)
            dcmlist.append(pathdict)
        else:
            for subf in filelist:
                subpath = os.path.join(folder, subf)
                dcmlist = traverser(subpath, dcmlist, root)
    return dcmlist

def subjectname(folder, root):
    remain = folder[len(root):]
    return remain.split('\\')[1]