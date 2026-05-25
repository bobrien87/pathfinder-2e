---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 2200}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a saving throw against a possession effect

**Requirements** You are a master in Will saves.

A shining onyx gemstone clutched in a pair of black steel jaws, this pendant is a potent defense against hostile spirits and other beings who commandeer the bodies of others. When you Activate it, you gain a +4 item bonus to your saving throw against the triggering effect. If your result prevents you from being possessed, the creature that attempted to possess you is subject to a DC 37 [[Seize Soul]] spell, which can trap it in the talisman as if it had recently died. The talisman's magic is exhausted after use, but a soul trapped this way remains imprisoned inside, as detailed in the spell description. Starting at the end of its next turn, the trapped creature gets a new save to end the effect at the end of each of its turns.

**Source:** `= this.source` (`= this.source-type`)
