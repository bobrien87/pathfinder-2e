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

This magical banner flaps enthusiastically in the breeze, gleaming across the battlefield. While holding a *quickened standard*, you can use the following ability.

**Activate—Speed Up** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** The banner offers a magical boost of adrenaline. An ally within the banner's aura becomes [[Quickened]] for 1 round and can use the additional action only to Stride.

**Source:** `= this.source` (`= this.source-type`)
