**Now python version is available!**  
Updating News:  
  -bug fixes  
  -stability enhancement  
  -add captions

---
---
# Dicom_Reader
> Read dicom headers, and convert headers to excel file.  
Implement on Matlab or Python.

# Dicom2Nifti
> Convert dicom to nifti.  
Implement on Python.  
Package requirements: pydicom=2.4.3, pandas  
Software requirements: MRIcroGL, can be downloaded from this website:
https://www.nitrc.org/projects/mricrogl

---
---
# Format of input dicom folder
```
inmainfolder >> 
    # all series of Dicom are saved in "inmainfolder"
    | series01 >> 
        | 001.dcm
        | 002.dcm
        | ...
    | series02 >>
        | 001.dcm
        | 002.dcm
        | ...
    | series03
    | ...

outmainfolder >> 
    # Nifti of all series will be saved in "outmainfolder
    | sereis01.nii
    | sereis02.nii
    | sereis03.nii
    | ...
```

---
---
*If there is any problem, please contact me.*
