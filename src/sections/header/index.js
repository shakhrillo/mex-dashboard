import React from 'react';
import './style.css';
import { BoxArrowRight, Person } from 'react-bootstrap-icons';

export const Header = () => {
    return <div className="header">
        <div className='header__container'>
            <div className='header__logo'>
                <img src='logo.png' alt='logo' style={{ height: 60 + 'px' }} />
            </div>
            {/* <div className='header__menu'>
                <ul>
                    <li className='user'>
                        <Person />
                        Marco
                    </li>
                    <li className='logout'>
                        <BoxArrowRight />
                    </li>
                </ul>
            </div> */}
        </div>
    </div>;
}