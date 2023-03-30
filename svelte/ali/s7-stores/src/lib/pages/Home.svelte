<script lang="ts">
  import { settings } from "../stores/settings";
  import location from "../stores/location";
  import { tweened } from "svelte/motion";
  import { Field, Form } from "../Form";
  import Button from "../components/Button.svelte";
  import {validateEmail,validateRequiredField} from "../utils/validation";

  // const scale =writable(1)
  const scale = tweened(1, { duration: 500 });
</script>

<!-- <h1>Home</h1>
<h2>Color:{$settings.colorScheme}</h2>
{$location?.lat},{$location?.lon}
<br />
<button
  on:click={() => {
    $scale += 1;
  }}
  >Make it bigger
</button>
<button
  on:click={() => {
    $scale -= 1;
  }}
  >Make it smaller
</button>
<div
  style="width:100px;height:100px;background-color: purple;transform: scale({$scale});transform-origin:0 0;"
/> -->

<Form
  on:submit={(e) => {
    console.log(e.detail);
  }}
  initialValues={{ username: "test", email: "test@test.com" }}
>
  <Field label="Username" name="username" type="text" validate={validateRequiredField} />
  <Field label="Email" name="email" type="email" validate={validateEmail} />
  <Field label="Password" name="password" type="password" validate={validateRequiredField} />
  <Button type="submit">Submit</Button>
</Form>
