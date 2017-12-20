(require '[clojure.java.io :as io]
         '[clojure.string :as str])

(def rdr (io/reader "./resources/day6-input.txt"))

(def input (vec (map read-string (str/split (first (line-seq rdr)) #"\t"))))

(defn next-idx [i size]
  (if (= i (- size 1)) 0 (inc i)))

;; Redistribute the highest block
(defn reallocate [ls]
  (let [start-num (apply max ls)
        start-idx (nth ls start-num)
        size      (count ls)]
    (loop [num  start-num
           i    (next-idx start-idx size)
           ls   (assoc ls start-idx 0)]
      (println "num" num)
      (println "i" i)
      (println ls)
      (if (= 0 num)
        ls
        (let [new-ls (assoc ls i (inc (nth ls i)))]
          (recur (dec num) (next-idx i size) new-ls))))))

(reallocate input)