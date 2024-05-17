// react function componnet
import React, { useEffect, useRef, useState } from "react";
import { machines, monthNames, weekdays } from "../global";
import { Popover } from "antd";

const Table = ({ columns, data }) => {
  const rightRef = useRef(null);
  const leftRef = useRef(null);
  const headerRef = useRef(null);
  const [width, setWidth] = useState(null);
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

  const setRightScroll = () => {
    if (rightRef.current) {
      const scrollPosition = rightRef.current.scrollTop;
      const scrolRight = rightRef.current.scrollLeft;
      leftRef.current.scrollTop = scrollPosition;
      headerRef.current.scrollLeft = scrolRight;
    }
  };

  const setLeftScroll = () => {
    if (leftRef.current) {
      const scrollPosition = leftRef.current.scrollTop;
      rightRef.current.scrollTop = scrollPosition;
    }
  };

  const setHeaderScroll = () => {
    if (headerRef.current) {
      const scrolRight = headerRef.current.scrollLeft;
      rightRef.current.scrollLeft = scrolRight;
    }
  };

  function calculateDaysBetweenDates(date1, date2) {
    // Convert both dates to milliseconds
    // const date1_ms = date1.getTime();
    // const date2_ms = date2.getTime();

    const date1_ms = new Date(date1);
    const date2_ms = new Date(date2);

    date1_ms.setHours(0, 0, 0, 0);
    date2_ms.setHours(0, 0, 0, 0);

    console.log("date1:", date1);
    console.log("date2:", date2);

    console.log("date1_ms:", date1_ms);
    console.log("date2_ms:", date2_ms);

    // Calculate the difference in milliseconds
    const difference_ms = Math.abs(date2_ms - date1_ms);

    // Convert the difference back to days
    const difference_days = Math.ceil(difference_ms / (1000 * 60 * 60 * 24));

    console.log("difference_days:", difference_days);

    if (difference_days > 4) {
      return difference_days - 2;
    }
    return difference_days;
  }

  // useEffect hook
  useEffect(() => {
    const getLastFiveWeekdays = () => {
      const weekdays = [];
      let currentDate = new Date();
      let daysToSubtract = 0;

      // Loop until we have collected five weekdays
      while (weekdays.length < 5) {
        // Subtract days one by one
        currentDate = new Date();
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
          let width = 70;

          for (let i = 0; i < data.length; i++) {
            const current = data[i];
            const next = data[i + 1];

            if (!current.toolMounted && !current.machineStopped) {
              if (next && !next.toolMounted && !next.machineStopped) {
                width += 70;
              } else {
                machineInfo.push({
                  barcodeProductionNo: current.barcodeProductionNo,
                  createdAt: current.createdAt,
                  shift: current.shift,
                  machine,
                  width,
                  status: "success",
                });
              }
            } else if (!current.toolMounted && current.machineStopped) {
              if (next && !next.toolMounted && next.machineStopped) {
                width += 70;
              } else {
                machineInfo.push({
                  barcodeProductionNo: current.barcodeProductionNo,
                  createdAt: current.createdAt,
                  shift: current.shift,
                  machine,
                  width,
                  status: "danger",
                });
              }
            } else if (current.toolMounted && !current.machineStopped) {
              if (next && next.toolMounted && !next.machineStopped) {
                width += 70;
              } else {
                machineInfo.push({
                  barcodeProductionNo: current.barcodeProductionNo,
                  createdAt: current.createdAt,
                  shift: current.shift,
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

  useEffect(() => {
    function handleResize() {
      if (rightRef.current) {
        const elementWidth = rightRef.current.getBoundingClientRect().width;
        headerRef.current.style.width = `${elementWidth}px`;
        setWidth(elementWidth);
      }
    }

    // Initial width calculation
    handleResize();

    // Attach resize event listener
    window.addEventListener("resize", handleResize);

    // Cleanup function to remove event listener
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  console.log("machines data:", machinesData);
  return (
    <div className="tab">
      {/* left side */}
      <div ref={leftRef} onScroll={setLeftScroll} className="tab-left">
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
      <div ref={rightRef} onScroll={setRightScroll} className="right-side">
        <div ref={headerRef} onScroll={setHeaderScroll} className="side-header">
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
        {/*  */}
        {machinesData.map((machine, index) => (
          <div key={index} className="squars">
            <div className="squars-line">
              {machine.map((item, key) => {
                return (
                  <Popover
                    content={
                      <div className="popover-content">
                        <p>
                          <span>Part No: </span>
                          {item["barcodeProductionNo"]}
                        </p>
                        <p>
                          <span>Part Name: </span>
                          part name
                        </p>
                        <p>
                          <span>Date and Time: </span>
                          {item["createdAt"]}
                        </p>
                      </div>
                    }
                    key={key}>
                    <div
                      style={{
                        left:
                          calculateDaysBetweenDates(
                            new Date(item["createdAt"]),
                            today
                          ) *
                            210 +
                          (item["shift"] === "F1"
                            ? 53.5
                            : item["shift"] === "S2"
                            ? 122.5
                            : 192.5),
                        width: item["width"],
                        backgroundColor:
                          item["status"] === "success"
                            ? "#5cb85c"
                            : item["status"] === "danger"
                            ? "#cc0000"
                            : "#fff",
                      }}
                      className="status">
                      <span>
                        {item["barcodeProductionNo"]}/{item["shift"]}/
                        {item["createdAt"]}
                      </span>
                    </div>
                  </Popover>
                );
              })}
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
