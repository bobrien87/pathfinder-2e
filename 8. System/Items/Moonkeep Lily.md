---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Plant]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These magical flowers are infused with the power to counteract the curse of the werecreature. Intentionally growing these flowers is nearly impossible, as they don't produce seeds, and the primal magic required to produce them has been lost to time. They occasionally grow in places where a particular powerful werecreature is buried, though if an exact process to guarantee their growth exists, it remains a mystery.

This thin, white lily has stamens that end in small, round portions resembling the moon. When you eat the flower, you gain the flower's protection for 1 week. During this time, your curse of the werecreature becomes partially inert. Your jaws Strike doesn't inflict the curse of the werecreature during this time.

**Source:** `= this.source` (`= this.source-type`)
