---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Visual]]"]
price: "{'gp': 650}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long and billowing scarf is typically woven of silk or sheer fabric and adorned with bells or other jangling bits of shiny metal. It grants a +2 item bonus to Performance checks to dance.

**Activate—Swirling Scarf** A (manipulate)

**Requirements** On your most recent action, you succeeded at a Performance check to dance

**Effect** You become [[Concealed]] until the beginning of your next turn. You can also Stride up to half your Speed or Step.

**Source:** `= this.source` (`= this.source-type`)
