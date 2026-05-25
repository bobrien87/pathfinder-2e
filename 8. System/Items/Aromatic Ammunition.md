---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 5}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

The components of this ammunition emit a strong smell when combined during its activation. A creature hit by an activated aromatic ammunition gains a distinct odor for up to 1 hour or until the scent is washed off (requiring at least a gallon of water and 10 minutes of scrubbing). Any creatures within 30 feet smell the target, allowing even those with a weak sense of smell to detect its presence, and all creatures gain a +1 item bonus to [[Track]] the affected creature for as long as it has the odor. A creature that has imprecise or precise scent doubles the range at which they can detect the target using their scent compared to the normal range of their scent.

> [!danger] Effect: Aromatic Ammunition

**Source:** `= this.source` (`= this.source-type`)
