import supabase from "../config/supabaseClient";
import { useEffect, useState } from "react";
//components
import SmoothieCard from "../components/SmoothieCard";

const Home = () => {
  const [fetchError, setFetchError] = useState(null);
  const [smoothies, setSmoothies] = useState(null);

  useEffect(() => {
    const fetchSmoothies = async () => {
      const { data, error } = await supabase.from("smoothies").select("*");
      if (error) {
        setFetchError(error);
        setSmoothies(null);
        console.log("error fetching smoothies");
      } else {
        setSmoothies(data);
        setFetchError(null);
      }
    };

    fetchSmoothies();
  }, []);

  return (
    <div className="page home">
      {fetchError && <div className="error">{fetchError.message}</div>}
      {smoothies && (
        <div className="smoothies">
          {/*order by rating*/}
          <div className="smoothie-grid">
            {smoothies.map((smoothie) => (
              <SmoothieCard key={smoothie.id} smoothie={smoothie} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
