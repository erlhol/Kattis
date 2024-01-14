fun main() {
    var line = readLine()
    while (line != null) {
        val(a,b) = line.split(' ')
        val diff = a.toLong() - b.toLong()
        if (diff < 0) {
            println(-diff)
        }
        else {
            println(diff)
        }
        line = readLine()
    }
}
