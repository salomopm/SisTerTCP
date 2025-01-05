const Hapi = require('@hapi/hapi');
const mysql = require('mysql');


const init = async () => {

    const server = Hapi.server({
      port: 3000,
      host: '127.0.0.1',
      routes: {
        cors: {
          origin: ['*'],
        },
      },
    });
  
    const connection = mysql.createConnection({
      host: '127.0.0.1',  // Use the Cloud SQL IP address or connection name
      user: '',
      password: '',
      database: '',
      port: 3306,
    });
  
    
    connection.connect((err) => {
      if (err) {
        console.error('Error connecting to the database:', err);
        process.exit(1);
      }
      console.log('Connected to the database');
    });
  
    
    await server.start();
    console.log(`Server berjalan pada ${server.info.uri}`);
  };
     
    init();