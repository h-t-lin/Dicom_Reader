import os
from pydicom import dcmread
from utils import DicomFinder, make_dir_if_not_exist


def main():

    print('*\n*\n----START----\n')

    # TODO
    # set input and output folder path
    outmainfolder = ""
    infolder = ""
    cmd = {
        # TODO
        # set path of dcm2niix.exe
        'exe': 'C:\\Users\\...\\MRIcroGL\\Resources\\dcm2niix',
        'para': '-a n -z n'
    }

    make_dir_if_not_exist(outmainfolder)

    dicom_path_dict = DicomFinder(infolder)
    for dcm in dicom_path_dict:
        # read dicom header
        dicom_info = dcmread(dcm['path'])
        MOD = dicom_info.Modality

        # create subfolder of the modality
        outfolder = os.path.join(outmainfolder, MOD)
        make_dir_if_not_exist(outfolder, False)

        # execute the dcm2niix command line
        command = f'{cmd["exe"]} {cmd["para"]} -f {dcm["subject"]} -o \"{outfolder}\" \"{dcm["folder"]}\"'
        print(f'\nConverting {MOD} of {dcm["subject"]}...')
        os.system(command)

    print('*\n*\n----FINISHED----\n')


if __name__ == "__main__":
    main()
