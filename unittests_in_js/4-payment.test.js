const sinon = require('sinon');
const assert = require('assert');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function () {
    const consoleSpy = sinon.spy(console, 'log');

    it('should call Utils.calculateNumber with correct arguments', function() {
        const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        sendPaymentRequestToApi(100, 20);
        assert(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20));
        assert(consoleSpy.calledOnceWithExactly('The total is: 10'));
    });
});
