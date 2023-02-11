<script>
  import {goto} from '$app/navigation'
  // import { browser } from '$app/env';
  let myCookie
  function getCookie(name) {
    const value = `${document.cookie}`;
    console.log(value)
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }
  export const logout = () => {
    const cook=getCookie("AuthorizationToken")
    console.log(cook)
      // goto('/login');
  };
  
</script>
<h1>Logout</h1>
<button on:click={logout}>Logout</button>