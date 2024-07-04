import "./App.css";
import Table from "./components/table";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <img
          style={{rotate: "90deg"}}
          width={50}
          src={
            require("./img/bar-chart.png")
          } />
          <h4>KTBU Maschinen Dashboard</h4>
        </nav>
      </header>
      <div className="tab-wrapper">
        <Table />
      </div>
    </div>
  );
}

export default App;
