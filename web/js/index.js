var localData = [
  {
    "ID": 202,
    "CHAR": "1",
    "TEXT": "TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_1",
    "NUM": 11.2,
    "XH": 1
  },
  {
    "ID": 201,
    "CHAR": "111",
    "TEXT": "TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_2",
    "DATE": new Date(),
    "XH": 2
  },
  {
    "ID": 200,
    "CHAR": "200",
    "TEXT": "TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_TEXT_3",
    "XH": 3
  },
  {
    "ID": 199,
    "CHAR": "199",
    "XH": 4
  },
  {
    "ID": 32,
    "CHAR": "34",
    "NUM": 12.1,
    "XH": 5
  }];

$(function () {
  vargridObj = $.fn.bsgrid.init('searchTable', {
    localData: localData,
    // autoLoad: false,
    pageSize: 5,
    stripeRows: true
  });
});