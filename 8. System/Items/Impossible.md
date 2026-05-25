---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]"]
price: "{'gp': 70000}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune makes a weapon capable of impossible offense and defense. The etched weapon is immune to [[Dispel Magic]] and similar effects that could counteract its magic. If it's a ranged weapon or thrown weapon, its range increment is doubled.

**Activate** `pf2:2` (concentrate, teleportation)

**Frequency** once per hour

**Effect** You and the weapon flash to a perfect attacking position, then return to where you started. Make a Strike with the etched weapon against one creature you can see, even if the target is beyond the weapon's reach or range. On this Strike, ignore any circumstance penalty, status penalty, and range increment penalty.

**Source:** `= this.source` (`= this.source-type`)
