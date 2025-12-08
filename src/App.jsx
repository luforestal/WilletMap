import React from 'react'
import TreeMap from './components/TreeMap'
import HomePage from './components/HomePage'
import './App.css'

function App() {
  // Check if we have a school parameter in URL
  const urlParams = new URLSearchParams(window.location.search)
  const schoolId = urlParams.get('school')
  
  return (
    <div className="App">
      {schoolId ? <TreeMap /> : <HomePage />}
    </div>
  )
}

export default App
