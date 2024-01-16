import { useEffect, useState } from "react";

function App() {
  const [selectedDate, setSelectedDate] = useState()
  const [currentDate, setCurrentDate] = useState(new Date());
  const [wordcloudImage, setWordcloudImage] = useState("");

 useEffect(() => {
    var fecha_actual_utc = new Date();
    var desplazamiento_utc_menos3 = -3 * 60 * 60 * 1000; // 3 horas en milisegundos
    fecha_actual_utc.setTime(fecha_actual_utc.getTime() + desplazamiento_utc_menos3);
    var fecha_actual = fecha_actual_utc.toISOString().slice(0, 10);
    document.getElementById("fecha_actual").textContent = fecha_actual;
    setWordcloudImage("/wordcloud/Wordcloud - " + fecha_actual + ".png");
    setSelectedDate(fecha_actual); 
}, [currentDate]);

  const handleDateChange = (event) => {
    const dateValue = event.target.value;
    setSelectedDate(dateValue);

    // Actualizar la imagen cuando se cambie la fecha seleccionada
    if (dateValue) {
      const formattedDate = new Date(dateValue).toISOString().slice(0, 10);
      document.getElementById("fecha_actual").textContent = formattedDate;
      setWordcloudImage("/wordcloud/Wordcloud - " + formattedDate + ".png");
    }
  };
  return (
    <>
      <div className="bg-slate-800 h-screen">
        <h1 className="text-3xl text-white font-bold text-center p-4 bg-slate-600">
          WordCloud del día <span id="fecha_actual"></span>
        </h1>
        <div className="justify-center align-middle flex flex-col text-center m-auto">
          <input
            type="date"
            className="max-w-32 flex m-auto"
            onChange={handleDateChange}
            value={selectedDate}
          />  </div>
          <img
            id="wordcloud_img"
            className='m-auto w-11/12'
            src={wordcloudImage}
            alt={`WordCloud del día ${selectedDate}`}
          />
      
      </div>
    </>
  );
}

export default App;
