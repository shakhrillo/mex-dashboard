import React from 'react';
import './style.css';
import { Tab } from '../../components/tab';

export const Body = () => {
    return (
        <div className="body">
            <div className='body__container'>
                <div className='body__content'>
                    <Tab />
                </div>
            </div>
        </div>
    )
}