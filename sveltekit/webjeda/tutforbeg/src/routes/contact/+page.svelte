<script>
  import Button from "$lib/Button.svelte";
  import { enhance, applyAction } from "$app/forms";
  
  export let form;

</script>

<div class="container">
  <h2>Contact Us</h2>
  {#if form?.success}
    <p class="success">{form?.status || ''}</p>
  {:else}
    <form method="POST" action="#"
          use:enhance={()=>{
          return async ({result})=>{await applyAction(result)}
        }}>
      <div class="form-group">
        <label class="col-md-3 control-label" for="name">Name</label>
        <div class="col-md-9">
          <input
            id="name"
            name="name"
            type="text"
            placeholder="Your name"
            class="form-control"
            value={ form?.name || ''}
            class:error={form && form?.errors?.name}
          />
          {#if form?.errors?.name}
            <p class="error">{form.errors.name}</p>
          {/if}
        </div>
      </div>
      
      <div class="form-group">
        <label class="col-md-3 control-label" for="email">Your E-mail</label>
        <div class="col-md-9">
          <input
            id="email"
            name="email"
            type="text"
            placeholder="Your email"
            class="form-control"
            value={ form?.email || ''}
            class:error={form && form?.errors?.email}
          />
          {#if form?.errors?.email}
            <p class="error">{form.errors.email}</p>
          {/if}
        </div>
      </div>
      
      <div class="form-group">
        <label class="col-md-3 control-label" for="message">Your message</label>
        <div class="col-md-9">
                    <textarea
                      class="form-control"
                      id="message"
                      name="message"
                      placeholder="Please enter your message here..."
                      rows="5"
                      value={ form?.message || ''}
                      class:error={form && form?.errors?.message}
                    />
        </div>
        {#if form?.errors?.message}
          <p class="error">{form.errors.message}</p>
        {/if}
      </div>
      
      <div class="form-group">
        <div class="col-md-12">
          <Button type="submit" size="small">Submit</Button>
        </div>
      </div>
    </form>
  {/if}
</div>

<style>
  .container {
    padding: 2em 0;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 0.5em 1em;
    border-radius: 0.25em;
    border: 1px solid #999;
  }
  
  .form-group {
    margin-bottom: 1.5em;
  }
  
  label {
    display: block;
    margin-bottom: 0.5em;
  }
  
  label,
  h2, p {
    color: var(--color-primary);
  }
  
  input {
    color: var(--primary-background);
  }
  
  h2 {
    font-weight: 500;
    font-size: 2em;
    margin-bottom: 1em;
  }
  
  .success {
    color: lightgray;
  }
  
  .error {
    border: 2px solid red;
  }
</style>
