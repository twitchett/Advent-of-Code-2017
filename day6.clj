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

(defn ls-key [input]
   (str/replace (str input) #"\s" "-"))

(defn reallocate-all [input]
  (loop [ls  input
         k   (ls-key input)
         cnt  0
         seen {}]
    (if (contains? seen k)
       (do
        (println "Total cycles: " cnt)
        (println "Loop cycles: " (- cnt (get seen k))))
      (let [next-ls (reallocate ls)
            next-k (ls-key next-ls)
            next-cnt (inc cnt)]
        (recur next-ls
          next-k
          next-cnt
          (assoc seen k cnt))))))

(reallocate-all (vec input))
