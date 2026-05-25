---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Cursed]]", "[[Invested]]", "[[Laminar]]", "[[Magical]]"]
price: "{'gp': 5}"
bulk: "3"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *shared-pain sankeit* seems to be an impressive suit of *+2 resilient fortification duskwood sankeit* shaped to resemble a mighty linnorm. However, it protects you by drawing on the health of your nearby allies. When you roll the flat check for the armor's fortification rune, it protects you normally when you roll a 20. When you roll a 17, 18, or 19, though, the GM determines damage for the critical hit normally, then distributes half to you and the other half evenly among allies within 30 feet of you. If no ally is within range to take the distributed damage, the fortification rune fails to function. This effect manifests the first time an attacker scores a critical hit on you, after which the armor fuses with you.

**Source:** `= this.source` (`= this.source-type`)
