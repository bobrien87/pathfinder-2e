---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 24000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner stands largest on any battlefield. While holding a titan's standard, you can use the following ability.

**Activate—Titan's Stature** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** The magical banner causes a rapid surge of growth. A Medium or smaller ally within the banner's aura becomes Large for 1 round. Its equipment grows with it but returns to its natural size afterwards. While Large, the ally is [[Clumsy]] 1, and its reach increases by 5 feet (or by 10 feet if it started out Tiny).

> [!danger] Effect: Titan's Standard

**Source:** `= this.source` (`= this.source-type`)
