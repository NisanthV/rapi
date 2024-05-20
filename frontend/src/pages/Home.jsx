import React, { useEffect, useState } from "react";
import api from "../api";
import Notes from "../components/Notes";
import "../styles/Home.css";

export default function Home() {
  const [title, setTitle] = useState("");
  const [notes, setNotes] = useState([]);
  const [content, setContent] = useState("");

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = () => {
    api
      .get("/bf/create/")
      .then((res) => {
        const data = res.data;
        setNotes(data);
      })
      .catch((err) => alert(err));
  };

  const deleteNotes = (id) => {
    api
      .delete(`/bf/delete/${id}`)
      .then((res) => {
        if (res.status === 204) alert("deleted");
        else alert("not deleted");
        getNotes();
      })
      .catch((err) => alert(err));
  };

  const createNotes = (e) => {
    e.preventDefault();

    api
      .post("/bf/create/", { content, title })
      .then((res) => {
        if (res.status === 201) alert("success");
        else alert("failed");
        getNotes();
      })
      .catch((err) => alert(err));
  };

  return (
    <>{console.log(notes)}
      {notes.map((note) => (
        <Notes note={note} onDelete={deleteNotes} key={note.id} />
      ))}
      <h2>Create a Note</h2>
      <form onSubmit={createNotes}>
        <label htmlFor="title">Title:</label>
        <br />
        <input
          type="text"
          id="title"
          name="title"
          required
          onChange={(e) => setTitle(e.target.value)}
          value={title}
        />
        <label htmlFor="content">Content:</label>
        <br />
        <textarea
          id="content"
          name="content"
          required
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
        <br />
        <input type="submit" value="Submit"></input>
      </form>
    </>
  );
}
