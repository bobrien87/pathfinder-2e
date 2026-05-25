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

This magical banner stands as a reminder to fight with everything because you're fighting for everything. While holding a zealous banner, you can use the following ability.

**Activate—Forward with Zeal** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** The magical banner offers a magical boost of zeal. An ally within the banner's aura becomes [[Quickened]] for 1 round and can use the additional action only to Strike.

**Source:** `= this.source` (`= this.source-type`)
