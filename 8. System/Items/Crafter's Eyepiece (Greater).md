---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rugged metal eyepiece etched with square patterns is designed to be worn over a single eye. Twisting the lens reveals a faint three-dimensional outline of an item you plan to build or repair, with helpful labels on the component parts.

You gain a +2 item bonus to Crafting checks. When you Repair an item, increase the Hit Points restored to 10 + 10 per proficiency rank on a success or 15 + 15 per proficiency rank on a critical success.

**Activate—Prototype** 1 minute (manipulate)

**Frequency** once per day

**Effect** You calibrate the eyepiece to have it cast a 5th-rank [[Creation]] spell over the course of 1 minute to construct a temporary item.

**Source:** `= this.source` (`= this.source-type`)
