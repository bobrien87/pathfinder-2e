---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Disarm]]", "[[Finesse]]", "[[Monk]]", "[[Parry]]", "[[Twin]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This short, single-edged sword typically features a cross guard that helps catch oncoming attacks. It's the preferred weapon of Butterfly Blades—highly skilled Gokan assassins. These swords are typically crafted and sold in pairs.

**Source:** `= this.source` (`= this.source-type`)
