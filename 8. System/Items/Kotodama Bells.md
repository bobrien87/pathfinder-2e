---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This set of bronze bells bear engravings with symbols representing the word "awaken." Among kotodama magic users, who seek to touch the souls of objects using the power of words, the peals of these bells are known to awaken the spirits of even inanimate objects.

**Activate—Awaken the Soul** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You ring the bell and focus on an object of negligible Bulk within 10 feet. The bell's toll animates the object for 24 hours. The object becomes a minion that can't attack but can move and take simple Interact actions appropriate for an item of its type, as determined by the GM. For example, a piece of chalk can write a message or draw a symbol, a hand fan can open or fan in a particular direction, or a magnifying glass can set itself up to dramatically reveal incriminating evidence. The animated item has AC 5, 5 Hit Points, a Speed of 10 feet, and automatically fails all saves. If the object is broken, it can no longer move, though it can still Interact as appropriate for an item of its type. As normal with minions you control, you must Command the object to grant it actions.

**Source:** `= this.source` (`= this.source-type`)
