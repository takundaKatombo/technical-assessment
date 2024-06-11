import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GroupComposition = () => {
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    const fetchGroups = async () => {
      try {
        const response = await axios.get('/api/groups');
        setGroups(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchGroups();
  }, []);

  // Implement CRUD operations for Group data here
  // Example: deleteGroup, updateGroup, addGroup

  return (
    <div>
      <h2>Group Compositions</h2>
      {groups.map(group => (
        <div key={group.id}>
          <h3>{group.name}</h3>
          <ul>
            {group.members.map(member => (
              <li key={member.id}>{member.name}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export { GroupComposition };