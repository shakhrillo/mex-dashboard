import React from 'react';
import './style.css';

export const TabLeftContent = ({ bold = false, status = "", machine = "Machine", productNo = "Product No" }) => {
    return (
        <div className='tab-left-content tr list-items'>
            <ul>
                <li className={bold && "header_title"}>{machine}</li>
                <li className={`${status && `status-${status}`} ${bold && "header_title"}`}>{bold ? "Status" : ""}</li>
                <li className={bold && "header_title"} >{productNo}</li>
            </ul>
        </div >
    )
}