import { useState, useEffect } from 'react'
import '../styles/components/basecard.css'
import backendURL from '../config';
import { CircularProgress } from '@mui/material';
import Typography from '@mui/material/Typography';

interface BaseCardProps {

    title: string;


}

function YoutubePlay(props: BaseCardProps) {
    const [link, setLink] = useState('')
    const [loading, setLoading] = useState<boolean>(false)
    const [Success, setSuccess] = useState<boolean>(false)
    const [failed, setFailed] = useState<boolean>(false)

    const uploadLink = () => {
        setLoading(true)
        setSuccess(false)
        setFailed(false)
        fetch(`${backendURL}/audio/yt?link=${link}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                "ngrok-skip-browser-warning": "69420"
            }
        }).then(res => res.json())
            .then(data => {
                if (data["success"]) {
                    setLoading(false)
                    setSuccess(true)
                } else {
                    setLoading(false)
                    setFailed(true)
                }
            })
    }

    return (
        <>
            <div className='audioUploadCard'>
                <h1 className='cardTitle audioTitle'>{props.title}</h1>
                <div className='buttonAndProgressContainer'>
                    <div style={{
                        display: 'flex',
                        width: '100%',
                        height: '7em',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexDirection: 'column'
                    }}>
                        {loading && (
                            <div style={{
                                height: '5em',
                            }}>
                                <CircularProgress style={{
                                    color: '#5d00ff88',
                                }} />
                                <div>Audio Playing...</div>
                            </div>
                        )

                        }
                        {Success &&
                            (<Typography style={{
                                display: 'flex',
                                alignItems: 'center',
                            }} variant='h6' fontStyle={"bold"}>
                                Audio Played Successfully
                            </Typography>
                            )}
                        {failed && (<Typography>
                            Audio Failed to Play
                        </Typography>)}
                        <input
                            type="text"
                            placeholder="Enter Youtube Link"
                            onChange={(e) => {
                                setLink(e.target.value)
                            }}
                            style={{
                                width: '75%',
                                height: '2em',
                                border: 'none',
                                borderRadius: '5px',
                                padding: '0.5em',
                            }}></input>
                    </div>

                </div>
                <button className="audioButton" onClick={uploadLink}>Upload and Play</button>

            </div>
        </>
    )
}

export default YoutubePlay
