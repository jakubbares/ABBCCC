import {firstBy} from 'thenby';
import * as moment from 'moment';

import * as _ from 'lodash';

export function parseFloats(stats) {
  return stats.map(s => {
    for (const key in s) {
      const result = parseFloat(s[key]);
      if (isNaN(result) || key === 'season') {
        continue;
      } else {
        s[key] = Math.round(result * 100) / 100;
      }
    }
    return s;
  });
}

export function transformData(data) {
  return data.map(d => {
    const object = {
      'id': d.id
    };
    if (d.hasOwnProperty('attributes')) {
      const keys = Object.keys(d.attributes);
      keys.forEach(key => {
        object[key] = d.attributes[key]
      });
      return object;
    } else {
      return d;
    }
  });
}

export function transformInMap(data, field) {
  const map = {};
  data.forEach(d => {
    const object = {
      'id': d.id
    };
    if (d.hasOwnProperty('attributes')) {
      const keys = Object.keys(d.attributes);
      keys.forEach(key => {
        object[key] = d.attributes[key]
      });
      map[object[field]] = object;
    } else {
      map[d[field]] = d;
    }
  });
  return map;
}

export function isEmpty(obj) {
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      return false;
    }
  }
  return true;
}

export function roundToDecimals(obj, numPlaces) {
  const multiplier = parseInt('1' + repeat('0', numPlaces));
  for(let key in obj) {
    if (!isNaN(obj[key])) {
      obj[key] = Math.round(obj[key] * multiplier) / multiplier;
    }
  }
  return obj
}

export function uniqueCounts(array) {
  return array.reduce((acc, btn) => {
    acc[btn] = acc[btn] ? acc[btn] + 1 : 1;
    return acc;
  }, Object.create(null));
}

export function highestKeyByValue(map) {
  const tuples = Object.keys(map).map(key => { return { key: key, value: map[key]}});
  return tuples.length ? tuples.sort((a, b) => b.value - a.value)[0].key : null;
}

export function range(max) {
  return _.range(max)
}

export function distinct(value, index, self) {
  return self.indexOf(value) === index;
}

export function filterRowToCustomKeys(row, keys) {
  const object = {};
  keys.forEach(key => {
    object[key] = row[key]
  });
  return object;
}

export function capitalizeField(field) {
  return field[0].toUpperCase() + field.slice(1).replace(/_/g, ' ');
}

export function capitalizeAllWords(field) {
  return field.replace(/_/g, ' ').split(' ').map(x => capitalizeField(x)).join(' ');
}

export function sort(array) {
  return array.sort(function(a, b) {
    if (a < b) {
      return -1;
    }
    if ( a > b) {
      return 1;
    }
    return 0;
  });
}

export function sortByFieldWithOrder(field, array, order) {
  return array.sort(function(a, b) {
    if (a[field] < b[field])
      return order ? 1 : -1;
    if (a[field] > b[field])
      return order ? -1 : 1;
    return 0;
  });
}

export function sortByField(array, field) {
  return array.sort(function(a, b) {
    if (a[field] < b[field]) {
      return -1;
    }
    if ( a[field] > b[field]) {
      return 1;
    }
    return 0;
  });
}

export function sortByTwoFields(items, field, field2) {
  return items.sort(
    firstBy(function (a, b) {
      if (a[field] < b[field])
        return -1;
      if ( a[field] > b[field])
        return 1;
      return 0;
    })
      .thenBy(function (a, b) {
        if (a[field2] < b[field2])
          return -1;
        if ( a[field2] > b[field2])
          return 1;
        return 0;
      }));
}

const monthNames = ["Jan", 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']

export function dateFromDate(date) {
  return `${date.getDate()} ${monthNames[date.getMonth()]}, ${date.getFullYear()}`
}

export function dateFromSQL(sqlDate) {
  const date = new Date(sqlDate);
  return `${date.getDate()} ${monthNames[date.getMonth()]}, ${date.getFullYear()}`
}

export function dateFromCzech(czechDate) {
  const date = moment(czechDate, "DD.MM.YYYY").toDate();
  return `${date.getDate()} ${monthNames[date.getMonth()]}, ${date.getFullYear()}`
}

export function parseTime(time) {
  time = parseFloat(time);
  const minutes = Math.round(time / 60);
  const seconds = Math.round(time % 60);
  return `${minutes}:${seconds}`
}


export function meanForField(numbers: number[], field: string) {
  let total = 0, i;
  for (i = 0; i < numbers.length; i += 1) {
    total += numbers[i][field];
  }
  return total / numbers.length;
}

export function average(data, field: string) {
  const sum = data.map(d => d[field]).reduce(function(sum, value) {
    return sum + value;
  }, 0);
  return sum / data.length;
}

export function repeat(item, times) {
  const arr = [];
  for (var i = 0; i < times; i++) {
    arr.push(item);
  }
  return arr;
}



export function scale(x, maxX, length) {
  return Math.round(x * (length) / maxX);
}
