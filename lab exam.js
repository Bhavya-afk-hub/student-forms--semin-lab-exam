// StudentForm.js
import React, { useState } from 'react';

function StudentForm() {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    className: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Student Details:\nName: ${formData.name}\nAge: ${formData.age}\nClass: ${formData.className}`);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h2>Student Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name: </label>
          <input
            type="text"
            name="name"
            placeholder="Enter name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <br />
        <div>
          <label>Age: </label>
          <input
            type="number"
            name="age"
            placeholder="Enter age"
            value={formData.age}
            onChange={handleChange}
            required
          />
        </div>
        <br />
        <div>
          <label>Class: </label>
          <input
            type="text"
            name="className"
            placeholder="Enter class"
            value={formData.className}
            onChange={handleChange}
            required
          />
        </div>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default StudentForm;
