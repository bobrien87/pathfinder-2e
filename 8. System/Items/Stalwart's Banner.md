---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 360, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical banner mimics the rich green of summer grass. While holding a stalwart's banner, you can use the following ability.

**Activate—Stand Firm** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** You and allies within your banner's aura gain 5 temporary Hit Points and a +1 status bonus to your Fortitude DC and Reflex DC against any effect that would move you or knock you [[Prone]]. These effects last for 1 round.

> [!danger] Effect: Stalwart's Banner

**Source:** `= this.source` (`= this.source-type`)
