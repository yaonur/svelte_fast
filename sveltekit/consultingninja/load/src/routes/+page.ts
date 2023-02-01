export async function load({ fetch }) {
  const resp = await fetch("http://randomuser.me/api/");
  const data = await resp.json();
  return {
    data
  };
}
