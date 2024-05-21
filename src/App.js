import "./App.css";
import Table from "./components/table";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav>
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
