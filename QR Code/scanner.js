const html5QrCode = new Html5Qrcode(/* element id */ "reader");

// File based scanning
const fileinput = document.getElementById('qr-input-file');
fileinput.addEventListener('change', e => {
  if (e.target.files.length == 0) {
    // No file selected, ignore 
    return;
  }

  // Use the first item in the list
  const imageFile = e.target.files[0];
  html5QrCode.scanFile(imageFile, /* showImage= */true)
  .then(qrCodeMessage => {
    // success, use qrCodeMessage
    console.log(qrCodeMessage);
  })
  .catch(err => {
    // failure, handle it.
    console.log(`Error scanning file. Reason: ${err}`)
  });
});

/**Use Html5Qrcode#scanFile() API to scan an image File.**/
/**
    * Scans an Image File for QR Code.
    * 
    * This feature is mutually exclusive to camera based scanning, you should call
    * stop() if the camera based scanning was ongoing.
    * 
    * @param {File} imageFile a local file with Image content.
    * @param {boolean} showImage if true the Image will be rendered on given element.
    * 
    * @returns Promise with decoded QR code string on success and error message on failure.
    *            Failure could happen due to different reasons:
    *            1. QR Code decode failed because enough patterns not found in image.
    *            2. Input file was not image or unable to load the image or other image load
    *              errors.
    */
 scanFile(imageFile, showImage /* default = true */)
 html5QrCode.clear();