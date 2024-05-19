import { BoxArrowRight, Person } from "react-bootstrap-icons";
import "./App.css";
import LastFiveDaysTimeline from "./components/calendar-table";
import Table from "./components/table";

function App() {
  return (
    <div className="App">
      {/* header with box shadow */}
      <header className="App-header">
        <nav>
          <h4>KTBU Maschinen <br />
            Dashboard</h4>
          {/* <div className="user-info"> */}
          {/* <span>
              <Person size={18} />
              <h4>User</h4>
            </span>
            <BoxArrowRight color="#cc0000" size={24} /> */}
          {/* </div> */}
        </nav>
      </header>
      {/* table component */}
      {/* table wrapper */}
      <div className="tab-wrapper">
        <Table />
      </div>

      {/* <LastFiveDaysTimeline /> */}
    </div>
  );
}

export default App;
