<script lang="ts">
  import { writable } from "svelte/store";
  import {createEventDispatcher} from "svelte";
  import { setContext } from "svelte";
  import formKey from "./form-key";
  export let initialValues = {};
  
  const formStore = writable({ values: { ...initialValues }, errors: {},showErrors:false });

  const dispatch = createEventDispatcher();
  setContext(formKey, formStore);
  
  const handleSubmit = (e) => {
    e.preventDefault();
    if(Object.keys($formStore.errors).length===0){
    dispatch("submit", $formStore.values);
    }else{
      $formStore.showErrors=true;
    }
  };
  
</script>

<pre>
  {JSON.stringify($formStore, null, 2)}
</pre>

<form on:submit={handleSubmit}>
  <slot />
</form>

<style lang="postcss">
  form {
  }
</style>
