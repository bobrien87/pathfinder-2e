---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Concussive]]", "[[Fatal aim d12]]"]
price: "{'gp': 11}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Jezails are simple, efficient long guns developed in Casmaron that typically feature a custom stock and a flintlock firing mechanism. Though lacking the range and stopping power of an arquebus or the raw force of a harmona gun, the jezail is an elegant, well-balanced weapon suitable for a variety of combat situations. It's even possible to tuck it under one arm to fire a less accurate attack that uses only one hand.

**Source:** `= this.source` (`= this.source-type`)
