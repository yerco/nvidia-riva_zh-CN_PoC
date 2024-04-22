import React, { useState, useEffect } from 'react';
import { Typography, Box, CircularProgress, LinearProgress } from '@mui/material';

import { useAudioRecorder} from "../hooks/useAudioRecorder";
import { STListener } from "./STListener";

const characters = ['汉语', '名字', '词典', '语言', '音乐', '车票', '自己', '好看', '厉害', '上海', '北京'];
// 'Hàn', 'zì', 'cí', 'yǔ', 'yīn', 'shēng', 'wén', 'zì', 'fú', 'hào'

function STSection() {
    const [isActive, setIsActive] = useState(false)
    const [seconds, setSeconds] = useState(5)
    const [level, setLevel] = useState(1)
    // const [score, setScore] = useState(null);
    const [character, setCharacter] = useState('汉')
    const playTime = 5;
    const { isRecording, startRecording, stopRecording } = useAudioRecorder();

    useEffect(() => {
        let timer = null;

        if (isActive) {
            if (seconds > 0) {
                timer = setInterval(() => {
                    setSeconds(prevSeconds => prevSeconds - 1);
                }, 1000);
            } else {
                clearInterval(timer);
                // Immediately invoke an async function to handle the stop
                (async () => {
                    await handleStop(); // Ensure we stop recording when time runs out
                })();
            }
        }
        return () => clearInterval(timer);
    }, [isActive, seconds]);

    const getRandomCharacter = () => {
        const randomIndex = Math.floor(Math.random() * characters.length);
        return characters[randomIndex];
    };

    const handleStart = async () => {
        try {
            setCharacter(getRandomCharacter());
            await startRecording();
            setIsActive(true);
            setSeconds(playTime); // Reset timer on start
        } catch (error) {
            console.error('Failed to start recording:', error);
        }
    };

    const handleStop = async () => {
        try {
            await stopRecording();
        } catch (error) {
            console.error('Failed to stop recording:', error);
        }
        setIsActive(false);
    };

    const handleStartStop = async () => {
        if (!isActive) {
            await handleStart();
        } else {
            await handleStop();
        }
    };

    return (
        <Box sx={{padding: 4, textAlign: 'center'}}>
            <Typography variant="h1" gutterBottom>
                {character}
            </Typography>
            <CircularProgress variant="determinate" value={isActive ? 100 * seconds / playTime : 0} size={50}
                              sx={{color: isActive ? 'green' : 'red'}}/>
            <Typography variant="body1">
                {isActive ? 'Mic is ON' : 'Mic is OFF'}
            </Typography>
            <Box sx={{marginY: 2}}>
                <LinearProgress variant="determinate" value={100 - playTime * seconds}/>
            </Box>
            <Typography variant="body2">
                Level: {level}
            </Typography>
            {/*<Typography variant="body2">
                Score: {score ? `${score}%` : 'N/A'}
            </Typography>*/}
            <button onClick={handleStartStop}>
                {isActive ? 'Stop' : 'Start'}
            </button>
            <STListener character={character}/>
        </Box>
    );
}

export default STSection;
