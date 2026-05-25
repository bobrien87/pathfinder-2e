---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Aura]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 60000, 'pp': 0, 'sp': 0}"
usage: "affixed-or-held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A single pale star shines bravely amid the dark cloth of this magical banner. The star can be seen even in the dead of night. While holding a banner of the rising star, you can use the following ability.

**Activate—Rise Up** `pf2:1` (concentrate, healing)

**Frequency** once per day

**Effect** The magical banner lifts your allies from the brink of death. An ally within the banner's aura with the [[Dying]] condition regains @Damage[30[healing]|traits:concentrate,healing] Hit Points, does not increase their [[Wounded]] condition, and can Stand as a free action. They become immune to Rise Up for 1 day.

**Source:** `= this.source` (`= this.source-type`)
