---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This special blend of potent herbs comes in the form of a compact ball the size of a marble that allows it to be held in the mouth, where it remains for 1 hour. An energizing pill has a bitter taste at first, but the longer one lets it soak, the more complex and sweet its flavor grows. It heightens your reactions, granting you a +2 item bonus to initiative rolls with Perception.

> [!danger] Effect: Energizing Pill

**Secondary Effect** `pf2:r`

**Trigger** You would become [[Clumsy]], [[Drained]], [[Enfeebled]], [[Frightened]], [[Sickened]], [[Slowed]], or [[Stupefied]]

**Effect** Reduce the value of the condition you just gained by 1; if this reduces the value to 0, you don't gain the triggering condition.

**Source:** `= this.source` (`= this.source-type`)
