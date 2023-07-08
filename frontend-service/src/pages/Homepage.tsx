
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import '../styles/bgimage.css'
import bgpeaks from '../static/background/peaks-bg.svg'
import { useState, useEffect } from 'react'
// import backendURL from '../config';
import { initializeApp } from "firebase/app";
import backendURL from '../config'
// import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyBHkc0sPaq9aorqoKp0BaIv7kVARYRiY0Q",
  authDomain: "homeauto-a855f.firebaseapp.com",
  projectId: "homeauto-a855f",
  storageBucket: "homeauto-a855f.appspot.com",
  messagingSenderId: "611237202110",
  appId: "1:611237202110:web:466d7f8e5454e68d2eb6ef",
  measurementId: "G-D2LERSPS0R"
};
function Homepage() {
  const app = initializeApp(firebaseConfig);
  // const analytics = getAnalytics(app);

  useEffect( ()=>{
  //   fetch( `${`${backendURL}`}/relay/all` , {
  //     method: 'GET',
  //     headers: {
  //         'Content-Type': 'application/json',
  //         'ngrok-'
  //     }
  //   })
  //   .then ( res => res.json())
  //   .then ( data => {
  //     console.log(data)
  // })
  }, [])

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
        <BaseCard title='Light 1' applianceId={22} />
        <BaseCard title='Light 2' applianceId={17} />
        <BaseCard title='Fan 1' applianceId={4} />
      </div>
    </div>
  )
}

export default Homepage
