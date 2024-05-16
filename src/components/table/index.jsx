// react function componnet
import React, { useEffect, useRef, useState } from "react";
import { machines, monthNames, weekdays } from "../global";
import { Popover } from "antd";

const Table = ({ columns, data }) => {
  const rightRef = useRef(null);
  const leftRef = useRef(null);
  const headerRef = useRef(null);
  // last five weekdays state
  const [lastFiveWeekdays, setLastFiveWeekdays] = useState([]);
  const [machinesData, setMachinesData] = useState([]);

  // get the current date
  const today = new Date();
  // get the day of the month
  const dayOfMonth = today.getDate();
  // get the month
  const month = monthNames[today.getMonth()];
  // get the year
  const year = today.getFullYear();

  const getDivScrollPosition = () => {
    if (rightRef.current) {
      const scrollPosition = rightRef.current.scrollTop;
      const scrolRight = rightRef.current.scrollLeft;
      leftRef.current.scrollTop = scrollPosition;
      headerRef.current.scrollLeft = scrolRight;
    }
  };

  // useEffect hook
  useEffect(() => {
    const getLastFiveWeekdays = () => {
      const weekdays = [];
      let currentDate = new Date();
      currentDate.setDate(currentDate.getDate() - 1);
      let daysToSubtract = 0;

      // Loop until we have collected five weekdays
      while (weekdays.length < 5) {
        // Subtract days one by one
        currentDate = new Date();
        currentDate.setDate(currentDate.getDate() - 1);
        currentDate.setDate(currentDate.getDate() - daysToSubtract);

        // Check if the current day is not Saturday or Sunday
        if (currentDate.getDay() !== 0 && currentDate.getDay() !== 6) {
          weekdays.push(new Date(currentDate));
        }

        daysToSubtract++; // Move to the previous day
      }

      return weekdays;
    };
    setLastFiveWeekdays(getLastFiveWeekdays());
  }, []);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const updatedMachinesData = [];
        for (const machine of machines) {
          const requestOptions = {
            method: "GET",
            redirect: "follow",
          };

          const response = await fetch(
            `http://34.31.212.138/api/all_machines/${machine}`,
            requestOptions
          );

          if (!response.ok) {
            throw new Error("Network response was not ok");
          }

          const data = await response.json();
          let machineInfo = [];
          let width = 35;

          for (let i = 0; i < data.length; i++) {
            const current = data[i];
            const next = data[i + 1];

            if (!current.toolMounted && !current.machineStopped) {
              if (next && !next.toolMounted && !next.machineStopped) {
                width += 35;
              } else {
                machineInfo.push({
                  machine,
                  width,
                  status: "success",
                });
              }
            } else if (!current.toolMounted && current.machineStopped) {
              if (next && !next.toolMounted && next.machineStopped) {
                width += 35;
              } else {
                machineInfo.push({
                  machine,
                  width,
                  status: "danger",
                });
              }
            } else if (current.toolMounted && !current.machineStopped) {
              if (next && next.toolMounted && !next.machineStopped) {
                width += 35;
              } else {
                machineInfo.push({
                  machine,
                  width,
                  status: "transparent",
                });
              }
            }
          }
          updatedMachinesData.push(machineInfo);
        }
        setMachinesData(updatedMachinesData);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  console.log("machines data:", machinesData);
  return (
    <div className="tab">
      {/* left side */}
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
              {today.toLocaleTimeString()}
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
      {/* right side */}
      <div
        ref={rightRef}
        onScroll={getDivScrollPosition}
        className="right-side">
        <div ref={headerRef} className="side-header">
          <div className="right-side-days">
            <div className="right-side-days-wrapper">
              {lastFiveWeekdays.map((day, index) => (
                <div key={index} className="right-side-days-item">
                  <span>{weekdays[day.getDay()]}</span>
                  <span>
                    {day.getDate()} {monthNames[day.getMonth()]}
                  </span>
                </div>
              ))}
            </div>
          </div>
          <div className="right-side-hours-wrapper">
            {lastFiveWeekdays.map((day, index) => (
              <div key={index} className="right-side-hours">
                <div className="right-side-hours-item">
                  <span>00</span>
                </div>
                <div className="right-side-hours-item">
                  <span>04</span>
                </div>
                <div className="right-side-hours-item">
                  <span>08</span>
                </div>
                <div className="right-side-hours-item">
                  <span>12</span>
                </div>
                <div className="right-side-hours-item">
                  <span>16</span>
                </div>
                <div className="right-side-hours-item">
                  <span>20</span>
                </div>
              </div>
            ))}
          </div>
        </div>
        <div style={{ height: 75.5 }}></div>
        {machinesData.map((machine, index) => (
          <div className="squars">
            <div className="squars-line">
              <div style={{ width: 52.5 }}></div>
              {machine.map((item, key) => (
                <Popover
                  content={
                    <div>
                      <p>{item["machine"]}</p>
                    </div>
                  }
                  key={key}>
                  <div
                    style={{
                      width: item["width"],
                      backgroundColor:
                        item["status"] == "success"
                          ? "#5cb85c"
                          : item["status"] == "danger"
                          ? "#cc0000"
                          : "#fff",
                    }}
                    className="status">
                    <span>{item["machine"]}</span>
                  </div>
                </Popover>
              ))}
            </div>
            {[...Array(30)].map((_, index) => (
              <div className="squar" key={index}></div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Table;
