import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching workouts from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data received:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3">Loading workouts...</p>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>💪 Workout Suggestions</h2>
      </div>
      <div className="row">
        {workouts.map((workout) => (
          <div key={workout.id} className="col-md-6 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <div className="mb-3">
                  <span className={`badge ${workout.difficulty === 'beginner' ? 'bg-success' : workout.difficulty === 'intermediate' ? 'bg-warning text-dark' : 'bg-danger'}`}>
                    {workout.difficulty ? workout.difficulty.charAt(0).toUpperCase() + workout.difficulty.slice(1) : 'N/A'}
                  </span>
                  {' '}
                  <span className="badge bg-info">{workout.category}</span>
                </div>
                <p className="card-text text-muted">{workout.description}</p>
                <hr />
                <div className="d-flex justify-content-between mb-3">
                  <div>
                    <small className="text-muted">Duration</small>
                    <p className="mb-0"><strong>{workout.duration_minutes} min</strong></p>
                  </div>
                  <div>
                    <small className="text-muted">Difficulty</small>
                    <p className="mb-0"><strong>{workout.difficulty ? workout.difficulty.charAt(0).toUpperCase() + workout.difficulty.slice(1) : 'N/A'}</strong></p>
                  </div>
                </div>
                {workout.exercises && Array.isArray(workout.exercises) && workout.exercises.length > 0 && (
                  <div>
                    <strong>Exercises:</strong>
                    <ul className="list-group list-group-flush mt-2">
                      {workout.exercises.map((exercise, index) => (
                        <li key={index} className="list-group-item">
                          {exercise.name} 
                          {exercise.sets && exercise.reps && ` - ${exercise.sets} sets x ${exercise.reps} reps`}
                          {exercise.duration && ` - ${exercise.duration}`}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Workouts;
