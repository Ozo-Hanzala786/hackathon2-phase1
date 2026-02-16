import { Task } from '../app/dashboard/page'; // Import the Task type from dashboard

type TaskProps = {
  task: Task;
  onToggleCompletion: (taskId: string) => void;
  onDelete: (taskId: string) => void;
};

export default function TaskComponent({ task, onToggleCompletion, onDelete }: TaskProps) {
  return (
    <li
      style={{
        border: '1px solid #ccc',
        padding: '1rem',
        margin: '0.5rem 0',
        borderRadius: '4px',
        backgroundColor: task.completed ? '#f0f0f0' : 'white'
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h3 style={{ margin: 0, textDecoration: task.completed ? 'line-through' : 'none' }}>
            {task.title}
          </h3>
          {task.description && <p>{task.description}</p>}
        </div>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            onClick={() => onToggleCompletion(task.id)}
            style={{ padding: '0.25rem 0.5rem' }}
          >
            {task.completed ? 'Undo' : 'Complete'}
          </button>
          <button
            onClick={() => onDelete(task.id)}
            style={{ padding: '0.25rem 0.5rem', backgroundColor: '#ffcccc' }}
          >
            Delete
          </button>
        </div>
      </div>
    </li>
  );
}