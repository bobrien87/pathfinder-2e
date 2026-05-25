---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This black pouch contains what appears to be fine bone dust. Pouring the dust in a special pattern over a corpse turns it into an undead creature. The type of undead created depends on the condition of the corpse, resulting in either a *skeleton* or a *zombie*. If the undead's level would be greater than 3, the dust fails to animate it. The body must be of an appropriate size and type for the undead you wish to create-for example, you must sprinkle the dust on a horse's skeleton to animate a *skeletal horse*. If more than one undead in the level range is appropriate, such as *skeletal guard* or *skeletal champion* for a Medium humanoid skeleton, you choose.

The animated undead has the *minion* trait, meaning it can use 2 actions when you Command it. You can issue a Command for the current turn as part of the activation. The undead creature remains animated for 1 minute before collapsing back into its corpse form. As usual, you can have a maximum of four minions under your control.

**Source:** `= this.source` (`= this.source-type`)
