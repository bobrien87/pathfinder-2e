---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You conjure a magical gamtu hat, which is a magic item of light Bulk. The gamtu persists for 1 hour, and you can give the gamtu to another creature to wear.

**Activate—Hat Trick** `pf2:2` (manipulate)

**Effect** You tap the hat and gain the effects of a 2nd-rank [[Invisibility]] spell, which lasts for the spell's normal duration, until the hat is removed, or until the hat's normal duration runs out, whichever comes first. After the spell ends, the gamtu disappears.

**Source:** `= this.source` (`= this.source-type`)
