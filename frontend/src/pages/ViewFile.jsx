import React from 'react';
import { useParams } from 'react-router-dom';

function ViewFile() {
  const { id } = useParams();

  const fileUrl = `http://localhost:8000/files/${id}`;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">View File</h1>
      <p>Download or view the file: </p>
      <a href={fileUrl} target="_blank" rel="noreferrer" className="text-blue-500 underline">
        Open File
      </a>
    </div>
  );
}

export default ViewFile;
