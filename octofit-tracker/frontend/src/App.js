
import './App.css';

import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from '../public/logo192.png';

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center fw-bold fs-3" to="/">
            <img src={logo} alt="OctoFit Logo" className="octofit-logo me-2" />
            OctoFit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><Link className="nav-link fs-5" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link fs-5" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link fs-5" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link fs-5" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link fs-5" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-4">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card shadow p-4 text-center">
              <h1 className="display-4 mb-3">Welcome to <span className="text-primary">OctoFit Tracker</span>!</h1>
              <p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p>
              <div className="d-flex justify-content-center gap-3 mt-4">
                <Link to="/activities" className="btn btn-primary btn-lg">View Activities</Link>
                <Link to="/leaderboard" className="btn btn-outline-primary btn-lg">Leaderboard</Link>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
