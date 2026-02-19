import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Teams from './components/Teams';
import Users from './components/Users';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <img src="/octofitapp-small.png" alt="OctoFit Logo" height="40" className="me-2" />
            <span className="fw-bold">OctoFit Tracker</span>
          </Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={
          <div className="container mt-4">
            <div className="hero-section text-center">
              <h1 className="display-3">🏋️ Welcome to OctoFit Tracker!</h1>
              <p className="lead">Track your fitness activities, compete with teams, and achieve your goals.</p>
              <hr className="my-4 bg-white" />
              <p className="mb-4">Join the fitness revolution and start tracking your progress today!</p>
            </div>
            
            <div className="row mt-4">
              <div className="col-md-4 mb-4">
                <div className="card text-center h-100">
                  <div className="card-body">
                    <div className="mb-3" style={{fontSize: '3rem'}}>🏆</div>
                    <h5 className="card-title">Teams</h5>
                    <p className="card-text text-muted">Join a team and compete together to reach fitness goals.</p>
                    <Link to="/teams" className="btn btn-primary">View Teams</Link>
                  </div>
                </div>
              </div>
              
              <div className="col-md-4 mb-4">
                <div className="card text-center h-100">
                  <div className="card-body">
                    <div className="mb-3" style={{fontSize: '3rem'}}>🏃</div>
                    <h5 className="card-title">Activities</h5>
                    <p className="card-text text-muted">Log your workouts and track your daily activities.</p>
                    <Link to="/activities" className="btn btn-primary">View Activities</Link>
                  </div>
                </div>
              </div>
              
              <div className="col-md-4 mb-4">
                <div className="card text-center h-100">
                  <div className="card-body">
                    <div className="mb-3" style={{fontSize: '3rem'}}>🏅</div>
                    <h5 className="card-title">Leaderboard</h5>
                    <p className="card-text text-muted">See who's leading the pack in fitness achievements.</p>
                    <Link to="/leaderboard" className="btn btn-primary">View Leaderboard</Link>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="row mt-2">
              <div className="col-md-6 mb-4">
                <div className="card text-center h-100">
                  <div className="card-body">
                    <div className="mb-3" style={{fontSize: '3rem'}}>👥</div>
                    <h5 className="card-title">Users</h5>
                    <p className="card-text text-muted">Connect with fitness enthusiasts and track member progress.</p>
                    <Link to="/users" className="btn btn-outline-primary">View Users</Link>
                  </div>
                </div>
              </div>
              
              <div className="col-md-6 mb-4">
                <div className="card text-center h-100">
                  <div className="card-body">
                    <div className="mb-3" style={{fontSize: '3rem'}}>💪</div>
                    <h5 className="card-title">Workouts</h5>
                    <p className="card-text text-muted">Get personalized workout suggestions for all fitness levels.</p>
                    <Link to="/workouts" className="btn btn-outline-primary">View Workouts</Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        } />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
