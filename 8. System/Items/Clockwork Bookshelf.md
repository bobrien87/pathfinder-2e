---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Clockwork]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "4"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This device was originally created by an inventor who had way more books they wanted to access than available wall space to store them. Each of the bookshelf's six levels is actually loaded with a pair of shelves instead of a single shelf. A simple switch on the side of the bookshelf flips the corresponding shelf to the other side, revealing any books stored in the paired shelf. While this makes the clockwork bookshelf a little deeper than a normal bookshelf, in order to fit both shelves, it effectively allows you to store twice as many books using the same amount of wall space. Those who wish to keep volumes hidden from visitors (or perhaps stow a weapon or potion within a false book) often load the hidden shelf first, then switch to the second shelf lined with more respectable volumes.

**Source:** `= this.source` (`= this.source-type`)
