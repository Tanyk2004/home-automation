
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import '../styles/bgimage.css'
import bgpeaks from '../static/background/peaks-bg.svg'
import { useState, useEffect } from 'react'
import backendURL from '../config';
function Homepage() {
  useEffect( ()=>{
    fetch("", {})
  }, [])

  return (
    <div  style={{
      width: '100vw',
      height: '100vh',
      display: 'flex',
      flexDirection: 'row',
      flexWrap: 'wrap',
      alignContent: 'center',
      justifyContent: 'center',
      alignItems: 'center',
      background: `url(${bgpeaks})  center center no-repeat `,
      backgroundSize: 'cover',
    }}>
      <div className='cardContainer'>
        <BaseCard title='Light 1' applianceId={22} />
        <BaseCard title='Light 2' applianceId={17} />
        <BaseCard title='Fan 1' applianceId={4} />
      </div>
    </div>
  )
}

export default Homepage
