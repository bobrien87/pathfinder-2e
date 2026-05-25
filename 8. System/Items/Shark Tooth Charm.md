---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 23}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

This dried-seaweed bracelet is lined with charms shaped like small shark teeth. When you activate the bracelet, attempt to [[Escape]] using Acrobatics with a +1 item bonus to the check. If you roll a success, you get a critical success instead (if you roll a critical failure, you get a failure instead). If you fail the Acrobatics check against a grabbing creature, the creature must either release you as a free action or take 2d8 piercing damage as shark's teeth momentarily emerge from your skin.

**Source:** `= this.source` (`= this.source-type`)
