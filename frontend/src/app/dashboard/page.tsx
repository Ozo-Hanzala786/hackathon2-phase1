'use client'

import { useState, useEffect } from 'react'
import { authService } from '@/lib/auth'
import TaskComponent from '@/components/TaskComponent'

// Define task type
type Task = {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  user_id: string;
  created_at: string;
  updated_at: string;
};

export default function DashboardPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [newTaskTitle, setNewTaskTitle] = useState('');
  const [newTaskDescription, setNewTaskDescription] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Get current user ID from auth service or mock for now
  const userId = authService.getToken() ? 'user123' : null;

  // Fetch tasks when component mounts
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        if (userId) {
          // For now, using mock data until backend is ready
          setTasks([
            {
              id: '1',
              title: 'Sample Task',
              description: 'This is a sample task',
              completed: false,
              user_id: userId,
              created_at: '2026-01-21T10:00:00Z',
              updated_at: '2026-01-21T10:00:00Z',
            }
          ]);
        }
      } catch (err) {
        setError('Failed to fetch tasks');
        console.error('Error fetching tasks:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [userId]);

  const handleAddTask = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTaskTitle.trim() || !userId) return;

    try {
      // For now, using mock until backend is ready
      const newTask: Task = {
        id: Date.now().toString(),
        title: newTaskTitle,
        description: newTaskDescription,
        completed: false,
        user_id: userId,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
      };

      setTasks([...tasks, newTask]);
      setNewTaskTitle('');
      setNewTaskDescription('');
    } catch (err) {
      setError('Failed to add task');
      console.error('Error adding task:', err);
    }
  };

  const toggleTaskCompletion = async (taskId: string) => {
    try {
      // For now, using mock until backend is ready
      setTasks(tasks.map(task =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      ));
    } catch (err) {
      setError('Failed to update task');
      console.error('Error updating task:', err);
    }
  };

  const deleteTask = async (taskId: string) => {
    try {
      // For now, using mock until backend is ready
      setTasks(tasks.filter(task => task.id !== taskId));
    } catch (err) {
      setError('Failed to delete task');
      console.error('Error deleting task:', err);
    }
  };

  if (!userId) {
    return <div>Please log in to view your tasks.</div>;
  }

  if (loading) {
    return <div>Loading tasks...</div>;
  }

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Your Tasks</h1>

      {error && <div style={{ color: 'red', marginBottom: '1rem' }}>{error}</div>}

      <form onSubmit={handleAddTask} style={{ marginBottom: '2rem' }}>
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}>
          <input
            type="text"
            value={newTaskTitle}
            onChange={(e) => setNewTaskTitle(e.target.value)}
            placeholder="Task title"
            style={{ flex: 1, padding: '0.5rem' }}
            required
          />
          <input
            type="text"
            value={newTaskDescription}
            onChange={(e) => setNewTaskDescription(e.target.value)}
            placeholder="Description (optional)"
            style={{ flex: 1, padding: '0.5rem' }}
          />
          <button type="submit" style={{ padding: '0.5rem 1rem' }}>
            Add Task
          </button>
        </div>
      </form>

      <div>
        {tasks.length === 0 ? (
          <p>No tasks yet. Add one above!</p>
        ) : (
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {tasks.map(task => (
              <TaskComponent
                key={task.id}
                task={task}
                onToggleCompletion={toggleTaskCompletion}
                onDelete={deleteTask}
              />
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}