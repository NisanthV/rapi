import React from "react";
import "../styles/Notes.css"

export default function Notes({note,onDelete}){
    //const formattedDate = new Date(note.date_time).toLocaleDateString("en-US")
    return(
        <div className="note-container">
        <p className="note-title">{note.title}</p>
        <p className="note-content">{note.content}</p>
        <p className="note-date">{note.data_time}</p>
        <button className="delete-button" onClick={() => onDelete(note.id)}>
            Delete
        </button>
    </div>
    )
}