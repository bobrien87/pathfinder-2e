---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 9}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:f` (concentrate)

This ammunition was developed in Dongun Hold to minimize casualties to friendly fire, and is always marked by a burnished copper head or tip so it can be easily identified. Before you can fire a trustworthy round, you must call out a target. You don't need to specify a name; the target could be "The angry tiger attacking our group on the left." The round will only hit the specified target and will turn to gossamer dust midair if it misses the intended target or comes into contact with anything else; this also prevents abilities that redirect attacks. The round doesn't have any capabilities beyond your own to determine whether someone is who you think they are, so you can't use it to determine a disguised creature's identity. If you specify a target of "Seltyiel" and shoot someone disguised as Seltyiel who you thought was Seltyiel, the attack will still hit, whereas if you were about to hit a disguised Seltyiel who you didn't recognize to be Seltyiel, the round would dissolve.

**Source:** `= this.source` (`= this.source-type`)
