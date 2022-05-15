# Medical Images Key Area Protection using Pixel Manipulation

## Base paper referenced: 
Reversible data hiding based key region protection method in medical images <br />
[https://ieeexplore.ieee.org/abstract/document/8983086](url) <br />
DOI: [http://dx.doi.org/10.1109/BIBM47256.2019.8983086](url)

## Other reference papers:
1. Medical Image Key Area Protection Scheme Based on QR Code and Reversible Data Hiding <br />
[https://www.hindawi.com/journals/scn/2021/5511806/](url) <br />
DOI: [https://doi.org/10.1155/2021/5511806](url)
2. Reversible data hiding in encrypted medical DICOM image <br />
[https://link.springer.com/article/10.1007/s00530-020-00739-5](url) <br />
DOI: [https://doi.org/10.1007/s00530-020-00739-5](url)
3. Reversible Data Hiding Based on Structural Similarity Block Selection <br />
[https://ieeexplore.ieee.org/abstract/document/8959154](url) <br />
DOI: [https://doi.org/10.1109/ACCESS.2020.2966515](url)
4. A pixel-based scrambling scheme for digital medical images protection <br />
[https://www.sciencedirect.com/science/article/abs/pii/S1084804509000423](url) <br />
DOI: [https://doi.org/10.1016/j.jnca.2009.02.009](url)

## Project code outline
Initial idea: <br />
_[/idea folder]_ <br />
This project involves hiding a diagnostic report in a medical scan using pixel manipulation, following which the processed image is blurred using a image blurring or distortion algorithm. 

Final project: <br />
_[/final folder]_ <br />
This project converts a diagnostic report to a QR code, allows user to manually identify the key area in a medical image, and embeds the QR onto the selected key area. The key area is extracted and  hidden in the resultant image using pixel manipulation, which subsequently blurs the QR code as well. This final output is both secure and hides the key area from public eyes.

## How to run
Both folders follow the same format to run the project. The python script named 'medical_encrypt.py' takes an input medical image and generates an encrypted output file which can be decrypted using the 'medical_decrypt.py' script.
