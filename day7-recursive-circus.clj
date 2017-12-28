(require '[clojure.java.io :as io]
         '[clojure.set :as cset]
         '[clojure.string :as cstr])

(def inputFile "./resources/day7.txt")
(def re #"[a-z]+")

;; regex splits file into seq of words
;; frequencies maps each word to number of occurances
;; map-invert reverses keys and values
;; get retrieves word with frequency of 1
(def root (get (cset/map-invert (frequencies (re-seq re (slurp inputFile)))) 1))

(println "Root node:" root)
