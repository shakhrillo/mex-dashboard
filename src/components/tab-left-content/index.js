import React, { useEffect } from 'react';
import './style.css';

export const TabLeftContent = ({ bold = false, status = "", machine = "Machine", productNo = "Product No" }) => {
    useEffect(() => {
        fetch('http://localhost:8000/api/machines/F450iA-1/status')
            .then(response => response.json())
            .then(data => console.log(data))
    }, [])
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