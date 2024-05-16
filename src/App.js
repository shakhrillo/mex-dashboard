import './App.css';
import Table from './components/table';

function App() {
  return (
    <div className='App'>
      {/* header with box shadow */}
      <header className='App-header'>
        <h4>logo</h4>
      </header>
      {/* table component */}
      {/* table wrapper */}
      <div className='tab-wrapper'>
        <Table />
      </div>
    </div>
  );
}

export default App;
