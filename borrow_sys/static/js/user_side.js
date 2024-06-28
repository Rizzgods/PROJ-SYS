// user_side.js

(function() {
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var fileName = document.getElementById('Name')
    var captureButton = document.getElementById('capture');
    var saveButton = document.getElementById('saveImage');
    var revertButton = document.getElementById('revert');
    var picInput = document.getElementById('pic');
    var capturedImage = document.getElementById('capturedImage');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(err) {
            console.log("An error occurred: " + err);
        });

    captureButton.addEventListener('click', function() {
        var width = video.videoWidth;
        var height = video.videoHeight;
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);
        canvas.classList.remove('hidden');
        video.classList.add('hidden');
        saveButton.classList.remove('hidden');
        captureButton.classList.add('hidden');
        revertButton.classList.remove('hidden');
    });

    saveButton.addEventListener('click', function() {
        canvas.toBlob(function(blob) {
            var fileName = document.getElementById('Name').value.trim();
            var file = new File([blob], fileName, { type: "image/png" });
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            picInput.files = dataTransfer.files;

            // Show the captured image
            var url = URL.createObjectURL(blob);
            capturedImage.src = url;
            capturedImage.classList.remove('hidden');
            canvas.classList.add('hidden');
            saveButton.classList.add('hidden');
            revertButton.classList.remove('hidden');
        });
    });

    revertButton.addEventListener('click', function() {
        capturedImage.classList.add('hidden');
        video.classList.remove('hidden');
        captureButton.classList.remove('hidden');
        saveButton.classList.add('hidden');
        revertButton.classList.add('hidden');
    });
})();
