const axios = require('axios');
const chai = require('chai');

describe('basic integration testing', () => {
  describe('GET /', () => {
    it('endpoint GET /', (done) => {
      axios.get('http://localhost:7865')
        .then((response) => {
          chai.expect(response.status).to.equal(200);
          chai.expect(response.data).to.equal('Welcome to the payment system');
          done();
        })
        .catch((error) => {
          done(error);
        });
    });
  });
});
