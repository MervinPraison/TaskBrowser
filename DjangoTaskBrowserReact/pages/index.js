import Layout from '../components/MyLayout';
import Link from 'next/link';
import fetch from 'isomorphic-unfetch';
import Table from 'react-bootstrap/Table'


const Index = props => (
  <Layout>
    
    <h1>Tasks Browser : React Interface</h1>
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Name</th>
          <th>Id</th>
          <th>Status</th>
          <th>Start date</th>
          <th>End date</th>
          <th>Parent</th>
          <th>Duration in Minutes</th>
        </tr>
      </thead>
      <tbody>
      {props.tasks.map(task => (
        <tr key={task.task_id}>
          <td> {task.name} </td>
          <td> {task.task_id} </td>
          <td> {task.status} </td>
          <td> {task.start_date} </td>
          <td> {task.end_date} </td>
          <td> {task.parent} </td>
          <td> {task.duration} </td>
        </tr>
      ))}
      </tbody>
    </Table>
  </Layout>
);

Index.getInitialProps = async function() {
  const res = await fetch('https://praison.com/tasksbrowser/api/');
  const data = await res.json();

  console.log(`Show data fetched. Count: ${data.length}`);

  return {
    tasks: data.map(entry => entry)
  };
};

export default Index;