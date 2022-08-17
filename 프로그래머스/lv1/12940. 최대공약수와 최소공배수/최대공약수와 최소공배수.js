let div = (a) => {
    return Array(a).fill(0).reduce((acc, cur, idx) => {
    acc.push(idx+1);
    return acc;
    }, []).filter((e)=>{
        return a%e === 0
    })
}

let gcd = (n,m)=>{
    const div_n = div(n)
    const cd = div_n.filter(e=>m%e===0)
    return cd[cd.length-1]
}

let gcm = (n,m)=>{
    const GCD = gcd(n,m)
    return (n * m)/GCD
}

function solution(n, m) {
    return n <= m 
        ? [gcd(n,m),gcm(n,m)] 
        : [gcd(m,n),gcm(m,n)]
}
console.log(div(12))