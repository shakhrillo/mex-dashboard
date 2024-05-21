// react function componnet
import React, { useEffect, useRef, useState } from "react";
import {
  addMinutes,
  calculateDaysExcludingWeekends,
  getLastFiveWeekdays,
  machines,
  monthNames,
  weekdays,
} from "../global";
import { Popover } from "antd";
import { ClipLoader } from "react-spinners";

const Table = ({ columns, data }) => {
  const rightRef = useRef(null);
  const leftRef = useRef(null);
  const headerRef = useRef(null);
  const [width, setWidth] = useState(null);
  const [loading, setLoading] = useState(true);

  // last five weekdays state
  const [lastFiveWeekdays, setLastFiveWeekdays] = useState([]);
  const [machinesData, setMachinesData] = useState([]);
  const [machinesList, setMachinesList] = useState([]);

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
      const scrollPosition = leftRef.current.scrollTop - 1;
      rightRef.current.scrollTop = scrollPosition + 1;
    }
  };

  const setHeaderScroll = () => {
    if (headerRef.current) {
      const scrolRight = headerRef.current.scrollLeft - 1;
      rightRef.current.scrollLeft = scrolRight + 1;
    }
  };

  const handleResize = () => {
    if (rightRef.current) {
      const elementWidth = rightRef.current.getBoundingClientRect().width;
      headerRef.current.style.width = `${elementWidth}px`;
      setWidth(elementWidth);
    }
  };

  useEffect(() => {
    handleResize();
    window.addEventListener("resize", handleResize);
    const fetchData = async () => {
      try {
        const updatedMachinesData = [];
        const updateMachinesList = [];
        for (const machine of machines) {
          const requestOptions = {
            method: "GET",
            redirect: "follow",
          };

          const response = await fetch(
            // `http://34.31.212.138/api/machine/status/${machine}`,
            `http://192.168.100.23:7878/api/machine/status/${machine}`,
            requestOptions
          );

          if (!response.ok) {
            throw new Error("Network response was not ok");
          }

          const data = await response.json();
          let machineInfo = [];
          let machineList = [];
          let width = 0;
          if (
            !(data["status"] === "Invalid") &&
            !data.toolMounted &&
            !data.machineStopped
          ) {
            machineInfo.push({
              barcodeProductionNo: data.barcodeProductionNo,
              partNo: data.partnumber,
              partName: data.partname,
              createdAt: data.createdAt,
              finishDate: addMinutes(
                data.createdAt,
                data.remainingProductionTime
              ),
              shift: data.shift,
              machine,
              width: (data.remainingProductionTime / 60) * 8.75,
              status: "success",
            });
          } else if (
            !(data["status"] === "Invalid") &&
            !data.toolMounted &&
            data.machineStopped
          ) {
            machineInfo.push({
              barcodeProductionNo: data.barcodeProductionNo,
              partNo: data.partnumber,
              partName: data.partname,
              createdAt: data.createdAt,
              finishDate: addMinutes(
                data.createdAt,
                data.remainingProductionTime
              ),
              shift: data.shift,
              machine,
              width: (data.remainingProductionTime / 60) * 8.75,
              status: "danger",
            });
          } else if (
            !(data["status"] === "Invalid") &&
            data.toolMounted &&
            !data.machineStopped
          ) {
            machineInfo.push({
              barcodeProductionNo: data.barcodeProductionNo,
              partNo: data.partnumber,
              partName: data.partname,
              createdAt: data.createdAt,
              finishDate: addMinutes(
                data.createdAt,
                data.remainingProductionTime
              ),
              shift: data.shift,
              machine,
              width: (data.remainingProductionTime / 60) * 8.75,
              status: "transparent",
            });
          }
          console.log("data:", data);
          updateMachinesList.push({
            machine,
            barcodeProductionNo: data["barcodeProductionNo"],
            status:
              data["machineStopped"] === true
                ? "danger"
                : data["machineStopped"] === false
                ? "success"
                : "transparent",
          });
          updatedMachinesData.push(machineInfo);
        }
        setMachinesData(updatedMachinesData);
        setMachinesList(updateMachinesList);
        setLoading(false);
      } catch (error) {
        console.error(error);
      }
    };
    setLastFiveWeekdays(getLastFiveWeekdays());
    fetchData();

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  console.log("machines data:", machinesData);
  return (
    <div className="tab-container">
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
                {today.toLocaleTimeString().slice(0, 5)}
              </span>
            </div>
            <div className="side-title header-tile">
              <div className="side-title-item">
                <h3>Maschine</h3>
              </div>
              <div className="side-title-item">
                <h3>Status</h3>
              </div>
              <div className="side-title-item">
                <h3>Production Nr</h3>
              </div>
            </div>
          </div>
          <div style={{ height: 66.5 }}></div>
          {/* data */}
          {machinesList.map((machine, index) => {
            console.log("machine", machine);
            return (
              <div key={index} className="side-title">
                <div className="side-title-item">
                  <span>{machine.machine}</span>
                </div>
                <div className="side-title-item">
                  <div className={`status-box bg-${machine.status}`}></div>
                </div>
                <div className="side-title-item">
                  <span>
                    {machine.barcodeProductionNo === null ||
                    machine.barcodeProductionNo === undefined
                      ? "---"
                      : machine.barcodeProductionNo}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
        {/* right side */}
        <div ref={rightRef} onScroll={setRightScroll} className="right-side">
          <div
            ref={headerRef}
            onScroll={setHeaderScroll}
            className="side-header">
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
          <div style={{ height: 66.5 }}></div>
          {/*  */}
          {machinesData.map((machine, index) => (
            // {[...Array(18)].map((machine, index) => (
            <div key={index} className="squars">
              <div className="squars-line">
                {machine.map((item, key) => {
                  console.log("item:", item);
                  return (
                    <Popover
                      content={
                        <div className="popover-content">
                          <p>
                            <span>Part No: </span>
                            {item.partNo}
                          </p>
                          <p>
                            <span>Part Name: </span>
                            {item.partName}
                          </p>
                          <p>
                            <span>Date and Time: </span>
                            {item.finishDate.toLocaleString()}
                          </p>
                        </div>
                      }
                      key={key}>
                      <div
                        style={{
                          left:
                            new Date(item["createdAt"]).getDate() ===
                            today.getDate()
                              ? new Date(item["createdAt"]).getHours() * 8.75
                              : 0,
                          width:
                            item["status"] === "danger"
                              ? "auto"
                              : item["width"] -
                                calculateDaysExcludingWeekends(
                                  item["createdAt"],
                                  today
                                ) *
                                  210,
                          backgroundColor:
                            item["status"] === "success"
                              ? "#5cb85c"
                              : item["status"] === "danger"
                              ? "#cc0000"
                              : "#fff",
                        }}
                        className="status">
                        <span>
                          {item.partNo}/{item.partName}/
                          {item.finishDate.toLocaleDateString()}{" "}
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
      <ClipLoader
        color={"#123abc"}
        loading={loading}
        css={{ position: "absolute", top: "50%", left: "50%" }}
        size={50}
      />
    </div>
  );
};

export default Table;
