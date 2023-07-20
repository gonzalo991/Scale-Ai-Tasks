class HashTableLinearProbing {
    constructor(size) {
        this.size = size;
        this.buckets = new Array(size).fill(null);
        this.entries = new Array(size).fill(null);
    }

    hash(key) {
        let total = 0;
        for (let i = 0; i < key.length; i++)
            total += key.charCodeAt(i);
        return total % this.size;
    }

    set(key, value) {
        let index = this.hash(key);
        while (this.buckets[index]) {
            index++;
            if (index >= this.size)
                index = 0;
        }
        this.buckets[index] = key;
        this.entries[index] = value;
    }

    get(key) {
        let startIndex = this.hash(key);
        let index = startIndex;
        do {
            if (this.buckets[index] === key)
                return this.entries[index];
            index++;
            if (index >= this.size)
                index = 0;
        } while (index !== startIndex);
        return undefined;
    }
}

const phoneBook = new HashTableLinearProbing(10);
phoneBook.set("Nathan", "555-0182");
phoneBook.set("Jane", "555-0182");
console.log(phoneBook.get("Nathan"));
console.log(phoneBook.get("Jane"));
