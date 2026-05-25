---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 4}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** R (concentrate)

**Trigger** A creature with the animal trait successfully Strikes you.

Frightened animals depicted on this fulu flee in all directions from a central figure (traditionally represented by a human hunter, but sometimes depicted as a skeletal undead creature or even a fiend with long, broken arms). You activate this fulu, gaining a +2 item bonus to AC against the triggering Strike. If this causes the Strike to miss, you become [[Concealed]] from the triggering creature until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
