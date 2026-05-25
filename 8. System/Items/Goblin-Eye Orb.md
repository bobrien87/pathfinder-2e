---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 24}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a weapon

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a Strike with the affixed firearm or crossbow against an enemy that's concealed or hidden to you.

**Requirements** You're an expert with the affixed firearm or crossbow and an expert in Perception.

This colorful marble dangles from a leather thong wrapped around the affixed weapon. When you activate the band, for the triggering Strike, you don't need to attempt a flat check due to the enemy being concealed or hidden to you.

**Source:** `= this.source` (`= this.source-type`)
