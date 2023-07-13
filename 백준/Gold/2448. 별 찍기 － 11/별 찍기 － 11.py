from sys import stdin
from collections import deque

N = int(stdin.readline())


def draw(N):
    if N == 3:
        basic = ["  *  "," * * ", "*****"]
        return basic
    else:
        l = draw(N // 2)
        result = []
        pad = " " * (N // 2)
        for i in range(N // 2):
            result.append(pad + l[i] + pad)
        for i in range(N // 2):
            result.append(l[i] + " " + l[i])
        return result

def pb(board):
    for i in range(len(board)):
        print(board[i])


pb(draw(N))
"""
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
"""
