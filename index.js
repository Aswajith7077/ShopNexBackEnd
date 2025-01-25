import express from "express";
import mysql from "mysql2";
import dotenv from "dotenv";
import cors from "cors";

dotenv.config();

// const corsOptions = {
//   origin: "https://shop-nex-front-end.vercel.app/",
//   methods: "GET,HEAD,PUT,PATCH,POST,DELETE",
//   credentials: true,
//   optionsSuccessStatus: 204
// };



const app = express();
// app.use(cors(corsOptions));
app.use(
  cors({
    origin: "https://shop-nex-front-end.vercel.app" // Front-end domain
  })
);

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DATABASE
});

/*

GET MINIMUM POINTS TO GET A REWARD

*/
app.get("/", (req, res) => {
  if (!req.body) {
    return;
  }
  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error : ", err);
      return res.status(500).json({ err: "Database Error" });
    }
    connection.query(
      `CALL GET_MIN_POINTS_FOR_REWARD('${req.body["USER_ID"]}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          return res.status(500).json({ error: "Query Error" });
        }
        res.json(rows[0]);
        console.log("GET_MIN_POINTS_FOR_REWARD Successfull Execution !");
      }
    );
  });
});

app.get("/getitems", (req, res) => {
  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error : ", err);
      return res.status(500).json({ err: "Database Error" });
    }

    connection.query(`CALL GET_ITEMS()`, (err, rows) => {
      connection.release();
      if (err) {
        console.log("Query Error", err);
        return res.status(500).json({ error: "Database Query Error" });
      }
      res.json(rows);
      console.log("GET ITEMS Successfull Execution !");
    });
  });
});

app.get("/searchitems", (req, res) => {
  if (!req.body) {
    return;
  }
  console.log(req.body["USER_ID"]);
  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error", err);
      return res.status(500).json({ message: "Database error", err: err });
    }
    const { searchText } = req.body;
    connection.query(
      `CALL GET_SEARCH_RESULTS('${searchText}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(400).json({ error: "Database Query Error" });
        }
        res.json(rows);
        console.log("GET SEARCH RESULTS Successfull Execution !");
      }
    );
  });
});
/*

A GET Request with body {"USER_ID" :'johndoe@example.com'} 

CHECKS USER EXISTANCE

*/

app.get("/userexists", (req, res) => {
  if (!req.body) return;

  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error : ", err);
      return res.status(500).json({ err: "Database Error" });
    }

    connection.query(
      `CALL CHECK_USER_EXISTS('${req.body["USER_ID"]}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json({ user_existance: rows[0] === "SUCCESS" ? true : false });
        console.log("CHECK_USER_EXISTS Successfull Execution !");
      }
    );
  });
});

/*

A GET Request with body {"USER_ID" :'johndoe@example.com',"PASSWD"} 

CREATES USER
*/

app.post("/createuser", (req, res) => {
  if (!req.body) return;

  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error : ", err);
      return res.status(500).json({ err: "Database Error" });
    }
    const { email, password } = req.body;

    connection.query(
      `CALL CREATE_USER('${email}','${password}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json({ user_existance: rows[0] === "SUCCESS" ? true : false });
        console.log("CREATE_USER Successfull Execution !");
      }
    );
  });
});
/* LOGS USER */
app.put("/login", (req, res) => {
  console.log(req);
  if (!req.body) return;

  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error : ", err);
      return res.status(500).json({ err: "Database Error" });
    }
    const { email, password } = req.body;
    connection.query(
      `CALL LOGIN_USER('${email}','${password}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json({ user_logged: rows[0] === "SUCCESS" ? true : false });
        console.log("LOGIN_USER Successfull Execution !");
      }
    );
  });
});

/*

A GET Request with body {"USER_ID" :'johndoe@example.com'} 
GET CART ITEMS OF A USER

*/

app.get("/cart", (req, res) => {
  if (!req.body) {
    return;
  }
  console.log(req.body["USER_ID"]);
  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error", err);
      return res.status(500).json({ error: "Database error" });
    }
    connection.query(
      `CALL GET_CART_ITEMS('${req.body["USER_ID"]}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json(rows[0]);
        console.log("GET_CART_ITEMS Successfull Execution !");
      }
    );
  });
});

/*

A Post Requst with  body { USER_ID: 'johndoe@example.com',PASSWD: 'johndoe'}

CHANGE_PASSWORD OF A USER

*/

app.put("/changepassword", (req, res) => {
  if (!req.body) {
    return;
  }

  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error", err);
      return res.status(500).json({ error: "Database error" });
    }
    connection.query(
      `CALL CHANGE_PASSWORD('${req.body["USER_ID"]}')`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error", err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json({ result: rows[0] });
        console.log("CHANGE PASSWORD Successfull Execution !");
      }
    );
  });
});

/*

A Post Requst with  body { USER_ID: 'johndoe@example.com', PRODUCT_ID: 1010, QUANTITY: 5 }

ADD AN ELEMENT TO CART

*/
app.post("/cart", (req, res) => {
  pool.getConnection((err, connection) => {
    if (err) {
      console.log("Database connection error", err);
      return res.status(500).json({ error: "Database error" });
    }
    connection.query(
      `CALL ADD_TO_CART('${req.body["USER_ID"]}',${req.body["PRODUCT_ID"]},${req.body["QUANTITY"]})`,
      (err, rows) => {
        connection.release();
        if (err) {
          console.log("Query Error");
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json(rows[0]);
        console.log("ADD_TO_CART Successfull Execution !");
      }
    );
  });
});

/*

PLACING an Order

*/

app.post("/product", (req, res) => {
  if (!req.body) {
    return;
  }
  // console.log(req.body["USER_ID"])
  pool.getConnection((err, connection) => {
    if (err) {
      // console.log('Database connection error',err);
      return res.status(500).json({ error: "Database error" });
    }
    connection.query(
      `CALL PLACE_ORDER('${req.body["USER_ID"]}',${req.body["PRODUCT_ID"]},${req.body["QUANTITY"]})`,
      (err, rows) => {
        connection.release();
        if (err) {
          // console.log('Query Error',err);
          return res.status(500).json({ error: "Database Query Error" });
        }
        res.json(rows[0]);
        console.log("GET_CART_ITEMS Successfull Execution !");
      }
    );
  });
});

app.listen(process.env.PORT, () => {});
