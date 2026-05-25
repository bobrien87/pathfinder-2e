---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Metal]]"]
price: "{'gp': 650}"
usage: "etched-onto-medium-heavy-metal-armor"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The metal of your armor can shift and rearrange at a moment's notice, allowing you to manipulate what kind of damage it resists.

**Activate—Reconfigure Armor** `pf2:1` (manipulate)

**Effect** The armor's composition shifts, changing its specialization group to a different one of your choice. This doesn't change what the armor is made of, and any runes or precious material it's made of apply to the new composition. Any property runes that can't apply to the new form are suppressed until the item takes a composition to which they can apply.

**Source:** `= this.source` (`= this.source-type`)
