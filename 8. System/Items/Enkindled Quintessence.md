---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You have fully subsumed your soul within that of a dragon's soul, overloading your very essence with eldritch potential. You immediately retrain your class to that of a sorcerer with the draconic bloodline, with your draconic exemplar matching your bound dragon. You are able to cast spells immediately as if you had a full 8 hours of rest and completed your daily preparations; however, you become [[Drained]] 2 from the strain of igniting your soul's magical potential.

Once per day, from any distance, the dragon can either teleport you to their lair or teleport to switch places with you. This is a 3-action activity with the teleportation trait and the dragon's tradition trait.

**Oathbreaker's Calamity** Should either party break the oath, both your souls begin to immolate through your physical forms. If either of you casts a spell, they immediately become [[Drained]] 3 unless they're casting it to harm the other party. If either of you die as a result of this calamity, you rise as a wraith (if it's you) or a wyrmwraith (if it's the dragon).

**Source:** `= this.source` (`= this.source-type`)
