import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserList = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {


        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const response = await axios.get('/admin/dashboard');
            setUsers(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const addUser = async (user) => {
        // Assuming user is an object with user details
        try {
            const response = await axios.post('/api/users', user);
            setUsers([...users, response.data]);
        } catch (error) {
            console.error(error);
        }
    };

    const updateUser = async (userId, updatedUser) => {
        try {
            await axios.put(`/api/users/${userId}`, updatedUser);
            fetchUsers(); // Refresh the list
        } catch (error) {
            console.error(error);
        }
    };

    const deleteUser = async (userId) => {
        try {
            await axios.delete(`/api/users/${userId}`);
            setUsers(users.filter((user) => user.id !== userId));
        } catch (error) {
            console.error(error);
        }
    };

    // Render your UserList component with the fetched users
    return (
        <div>
            <h2>User List</h2>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.name}</li>
                ))}
            </ul>
        </div>
    );
};

const GroupComposition = () => {
    const [groups, setGroups] = useState([]);

    useEffect(() => {


        fetchGroups();
    }, []);



    const fetchGroups = async () => {
        try {
            const response = await axios.get('/admin/dashboard');
            setGroups(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const addGroup = async (group) => {
        try {
            const response = await axios.post('/api/groups', group);
            setGroups([...groups, response.data]);
        } catch (error) {
            console.error(error);
        }
    };

    const updateGroup = async (groupId, updatedGroup) => {
        try {
            await axios.put(`/api/groups/${groupId}`, updatedGroup);
            fetchGroups(); // Refresh the list
        } catch (error) {
            console.error(error);
        }
    };

    const deleteGroup = async (groupId) => {
        try {
            await axios.delete(`/api/groups/${groupId}`);
            setGroups(groups.filter((group) => group.id !== groupId));
        } catch (error) {
            console.error(error);
        }
    };

    // Render your GroupComposition component with the fetched groups
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



const CombinedComponent = () => {
    return (
        <div>
            <UserList />
            <GroupComposition />
        </div>
    );
};

export default CombinedComponent;