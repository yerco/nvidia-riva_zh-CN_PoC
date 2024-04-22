import React, {useEffect, useState, useRef, useContext} from "react";
import { TextField, Button, Typography, Paper } from '@mui/material';
import Stack from '@mui/material/Stack';
import { SocketContext } from '../contexts/SocketContext';
import { TextFetcher } from "./TextFetcher";

export function STListener({ character }) {
    const [transcript, setTranscript] = useState("");
    // const [autoSubmit, setAutoSubmit] = useState(false);
    const [ttsEnabled, setTtsEnabled] = useState(false);
    const audioRef = useRef(null);
    const socket = useContext(SocketContext);

    const initializeEventSource  = () => {
        const eventSource = new EventSource('http://127.0.0.1:5001/stream/1');

        eventSource.onmessage = function(event) {
            // This will handle messages that don't have a specified event type
            console.log('New message received:', event.data);
        };

        eventSource.addEventListener("intermediate-transcript", function(e) {
            console.log('Intermediate transcript:', e.data);
            setTranscript(e.data);
        }, false);

        eventSource.addEventListener("finished-speaking", function(e) {
            console.log('Finished speaking:', e.data);
            setTranscript(e.data);
            /*if (autoSubmit) {
                // Trigger any submit action
                console.log("Auto-submitting because the checkbox is checked.");
            }*/
        }, false);

        eventSource.onerror = function(event) {
            if (event.currentTarget.readyState === EventSource.CLOSED) {
                console.log('EventSource closed by the server, trying to reconnect...');
                eventSource.close(); // Clean up the old eventSource
                // setTimeout(initializeEventSource, 1000); // Try to reconnect after 1 second
            } else {
                console.log('Error detected:', event);
            }
        };

        return () => {
            console.log('Closing EventSource...');
            eventSource.close();  // Clean up the event source if the component unmounts
        };
    };

    useEffect(() => {
        return initializeEventSource(); // This function is called by React on component unmount
    }, []); // Empty dependency array ensures this effect runs only once on mount

    const handleTtsToggle = () => {
        if (!ttsEnabled) {
            // Generate a unique URL each time to bypass browser cache
            const uniqueSrc = `http://localhost:5001/audio?${new Date().getTime()}`;
            audioRef.current.src = uniqueSrc;  // Set the new unique source
            audioRef.current.load();  // Load the new source
            // Start TTS
            console.log("TTS Play button clicked");
            setTtsEnabled(true);
            // Implement the socket emit and audio playing logic here
            socket.emit("start_tts", { "user_conversation_index": 1 });

            const playPromise = audioRef.current.play();

            playPromise.then(() => {
                console.log("Audio playback started successfully.");
                setTtsEnabled(false)
            }).catch(error => {
                console.error("Failed to start playback:", error);
                setTtsEnabled(false);  // Revert state if playback fails
            });
        } else {
            // Stop TTS
            console.log("TTS Stop button clicked");
            if (audioRef.current) {
                audioRef.current.pause();
                console.log("Audio playback paused successfully.");
            }
            setTtsEnabled(false);
        }
    };

    return (
        <Paper elevation={3} sx={{padding: 2, margin: '24px 0', backgroundColor: '#f5f5f5'}}>
            <Typography variant="h6" gutterBottom>
                Real-time Transcription
            </Typography>
            <TextField
                fullWidth
                multiline
                variant="outlined"
                value={transcript}
                onChange={(e) => setTranscript(e.target.value)}
                placeholder="Transcripts will appear here..."
                InputProps={{
                    style: {fontFamily: 'monospace'},
                }}
                sx={{marginBottom: 2}}
            />
            <Typography variant="subtitle1" gutterBottom>
                You said: {transcript}
            </Typography>
            <audio src="http://localhost:5001/audio" ref={audioRef} id="audio-tts" preload="none" allow="autoplay" type="audio/x-wav;codec=pcm">
                Your browser does not support the audio element.
            </audio>
            <Stack spacing={2}>
                <Button
                    onClick={handleTtsToggle}
                    variant="contained"
                    color="primary"
                    sx={{mt: 2}}
                >
                    {ttsEnabled ? "Mute" : "Speak"}
                </Button>
                <Typography variant="h8" gutterBottom>
                    Translation to English below ↓
                </Typography>
                <TextFetcher />
            </Stack>
        </Paper>
    );
}
