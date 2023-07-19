import React, { ChangeEvent, useState } from 'react'
import backendURL from '../config';
import '../styles/components/audioupload.css'

function AudioUpload() {

    const [selectedFile, setSelectedFile] = useState<File | null>(null)

    const handldedSelectedFile = (event: ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0]
        setSelectedFile(file || null)
    };

    const handleUpload = () => {
        if (selectedFile) {
            const reader = new FileReader()


            reader.onload = (event) => {
                const fileData = event.target?.result
                const uintArray = new Uint8Array(fileData as ArrayBuffer)
                console.log("heyo")
                const dataArray = Array.from(uintArray)
                const base64Data = btoa(String.fromCharCode.apply(null, dataArray))

                // call the function that uploads data to the backend here
                fetch(`${backendURL}/audio/play`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'ngrok-skip-browser-warning': '69420',
                    },
                    body: JSON.stringify({
                        audioData: base64Data,
                    })
                }).then(res => res.json())
                    .then(data => {
                        console.log(data)
                    })

            }
            reader.readAsDataURL(selectedFile)
        }
    }
    return (
        <>
            <div className='audioUploadCard'>
                <h1 className='cardTitle'>Upload Audio</h1>
                <input className="audioInput" type="file" accept="audio/*" onChange={handldedSelectedFile} />
                <button className="audioButton" onClick={handleUpload}>Upload</button>
            </div>
        </>
    )
}

export default AudioUpload
