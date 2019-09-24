import Layout from '../../components/MyLayout';
import fetch from 'isomorphic-unfetch';

const Post = props => (
  <Layout>
    <h1>{props.task.name}</h1>
    <p>{props.task.start_date.replace(/<[/]?p>/g, '')}</p>
  </Layout>
);

Post.getInitialProps = async function(context) {
  const { id } = context.query;
  const res = await fetch(`http://127.0.0.1:8000/api/${id}`);
  const task = await res.json();

  console.log(`Fetched show: ${task.name}`);

  return { task };
};

export default Post;