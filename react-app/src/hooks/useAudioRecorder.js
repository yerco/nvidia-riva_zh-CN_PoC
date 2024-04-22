import { useState, useCallback, useContext } from 'react';
import { SocketContext } from '../contexts/SocketContext';

const processorUrl = `${process.env.PUBLIC_URL}/myapp-audio-processor.js`;

export const useAudioRecorder = () => {
    const [audioContext, setAudioContext] = useState(null);
    const [isRecording, setIsRecording] = useState(false);
    const socket = useContext(SocketContext);

    const startRecording = useCallback(async () => {
        // Initialize audio context
        const context = new AudioContext();
        await context.audioWorklet.addModule(processorUrl);  // Load the processor
        const processor = new AudioWorkletNode(context, 'myapp-audio-processor');

        processor.port.onmessage = (event) => {
            socket.emit('audioIn', { data: event.data.buffer });
            //console.log("Data received from processor: ", event.data.buffer );
        };

        // Connect the processor to context
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const source = context.createMediaStreamSource(stream);
        source.connect(processor);
        processor.connect(context.destination);

        setAudioContext(context);
        setIsRecording(true);
    }, [isRecording]);

    const stopRecording = useCallback(async () => {
        try {
            await audioContext.close();
            console.log("Audio context closed and resources released");
            setAudioContext(null);
            setIsRecording(false);
        } catch (error) {
            console.error("Error closing audio context:", error);
        }
    }, [audioContext]);

    return { isRecording, startRecording, stopRecording };
};
