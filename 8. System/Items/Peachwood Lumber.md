---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Precious]]"]
price: "{'gp': 6000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Peachwood, often cultivated by Pharasmin priests, can ward against undead—even incorporeal ones. However, the wood loses its magical properties when it comes in contact with metal, requiring advanced carpentry to make full use of it.

Peachwood ItemsPeachwood ItemsHardnessHPBT**Thin Items**Standard-grade4168High-grade62412**Items**Standard-grade52010High-grade83216**Structure**Standard-grade124824High-grade186432

**Source:** `= this.source` (`= this.source-type`)
