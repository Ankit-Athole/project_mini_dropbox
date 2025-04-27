import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FileList from '../components/FileList';
import UploadForm from '../components/UploadForm';

function Home() {
  const [files, setFiles] = useState([]);

  const fetchFiles = async () => {
    const res = await axios.get('http://localhost:8000/files');
    setFiles(res.data);
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-3xl font-bold mb-4">My Files</h1>
      <UploadForm onUpload={fetchFiles} />
      <FileList files={files} />
    </div>
  );
}

export default Home;
