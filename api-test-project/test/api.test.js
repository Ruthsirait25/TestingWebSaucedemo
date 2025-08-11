const axios = require('axios');
const assert = require('assert');

const baseURL = 'http://localhost:3000';

describe('Local API Test', () => {
  it('should return empty user list', async () => {
    const res = await axios.get(`${baseURL}/users`);
    assert.strictEqual(res.status, 200);
    assert.ok(Array.isArray(res.data));
  });

  it('should create a new user', async () => {
    const res = await axios.post(`${baseURL}/users`, {
      name: 'ruth',
      job: 'developer'
    });

    assert.strictEqual(res.status, 201);
    assert.strictEqual(res.data.name, 'ruth');
    assert.strictEqual(res.data.job, 'developer');
  });

  it('should return 404 for non-existent user', async () => {
    try {
      await axios.get(`${baseURL}/users/999`);
    } catch (err) {
      assert.strictEqual(err.response.status, 404);
    }
  });
});
