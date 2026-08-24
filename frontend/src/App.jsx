import { useEffect, useState } from "react";

function App() {
  const [backendStatus, setBackendStatus] = useState("Checking...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((response) => response.json())
      .then((data) => {
        setBackendStatus(
          `${data.status} - Version ${data.version}`
        );
      })
      .catch(() => {
        setBackendStatus("Backend unavailable");
      });
  }, []);

  return (
    <div>
      <h1>Employee Management System</h1>

      <h2>Backend Status</h2>

      <p>{backendStatus}</p>

      <hr />

      <h2>Employees</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Salary</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td>1</td>
            <td>Rahul</td>
            <td>50000</td>
          </tr>

          <tr>
            <td>2</td>
            <td>Priya</td>
            <td>60000</td>
          </tr>

          <tr>
            <td>3</td>
            <td>Amith</td>
            <td>70000</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default App;
