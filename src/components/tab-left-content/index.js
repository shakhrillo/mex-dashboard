import React, { useEffect } from 'react';
import './style.css';

export const TabLeftContent = ({ bold = false, status = "", machine = "Machine" }) => {
    const [data, setData] = React.useState({
        machineQrCode: "Invalid",
        machineStatus: "Invalid",
        productNo: "Invalid"
    });

    useEffect(() => {
        fetch(`http://localhost:8000/api/machines/${machine}/status`)
            .then(response => response.json())
            .then(data => {
                setData(data);
            })
    }, []);
    return (
        <div className='tab-left-content tr list-items'>
            <ul>
                <li className={bold && "header_title"}>{machine}</li>
                <li className={`${`status-${data.machineStatus}`} ${bold && "header_title"}`}>{bold ? "Status" : ""}</li>
                <li className={bold && "header_title"} >{!bold ? data.productNo : "Product No"}</li>
            </ul>
        </div >
    )
}