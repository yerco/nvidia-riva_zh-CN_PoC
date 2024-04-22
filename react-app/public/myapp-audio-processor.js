// AudioWorkletNode has a fixed buffer size of 128
class MyAppAudioProcessor extends AudioWorkletProcessor {
    constructor() {
        super();
        this.sampleFrameSize = 4096;  // Accumulate this many samples before processing
        this.sampleBuffer = new Float32Array(this.sampleFrameSize);
        this.currentIndex = 0;
    }

    process(inputs, outputs, parameters) {
        const input = inputs[0];
        const output = outputs[0];
        const channelData = input[0];

        if (channelData) {
            // Accumulate samples until we reach the desired frame size
            for (let i = 0; i < channelData.length; i++) {
                this.sampleBuffer[this.currentIndex++] = channelData[i];
                if (this.currentIndex >= this.sampleFrameSize) {
                    // Process the accumulated buffer
                    const outputData = this.floatTo16Bit(this.sampleBuffer);
                    // console.log("This is outputData", outputData);
                    this.port.postMessage(outputData);
                    this.currentIndex = 0;  // Reset for next accumulation
                }
            }
        }

        return true;
    }

    floatTo16Bit(inputArray) {
        const output = new Int16Array(inputArray.length / 3);
        for (let i = 0; i < inputArray.length; i += 3) {
            let s = Math.max(-1, Math.min(1, inputArray[i]));
            output[i / 3] = s < 0 ? s * 0x8000 : s * 0x7fff;
        }
        return output;
    }
}

registerProcessor('myapp-audio-processor', MyAppAudioProcessor);
