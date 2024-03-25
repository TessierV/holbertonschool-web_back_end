const sinon = require('sinon');
const assert = require('assert');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with correct arguments', function() {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    assert(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20));
    calculateNumberSpy.restore();
  });
});
