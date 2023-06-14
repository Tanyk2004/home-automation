import React from 'react'
import { useState, useEffect } from 'react'
import '../styles/components/basecard.css'
import { stat } from 'fs';


interface BaseCardProps {
    title: string;
    status?: boolean;
    applicaneId?: string;
    // todo: add applianceId based on which we can make api calls and get and put the status

}

const ON_COLOR = '#31FF3166'

function BaseCard(props: BaseCardProps) {

    const [status, setStatus] = useState(false)
    const [cardColor, setCardColor] = useState('#ffffffd4')

    useEffect(() => {

        

        setStatus(props.status || false)
        if ( status ) {
            setCardColor(ON_COLOR)
        } else {
            setCardColor('#ffffffd4')
        }
    },[])

    useEffect(() => {
        console.log(status)
        if ( status ) {
            document.documentElement.style.setProperty('--card-background-color', ON_COLOR)
        }
        else {
            document.documentElement.style.setProperty('--card-background-color', '#FFFFFF66')
        }
        
    }, [status])

    const handleOn = () => {
        setStatus(true)
        setCardColor(ON_COLOR)
    }
    const handleOff = () => {
        setStatus(false)
        setCardColor('#ffffff')
    }


    return (
        <div className="baseCardContainer on">
            <h1 className='cardTitle'>{props.title}</h1>
            <div className="cardButtonContainer">
                <button className='cardButton' id='onButton' onClick={handleOn}><h2>On</h2></button>
                <button className='cardButton' id='offButton' onClick={handleOff}><h2>Off</h2></button>
            </div>
        </div>
    )
}

export default BaseCard
