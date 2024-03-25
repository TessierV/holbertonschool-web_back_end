const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function() {
  it('should return the rounded sum of two numbers', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1, 3), 2);
    assert.strictEqual(calculateNumber(1, -3), -2);
  });
  it('should return NaN if one of the arguments is not a number', function() {
    assert.strictEqual(isNaN(calculateNumber('a', 3)), true);
    assert.strictEqual(isNaN(calculateNumber(1, 'b')), true);
    assert.strictEqual(isNaN(calculateNumber('foo', 'bar')), true);
  });
});
