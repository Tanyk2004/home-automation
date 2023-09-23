
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import '../styles/bgimage.css'
import bgpeaks from '../static/background/peaks-bg.svg'
import { useState, useEffect } from 'react'
import AudioUpload from '../components/AudioUpload'
import YoutubePlay from '../components/YoutubePlay'
import backendURL from '../config'
import { Skeleton } from '@mui/material';

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
  const [backendUp, setBackendUp] = useState(false)
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
        setBackendUp(true)
        setRelayState(data["relayState"]);
      })
      .catch((err) => {
        console.log(err);
        setBackendUp(false)
        console.log("Backend is down")

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
          backendUp ? relayStates.map((relay, index) => (
            <BaseCard 
              key={index}
              title={`${relayIds[index]}`}
              applianceId={relay[0]}
              status={relay[1] === 1}
            />
          )) : <div className='skeletonContainer'>
            <div></div>
            <Skeleton animation="wave" variant="rounded" width={450} height={60} />
            <Skeleton animation="wave" variant="rounded" width={80} height={70} />
            <Skeleton animation="wave" variant="rounded" width={450} height={100} />
            </div>
          
        }
        <AudioUpload />
        <YoutubePlay title="Play Audio From Youtube"/>
      </div>
    </div>
  )
}

export default Homepage
