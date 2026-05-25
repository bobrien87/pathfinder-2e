---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a Diplomacy check to [[Make an Impression]].

These wooden discs sometimes form spontaneously at the Wood Pile, a secret conrasu location suffused with extraplanar energy. A conrasu coin can be activated to call upon the power of a specific type of aeon.

This coin has small wings like an arbiter, the messenger and diplomat aeon. When you activate the coin, you gain a +2 circumstance bonus on the Diplomacy check, which increases to a +3 circumstance bonus to `act make-an-impression` on a creature with the aeon trait.

**Source:** `= this.source` (`= this.source-type`)
