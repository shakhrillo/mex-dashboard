// react function componnet
import React, { useEffect, useRef, useState } from "react";
import {
  addMinutes,
  addTimeSkippingWeekends,
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

    const fetchMachines = async () => {
      try {
        const requestOptions = {
          method: "GET",
          redirect: "follow",
        };

        let response = await fetch(
          "http://192.168.100.23:7878/api/machines",
          requestOptions
        );

        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        let data = await response.json();
        fetchData(data);
      } catch (error) {
        console.error(error);
      }
    };

    const fetchData = async (machinesList) => {
      try {
        const updatedMachinesData = [];
        const updateMachinesList = [];
        for (let machine of machinesList) {
          machine = machine["machineQrCode"];
          const requestOptions = {
            method: "GET",
            redirect: "follow",
          };

          const response = await fetch(
            `http://35.184.23.4/api/machine/status/${machine}`,
            // `http://34.31.212.138/api/machine/status/${machine}`,
            // `http://192.168.100.23:7878/api/machine/status/${machine}`,
            requestOptions
          );

          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          let data = await response.json();
          if (data["status"] === "Invalid") {
            const reResponse = await fetch(
              // `http://35.184.23.4/api/machine/status/${machine.replace(
              // `http://34.31.212.138/api/machine/status/${machine.replace(
                `http://192.168.100.23:7878/api/machine/status/${machine.replace(
                /\s+/g,
                ""
              )}`,
              requestOptions
            );

            if (!reResponse.ok) {
              throw new Error("Network response was not ok on retry");
            }

            data = await reResponse.json();
          }
          console.log(data);
          let machineInfo = [];
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
              finishDate: addTimeSkippingWeekends(
                data.createdAt,
                data.remainingProductionDays,
                data.remainingProductionTime
              ),
              shift: data.shift,
              machine,
              width:
                (data.remainingProductionTime / 60 +
                  data.remainingProductionDays * 24-
                  //if the current date is the same as the created date then minus one else minus 0
                  (new Date(data.createdAt).getDate() === today.getDate() ? 0 : 1) 
                  ) *
                  8.75 -
                calculateDaysExcludingWeekends(data.createdAt, today) *
                  8.75,
              status: "success",
            });
          } else if (
            !(data["status"] === "Invalid") &&
            data.machineStopped
          ) {
            machineInfo.push({
              barcodeProductionNo: data.barcodeProductionNo,
              partNo: data.partnumber,
              partName: data.partname,
              createdAt: data.createdAt,
              finishDate: addMinutes(
                data.createdAt,
                data.remainingProductionTime,
                data.remainingProductionDays
              ),
              shift: data.shift,
              note: data.note,
              machine,
              width: "auto",
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
                data.remainingProductionTime,
                data.remainingProductionDays
              ),
              shift: data.shift,
              machine,
              width: 0,
              status: "transparent",
            });
          }

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
    // fetchData();
    fetchMachines();

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <div className="tab-container">
      <div className="tab">
        {/* left side */}
        <div ref={leftRef} onScroll={setLeftScroll} className="tab-left">
          {/* header of the table */}
          <div className="side-header">
            <div className="tab-header-today">
              <div className="tab-header-today-day">
                <h3>Heute:</h3>
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
              <div className="side-title-item side-title-item-status">
                <h3>Status</h3>
              </div>
              <div className="side-title-item side-title-item-productionNr">
                <h3>ProductionsNr.</h3>
              </div>
            </div>
          </div>
          <div style={{ height: 63 }}></div>
          {/* data */}
          {machinesList.map((machine, index) => {
            return (
              <div key={index} className="side-title">
                <div className="side-title-item">
                  <span>{machine.machine}</span>
                </div>
                <div className="side-title-item side-title-item-status">
                  <div className={`status-box bg-${machine.status}`}></div>
                </div>
                <div className="side-title-item side-title-item-productionNr">
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
          <div style={{ height: 63 }}></div>
          {machinesData.map((machine, index) => (
            <div key={index} className="squars">
              <div className="squars-line">
                {machine.map((item, key) => {
                  return (
                    <Popover
                      content={
                        <div className="popover-content">
                          <p>
                            <span>ArtikelNr: </span>
                            {item.partNo}
                          </p>
                          <p>
                            <span>Artikelname: </span>
                            {item.partName}
                          </p>
                          <p>
                            <span>Fertigstellungstermin: </span>
                            {item.finishDate.toLocaleDateString()}{" "}
                            {item.finishDate.toLocaleTimeString().slice(0, 5)}
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
                          width: item.width < 0 ? 0 : item.width,
                          padding: item.width < 0 ? 0 : 2,
                          backgroundColor:
                            item["status"] === "success"
                              ? "#00cc00"
                              : item["status"] === "danger"
                              ? "#FC863E"
                              : "#fff",
                        }}
                        className={`status ${item["status"]}`}>
                          {item["status"] === "danger" ? (
                        <span>
                          {item.partNo}/{item.partName}/{item.note}
                          {/* {item.finishDate.toLocaleDateString()}{" "}
                          {item.finishDate.toLocaleTimeString().slice(0, 5)} */}
                        </span>) : (
                          <span>
                          {item.partNo}/{item.partName}/
                          {item.finishDate.toLocaleDateString()}{" "}
                          {item.finishDate.toLocaleTimeString().slice(0, 5)}
                        </span>)}
                      </div>
                    </Popover>
                  );
                })}
              </div>
              {[...Array(42)].map((_, index) => (
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
