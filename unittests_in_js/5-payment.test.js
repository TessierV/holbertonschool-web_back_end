const sinon = require('sinon');
const assert = require('assert');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./5-payment.js');

describe('sendPaymentRequestToApi', function () {
    let consoleSpy;

    beforeEach(function () {
        consoleSpy = sinon.spy(console, 'log');
    });

    afterEach(function () {
        sinon.restore();
    });

    it('payement test 100 20', function () {
        sendPaymentRequestToApi(100, 20);
        assert(consoleSpy.calledOnceWithExactly('The total is: 120'));
    });

    it('payement test 10 10', function () {
        sendPaymentRequestToApi(10, 10);
        assert(consoleSpy.calledOnceWithExactly('The total is: 20'));
    });
});
