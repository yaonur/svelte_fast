<script lang="ts">
  import TodoList from "./lib/TodoList.svelte";
  import { v4 as uuid } from "uuid";
  import { tick } from "svelte";
  
  
  let todos = [
    { id: uuid(), title: "todo1", completed: true },
    { id: uuid(), title: "todo2", completed: true },
    { id: uuid(), title: "todo3", completed: false }
  ];
  let todoList = null;
  let showList = true;
  const handleAddTodo = async ({ detail }) => {
    setTimeout( async () => {
      console.log(document.querySelectorAll(".todo-list li"));
      let newTodo = { id: uuid(), title: detail.title, completed: false };
      todos = [...todos, newTodo];
      
      todoList.clearInput();
      await tick()
      console.log(document.querySelectorAll(".todo-list li"));
    }, 1000);
  };
  let handleRemoveTodo = ({ detail }) => {
    todos = todos.filter((todo) => todo.id !== detail.id);
  };
  let handleToggleTodo = ({ detail }) => {
    todos = todos.map((todo) => {
      if (todo.id === detail.id) {
        return { ...todo, completed: detail.completed };
      }
      return todo;
    });
  };
</script>
<label>
  <input type="checkbox" bind:checked={showList}>
  Show/Hide List
</label>
{#if showList}
  
  <TodoList bind:this={todoList} {todos} on:addTodo={handleAddTodo} on:removeTodo={handleRemoveTodo}
            on:toggleTodo={handleToggleTodo} />
  <button class="self-center" on:click={()=>todoList.focusInput()}>Focus</button>
{/if}
