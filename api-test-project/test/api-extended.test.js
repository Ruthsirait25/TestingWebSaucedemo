const axios = require('axios');
const { expect } = require('chai');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'http://localhost:3000/users';
let createdUserId;

// Helper function to read JSON payload
function loadJSON(fileName) {
  const filePath = path.join(__dirname, '../json', fileName);
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

describe('Extended Local API Test (using Chai)', () => {
  // it('should create a user for further testing', async () => {
  //   const payload = loadJSON('create-user.json');
  //   const res = await axios.post(BASE_URL, payload);
  //   expect(res.status).to.equal(201);
  //   expect(res.data).to.have.property('name', payload.name);
  //   createdUserId = res.data.id;
  // });
it('should create a user for further testing', async () => {
  const payload = loadJSON('create-user.json');
  const res = await axios.post(BASE_URL, payload);
  expect(res.status).to.equal(201);
  expect(res.data).to.have.property('name', payload.name);
  createdUserId = res.data.id;
  console.log('Created User ID:', createdUserId);  // 👉 Cek ID-nya valid atau tidak
});
  it('should get user by ID', async () => {
    const res = await axios.get(`${BASE_URL}/${createdUserId}`);
    expect(res.status).to.equal(200);
    expect(res.data).to.have.property('name', 'ruth');
  });

  it('should update user data', async () => {
    const payload = loadJSON('update-user.json');
    const res = await axios.put(`${BASE_URL}/${createdUserId}`, payload);
    expect(res.status).to.equal(200);
    expect(res.data).to.have.property('name', payload.name);
  });

  it('should delete the user', async () => {
    const res = await axios.delete(`${BASE_URL}/${createdUserId}`);
    expect(res.status).to.equal(204);
  });

  it('should return 404 after user is deleted', async () => {
    try {
      await axios.get(`${BASE_URL}/${createdUserId}`);
    } catch (err) {
      expect(err.response.status).to.equal(404);
    }
  });
});
