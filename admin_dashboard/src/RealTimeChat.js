import React, { useState, useEffect } from 'react';
import firebase from 'firebase/app';
import 'firebase/firestore';
import firebase from 'firebase/app';
import 'firebase/messaging';



// Request permission to receive notifications
const messaging = firebase.messaging();
messaging.requestPermission()
  .then(function () {
    console.log('Notification permission granted.');
    // Get the token in your client app
    return messaging.getToken();
  })
  .then(function (token) {
    console.log('Token obtained:', token);
    // Send the token to your server to send notifications later
  })
  .catch(function (err) {
    console.log('Unable to get permission to notify.', err);
  });

const RealTimeChat = ({ groupId }) => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const unsubscribe = firebase.firestore()
      .collection('groups')
      .doc(groupId)
      .collection('messages')
      .orderBy('timestamp', 'desc')
      .onSnapshot(snapshot => {
        setMessages(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() })));
      });

    return () => unsubscribe();
  }, [groupId]);

  // Implement CRUD operations for Messages here
  // Example: deleteMessage, updateMessage, sendMessage

  return (
    <div>
      <h2>Real-Time Chat</h2>
      <ul>
        {messages.map(message => (
          <li key={message.id}>
            <p>{message.text}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export { RealTimeChat };