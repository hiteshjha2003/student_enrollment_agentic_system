import React from 'react';

function ChatMessage({ message }) {
    if (message.type === 'error') {
        return (
            <div className="message">
                <div className="message-avatar" style={{
                    background: 'linear-gradient(135deg, #ff006e, #ff6600)',
                    boxShadow: '0 0 20px rgba(255, 0, 110, 0.5)'
                }}>
                    ⚠️
                </div>
                <div className="message-bubble" style={{
                    background: 'linear-gradient(135deg, rgba(255, 0, 110, 0.2), rgba(255, 102, 0, 0.2))',
                    border: '2px solid #ff006e',
                    borderLeft: '4px solid #ff006e'
                }}>
                    <div className="message-content">{message.content}</div>
                </div>
            </div>
        );
    }

    if (message.type === 'user') {
        return (
            <div className="message user-message">
                <div className="message-bubble">
                    <div className="message-content">{message.content}</div>
                </div>
                <div className="message-avatar user-avatar">👤</div>
            </div>
        );
    }

    // Agent message
    return (
        <div className="message agent-message">
            <div className="message-avatar agent-avatar">🤖</div>
            <div>
                <div className="message-bubble">
                    <div className="message-content">{message.content}</div>
                    {message.tools && message.tools.length > 0 && (
                        <div style={{ marginTop: '0.5rem' }}>
                            {message.tools.map((tool, idx) => (
                                <span key={idx} className="tools-badge">
                                    {tool.replace(/_/g, ' ')}
                                </span>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default ChatMessage;
