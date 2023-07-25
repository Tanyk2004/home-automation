import React, { ChangeEvent, useState } from 'react'
import backendURL from '../config';
import '../styles/components/audioupload.css'
import { CircularProgress } from '@mui/material';
import Typography from '@mui/material/Typography';
function AudioUpload() {

    const [selectedFile, setSelectedFile] = useState<File | null>(null)
    const [isFilePicked, setIsFilePicked] = useState<boolean>(false)
    const [loading, setLoading] = useState<boolean>(false)
    const [Success, setSuccess] = useState<boolean>(false)
    const [failed, setFailed] = useState<boolean>(false)
    const changeHandler = (event: ChangeEvent<HTMLInputElement>) => {
        setSelectedFile(event.target.files![0])
        setIsFilePicked(true)
    }

    const handleUpload = () => {
        setLoading(true)
        setSuccess(false)
        setFailed(false)
        if (isFilePicked) {
            const formData = new FormData()
            formData.append('audio', selectedFile!)
            fetch(`${backendURL}/audio/play`, {
                method: 'POST',
                body: formData
            })
                .then(response => response.json())
                .then(result => {
                    console.log('Success:', result);
                    setLoading(false)
                    if (result["success"]) {
                        setSuccess(true)
                    } else {
                        setFailed(true)
                    }

                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }
    return (
        <>
            <div className='audioUploadCard'>
                <h1 className='cardTitle'>Upload Audio (.wav)</h1>
                <div className='buttonAndProgressContainer'>
                    <div style={{
                        flex: 4,
                        width: '1em',
                       
                    }}>
                        <input formEncType='multipart/form-data' className="audioInput" type="file" accept="audio/wav" onChange={changeHandler} />
                    </div>
                    <div style={{
                        flex: 3,
                        marginLeft: '5em',
                        marginRight: '1em',
                    }}>
                        {loading && (<CircularProgress style={{
                            color: '#5d00ff88',
                        }}/>)}
                        {Success &&
                            (<Typography style={{
                                display: 'flex',
                                alignItems: 'center',
                            }}variant='h6' fontStyle={"bold"}>
                                Audio Played Successfully
                            </Typography>
                            )}
                        {failed && (<Typography>
                            Audio Failed to Play
                        </Typography>)}

                    </div>
                </div>
                <button className="audioButton" onClick={handleUpload}>Upload and Play</button>

            </div>
        </>
    )
}

export default AudioUpload
