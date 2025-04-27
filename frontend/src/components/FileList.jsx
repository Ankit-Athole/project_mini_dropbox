import React from 'react';
import { Link } from 'react-router-dom';

function FileList({ files }) {
  return (
    <div className="mt-6">
      {files.map((file) => (
        <div key={file.id} className="mb-2">
          <Link to={`/view/${file.id}`} className="text-blue-700 underline">
            {file.filename}
          </Link>
        </div>
      ))}
    </div>
  );
}

export default FileList;
