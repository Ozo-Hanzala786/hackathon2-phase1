import Link from 'next/link'

export default function Home() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>Todo Web Application</h1>
      <p>Welcome to the secure todo application with user authentication.</p>
      <nav>
        <ul>
          <li><Link href="/login">Login</Link></li>
          <li><Link href="/signup">Sign Up</Link></li>
          <li><Link href="/dashboard">Dashboard</Link></li>
        </ul>
      </nav>
    </div>
  )
}