import { useState, useEffect } from 'react'
import '../styles/components/basecard.css'
import backendURL from '../config';

interface BaseCardProps {
    key: number;
    title: string;
    status?: boolean;
    applianceId?: number;

}

function BaseCard(props: BaseCardProps) {

    const [status, setStatus] = useState(props.status)
    const [cardClass, setCardClass] = useState(status ? 'on' : 'off')

    useEffect(() => {
        console.log(props.status);
        setStatus(props.status);
      }, [props.status]);

    useEffect(() => {
        setCardClass(status ? 'on' : 'off')
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
