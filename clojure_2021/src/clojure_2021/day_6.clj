(ns clojure-2021.day-6
  (:gen-class))


(defn lanternfish [state]
  (loop [i 0
    fishmap {}]
    (if (>= i (count state))
      fishmap
      (let [fish (get state i)]
        (recur (inc i)
          (update fishmap fish (fnil inc 0)))))))
               
(defn sim-day [initial-state]
  (println initial-state)
  (loop [remaining-state initial-state
    new-state {}]
      (if (empty? remaining-state)
        new-state
        (let [[part & remaining] remaining-state
            key (first part)
            val (second part)]
            (recur remaining
                (if (zero? key)
                    (assoc new-state 8 val 6 val)
                    (assoc new-state (dec key) val))))))) ;; bug in here



(defn -main [& args]
    (loop [day 0
        state (lanternfish [3 4 3 1 2])]
        (if (< 18 day)
        (println "answer is" (reduce + (vals state)))
        (recur (inc day) (sim-day state)))))

