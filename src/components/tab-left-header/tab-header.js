import React from 'react';
import './style.css';

export const TabLeftHeader = ({ tab, activeTab, setActiveTab }) => {
    return (
        <div className='tab-header tr'>
            <div className='tab-header__date'>
                <h4 style={{
                    fontWeight: 400,
                }}>Today: </h4>
                <span>{
                    new Date().toLocaleDateString('en-US', {
                        // weekday: 'long',
                        year: 'numeric',
                        day: 'numeric',
                        month: 'long'
                    })
                }</span>
            </div>
            <div className='tab-header__time'>
                <span>{
                    new Date().toLocaleTimeString('en-US', {
                        hour: '2-digit',
                        minute: '2-digit',
                        hour12: false
                    })
                }</span>
            </div>
        </div>
    )
}