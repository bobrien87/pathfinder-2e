---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 60000}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This delicate necklace contains bottled whispers distilled from a source on the Astral Plane rumored to be connected to the first lie ever told.

While wearing the necklace, you gain a +3 item bonus to Deception checks, and you can attempt to counteract effects that would force you to tell the truth or determine whether you are lying.

Success on this counteract attempt lets you ignore the effect, rather than removing the effect entirely. The counteract rank is 9, with a counteract modifier of `r 1d20+35`.

**Activate—Release the Lie** `pf2:3` (concentrate, manipulate)

**Effect** You unstopper the vial and release the lie, creating the effect of a [[Fabricated Truth]] (DC 47). The vial is emptied and can never be activated again.

**Craft Requirements** Supply a casting of *fabricated truth*.

**Source:** `= this.source` (`= this.source-type`)
