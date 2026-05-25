---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 120, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The very fabric of this off-putting magical banner seems to be rotting with a slick, foul texture. Traditionally, these banners were created from the uniforms of fallen enemy troops, but this is considered a cruel and dishonorable practice by many modern nations. While holding a banner of creeping death, you can use the following ability.

**Activate—Void's Embrace** `pf2:1` (concentrate, void)

**Frequency** once per minute

**Effect** A massive wave of void energy floods out from the banner in all directions. All living creatures within the banner's aura take @Damage[(1d4+1)[void]|options:area-damage|traits:concentrate,void] damage ([[Fortitude]] save).

**Source:** `= this.source` (`= this.source-type`)
