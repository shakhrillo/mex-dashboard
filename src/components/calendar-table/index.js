import React, { useState, useRef } from 'react';
import 'react-calendar-timeline/lib/Timeline.css'
import Timeline from 'react-calendar-timeline';
import moment from 'moment';
import { machines } from '../global';

const LastFiveDaysTimeline = () => {
    const leftRef = useRef(null);

    const dayOfMonth = moment().format('D');
    const month = moment().format('MMMM');
    const year = moment().format('YYYY');

    const today = moment().startOf('day'); // Today
    const endDate = today.clone(); // Today
    const startDate = today.clone().subtract(5, 'days'); // Start 5 days ago

    const [visibleTimeStart, setVisibleTimeStart] = useState(endDate);
    const [visibleTimeEnd, setVisibleTimeEnd] = useState(startDate);

    const handleTimeChange = (visibleTimeStart, visibleTimeEnd, updateScrollCanvas) => {
        const newVisibleTimeStart = moment(visibleTimeStart).isBefore(startDate)
            ? startDate
            : visibleTimeStart;
        const newVisibleTimeEnd = moment(visibleTimeEnd).isAfter(endDate)
            ? endDate
            : visibleTimeEnd;
        setVisibleTimeStart(newVisibleTimeStart);
        setVisibleTimeEnd(newVisibleTimeEnd);
        updateScrollCanvas(newVisibleTimeStart, newVisibleTimeEnd);
    };

    const groups = [{ id: 1, title: 'Group 1' }, { id: 2, title: 'Group 2' }, { id: 3, title: 'Group 3' }, { id: 4, title: 'Group 4' }, { id: 5, title: 'Group 5' }];
    const items = [
        {
            id: 1,
            group: 1,
            title: 'Item 1',
            start_time: startDate.toDate(),
            end_time: endDate.toDate(),
        },
    ];

    // Reverse the arrays
    const reversedGroups = [...groups].reverse();
    const reversedItems = [...items].reverse();

    return (
        <div style={{ display: "flex" }}>
            <div ref={leftRef} className="tab-left">
                {/* header of the table */}
                <div className="side-header">
                    <div className="tab-header-today">
                        <div className="tab-header-today-day">
                            <h3>Today:</h3>
                            {/* day mont on text year */}
                            <span>
                                {dayOfMonth} {month} {year}
                            </span>
                        </div>
                        {/* actual time */}
                        <span className="tab-header-today-time">
                            {/* {today.toLocaleTimeString()} */}
                        </span>
                    </div>
                    <div className="side-title header-tile">
                        <div className="side-title-item">
                            <h3>Machine</h3>
                        </div>
                        <div className="side-title-item">
                            <h3>Status</h3>
                        </div>
                        <div className="side-title-item">
                            <h3>Product No</h3>
                        </div>
                    </div>
                </div>
                <div style={{ height: 75.5 }}></div>
                {/* data */}
                {machines.map((machine, index) => (
                    <div key={index} className="side-title">
                        <div className="side-title-item">
                            <span>{machine}</span>
                        </div>
                        <div className="side-title-item bg-yellow"></div>
                        <div className="side-title-item">
                            <span>12415312</span>
                        </div>
                    </div>
                ))}
            </div>
            <Timeline
                sidebarWidth={0}
                groups={reversedGroups}
                items={reversedItems}
                defaultTimeStart={startDate}
                defaultTimeEnd={endDate}
                visibleTimeStart={visibleTimeStart}
                visibleTimeEnd={visibleTimeEnd}
                onTimeChange={handleTimeChange}
            />
        </div>
    );
};

export default LastFiveDaysTimeline;
