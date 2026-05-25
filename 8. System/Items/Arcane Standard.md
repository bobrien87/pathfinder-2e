---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 960, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner has glittery, arcane threads cross-woven into the fabric, causing it to reflect light in little sparkles. While holding an arcane standard, you can use the following ability.

**Activate—Magical Weakness** `pf2:1` (concentrate)

**Frequency** once per turn

**Effect** The magic of the banner causes energy to linger, tearing away at its target, leaving them vulnerable to more. One creature within the banner's aura that has taken acid, cold, electricity, fire, or sonic damage this turn gains weakness 5 to that damage type for 1 round.

> [!danger] Effect: Arcane Standard

*PFS Note:* If a PC uses this item's Magical Weakness ability against a creature which has taken more than one type of energy damage, the player chooses which energy type the creature gains weakness to.

**Source:** `= this.source` (`= this.source-type`)
