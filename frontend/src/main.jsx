import React, { useState } from 'react'
import { createRoot } from 'react-dom/client'

const API = 'http://localhost:8000'

function App() {
  const [token, setToken] = useState('')
  const [email, setEmail] = useState('admin@example.com')
  const [password, setPassword] = useState('admin12345')
  const [routers, setRouters] = useState([])

  async function login() {
    const r = await fetch(`${API}/auth/login`, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({email, password})})
    const j = await r.json(); if (j.access_token) setToken(j.access_token)
  }

  async function loadRouters() {
    const r = await fetch(`${API}/routers`, { headers:{Authorization:`Bearer ${token}`}})
    setRouters(await r.json())
  }

  return <main style={{fontFamily:'sans-serif',maxWidth:900,margin:'2rem auto'}}>
    <h1>Retech Full Control Panel</h1>
    <p>Login:</p>
    <input value={email} onChange={e=>setEmail(e.target.value)} />
    <input value={password} onChange={e=>setPassword(e.target.value)} type='password' />
    <button onClick={login}>Entrar</button>
    <button onClick={loadRouters} disabled={!token}>Cargar Routers</button>
    <pre>{JSON.stringify(routers,null,2)}</pre>
  </main>
}

createRoot(document.getElementById('root')).render(<App />)
