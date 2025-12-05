import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : '/api/activities/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', results);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <ul className="list-group">
        {activities.map((a, i) => (
          <li className="list-group-item" key={a.id || i}>{JSON.stringify(a)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;
