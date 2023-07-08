import { useState, useEffect } from 'react'
import '../styles/components/basecard.css'
import backendURL from '../config';

interface BaseCardProps {
    title: string;
    status?: boolean;
    applianceId?: number;

}

const ON_COLOR = '#31FF3166'

function BaseCard(props: BaseCardProps) {

    const [status, setStatus] = useState(false)
    const [cardClass, setCardClass] = useState('off')


    useEffect(() => {
        console.log(status)
        if ( status ) {

        }
        else {
         
        }
        
    }, [status])

    const handleOn = () => {
        setStatus(true)
        setCardClass('on')

        fetch( `${backendURL}/relay/update` , {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              relayNumber: props.applianceId,
              relayState: true
            })
          })
          .then ( res => res.json())
          .then ( data => {
            if(data["success"] == true) {console.log(data["updatedRelayState"])}
            else {
                console.log(data)
            }
        })




    }
    const handleOff = () => {
        setStatus(false)
        setCardClass('off')

        
        fetch( `${backendURL}/relay/update` , {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              relayNumber: props.applianceId,
              relayState: false
            })
          })
          .then ( res => res.json())
          .then ( data => {
            if(data["success"] == true) {console.log(data["updatedRelayState"])}
            
        })

          
    }


    return (
        <div className={`baseCardContainer ${cardClass}`}>
            <h1 className='cardTitle'>{props.title}</h1>
            <div className="cardButtonContainer">
                <button className='cardButton' id='onButton' onClick={handleOn}><h2>On</h2></button>
                <button className='cardButton' id='offButton' onClick={handleOff}><h2>Off</h2></button>
            </div>
        </div>
    )
}

export default BaseCard
