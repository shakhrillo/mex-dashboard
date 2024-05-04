import React, { useEffect } from 'react';
import './style.css';
import { Popover } from 'antd';

export const TabRightContent = ({ hours = false, partInfo = [], header }) => {
    const [hoursData, setHoursData] = React.useState([{
        hours: "00",
    }, {
        hours: "01",
    }, {
        hours: "02",
    }, {
        hours: "03",
    }, {
        hours: "04",
    }, {
        hours: "05",
    }, {
        hours: "06",
    }, {
        hours: "07",
    }, {
        hours: "08",
    }, {
        hours: "09",
    }, {
        hours: "10",
    }, {
        hours: "11",
    }, {
        hours: "12",
    }, {
        hours: "13",
    }, {
        hours: "14",
    }, {
        hours: "15",
    }, {
        hours: "16",
    }, {
        hours: "17",
    }, {
        hours: "18",
    }, {
        hours: "19",
    }, {
        hours: "20",
    }, {
        hours: "21",
    }, {
        hours: "22",
    }, {
        hours: "23",
    }, {
        hours: "24",
    }])

    return (
        <div className='tab-right-content tr'>
            <ul style={{ position: "relative" }}>
                {hoursData.map((item, index) => <li key={index}>
                    {hours && item.hours}
                </li>)}
                
                {!hours && <div style={{ 
                    display: "flex",
                    height: 16,
                    width: 100 + "%",
                    position: "absolute",
                }}>
                    {
                        partInfo.map((item) => {
                            return <Popover placement='bottom' content={
                                item.title &&
                                <span style={{
                                    textOverflow: "ellipsis",
                                    overflow: "hidden",
                                    whiteSpace: "nowrap",
                                    display: "block",
                                    fontSize: 12,
                                    fontWeight: "bold",
                                    color: "#336699",
                                }}>
                                    {item.title} <br /> {item.partName} <br />  {item.date}
                                </span>
                            }
                            trigger="hover">
                                <div style={{ 
                                    backgroundColor: item.type ? item.type === "active" ?  "#5CB85C" : "#cc0000" : "none", 
                                    height: "100%", 
                                    width: `calc(${100/24 * item.time}%)`
                                }}>
                                    <span style={{
                                        textOverflow: "ellipsis",
                                        overflow: "hidden",
                                        whiteSpace: "nowrap",
                                        display: "block",
                                        fontSize: 12,
                                        fontWeight: "bold",
                                        color: "white",
                                    }}>
                                        {item.title && `${item.title} / ${item.partName} / ${item.date}`}
                                    </span>
                                </div>
                            </Popover>
                        })
                    }

                    {/* <Popover placement='bottom' content={
                        <span style={{
                            textOverflow: "ellipsis",
                            overflow: "hidden",
                            whiteSpace: "nowrap",
                            display: "block",
                            fontSize: 12,
                            fontWeight: "bold",
                            color: "#336699",
                        }}>
                            Part No: 345532 <br /> Part name: Part name <br />  Date and time: 15. 11. 2024
                        </span>} trigger="hover">
                        <div style={{ backgroundColor: "#cc0000", height: "100%", width: `calc(${100 / 24}%)`, padding: red ? "0 6px" : 0 }}>
                            <span style={{
                                textOverflow: "ellipsis",
                                overflow: "hidden",
                                whiteSpace: "nowrap",
                                display: "block",
                                fontSize: 12,
                                fontWeight: "bold",
                                color: "white",
                            }}>345532 / Part name / 15. 11. 2024</span>
                        </div>
                    </Popover> */}
                </div>}
            </ul>
        </div>
    )
}