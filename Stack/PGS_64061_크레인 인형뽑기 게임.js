let board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
let moves = [1, 5, 3, 5, 1, 2, 1, 4];

function solution(board, moves) {
  let score = 0;
  let res = [];
  moves.forEach((element) => {
    let index = element - 1;
    board.some((array, i) => {
      if (array[index] === 0) return false;
      res.push(array[index]);
      board[i][index] = 0;
      if (res.length > 1) {
        let x = res.pop();
        let y = res.pop();
        if (x === y) {
          score += 2;
        } else {
          res.push(y);
          res.push(x);
        }
      }

      return true; // 순회 중단
    });
  });

  return score;
}

solution(board, moves);
