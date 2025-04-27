import React, { useState } from 'react';
import axios from 'axios';
import { toast } from 'react-toastify';

function UploadForm({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('uploaded_file', file);

    try {
      await axios.post('http://localhost:8000/upload', formData);
      toast.success('File uploaded successfully!');
      onUpload();
    } catch (error) {
      toast.error('Failed to upload file.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded ml-2">
        Upload
      </button>
    </form>
  );
}

export default UploadForm;
