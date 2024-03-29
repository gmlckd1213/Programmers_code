SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM PATIENT P
JOIN APPOINTMENT A
ON P.PT_NO = A.PT_NO
JOIN DOCTOR D
ON D.DR_ID = A.MDDR_ID
WHERE DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = DATE_FORMAT( '2022-04-13', '%Y-%m-%d') AND A.MCDP_CD = 'CS' AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD
