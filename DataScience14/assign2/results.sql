-- (a) select: σdocid=10398_txt_earn(frequency)
select * from frequency where frequency.docid = '10398_txt_earn';

-- (b) project: πterm(σdocid=10398_txt_earn and count=1(frequency)) 
select * from frequency where frequency.docid = '10398_txt_earn' and frequency.count = 1;

-- (c) union: πterm( σdocid=10398_txt_earn and count=1(frequency)) U πterm( σdocid=925_txt_trade and count=1(frequency)) 
select term from frequency f1 where f1.docid='10398_txt_earn' and f1.count=1 union select term from frequency f2 where f2.docid='925_txt_trade' and f2.count=1;

-- (d) count: Write a SQL statement to count the number of documents containing the word “parliament”
select count(*) from frequency where frequency.term = 'parliament';

-- (e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.
select docid, sum(count) from frequency group by frequency.docid having sum(count) > 300;

--(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. 
select count(*) from frequency f inner join frequency f2 on f.docid = f2.docid where f.term = 'world' and f2.term = 'transactions';

----Problem 2: Matrix Multiplication in SQL --
--(g) multiply: Express A X B as a SQL query, referring to the class lecture for hints.
select A.row_num, B.col_num, sum(A.value * B.value) from A join B on A.col_num = B.row_num group by A.row_num, B.col_num;

----Problem 3: Working with a Term-Document Matrix --
-- (h)I. similarity matrix: Write a query to compute the similarity matrix DDT.
select f.docid, f2.docid, sum(f.count * f2.count) 
from frequency f inner join frequency f2 on f.docid = '10080_txt_crude' and f2.docid = '17035_txt_earn' 
where f.docid < f2.docid ;
group by f.docid, f2.docid;

-- (h)II. similarity matrix: Write a query to compute the similarity matrix DDT.



-- (i) keyword search
CREATE VIEW IF NOT EXISTS new_frequency AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select f.docid, f2.docid, sum(f.count * f2.count)
from new_frequency f join new_frequency f2 on f.term = f2.term 
where f.docid = 'q' and f2.docid != 'q'
group by f.docid, f2.docid
order by sum(f.count * f2.count) desc
limit 5;
