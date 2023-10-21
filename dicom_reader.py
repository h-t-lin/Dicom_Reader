import os
import pandas as pd
from pydicom import dcmread
from utils import DicomFinder


def main():

    print('*\n*\n----START----\n')

    # TODO
    # Set input and output folder path.
    # Specify certain modality and dicom attributes you want to extract.
    outfolder = ""
    infolder = ""
    MODALITY = 'PT'
    HEADERS = [
        'AcquisitionDate',
        'Modality',
    ]

    dicom_path_dict = DicomFinder(infolder)
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
            print(f'Reading {dcm["subject"]}.')
    
    # export excel file
    print('\nExporting excel...')
    df = pd.DataFrame(data)
    df.to_excel(os.path.join(outfolder, 'dcminfo.xlsx'), sheet_name=MODALITY, index=False)

    print('*\n*\n----FINISHED----\n')


if __name__ == "__main__":
    main()
