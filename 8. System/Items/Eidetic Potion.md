---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 40}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Bright pink, pale lavender, and vibrant orange colors swirl through this purplish liquid, making the eidetic potion resemble an unforgettable sunset. When you drink this potion, for 1 round, anything you observe becomes locked into your memory. You can recall the memory perfectly and gain a +2 status bonus to create representations of that memory, whether using Crafting to create an artistic rendition or Society to create a Forgery. The memory remains locked for 1 week or until you benefit from the bonus it imparts for the first time, whichever comes first; afterward, it becomes a normal, fallible memory. You can only have a single memory locked in your mind at a time. Using this potion while you have a locked memory from a previous use makes the previously locked memory fallible but allows you to lock a new memory.

**Source:** `= this.source` (`= this.source-type`)
