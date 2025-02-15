const express = require("express");
const path = require("path");
const app = express();

app.get("/", (req, res) => {
  res.redirect("/view?file=index.html");
});

app.get("/view", (req, res) => {
  let file = req.query.file;
  console.log("Requested file:", file);

  if (!file) {
    res.redirect("/view?file=index.html");
    return;
  }

  file = decodeURIComponent(file);
  file = sanitizePath(file);
  console.log("Sanitized file:", file);

  res.sendFile(resolvePath(file), (err) => {
    if (err && !res.headersSent) {
      try {
        res.send(clean(file) + " not found");
      } catch {
        res.end();
      }
    }
  });
});

function sanitizePath(input) {
  return input.replace(/(\.\.[\/\\])/g, "");
}

function resolvePath(input) {
  return path.resolve("./public/" + input);
}

app.listen(3333, () => {
  console.log("Server running on http://0.0.0.0:3333");
});
