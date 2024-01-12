//Date

const data1 = new Date()
const date2 = new Date('July 29 2023 01:01')
const date3 = new Date(2019,07,28,1,01)

date3.setFullYear(2032)


console.log(date3)


date2.toDateString()
date2.toTimeString()
date2.toISOString()