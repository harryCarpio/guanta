// select buyer, count(*), sum(budget) from compraspublicas.procesos group by buyer
// 1349 -   1784    - 1932  -1964   - 1979
// select count(*) from compraspublicas.procesos

//select count(*) from compraspublicas.proceso_ocds


//select buyer, COUNT(*), sum(toDecimal(budget)) from compraspublicas.procesos group by buyer


select arrayElemAt(releases,0) from compraspublicas.proceso_ocds where _id="ocds-5wno2w-CE-20220002207618-158404"