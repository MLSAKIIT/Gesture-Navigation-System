const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');

function onResults(results) {
    canvasCtx.save();
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(
        results.image, 0, 0, canvasElement.width, canvasElement.height);
    if (results.multiHandLandmarks) {
        for (const landmarks of results.multiHandLandmarks) {
            // HOVERING
            let backDist = Math.sqrt(
                Math.pow((landmarks[8].x - landmarks[4].x)*canvasElement.width, 2) +
                Math.pow((landmarks[8].y - landmarks[4].y)*canvasElement.height, 2)
            )
            let frwdDist = Math.sqrt(
                Math.pow((landmarks[8].x - landmarks[12].x)*canvasElement.width, 2) +
                Math.pow((landmarks[8].y - landmarks[12].y)*canvasElement.height, 2)
            )
            if(backDist < 20){
                window.history.back()
            }
            else if (frwdDist<40){
                window.history.forward();
            }
            drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
                {color: '#00FF00', lineWidth: 5});
            drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
        }
    }
    canvasCtx.restore();
}

const hands = new Hands({locateFile: (file) => {
        return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
    }});
hands.setOptions({
    maxNumHands: 2,
    modelComplexity: 1,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5
});
hands.onResults(onResults);

const camera = new Camera(videoElement, {
    onFrame: async () => {
        await hands.send({image: videoElement});
    },
    width: 1280,
    height: 720
});
camera.start();