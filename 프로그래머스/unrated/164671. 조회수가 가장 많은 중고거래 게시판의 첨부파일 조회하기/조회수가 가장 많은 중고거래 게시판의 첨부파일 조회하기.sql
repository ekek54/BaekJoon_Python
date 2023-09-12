-- 코드를 입력하세요
SELECT CONCAT("/home/grep/src/", F.BOARD_ID, "/", F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE F
WHERE F.BOARD_ID = (
    SELECT B.BOARD_ID
    FROM USED_GOODS_BOARD B
    WHERE B.VIEWS = (
        SELECT MAX(BB.VIEWS) FROM USED_GOODS_BOARD BB
    )
)
ORDER BY F.FILE_ID DESC