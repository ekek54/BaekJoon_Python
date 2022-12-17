class Solution {
    fun solution(board: Array<IntArray>): Int {
        var answer: Int = 0
        var bomb_site = Array(board.size,{IntArray(board.size,{0})})
        for(i in 0 until board.size){
            for(j in 0 until board.size){
                if(board[i][j] == 1){
                    bomb_site = bomb_site_checker(bomb_site, i, j)
                }
            }
        }
        for(i in 0 until board.size){
            for(j in 0 until board.size){
                if(bomb_site[i][j] == 0) answer += 1
            }
        }
        return answer
    }
    
    fun bomb_site_checker(board: Array<IntArray>, bomb_i: Int, bomb_j: Int): Array<IntArray>{
        board[bomb_i][bomb_j] = 1
        val bomb_range = arrayOf(intArrayOf(1, 0),intArrayOf(0, 1), intArrayOf(-1, 0), intArrayOf(0, -1), intArrayOf(1, 1), intArrayOf(1, -1),intArrayOf(-1, 1), intArrayOf(-1, -1))
        for(i in 0 until bomb_range.size){
            val dx = bomb_range[i][0]
            val dy = bomb_range[i][1]
            if( 0 <= bomb_i + dx && bomb_i + dx < board.size && 0 <= bomb_j + dy && bomb_j + dy < board.size){
                board[bomb_i + dx][bomb_j + dy] = 1
            }
        }
        return board
    }
}