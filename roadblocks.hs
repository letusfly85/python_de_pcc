import Data.List

data Vector = Vector {s:: Int, e:: Int, cost:: Int}
    deriving (Show, Eq, Ord)

genVList :: [Vector]
genVList =  [Vector x y (x + y) | x <- [1..10], y <- [1..10], x < y]

vList = [(Vector 1 2 100), (Vector 2 4 200), (Vector 2 3 250), (Vector 3 4 100)]

shortVector :: Int -> [Vector] -> Vector
shortVector start [] = undefined
shortVector start list = let list' = filter (\v -> s v == start) list
                         in  head $ sortBy (\v0 v1 -> compare (cost v0) (cost v1)) list'

longVector :: Int -> [Vector] -> Vector
longVector start [] = undefined
longVector start list = let list' = filter (\v -> s v == start) list
                        in  head $ sortBy (\v0 v1 -> compare (cost v0) (cost v1)) list'

main = do mapM_ print genVList

shortestWay :: [Vector] -> Int
shortestWay [] = 0
shortestWay (x:xs) = cost x + shortestWay xs

secondWay :: [Vector] -> Int
secondWay []   = 0
secondWay (x:xs) = cost x + shortestWay xs 
