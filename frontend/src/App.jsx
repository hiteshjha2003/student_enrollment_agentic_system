import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import ChatMessage from './components/ChatMessage';

const API_BASE_URL = 'http://localhost:8000/api';

function App() {
    const [userId, setUserId] = useState('');
    const [tempUserId, setTempUserId] = useState('');
    const [messages, setMessages] = useState([]);
    const [inputValue, setInputValue] = useState('');
    const [loading, setLoading] = useState(false);
    const [userIdSet, setUserIdSet] = useState(false);
    const messagesEndRef = useRef(null);

    // Auto-scroll to bottom when new messages arrive
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    // Set user ID
    const handleSetUserId = () => {
        if (tempUserId.trim()) {
            setUserId(tempUserId.trim());
            setUserIdSet(true);
            setMessages([]);
            setTempUserId('');
        }
    };

    // Handle Enter key in user ID input
    const handleUserIdKeyPress = (e) => {
        if (e.key === 'Enter') {
            handleSetUserId();
        }
    };

    // Send message
    const handleSendMessage = async () => {
        if (!inputValue.trim() || !userIdSet) {
            return;
        }

        const userMessage = inputValue.trim();
        setInputValue('');
        
        // Add user message to chat
        setMessages((prev) => [...prev, {
            type: 'user',
            content: userMessage,
            tools: []
        }]);

        setLoading(true);

        try {
            const response = await axios.post(`${API_BASE_URL}/chat`, {
                user_id: userId,
                message: userMessage
            });

            // Add agent response to chat
            setMessages((prev) => [...prev, {
                type: 'agent',
                content: response.data.agent_message,
                tools: response.data.tools_used
            }]);
        } catch (error) {
            console.error('Error:', error);
            const errorMessage = error.response?.data?.detail || 'Failed to get response from the agent. Please try again.';
            setMessages((prev) => [...prev, {
                type: 'error',
                content: errorMessage,
                tools: []
            }]);
        } finally {
            setLoading(false);
        }
    };

    // Handle Enter key in message input
    const handleMessageKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    // Clear chat
    const handleClearChat = async () => {
        try {
            await axios.delete(`${API_BASE_URL}/session/${userId}`);
            setMessages([]);
        } catch (error) {
            console.error('Error clearing chat:', error);
        }
    };

    return (
        <div className="app-container">
            {/* Header */}
            <div className="header">
                <h1>🎓 ENROLLMENT ASSISTANT</h1>
                <p>AI-Powered Student Enrollment Support Agent</p>
            </div>

            {/* User ID Setup */}
            {!userIdSet ? (
                <div className="user-id-container">
                    <span style={{ fontSize: '1.1rem', color: 'var(--neon-cyan)' }}>👤 Enter Your ID:</span>
                    <div className="user-id-input-wrapper">
                        <input
                            type="text"
                            placeholder="e.g., USER-001"
                            value={tempUserId}
                            onChange={(e) => setTempUserId(e.target.value)}
                            onKeyPress={handleUserIdKeyPress}
                        />
                    </div>
                    <button className="set-user-button" onClick={handleSetUserId}>
                        Start Chat
                    </button>
                </div>
            ) : (
                <div className="user-id-container">
                    <span style={{ color: 'var(--neon-green)', fontWeight: '600' }}>
                        ✓ User ID: {userId}
                    </span>
                    <button className="clear-button" onClick={() => {
                        setUserIdSet(false);
                        setUserId('');
                        setMessages([]);
                        setTempUserId('');
                        handleClearChat();
                    }}>
                        Change User
                    </button>
                </div>
            )}

            {/* Chat Area */}
            {userIdSet && (
                <div className="chat-container">
                    <div className="chat-wrapper">
                        {/* Messages */}
                        <div className="messages-container">
                            {messages.length === 0 ? (
                                <div className="welcome-container">
                                    <h2>Welcome! 👋</h2>
                                    <p>
                                        I'm your Student Enrollment Assistant. I can help you with:
                                    </p>
                                    <ul style={{ textAlign: 'left', marginTop: '1rem', lineHeight: '2' }}>
                                        <li>💼 Information about our programs</li>
                                        <li>📅 Application deadlines</li>
                                        <li>📋 Your application status</li>
                                    </ul>
                                    <p style={{ marginTop: '1rem' }}>
                                        Feel free to ask any questions about enrollment!
                                    </p>
                                </div>
                            ) : (
                                <>
                                    {messages.map((msg, index) => (
                                        <ChatMessage key={index} message={msg} />
                                    ))}
                                    {loading && (
                                        <div className="message">
                                            <div className="message-avatar agent-avatar">🤖</div>
                                            <div className="message-bubble" style={{ background: 'rgba(0, 240, 255, 0.1)' }}>
                                                <div className="loading">Agent is thinking</div>
                                            </div>
                                        </div>
                                    )}
                                    <div ref={messagesEndRef} />
                                </>
                            )}
                        </div>

                        {/* Input Area */}
                        <div className="input-container">
                            <div className="input-wrapper">
                                <span style={{ color: 'var(--neon-cyan)' }}>💬</span>
                                <input
                                    type="text"
                                    placeholder="Ask me anything about enrollment..."
                                    value={inputValue}
                                    onChange={(e) => setInputValue(e.target.value)}
                                    onKeyPress={handleMessageKeyPress}
                                    disabled={!userIdSet || loading}
                                />
                            </div>
                            <button
                                className="send-button"
                                onClick={handleSendMessage}
                                disabled={!inputValue.trim() || loading}
                            >
                                {loading ? 'Sending...' : 'Send'}
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
