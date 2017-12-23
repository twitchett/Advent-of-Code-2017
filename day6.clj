(require '[clojure.java.io :as io]
         '[clojure.string :as str])

(def rdr (io/reader "./resources/day6-input.txt"))

(def input (map read-string (str/split (first (line-seq rdr)) #"\t")))

(defn next-idx [i size]
  (if (= i (- size 1)) 0 (inc i)))

;; Redistribute the highest block
(defn reallocate [ls]
  (let [start-num (apply max ls)
        start-idx (.indexOf ls start-num)
        size      (count ls)]
    (loop [num start-num
           i   (next-idx start-idx size)
           ls  (assoc ls start-idx 0)]
      (if (= 0 num)
        ls
        (recur (dec num)
          (next-idx i size)
          (assoc ls i (inc (nth ls i))))))))

(defn reallocate-all [input]
  (loop [cur  input
         cnt  0
         seen (set #{})]
    (if (not (= cnt (count seen)))
      cnt
      (let [next-ls (reallocate (vec cur))]
        (recur next-ls
          (inc cnt)
          (conj seen next-ls))))))

(println (reallocate-all input))
