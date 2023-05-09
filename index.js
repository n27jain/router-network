const express = require('express');
const app = express();
const PORT = 8080;


//   Distance = 10^((Measured Power - Instant RSSI)/10*N).


//TODO: Modify this value
const N = 2 // 2-4
const mp = -44



app.use( express.json() );
var tables = new Object();
// app.use(express.json() ); 

app.listen(
    PORT,
    () => console.log(`its alive on http://localhost:${PORT}`)
)

app.get('/infotest', (req, res) => {
    res.status(200).send({
        tshirt: "naman",
        color: "red"
    });

});


// app.post('addTable/:id', (req, res) => {

// }
app.post('/addTable/:device_id', (req, res) => {


    const { device_id } = req.params; // This is the ID of the device sending its table 
    var toDo = true;
    const { routes } = req.body;
    console.log(device_id, routes);
    const table =  {
        routes: routes
    }
    
    tables[device_id] = table;

    console.log("newObj:", tables);
   
    // TODO: change this number to match the number of esp devices we are calculating for. 
    if(Object.keys(tables).length >= 5){
        // we are assuming that we are waiting for the routing for 5 different esp modules
        console.log()
        res.send({
            message: "we have 5 routes and can now run the python script! done it!",
            newObj: tables
        });
    }
    else{
        res.send({
            message: "we done it!",
            newObj: tables
        });
    }

   
})