import React, { useState } from "react";
import { TabLeft } from "../tab-left"
import { TabRight } from "../tab-right"
import './style.css';

export const Tab = ({ children }) => {
    const [scrollPosition, setScrollPosition] = useState(0);
    const [data, setData] = React.useState([])

    React.useEffect(() => {
        fetch('http://localhost:5001/machines')
            .then(response => response.json())
            .then(data => setData(data))
    }, [])

    return (
        <div className='tab'>
            <TabLeft data={data} />
            
            <div style={{
                display: "flex",
                overflow: "hidden",
                position: "relative",
            }}>

                <div
                    style={{
                        height: 100 + "%",
                        width: 30 + "px",
                        background:
                            "linear-gradient(90deg, rgba(210,210,210,.4) 0%, rgba(255,255,255,0) 100%)",
                        position: "absolute",
                        right: `${!scrollPosition ? "0" : "auto"}`,
                        transform: `${!scrollPosition ? "rotate(180deg)" : "rotate(0deg)"}`,
                    }}
                ></div>
                <div onScroll={e => {
                    e.preventDefault()
                    e.stopPropagation()
                    if (e.target.scrollLeft === 0) {
                        setScrollPosition(0)
                    } else {
                        setScrollPosition(1)
                    }
                }} style={{ display: "flex", overflow: "auto", whiteSpace: "nowrap" }}>
                    {/* <TabRight header={'02 May 2024 - Thursday'} data={data} /> */}
                    <TabRight header={'03 May 2024 - Friday'} data={data} />
                    {/* <TabRight header={'04 May 2024 - Saturday'} data={data} />
                    <TabRight header={'05 May 2024 - Sunday'} data={data} />
                    <TabRight header={'06 May 2024 - Monday'} data={data} /> */}
                </div>
            </div>
        </div>
    )
}