import os
# import dicom2nifti.compressed_dicom as compressed_dicom
# import dicom2nifti.settings
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
    
    outmainfolder >> 
        # Nifti of all series will be saved in "outmainfolder"
        | sereis01.nii
        | sereis02.nii
        | sereis03.nii
        | ...
    '''
    # TODO: Define input and output folder path
    outmainfolder = ""
    inmainfolder = ""
    cmd = {
        # TODO: set path of dcm2niix.exe
        'exe': 'C:\\Users\\...\\MRIcroGL\\Resources\\dcm2niix',
        'para': '-a n -z n'
    }

    os.makedirs(outmainfolder, exist_ok=True)

    dicom_path_dict = DicomFinder(inmainfolder)
    for dcm in dicom_path_dict:
        # read dicom header
        dicom_info = dcmread(dcm['path'])
        MOD = dicom_info.Modality

        # create subfolder of the modality
        outfolder = os.path.join(outmainfolder, MOD)
        os.makedirs(outfolder, exist_ok=True)

        # execute the dcm2niix command line
        command = f'{cmd["exe"]} {cmd["para"]} -f {dcm["subject"]} -o \"{outfolder}\" \"{dcm["folder"]}\"'
        print(f'\nConverting {MOD} of {dcm["subject"]}...')
        os.system(command)

    print('*\n*\n----FINISHED----\n')


if __name__ == "__main__":
    main()
