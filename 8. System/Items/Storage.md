---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Adjustment]]"]
price: "{'gp': 1}"
usage: "applied-to-armor-or-unarmored-defense-clothing"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The storage adjustment fits the armor or clothing with belts, buckles, pouches, and loops for holding and storing tools. Countless fasteners make the armor as jangly as chain mail. While wearing armor with this adjustment, you can wear up to 3 Bulk of toolkits instead of the usual 2. However, the armor acquires the noisy trait. If it already has the noisy trait, increase its penalty to Stealth checks by 1.

**Source:** `= this.source` (`= this.source-type`)
