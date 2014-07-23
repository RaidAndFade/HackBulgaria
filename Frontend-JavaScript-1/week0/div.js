// returns a list of divisors
// recursive version
var divisors = function(n) {
  var divisorsInner = function(start, n) {
    if (start === n) {
      return [n];
    }

    if (n % start === 0) {
      return [start].concat(divisorsInner(start + 1, n));
    } else {
      return [].concat(divisorsInner(start + 1, n));
    }
  };

  return divisorsInner(1, n);
};

console.log(divisors(8));

var divisors2 = function(n) {
  var divisorsInner = function(start, n, result) {
    if (start > n) {
      return result;
    }

    if (n % start === 0) {
      result.push(start);
    }

    return divisorsInner(start + 1, n, result);
  };

  return divisorsInner(1, n, []);
};

console.log(divisors2(8));
