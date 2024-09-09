import os
import pandas as pd
from pydicom import dcmread
from utils import DicomFinder


def main():

    print('*\n*\n----START----\n')

    '''
    Path format example:
    inmainfolder >> 
        # all series of Dicom are saved in "inmainfolder"
        | series01 >> 
            | 001.dcm
            | 002.dcm
            | ...
        | series02
            | 001.dcm
            | 002.dcm
            | ...
        | series03
        | ...
    
    outfolder >> 
        # The output excel will be saved in "outmainfolder"
        | tempinfo.xlsx
        | ...
    '''
    # TODO: 
    # Set input and output folder path.
    # Specify certain modality and dicom attributes you want to extract.
    outfolder = ""
    inmainfolder = ""
    MODALITY = 'PT'
    HEADERS = [
        'AcquisitionDate',
        'Modality',
    ]

    assert os.path.isdir(inmainfolder), 'Wrong path of dicom folder'
    dicom_path_dict = DicomFinder(inmainfolder)
    data = []
    for dcm in dicom_path_dict:
        # read dicom header
        dicom_info = dcmread(dcm['path'])
        if dicom_info.Modality == MODALITY:
            infodict = {}
            for hdr in HEADERS:
                if hdr in dicom_info:
                    infodict[hdr] = dicom_info[hdr].value
            data.append(infodict)

    # export excel file
    assert len(data)!=0, 'Find No File'
    df = pd.DataFrame(data)
    df.to_excel(os.path.join(outfolder, 'tempinfo.xlsx'), sheet_name=MODALITY, index=False)

    print('*\n*\n----FINISHED----\n')
    print(df)


if __name__ == "__main__":
    main()
