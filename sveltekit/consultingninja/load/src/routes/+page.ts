export async function load({ fetch }) {
  const resp = await fetch("http://universities.hipolabs.com/search?country=Turkey");
  const data = await resp.json();
  return {
    data
  };
}
