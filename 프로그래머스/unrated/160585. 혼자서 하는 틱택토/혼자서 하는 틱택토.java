/* 
선공이 O 후공이 X: O가 하나 많거나 같다.
게임이 끝난 상황:
    O가 이긴 경우: O가 하나 많고 3개 일렬로 배치, X의 일렬 배치가 있으면 안됨
    X가 이긴 경우: O와 개수가 같고 O의 일렬 배치가 있으면 안됨, X의 일렬배치가 있어야함
코드 흐름
    1. 개수 판별 -> 누구의 턴인지 식별
    2. 게임 종료 판별 -> 현재 턴의 사람이 승리했는지 판별
*/
import java.util.*;

class Solution {
    public int solution(String[] board) {
        int answer = 0;
        int[] cntOX = countOX(board);
        boolean Oturn = false;
        // 말의 개수 위반
        if (cntOX[0] < cntOX[1] || cntOX[0] > cntOX[1] + 1){
            return 0;
        }
        
        if (cntOX[0] == cntOX[1] + 1) Oturn = true;
        
        if (Oturn && (winner(board) == 0 || winner(board) ==1)){
            return 1;
        }
        
        if (!Oturn && (winner(board) == 0 || winner(board) ==2)){
            return 1;
        }
        else return 0;
    }
    /*
      0: 승자 x
      1: O 승리
      2: X 승리
      3: O, X 둘다 빙고 존재
    */
    public int winner(String[] board){
        int resultRow = chkRow(board);
        int resultCol = chkCol(board);
        int resultX = chkX(board);
        if (resultRow == 3 || resultCol == 3){
            return 3;
        }
        if (resultRow == 0 && resultCol == 0 && resultX == 0){
            return 0;
        }
        else{
            return Math.max(Math.max(resultRow, resultCol), resultX);
        }
    }
    
    public int chkRow(String[] board){
        boolean Oflag = false;
        boolean Xflag = false;
        for(int i = 0; i < board.length; i ++){
            if(board[i].charAt(0) == '.') continue;
            char curSymbol = board[i].charAt(0);
            boolean flag = true;
            for(int j = 0; j < board[i].length(); j ++){
                if (curSymbol != board[i].charAt(j)) {
                    flag = false;
                    break;
                }
            }
            if (flag){
                if (curSymbol == 'O') Oflag = true;
                if (curSymbol == 'X') Xflag = true;
            }
        }
        int ret = Oflag && Xflag ? 3 : Xflag ? 2 : Oflag ? 1 : 0;
        return ret;
    }
    
    
    public int chkCol(String[] board){
        boolean Oflag = false;
        boolean Xflag = false;
        for(int i = 0; i < board[0].length(); i ++){
            if(board[0].charAt(i) == '.') continue;
            char curSymbol = board[0].charAt(i);
            boolean flag = true;
            for(int j = 0; j < board.length; j ++){
                if (curSymbol != board[j].charAt(i)) {
                    flag = false;
                    break;
                }
            }
            if (flag){
                if (curSymbol == 'O') Oflag = true;
                if (curSymbol == 'X') Xflag = true;
            }
        }
        int ret = Oflag && Xflag ? 3 : Xflag ? 2 : Oflag ? 1 : 0;
        return ret;
    }
    
    public int chkX(String[] board){
        boolean Oflag = false;
        boolean Xflag = false;
        if(board[0].charAt(0) != '.') {
            char curSymbol = board[0].charAt(0);
            boolean flag = true;
            for(int i = 0; i < board.length; i ++){
                if (board[i].charAt(i) != curSymbol){
                    flag = false;
                    break;
                }
            }
            if (flag){
                if (curSymbol == 'O'){
                    Oflag = true;
                }
                if (curSymbol == 'X'){
                    Xflag = true;
                }
            }
        }
        if(board[0].charAt(2) != '.'){
            char curSymbol = board[0].charAt(2);
            boolean flag = true;
            for(int i = 0; i < board.length; i ++){
                if (board[i].charAt(2 - i) != curSymbol){
                    flag = false;
                    break;
                }
            }
            if (flag){
                if (curSymbol == 'O'){
                    Oflag = true;
                }
                if (curSymbol == 'X'){
                    Xflag = true;
                }
            }
        }
        int ret = Oflag && Xflag ? 3 : Xflag ? 2 : Oflag ? 1 : 0;
        return ret;
    }
    
    public int[] countOX(String[] board){
        int [] ret = {0, 0};
        for (int i = 0; i < board.length; i ++){
            for (int j = 0; j < board[i].length(); j ++){
                if (board[i].charAt(j) == 'O'){
                    ret[0] += 1;
                }
                else if(board[i].charAt(j) == 'X'){
                    ret[1] += 1;
                }
            }
        }
        return ret;
    }
}