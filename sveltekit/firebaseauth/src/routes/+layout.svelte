<script lang="ts">
  import { onMount } from "svelte";
  import {auth} from "../lib/firebase/firebase.client";
  
  onMount(() => {
    const unsubscribe = auth.onAuthStateChanged((user) => {
      if (user) {
        // User is signed in.
        console.log(user)
      } else {
        // No user is signed in.
      }
    });
  });
</script>
<slot></slot>