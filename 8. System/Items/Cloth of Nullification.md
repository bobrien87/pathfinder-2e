---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]"]
price: "{'gp': 75000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small piece of embroidered cloth is inimical to all magic.

**Activate—Nullify Magic** `pf2:2` (manipulate)

**Effect** You cover a magic item with the cloth or wave the cloth near a magic effect and attempt to counteract the effect or item. The cloth's counteract check modifier is +32, and its counteract rank is 10. Regardless of the result, the cloth of nullification can't be activated again for 2d6 hours. On a success, the effect or item is deactivated for the same amount of time, and its duration, if any, continues to expire during that time. With a successful counteract check, you can instead choose to completely absorb the magic from the effect or item into the cloth of nullification. If you do, both become completely non-magical and their magic can't be recovered, even by the remake spell.

The cloth of nullification automatically fails to counteract most artifacts and similarly powerful items

**Source:** `= this.source` (`= this.source-type`)
