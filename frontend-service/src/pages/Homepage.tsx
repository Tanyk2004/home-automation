import React from 'react'
import BaseCard from '../components/BaseCard'
import '../styles/homepage.css'
import { useState, useEffect } from 'react'
function Homepage() {
  
  useEffect(() => {
    fetch("http://localhost:5000/")
      .then( res => res.json())
      .then( data => console.log(data["message"]))
  }, [])

  return (
    <div className='homepageContainer'>
      <BaseCard title='Light #1' />
    </div>
  )
}

export default Homepage
