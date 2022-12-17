class Solution {
    fun solution(num: Int, total: Int): Array<Int> {
        val start: Int = (total-num*(num-1)/2)/num
        print(start)
        val answer: Array<Int> = Array<Int>(num){i -> i + start}
        return answer
    }
}