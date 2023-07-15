
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import '../styles/bgimage.css'
import bgpeaks from '../static/background/peaks-bg.svg'
import { useState, useEffect } from 'react'
import AudioUpload from '../components/AudioUpload'
import backendURL from '../config'

const relayIds = [
  "Fan 1",
  "Light 1",
  "Light 2",
  "Misc appliance",
]
function Homepage() {
  // const app = initializeApp(firebaseConfig);
  // const analytics = getAnalytics(app);
  const [relayStates, setRelayState] = useState([])
  async function syncStates() {
    fetch(`${backendURL}/relay/all`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        "ngrok-skip-browser-warning": "69420"
      }
    })
      .then(res => res.json())
      .then(data => {
        setRelayState(data["relayState"]);
      });
  }
  useEffect( ()=>{
    syncStates()

    const timer = setInterval(syncStates, 3000)
    return () => clearInterval(timer)
  }, [])

  useEffect(() => {
  }, [relayStates])

// TODO Look into something called an error boundary
  return (
    <div  style={{
      width: '100vw',
      height: '100vh',
      display: 'flex',
      flexDirection: 'column',
      flexWrap: 'wrap',
      alignContent: 'center',
      justifyContent: 'center',
      alignItems: 'center',
      background: `url(${bgpeaks})  center center no-repeat `,
      backgroundSize: 'cover',
    }}>
      <div className='cardContainer'>
        {
          relayStates.map((relay, index) => (
            <BaseCard 
              key={index}
              title={`${relayIds[index]}`}
              applianceId={relay[0]}
              status={relay[1] === 1}
            />
          ))
        }
        <AudioUpload />
      </div>
    </div>
  )
}

export default Homepage
