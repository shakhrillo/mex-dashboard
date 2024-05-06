import React, { useEffect } from 'react';
import './style.css';

export const TabLeftContent = ({ bold = false, status = "", machine = "Machine", productNo = "Product No" }) => {
    const [data, setData] = React.useState({
        machineQrCode: "Invalid",
        machineStatus: "Invalid"
    });
    useEffect(() => {
        fetch(`http://localhost:8000/api/machines/${machine}/status`)
            .then(response => response.json())
            .then(data => {
                setData(data);
            })
    }, []);

    useEffect(() => {
        console.log('data', data);
    }, [data]);
    return (
        <div className='tab-left-content tr list-items'>
            <ul>
                <li className={bold && "header_title"}>{machine}</li>
                <li className={`${`status-${data.machineStatus}`} ${bold && "header_title"}`}>{bold ? "Status" : ""}</li>
                <li className={bold && "header_title"} >{data.machineQrCode}</li>
            </ul>
        </div >
    )
}